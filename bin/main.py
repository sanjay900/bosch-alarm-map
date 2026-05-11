import asyncio
from aiohttp import ClientSession, TCPConnector
from bosch_alarm_map.panel import Panel
import ssl
from bosch_alarm_map.panel import SubscriptionEventType, SubscriptionProperties


async def main():
    ssl_context = ssl.create_default_context()
    ssl_context.set_ciphers('AES128-GCM-SHA256')
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with ClientSession(connector=TCPConnector(ssl=ssl_context)) as session:
        panel = Panel("https://192.168.0.163", "Digiflex", "Digiflex01", session)
        await panel.load()
        # async for event in panel.subscribe(10, 50, [SubscriptionProperties(["*"],[SubscriptionEventType.CREATED])]):
        #     print(event)
asyncio.run(main())