from aiohttp import ClientSession, ClientResponse, DigestAuthMiddleware, ClientTimeout
from enum import Enum
import json
from dataclasses import dataclass
import dataclasses
from bosch_alarm_map.models.area_list import AreaList, Area
from bosch_alarm_map.models.point_list import PointList, Point
from bosch_alarm_map.models.output_list import OutputList, Output
from bosch_alarm_map.models.desc import Desc
from bosch_alarm_map.models.devices_list import Device, DevicesList
from bosch_alarm_map.utils import Observable


class ArmCommand(str, Enum):
    DISARM = "DISARM"
    ARM = "ARM"


class ExitDelay(str, Enum):
    EXTENDED = "EXTENDED"
    ZERO = "ZERO"


class SubscriptionEventType(str, Enum):
    CHANGED = ("CHANGED",)
    CREATED = ("CREATED",)
    DELETED = "DELETED"


@dataclass
class SubscriptionProperties:
    urls: list[str]
    eventType: list[SubscriptionEventType]


class Panel:
    def __init__(self, host, username, password, session: ClientSession):
        self.digest_auth = DigestAuthMiddleware(login=username, password=password)
        self.host = host
        self.session = session
        self.modelName = None
        self.areas: dict[int, Area] = dict()
        self.points: dict[int, Point] = dict()
        self.outputs: dict[int, Output] = dict()
        self.devices: dict[int, Device] = dict()
        self.response: ClientResponse | None = None
        self.connection_status_observer = Observable()
        self.description: Desc | None = None

    def connected(self) -> bool:
        return self.response is not None and not self.response.closed

    async def _get(self, path):
        async with self.session.get(
            url=f"{self.host}/{path}", middlewares=(self.digest_auth,)
        ) as resp:
            return await resp.json(content_type=None)

    async def _post(self, path, body):
        async with self.session.post(
            url=f"{self.host}/{path}", middlewares=(self.digest_auth,), json=body
        ) as resp:
            return await resp.json(content_type=None)

    async def describe(self) -> Desc:
        return Desc.from_dict(await self._get("desc"))

    async def load(self):
        self.description = await self.describe()
        for area in await self._load_areas():
            self.areas[len(self.areas) + 1] = area
        for device in await self._load_devices():
            self.devices[len(self.devices) + 1] = device
        for output in await self._load_outputs():
            self.outputs[len(self.outputs) + 1] = output
        for point in await self._load_points():
            self.points[len(self.points) + 1] = point

    async def _load_outputs(self):
        return OutputList.from_dict(await self._get("outputs")).list

    async def _load_devices(self):
        return DevicesList.from_dict(await self._get("devices")).list

    async def _load_areas(self):
        return AreaList.from_dict(await self._get("areas")).list

    async def _load_points(self):
        return PointList.from_dict(await self._get("points")).list

    async def arm(self, cmd: ArmCommand, bypassOffNormal: bool, exitDelay: ExitDelay):
        try:
            return await self._post(
                "areas",
                {
                    "@cmd": cmd.name,
                    "bypassOffNormalDevices": bypassOffNormal,
                    "exitDelay": exitDelay,
                },
            )
        except Exception as e:
            # TODO: firmware is bugged and returns invalid json
            pass

    async def _process_event_armed_by_user(self, event: dict):
        areaId: int = event["data"]["areaId"]
        areaName: str = event["data"]["areaName"]
        self.areas[areaId].armed = True
        self.areas[areaId].status_observer._notify()

    async def _process_event_disarmed_by_user(self, event: dict):
        areaId: int = event["data"]["areaId"]
        areaName: str = event["data"]["areaName"]
        self.areas[areaId].armed = False
        self.areas[areaId].status_observer._notify()

    async def subscribe_to_events(self):
        await self._subscribe(
            10, 50, [SubscriptionProperties(["*"], [SubscriptionEventType.CREATED])]
        )

    async def _subscribe(
        self,
        lease_time: int,
        buffer_size: int,
        properties: list[SubscriptionProperties],
    ):
        body = {
            "@cmd": "SUBSCRIBE",
            "lease_time": lease_time,
            "buffer_size": buffer_size,
            "subscriptions": [[dataclasses.asdict(x) for x in properties]],
        }
        events = {
            "Armed By User": self._process_event_armed_by_user,
            "Disarmed By User": self._process_event_disarmed_by_user,
        }
        async with self.session.post(
            url=f"{self.host}/sub",
            middlewares=(self.digest_auth,),
            json=body,
            timeout=ClientTimeout(0),
        ) as resp:
            self.response = resp
            data = {}
            async for line in resp.content:
                line = line.decode("utf-8")
                if line.startswith(":"):
                    # comment line
                    continue
                if ":" in line:
                    field, value = line.split(":", 1)
                    try:
                        data[field] = json.loads(value.strip())
                    except json.JSONDecodeError:
                        data[field] = value.strip()
                if line == "\n":
                    event = data.get("event")
                    if event in events:
                        await events[event](data)
                    data = {}
