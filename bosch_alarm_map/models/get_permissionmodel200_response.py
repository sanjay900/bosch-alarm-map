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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from bosch_alarm_map.models.permission_model_arm_category_permissions import PermissionModelArmCategoryPermissions
from bosch_alarm_map.models.permission_model_event_category_permissions import PermissionModelEventCategoryPermissions
from bosch_alarm_map.models.permission_model_maintenance_category_permissions import PermissionModelMaintenanceCategoryPermissions
from bosch_alarm_map.models.permission_model_operations_category_permissions import PermissionModelOperationsCategoryPermissions
from bosch_alarm_map.models.permission_model_remote_service_category_permissions import PermissionModelRemoteServiceCategoryPermissions
from bosch_alarm_map.models.permission_model_status_category_permissions import PermissionModelStatusCategoryPermissions
from bosch_alarm_map.models.permission_model_user_category_permissions import PermissionModelUserCategoryPermissions
from typing import Optional, Set
from typing_extensions import Self

class GetPermissionmodel200Response(BaseModel):
    """
    GetPermissionmodel200Response
    """ # noqa: E501
    permission_model_id: StrictStr = Field(description="Unique name of an existing permission model.  The name is used to identify the item on the MAP system. The following charaters are forbidden in identifier name: \" @ ; ", alias="permissionModelID")
    arm_category_permissions: Optional[PermissionModelArmCategoryPermissions] = Field(default=None, alias="armCategoryPermissions")
    event_category_permissions: Optional[PermissionModelEventCategoryPermissions] = Field(default=None, alias="eventCategoryPermissions")
    maintenance_category_permissions: Optional[PermissionModelMaintenanceCategoryPermissions] = Field(default=None, alias="maintenanceCategoryPermissions")
    operations_category_permissions: Optional[PermissionModelOperationsCategoryPermissions] = Field(default=None, alias="operationsCategoryPermissions")
    remote_service_category_permissions: Optional[PermissionModelRemoteServiceCategoryPermissions] = Field(default=None, alias="remoteServiceCategoryPermissions")
    status_category_permissions: Optional[PermissionModelStatusCategoryPermissions] = Field(default=None, alias="statusCategoryPermissions")
    user_category_permissions: Optional[PermissionModelUserCategoryPermissions] = Field(default=None, alias="userCategoryPermissions")
    permission_model_sync_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="Synchronization ID for the permission table. Will be changed for each change in the permission database table.", alias="permissionModelSyncID")
    __properties: ClassVar[List[str]] = ["permissionModelID", "armCategoryPermissions", "eventCategoryPermissions", "maintenanceCategoryPermissions", "operationsCategoryPermissions", "remoteServiceCategoryPermissions", "statusCategoryPermissions", "userCategoryPermissions", "permissionModelSyncID"]

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
        """Create an instance of GetPermissionmodel200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of arm_category_permissions
        if self.arm_category_permissions:
            _dict['armCategoryPermissions'] = self.arm_category_permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event_category_permissions
        if self.event_category_permissions:
            _dict['eventCategoryPermissions'] = self.event_category_permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maintenance_category_permissions
        if self.maintenance_category_permissions:
            _dict['maintenanceCategoryPermissions'] = self.maintenance_category_permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operations_category_permissions
        if self.operations_category_permissions:
            _dict['operationsCategoryPermissions'] = self.operations_category_permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of remote_service_category_permissions
        if self.remote_service_category_permissions:
            _dict['remoteServiceCategoryPermissions'] = self.remote_service_category_permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_category_permissions
        if self.status_category_permissions:
            _dict['statusCategoryPermissions'] = self.status_category_permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_category_permissions
        if self.user_category_permissions:
            _dict['userCategoryPermissions'] = self.user_category_permissions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetPermissionmodel200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "permissionModelID": obj.get("permissionModelID"),
            "armCategoryPermissions": PermissionModelArmCategoryPermissions.from_dict(obj["armCategoryPermissions"]) if obj.get("armCategoryPermissions") is not None else None,
            "eventCategoryPermissions": PermissionModelEventCategoryPermissions.from_dict(obj["eventCategoryPermissions"]) if obj.get("eventCategoryPermissions") is not None else None,
            "maintenanceCategoryPermissions": PermissionModelMaintenanceCategoryPermissions.from_dict(obj["maintenanceCategoryPermissions"]) if obj.get("maintenanceCategoryPermissions") is not None else None,
            "operationsCategoryPermissions": PermissionModelOperationsCategoryPermissions.from_dict(obj["operationsCategoryPermissions"]) if obj.get("operationsCategoryPermissions") is not None else None,
            "remoteServiceCategoryPermissions": PermissionModelRemoteServiceCategoryPermissions.from_dict(obj["remoteServiceCategoryPermissions"]) if obj.get("remoteServiceCategoryPermissions") is not None else None,
            "statusCategoryPermissions": PermissionModelStatusCategoryPermissions.from_dict(obj["statusCategoryPermissions"]) if obj.get("statusCategoryPermissions") is not None else None,
            "userCategoryPermissions": PermissionModelUserCategoryPermissions.from_dict(obj["userCategoryPermissions"]) if obj.get("userCategoryPermissions") is not None else None,
            "permissionModelSyncID": obj.get("permissionModelSyncID")
        })
        return _obj


