# coding: utf-8

"""
    REST-API_basic

    # Overview   This document specifies the MAP REST-API (OII) - **O**pen **I**ntrusion **I**nterface (**OII**).  The REST-API (former known as **O**pen **I**ntrusion **I**nterface [**OII**]), is implemented on the MAP system. This document is fully valid to the MAP panel firmware Version: <br> <br> **MAP_Update.1.4.0272.tar.bz2**<br>  To be backward compatible, all \"/get\", \"/post\" and other commands which includes \"OII\", will be still \"OII\".  New implemented features will be named as \"REST-API\" instead of \"OII\".  Please note that the following rules have been ignored when checking the OpenAPI documentation file against errors and warnings:   - [no-identical-paths](https://redocly.com/docs/cli/rules/no-identical-paths/)   - [no-ambiguous-paths](https://redocly.com/docs/cli/rules/no-ambiguous-paths/)   - [spec](https://redocly.com/docs/cli/rules/spec/)  The OpenAPI file is structured in the following groups: 1. REST-API_basic 2. REST-API_MUM  ## 1: REST-API_basic  All URLs described under this group contain all functions of released MAP panel firmware version 1.4.0176 All REST-API (OII) functions are also described in the following previous documents (PDF):     - ApplicationNotes.pdf   - BaseSpecification.pdf   - ResourceModel.pdf  This previous REST-API (OII) documentation can be downloaded [here](https://media.boschsecurity.com/fs/media/pb/media/extranet/map_partners/2019_oii_openintrusioninterface.zip). <br>   New features: - *Memory Info & statistics*     This feature is available from the MAP panel firmware version *<1.4.0xxx ToDo, replace*   - *NTP*  This feature is available from the MAP panel firmware version *<1.4.0xxx ToDo, replace*  - *supportfiles*     This feature is available from the MAP panel firmware version 1.4.0231  ## 2: REST-API_MUM  All URLs described in this group contain the features, which are added by the firmware version 1.4.0245   New Features: - *VDS2252 permissions*    Updated internal permissions with both mayClearMainPowerFailure and mayClearATS   ## HTTPS server certificates The MAP system is using so named \"unique self signed server certificates\" for HTTPS. The certificate files are created during the MAP panel start, if not already existing. Due to missing entropy and hardware resources, 2048-bit certificates are created. The MAP system guarantees those certificates will not change uncontrolled during lifetime. This guarantee is fullfilled by automated test during development.  ## General client requests   The MAP systems are **strongly limited** in hardware and software resources. This is why there are **limitations** using the MAP REST-API which **must** be considered to avoid erroneous behavior and a poor user experience.<br> - Use a ping to check the network availability **before** sending HTTP requests to the MAP panel. - The MAP panel can handle parallel requests. However, it is strongly recommended that a single client makes only serial requests.  - Parallel processing of many multiple requests will typically fail with negative response codes and overload the system. - Multiple requests to the same MAP panel must be serialized with a delay of at least 1 second between the last response and the next request. - The MAP panel might return the response codes 500 or a 503 or other response codes in case of overload. - Requests with HTTP Content-Length higher than 30000 bytes are not supported, HTTP Error Code 411 will be raised. - Receiving negative response codes caused by overload require a 60 seconds communication delay. - If the MAP panel does not (anymore) response at all, a delay of at least 5 minutes must be considered. - It is strongly recommended to use a connection pool for better HTTPS performance as well as lower CPU load on the MAP panel. - If the connection is cancelled or runs into timeout it is undefined whether the request will still be processed or not.  - After connection errors, the HTTPS connection must be closed and it is necessary again to check network availability by ping. - Cyclic request, e.g. ping, getting synchronization states and performing a time synchronization are allowed. - Cyclic request must not be more frequent than every 5 minutes. - Enabled **User Passcode Tamper** feature will prevent potential bruteforce attack. Retry count and lockout time is configurable via RPS for MAP. During the lockout any request will return code 401 for attacking IP. - In case of negative response codes, the client side should provide request and response logging to a file, with milliseconds timestamps, to support further analyses. - In case of interface errors or unexpected behaviour, the client side must provide request and response logging to a file, with milliseconds timestamps, e.g. activated by a client side debug level. - The MAP panel itself logs all database modifications, per default, to the history.log, what is strongly limited in number of entries and content. - The MAP panel itself does not log all HTTPS request and responses because of file system limitations. - TCP keepalive is enabled, lost connections will be dropped after 25 seconds.   ## HTTPS server limitations  Due to limited resources, MAP system generally does not process HTTPS requests simultaneously.  However, there are exceptions that are processed simultaneously: - **/syncstatus** - **/panel** - **/sub** - **/sub/\\*** - **/history**  All other URLs are executed sequentially.  Requests are queued and executed once execution units are available.  Simultaneous execution is limited to 3 simultaneous requests, processing time will be slower for multiple simultaneous requests.  Overloading REST-API can make MAP less responsive, in case of overload, the REST-API will generally respond with HTTP code 503, or, in case of heavy overload, will immediately close TCP socket without any response.    ## Response time guarantees  The following URLs have a guaranteed time, only if one HTTPS client connection at the same time.  The following URLs are guaranteed to execute their requests within 120 seconds: - **/history** - **/supportfile** - **/points** - **/couplers** - **/lsnauxs**  The following URLs are guaranteed to execute their requests within 60 seconds: - **/network** - **/syncstatus** - **/usermodellist** - **/outputs** - **/user** - **/mains** - **/groundfaults**  All other REST-API requests are guaranteed to be executed within 10 seconds.  ## License  Following URLs are only accessible with a valid MUM software license and only with a MAP-COM panel: - usermodel - usermodel/* - usermodellist - daymodel - daymodel/* - daymodellist - timemodel - timemodel/* - timemodellist - specialdaymodel - specialdaymodel/* - specialdaymodellist - smartkeymodel - smartkeymodel/* - smartkeymodellist - areaandtimemodel - areaandtimemodel/* - areaandtimemodellist - accessmodel - accessmodel/* - accessmodellist - permissionmodel - permissionmodel/* - permissionmodellist - mumusergroup - sharedkey - statistics - statistics/oii - statistics/db  Missing license will lead to HTTP 403 plain-text response, for example \"License missing MUM/usermodel\"  ## Security  Supported cipher suites:  **TLS1.3** (**recommended**) - TLS_AES_256_GCM_SHA384 - TLS_CHACHA20_POLY1305_SHA256 - TLS_AES_128_GCM_SHA256  **TLS1.2** - ECDHE-RSA-AES128-SHA256 - ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-RSA-AES256-SHA384 - ECDHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-SHA256 - DHE-RSA-AES128-GCM-SHA256 - DHE-RSA-AES256-SHA256 - DHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-SHA  **TLS1.0** (**deprecated**! Not recommended to be used, has to be manually enabled in MAP panel configuration via RPS for MAP) - AES128-SHA - AES256-SHA

    The version of the OpenAPI document: 1.4.0272, 18.09.2024
    Contact: intrusion.emea@de.bosch.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from bosch_alarm_map.models.handling_state import HandlingState
from typing import Optional, Set
from typing_extensions import Self

class Inc(BaseModel):
    """
    Inc
    """ # noqa: E501
    type: Optional[List[StrictStr]] = Field(default=None, description="Fixed type identifier", alias="@type")
    var_self: Optional[StrictStr] = Field(default=None, description="Link to the current resource", alias="@self")
    inc_type: Optional[StrictStr] = Field(default=None, description="The following table provides an overview of the types of troubles the MAP system is supporting. In case a particular type adds additional information items or operation, a detailed specification will be given in a dedicated section. * ALARMS: Alarms indicate significant situation has been detected in the MAP system that requires immediate action (e.g. intrusion alarm, fire alarm).   <table>     <tr>       <td>----</td>       <td>--------</td>       <td>-------------</td>       <td>-----------</td>     </tr>     <tr>       <td>TYPE</td>       <td>CATEGORY</td>       <td>SUB-CATEGORY</td>       <td>DESCRIPTION</td>     </tr>     <tr>       <td>----</td>       <td>--------</td>       <td>-------------</td>       <td>-----------</td>     </tr>     <tr>       <td>Alarm</td>       <td>Intrusion</td>       <td>General</td>       <td>Alarm from any Intrusion Detector</td>     </tr>     <tr>       <td>Alarm</td>       <td>Intrusion</td>       <td>Hold-up</td>       <td>Alarm from a detector under panic situation</td>     </tr>     <tr>       <td>Alarm</td>       <td>Intrusion</td>       <td>Amok</td>       <td>Alarm from a detector under amok situation</td>     </tr>     <tr>       <td>Alarm</td>       <td>Intrusion</td>       <td>Duress</td>       <td>Alarm from a detector under threat</td>     </tr>     <tr>       <td>Alarm</td>       <td>Intrusion</td>       <td>Door Not Locked</td>       <td>Alarm when a door is not locked properly, even after Exit Delay Expiry</td>     </tr>     <tr>       <td>Alarm</td>       <td>Intrusion</td>       <td>Exit Error</td>       <td>Alarm in case of un-authorised presence in premises, even after Exit Delay expiry.</td>     </tr>     <tr>       <td>Alarm</td>       <td>Fire</td>       <td>General</td>       <td>Alarm from any Fire detector</td>     </tr>     <tr>       <td>Alarm</td>       <td>Technical</td>       <td>General</td>       <td>Alarm from any Technical detector</td>     </tr>     <tr>       <td>Alarm</td>       <td>System</td>       <td>General</td>       <td>Alarm from any system device</td>     </tr>     <tr>       <td>Alarm</td>       <td>System</td>       <td>User CodeTamper</td>       <td>Invalid PIN entry consecutively multiple times</td>     </tr>     <tr>       <td>Alarm</td>       <td>System</td>       <td>Tamper</td>       <td>Sabotage Alarm</td>     </tr>     <tr>       <td>Alarm</td>       <td>System</td>       <td>Exit Error</td>       <td>Alarm from a supervised output</td>     </tr>   </table>   <br>  * TROUBLES: Troubles indicate that the system is not fully operational and action may be advised (e.g. device in an unarmed area malfunctioning).   <table>     <tr>       <td>----</td>       <td>--------</td>       <td>-------------</td>       <td>-----------</td>     </tr>     <tr>       <td>TYPE</td>       <td>CATEGORY</td>       <td>SUB-CATEGORY</td>       <td>DESCRIPTION</td>     </tr>     <tr>       <td>----</td>       <td>--------</td>       <td>-------------</td>       <td>-----------</td>     </tr>     <tr>       <td>Trouble</td>       <td>Intrusion</td>       <td>General</td>       <td>Malfunction of an intrusion device</td>     </tr>     <tr>       <td>Trouble</td>       <td>Intrusion</td>       <td>Antimask</td>       <td>When a PIR detector is covered or masked.</td>     </tr>     <tr>       <td>Trouble</td>       <td>Fire</td>       <td>General</td>       <td>Malfunction of a fire detector</td>     </tr>     <tr>       <td>Trouble</td>       <td>Fire</td>       <td>Optical</td>       <td>Malfunction of the optical sensor of the fire detector</td>     </tr>     <tr>       <td>Trouble</td>       <td>Fire</td>       <td>Chemical</td>       <td>Malfunction of the chemical detector of the fire sensor</td>     </tr>     <tr>       <td>Trouble</td>       <td>Fire</td>       <td>Thermal</td>       <td>Malfunction of the thermal sensors of the fire detector</td>     </tr>     <tr>       <td>Trouble</td>       <td>Fire</td>       <td>Output Supervisory</td>       <td>Malfunction of a supervised output device</td>     </tr>     <tr>       <td>Trouble</td>       <td>Technical</td>       <td>General</td>       <td>Malfunction of a technical detector</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>General</td>       <td>Malfunction of a general system device (Specific device would detect specific malfunction incidents)</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Initialization</td>       <td>Incident detected when an element in the system went into initialization state when it was not expected.</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Failure</td>       <td>Incident detected when there is a system failure</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Communication</td>       <td>Malfunction of a communication device like AT2000 communicator</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Battery Low</td>       <td>The battery connected to the power supply is low on power</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Battery failure</td>       <td>The battery connected to the power supply has failed</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Battery Missing</td>       <td>The battery configured in the system is not connected</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Battery Self Test Failed</td>       <td>Self Test of the battery failed</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Main Power Failure</td>       <td>Failure in the main power to the power supply</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Ground fault</td>       <td>Fault detected from a Power supply due to Improper Grounding</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Over Current</td>       <td>Incident indicating that more power is being drawn from the device than the expected limits</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Output Fault</td>       <td>Malfunction of a supervised output device</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Printer Paper Low</td>       <td>Printer is low on paper</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Printer Cover Over</td>       <td>Printer cover is open</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Device Firmware Corrupt</td>       <td>Firmware on the peripheral device is corrupted. Detected for system keypad, gateway, DE Module and the power supply</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Device Firmware Programming</td>       <td>Firmware on the peripheral device is being updated. Detected for system keypad, gateway, DE Module and the power supply</td>     </tr>     <tr>       <td>Trouble</td>       <td>System</td>       <td>Management System Interface</td>       <td>Management System monitoring the panel has lost connection to the panel</td>     </tr>   </table> ", alias="incType")
    ext_inc: Optional[StrictBool] = Field(default=None, description="Indicates whether the incident is an external incident or an internal incident (external incidents are in general incidents that are reported to the central station)", alias="extInc")
    time: Optional[StrictStr] = Field(default=None, description="Time when the incident occurred in REST-API compliant format in precision of seconds.")
    handling_state: Optional[List[HandlingState]] = Field(default=None, description="Triple of “state”, “user”, “interface”", alias="handlingState")
    handling_required: Optional[StrictBool] = Field(default=None, description="Indicates whether the incident requires handling by the user in order to be resolved. If false, the incident will get deleted once the reason for the incident is not present anymore.", alias="handlingRequired")
    triggered_by: Optional[StrictStr] = Field(default=None, description="The id of the element that triggered the incidents (e.g. ID of the door contact that triggered an intrusion alarm)", alias="triggeredBy")
    relates_to: Optional[StrictStr] = Field(default=None, description="Reference to other elements that are affected by the alarm. Will at least contain the url of the area in which the incident occurred.", alias="relatesTo")
    silenced: Optional[StrictBool] = Field(default=None, description="Indicates whether the outputs and sirens configured to sound for this incident are turned on or off.")
    counter: Optional[StrictInt] = Field(default=None, description="Number of times the incident occurred. Value will usually be one, as an incident is normally triggered only once. In case of a duress alarm, the counter will increase with every activation of a duress alarm from the same location (pressing the duress button multiple times)")
    __properties: ClassVar[List[str]] = ["@type", "@self", "incType", "extInc", "time", "handlingState", "handlingRequired", "triggeredBy", "relatesTo", "silenced", "counter"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Inc from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in handling_state (list)
        _items = []
        if self.handling_state:
            for _item_handling_state in self.handling_state:
                if _item_handling_state:
                    _items.append(_item_handling_state.to_dict())
            _dict['handlingState'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Inc from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@type": obj.get("@type"),
            "@self": obj.get("@self"),
            "incType": obj.get("incType"),
            "extInc": obj.get("extInc"),
            "time": obj.get("time"),
            "handlingState": [HandlingState.from_dict(_item) for _item in obj["handlingState"]] if obj.get("handlingState") is not None else None,
            "handlingRequired": obj.get("handlingRequired"),
            "triggeredBy": obj.get("triggeredBy"),
            "relatesTo": obj.get("relatesTo"),
            "silenced": obj.get("silenced"),
            "counter": obj.get("counter")
        })
        return _obj


