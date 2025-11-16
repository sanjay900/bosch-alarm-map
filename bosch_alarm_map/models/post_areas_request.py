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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from bosch_alarm_map.models.area_arm import AreaArm
from bosch_alarm_map.models.area_disarm import AreaDisarm
from bosch_alarm_map.models.bell_test_start import BellTestStart
from bosch_alarm_map.models.chime_mode_start_stop import ChimeModeStartStop
from bosch_alarm_map.models.motion_detector_test_start_stop import MotionDetectorTestStartStop
from bosch_alarm_map.models.walktest_start import WalktestStart
from bosch_alarm_map.models.walktest_stop import WalktestStop
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

POSTAREASREQUEST_ONE_OF_SCHEMAS = ["AreaArm", "AreaDisarm", "BellTestStart", "ChimeModeStartStop", "MotionDetectorTestStartStop", "WalktestStart", "WalktestStop"]

class PostAreasRequest(BaseModel):
    """
    PostAreasRequest
    """
    # data type: AreaArm
    oneof_schema_1_validator: Optional[AreaArm] = None
    # data type: AreaDisarm
    oneof_schema_2_validator: Optional[AreaDisarm] = None
    # data type: WalktestStart
    oneof_schema_3_validator: Optional[WalktestStart] = None
    # data type: WalktestStop
    oneof_schema_4_validator: Optional[WalktestStop] = None
    # data type: MotionDetectorTestStartStop
    oneof_schema_5_validator: Optional[MotionDetectorTestStartStop] = None
    # data type: ChimeModeStartStop
    oneof_schema_6_validator: Optional[ChimeModeStartStop] = None
    # data type: BellTestStart
    oneof_schema_7_validator: Optional[BellTestStart] = None
    actual_instance: Optional[Union[AreaArm, AreaDisarm, BellTestStart, ChimeModeStartStop, MotionDetectorTestStartStop, WalktestStart, WalktestStop]] = None
    one_of_schemas: Set[str] = { "AreaArm", "AreaDisarm", "BellTestStart", "ChimeModeStartStop", "MotionDetectorTestStartStop", "WalktestStart", "WalktestStop" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = PostAreasRequest.model_construct()
        error_messages = []
        match = 0
        # validate data type: AreaArm
        if not isinstance(v, AreaArm):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AreaArm`")
        else:
            match += 1
        # validate data type: AreaDisarm
        if not isinstance(v, AreaDisarm):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AreaDisarm`")
        else:
            match += 1
        # validate data type: WalktestStart
        if not isinstance(v, WalktestStart):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WalktestStart`")
        else:
            match += 1
        # validate data type: WalktestStop
        if not isinstance(v, WalktestStop):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WalktestStop`")
        else:
            match += 1
        # validate data type: MotionDetectorTestStartStop
        if not isinstance(v, MotionDetectorTestStartStop):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MotionDetectorTestStartStop`")
        else:
            match += 1
        # validate data type: ChimeModeStartStop
        if not isinstance(v, ChimeModeStartStop):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ChimeModeStartStop`")
        else:
            match += 1
        # validate data type: BellTestStart
        if not isinstance(v, BellTestStart):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BellTestStart`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in PostAreasRequest with oneOf schemas: AreaArm, AreaDisarm, BellTestStart, ChimeModeStartStop, MotionDetectorTestStartStop, WalktestStart, WalktestStop. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in PostAreasRequest with oneOf schemas: AreaArm, AreaDisarm, BellTestStart, ChimeModeStartStop, MotionDetectorTestStartStop, WalktestStart, WalktestStop. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into AreaArm
        try:
            instance.actual_instance = AreaArm.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AreaDisarm
        try:
            instance.actual_instance = AreaDisarm.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WalktestStart
        try:
            instance.actual_instance = WalktestStart.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WalktestStop
        try:
            instance.actual_instance = WalktestStop.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MotionDetectorTestStartStop
        try:
            instance.actual_instance = MotionDetectorTestStartStop.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ChimeModeStartStop
        try:
            instance.actual_instance = ChimeModeStartStop.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BellTestStart
        try:
            instance.actual_instance = BellTestStart.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into PostAreasRequest with oneOf schemas: AreaArm, AreaDisarm, BellTestStart, ChimeModeStartStop, MotionDetectorTestStartStop, WalktestStart, WalktestStop. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PostAreasRequest with oneOf schemas: AreaArm, AreaDisarm, BellTestStart, ChimeModeStartStop, MotionDetectorTestStartStop, WalktestStart, WalktestStop. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AreaArm, AreaDisarm, BellTestStart, ChimeModeStartStop, MotionDetectorTestStartStop, WalktestStart, WalktestStop]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


