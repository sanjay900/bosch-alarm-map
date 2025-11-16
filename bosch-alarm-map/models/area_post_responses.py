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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from bosch-alarm-map.models.arming_info_why_not_ready_to_arm import ArmingInfoWhyNotReadyToArm
from bosch-alarm-map.models.arming_info_why_not_ready_to_disarm import ArmingInfoWhyNotReadyToDisarm
from bosch-alarm-map.models.arming_info_why_not_ready_to_force_arm import ArmingInfoWhyNotReadyToForceArm
from typing import Optional, Set
from typing_extensions import Self

class AreaPostResponses(BaseModel):
    """
    AreaPostResponses
    """ # noqa: E501
    type: Optional[List[StrictStr]] = Field(default=None, description="Fixed type identifier", alias="@type")
    var_self: Optional[StrictStr] = Field(default=None, description="Link to the current resource", alias="@self")
    armed: Optional[StrictBool] = Field(default=None, description="Indicates whether area is armed")
    transitional_state: Optional[StrictStr] = Field(default=None, description="An empty JSON string (i.e. “”) indicates that area is not in a transitional state at the moment", alias="transitionalState")
    oii_armable: Optional[StrictBool] = Field(default=None, description="True, if it is possible to disarm/arm the area over the REST-API interface. False, if Areas are configured only to be disarmed/armed blocklocks. False, if Area has relationships to Parent Area Type: Shared Area or Parent Area Type: Pass Thru Area. ", alias="oiiArmable")
    ready_to_arm: Optional[StrictBool] = Field(default=None, description="Indicates whether is area is ready to arm. If the area is already armed, then this flag will be false", alias="readyToArm")
    ready_to_disarm: Optional[StrictBool] = Field(default=None, description="Indicates whether this area can be disarmed. Will be false if the area is already disarmed.", alias="readyToDisarm")
    number_of_bypassed_devices: Optional[Annotated[int, Field(le=1500, strict=True, ge=0)]] = Field(default=None, description="Number of devices that are bypassed in that area", alias="numberOfBypassedDevices")
    walktest: Optional[StrictStr] = None
    motion_detector_test_active: Optional[StrictBool] = Field(default=None, description="Indicates whether motion detector test is active", alias="motionDetectorTestActive")
    chime_mode_active: Optional[StrictBool] = Field(default=None, description="Indicates whether chime mode is active", alias="chimeModeActive")
    incs: Optional[List[StrictStr]] = Field(default=None, description="This field shows the relationship between incidents (alarm/trouble) and an individual area. Details about the incident are contained in the incident resource at its URL.")
    ready_to_force_arm: Optional[StrictBool] = Field(default=None, description="Indicates whether this area can be armed by bypassing off normal devices. If the area is already armed, this flag will be false.", alias="readyToForceArm")
    why_not_ready_to_arm: Optional[ArmingInfoWhyNotReadyToArm] = Field(default=None, alias="whyNotReadyToArm")
    why_not_ready_to_force_arm: Optional[ArmingInfoWhyNotReadyToForceArm] = Field(default=None, alias="whyNotReadyToForceArm")
    why_not_ready_to_disarm: Optional[ArmingInfoWhyNotReadyToDisarm] = Field(default=None, alias="whyNotReadyToDisarm")
    __properties: ClassVar[List[str]] = ["@type", "@self", "armed", "transitionalState", "oiiArmable", "readyToArm", "readyToDisarm", "numberOfBypassedDevices", "walktest", "motionDetectorTestActive", "chimeModeActive", "incs", "readyToForceArm", "whyNotReadyToArm", "whyNotReadyToForceArm", "whyNotReadyToDisarm"]

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
        """Create an instance of AreaPostResponses from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of why_not_ready_to_arm
        if self.why_not_ready_to_arm:
            _dict['whyNotReadyToArm'] = self.why_not_ready_to_arm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of why_not_ready_to_force_arm
        if self.why_not_ready_to_force_arm:
            _dict['whyNotReadyToForceArm'] = self.why_not_ready_to_force_arm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of why_not_ready_to_disarm
        if self.why_not_ready_to_disarm:
            _dict['whyNotReadyToDisarm'] = self.why_not_ready_to_disarm.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AreaPostResponses from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@type": obj.get("@type"),
            "@self": obj.get("@self"),
            "armed": obj.get("armed"),
            "transitionalState": obj.get("transitionalState"),
            "oiiArmable": obj.get("oiiArmable"),
            "readyToArm": obj.get("readyToArm"),
            "readyToDisarm": obj.get("readyToDisarm"),
            "numberOfBypassedDevices": obj.get("numberOfBypassedDevices"),
            "walktest": obj.get("walktest"),
            "motionDetectorTestActive": obj.get("motionDetectorTestActive"),
            "chimeModeActive": obj.get("chimeModeActive"),
            "incs": obj.get("incs"),
            "readyToForceArm": obj.get("readyToForceArm"),
            "whyNotReadyToArm": ArmingInfoWhyNotReadyToArm.from_dict(obj["whyNotReadyToArm"]) if obj.get("whyNotReadyToArm") is not None else None,
            "whyNotReadyToForceArm": ArmingInfoWhyNotReadyToForceArm.from_dict(obj["whyNotReadyToForceArm"]) if obj.get("whyNotReadyToForceArm") is not None else None,
            "whyNotReadyToDisarm": ArmingInfoWhyNotReadyToDisarm.from_dict(obj["whyNotReadyToDisarm"]) if obj.get("whyNotReadyToDisarm") is not None else None
        })
        return _obj


