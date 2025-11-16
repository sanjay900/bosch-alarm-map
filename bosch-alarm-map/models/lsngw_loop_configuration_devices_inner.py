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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from bosch-alarm-map.models.lsn_std_intr50_configuration import LSNStdIntr50Configuration
from bosch-alarm-map.models.lsn_std_intr51_configuration import LSNStdIntr51Configuration
from bosch-alarm-map.models.lsn_std_intr52_configuration import LSNStdIntr52Configuration
from bosch-alarm-map.models.lsn_std_intr53_configuration import LSNStdIntr53Configuration
from bosch-alarm-map.models.lsn_std_intr54_configuration import LSNStdIntr54Configuration
from bosch-alarm-map.models.lsn_std_intr55_configuration import LSNStdIntr55Configuration
from bosch-alarm-map.models.lsn_std_intr56_configuration import LSNStdIntr56Configuration
from bosch-alarm-map.models.lsnemk36_configuration import LSNEMK36Configuration
from bosch-alarm-map.models.lsnemk36_s_configuration import LSNEMK36SConfiguration
from bosch-alarm-map.models.lsnnd100_configuration import LSNND100Configuration
from bosch-alarm-map.models.lsnnd200_configuration import LSNND200Configuration
from bosch-alarm-map.models.lsnska100_configuration import LSNSKA100Configuration
from bosch-alarm-map.models.lsnup370_t_configuration import LSNUP370TConfiguration
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

LSNGWLOOPCONFIGURATIONDEVICESINNER_ANY_OF_SCHEMAS = ["LSNEMK36Configuration", "LSNEMK36SConfiguration", "LSNND100Configuration", "LSNND200Configuration", "LSNSKA100Configuration", "LSNStdIntr50Configuration", "LSNStdIntr51Configuration", "LSNStdIntr52Configuration", "LSNStdIntr53Configuration", "LSNStdIntr54Configuration", "LSNStdIntr55Configuration", "LSNStdIntr56Configuration", "LSNUP370TConfiguration"]

class LSNGWLoopConfigurationDevicesInner(BaseModel):
    """
    LSNGWLoopConfigurationDevicesInner
    """

    # data type: LSNEMK36Configuration
    anyof_schema_1_validator: Optional[LSNEMK36Configuration] = None
    # data type: LSNEMK36SConfiguration
    anyof_schema_2_validator: Optional[LSNEMK36SConfiguration] = None
    # data type: LSNSKA100Configuration
    anyof_schema_3_validator: Optional[LSNSKA100Configuration] = None
    # data type: LSNStdIntr50Configuration
    anyof_schema_4_validator: Optional[LSNStdIntr50Configuration] = None
    # data type: LSNStdIntr51Configuration
    anyof_schema_5_validator: Optional[LSNStdIntr51Configuration] = None
    # data type: LSNStdIntr52Configuration
    anyof_schema_6_validator: Optional[LSNStdIntr52Configuration] = None
    # data type: LSNStdIntr53Configuration
    anyof_schema_7_validator: Optional[LSNStdIntr53Configuration] = None
    # data type: LSNStdIntr54Configuration
    anyof_schema_8_validator: Optional[LSNStdIntr54Configuration] = None
    # data type: LSNStdIntr55Configuration
    anyof_schema_9_validator: Optional[LSNStdIntr55Configuration] = None
    # data type: LSNStdIntr56Configuration
    anyof_schema_10_validator: Optional[LSNStdIntr56Configuration] = None
    # data type: LSNND100Configuration
    anyof_schema_11_validator: Optional[LSNND100Configuration] = None
    # data type: LSNND200Configuration
    anyof_schema_12_validator: Optional[LSNND200Configuration] = None
    # data type: LSNUP370TConfiguration
    anyof_schema_13_validator: Optional[LSNUP370TConfiguration] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[LSNEMK36Configuration, LSNEMK36SConfiguration, LSNND100Configuration, LSNND200Configuration, LSNSKA100Configuration, LSNStdIntr50Configuration, LSNStdIntr51Configuration, LSNStdIntr52Configuration, LSNStdIntr53Configuration, LSNStdIntr54Configuration, LSNStdIntr55Configuration, LSNStdIntr56Configuration, LSNUP370TConfiguration]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "LSNEMK36Configuration", "LSNEMK36SConfiguration", "LSNND100Configuration", "LSNND200Configuration", "LSNSKA100Configuration", "LSNStdIntr50Configuration", "LSNStdIntr51Configuration", "LSNStdIntr52Configuration", "LSNStdIntr53Configuration", "LSNStdIntr54Configuration", "LSNStdIntr55Configuration", "LSNStdIntr56Configuration", "LSNUP370TConfiguration" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

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
    def actual_instance_must_validate_anyof(cls, v):
        instance = LSNGWLoopConfigurationDevicesInner.model_construct()
        error_messages = []
        # validate data type: LSNEMK36Configuration
        if not isinstance(v, LSNEMK36Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNEMK36Configuration`")
        else:
            return v

        # validate data type: LSNEMK36SConfiguration
        if not isinstance(v, LSNEMK36SConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNEMK36SConfiguration`")
        else:
            return v

        # validate data type: LSNSKA100Configuration
        if not isinstance(v, LSNSKA100Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNSKA100Configuration`")
        else:
            return v

        # validate data type: LSNStdIntr50Configuration
        if not isinstance(v, LSNStdIntr50Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNStdIntr50Configuration`")
        else:
            return v

        # validate data type: LSNStdIntr51Configuration
        if not isinstance(v, LSNStdIntr51Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNStdIntr51Configuration`")
        else:
            return v

        # validate data type: LSNStdIntr52Configuration
        if not isinstance(v, LSNStdIntr52Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNStdIntr52Configuration`")
        else:
            return v

        # validate data type: LSNStdIntr53Configuration
        if not isinstance(v, LSNStdIntr53Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNStdIntr53Configuration`")
        else:
            return v

        # validate data type: LSNStdIntr54Configuration
        if not isinstance(v, LSNStdIntr54Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNStdIntr54Configuration`")
        else:
            return v

        # validate data type: LSNStdIntr55Configuration
        if not isinstance(v, LSNStdIntr55Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNStdIntr55Configuration`")
        else:
            return v

        # validate data type: LSNStdIntr56Configuration
        if not isinstance(v, LSNStdIntr56Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNStdIntr56Configuration`")
        else:
            return v

        # validate data type: LSNND100Configuration
        if not isinstance(v, LSNND100Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNND100Configuration`")
        else:
            return v

        # validate data type: LSNND200Configuration
        if not isinstance(v, LSNND200Configuration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNND200Configuration`")
        else:
            return v

        # validate data type: LSNUP370TConfiguration
        if not isinstance(v, LSNUP370TConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LSNUP370TConfiguration`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in LSNGWLoopConfigurationDevicesInner with anyOf schemas: LSNEMK36Configuration, LSNEMK36SConfiguration, LSNND100Configuration, LSNND200Configuration, LSNSKA100Configuration, LSNStdIntr50Configuration, LSNStdIntr51Configuration, LSNStdIntr52Configuration, LSNStdIntr53Configuration, LSNStdIntr54Configuration, LSNStdIntr55Configuration, LSNStdIntr56Configuration, LSNUP370TConfiguration. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[LSNEMK36Configuration] = None
        try:
            instance.actual_instance = LSNEMK36Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[LSNEMK36SConfiguration] = None
        try:
            instance.actual_instance = LSNEMK36SConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[LSNSKA100Configuration] = None
        try:
            instance.actual_instance = LSNSKA100Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[LSNStdIntr50Configuration] = None
        try:
            instance.actual_instance = LSNStdIntr50Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[LSNStdIntr51Configuration] = None
        try:
            instance.actual_instance = LSNStdIntr51Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[LSNStdIntr52Configuration] = None
        try:
            instance.actual_instance = LSNStdIntr52Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_7_validator: Optional[LSNStdIntr53Configuration] = None
        try:
            instance.actual_instance = LSNStdIntr53Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_8_validator: Optional[LSNStdIntr54Configuration] = None
        try:
            instance.actual_instance = LSNStdIntr54Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_9_validator: Optional[LSNStdIntr55Configuration] = None
        try:
            instance.actual_instance = LSNStdIntr55Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_10_validator: Optional[LSNStdIntr56Configuration] = None
        try:
            instance.actual_instance = LSNStdIntr56Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_11_validator: Optional[LSNND100Configuration] = None
        try:
            instance.actual_instance = LSNND100Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_12_validator: Optional[LSNND200Configuration] = None
        try:
            instance.actual_instance = LSNND200Configuration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_13_validator: Optional[LSNUP370TConfiguration] = None
        try:
            instance.actual_instance = LSNUP370TConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into LSNGWLoopConfigurationDevicesInner with anyOf schemas: LSNEMK36Configuration, LSNEMK36SConfiguration, LSNND100Configuration, LSNND200Configuration, LSNSKA100Configuration, LSNStdIntr50Configuration, LSNStdIntr51Configuration, LSNStdIntr52Configuration, LSNStdIntr53Configuration, LSNStdIntr54Configuration, LSNStdIntr55Configuration, LSNStdIntr56Configuration, LSNUP370TConfiguration. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], LSNEMK36Configuration, LSNEMK36SConfiguration, LSNND100Configuration, LSNND200Configuration, LSNSKA100Configuration, LSNStdIntr50Configuration, LSNStdIntr51Configuration, LSNStdIntr52Configuration, LSNStdIntr53Configuration, LSNStdIntr54Configuration, LSNStdIntr55Configuration, LSNStdIntr56Configuration, LSNUP370TConfiguration]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


