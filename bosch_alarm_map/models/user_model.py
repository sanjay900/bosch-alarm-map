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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UserModel(BaseModel):
    """
    UserModel
    """ # noqa: E501
    user_type: Optional[StrictStr] = Field(default=None, description="The userType value classifies users in two ways. - First, an Installer user has per default more privileges than a standard user. This rights are needed for example for maintenance work one the system. - Second, the userType defines if the user account is time-limited (*One-Time-Use* or *Temporary*) or not (*Standard*).   The User type *Standard* is active over the full system time, which is defined from 01.01.1970 to 19.01.2038.   Time-limited users are only active in a defined time period. To define this period the key values *activeFrom* and *activeUntil* are used to set a time interval.   The time period must be between 01.01.1970 - 19.01.2038. ", alias="userType")
    access_model: Optional[StrictStr] = Field(default=None, description="Name of an existing access Model", alias="accessModel")
    active: Optional[StrictBool] = Field(default=True, description="Identifies if the user is currently active and can access the MAP system.")
    active_from: Optional[StrictStr] = Field(default=None, description="Start date when user will be activated and can access the MAP system. If active is true the attribute activeFrom must not be used. ", alias="activeFrom")
    active_until: Optional[StrictStr] = Field(default=None, description="Date when the users access to the System expires. Used for Temporary User Types ", alias="activeUntil")
    smartkey_model_name: Optional[StrictStr] = Field(default=None, description="Name of an existing Smartkey Model, a part of Smartkey Profile set. Smartkey Profile is an optional attribute set, it up to 3 attributes Name - Access Type, Token. Name and Access Type must be specified together. 'Token Only' and 'Token And PINpad' Access Types require Token. ", alias="smartkeyModelName")
    is_oii_user: Optional[StrictBool] = Field(default=None, description="User have permission for REST-API (OII) ", alias="isOiiUser")
    is_oii_user_kp_user: Optional[StrictBool] = Field(default=None, description="User have permission for login from MAP Keypad ", alias="isOiiUserKpUser")
    language: Optional[StrictStr] = Field(default=None, description="The Language shown on the MAP Keypad when this user logs into the MAP system. Supported Languages: - English: en-US - German: de-DE - French: fr-FR - Dutch: nl-NL - Hungarian: hu-HU - Polish: pl-PL - Italian: it-IT - Russian: ru-RU - Spanish: es-ES - Czech: cs-CZ - Portuguese: pt-PT - Latvian: lv-LV - Romanian: ro-RO - Lithuanian: lt-LT - Ukrainian: uk-UK ")
    passcode_chng_rqd: Optional[StrictBool] = Field(default=None, description="Defines whether the user has to change the passcode at the next Login", alias="passcodeChngRqd")
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    passcode: Optional[StrictStr] = Field(default=None, description="6 digit numerical passcode for login from MAP Keypad")
    smartkey_access_type: Optional[StrictStr] = Field(default=None, description="'Token Only' and 'Token And PINpad' require Smartkey Token", alias="smartkeyAccessType")
    smartkey_token: Optional[StrictStr] = Field(default=None, description="Token for the Smartkey. 8 character long hexadecimal value. Must be unique for each user. Requires 'Token Only' and 'Token And PINpad' Smartkey Access Type", alias="smartkeyToken")
    oii_username: Optional[StrictStr] = Field(default=None, description="Username used for login authentication. It must be at least 8, but no more than 32 characters. It must only consist of characters with ASCII code 33, [ 35, 126]. The used oiiUsername must also be unique on the MAP system. If the selected oiiUsername is already used by another user on the MAP device, a 409 error response message is sent to the client. ", alias="oiiUsername")
    oii_password: Optional[StrictStr] = Field(default=None, description="Password used to login from REST-API. It must be at least 8, but no more than 16 characters. It must contain at least one UPPERCASE letter. It must contain at least one lowercase letter. It must contain at least one number digit. It must contain at least one special character: [ ! , @ $ % ^ * ? _ ~ - £ ( ) ]", alias="oiiPassword")
    use_extended_delay: Optional[StrictBool] = Field(default=None, description="This parameter determines whether the user requires extended entry/exit delay time", alias="useExtendedDelay")
    encrypted_secrets: Optional[StrictBool] = Field(default=False, description="Shows whether secrets are encrypted", alias="encryptedSecrets")
    duress_offset: Optional[Annotated[int, Field(le=9, strict=True, ge=0)]] = Field(default=1, description="Duress offset configures duress passcode. Duress passcode is not available for Installer User Type. Offset of 0 disables duress for user. To calculate duress passcode, last digit of user's passcode is ***incremented by offset amount***, incremented digit can wrap around. Example for passcode 123450: offset 1: duress 123451. Example for passcode 123459: offset 2: duress 123451.", alias="duressOffset")
    __properties: ClassVar[List[str]] = ["userType", "accessModel", "active", "activeFrom", "activeUntil", "smartkeyModelName", "isOiiUser", "isOiiUserKpUser", "language", "passcodeChngRqd", "firstName", "lastName", "passcode", "smartkeyAccessType", "smartkeyToken", "oiiUsername", "oiiPassword", "useExtendedDelay", "encryptedSecrets", "duressOffset"]

    @field_validator('user_type')
    def user_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Installer:Standard', 'Installer:One-Time-Use', 'Installer:Temporary', 'User:Standard', 'User:One-Time-Use', 'User:Temporary']):
            raise ValueError("must be one of enum values ('Installer:Standard', 'Installer:One-Time-Use', 'Installer:Temporary', 'User:Standard', 'User:One-Time-Use', 'User:Temporary')")
        return value

    @field_validator('language')
    def language_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['en-US', 'de-DE', 'fr-FR', 'nl-NL', 'hu-HU', 'pl-PL', 'it-IT', 'ru-RU', 'es-ES', 'cs-CZ', 'pt-PT', 'lv-LV', 'ro-RO', 'lt-LT', 'uk-UK']):
            raise ValueError("must be one of enum values ('en-US', 'de-DE', 'fr-FR', 'nl-NL', 'hu-HU', 'pl-PL', 'it-IT', 'ru-RU', 'es-ES', 'cs-CZ', 'pt-PT', 'lv-LV', 'ro-RO', 'lt-LT', 'uk-UK')")
        return value

    @field_validator('smartkey_access_type')
    def smartkey_access_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PINpad Only', 'Token Only', 'Token And PINpad']):
            raise ValueError("must be one of enum values ('PINpad Only', 'Token Only', 'Token And PINpad')")
        return value

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
        """Create an instance of UserModel from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "userType": obj.get("userType"),
            "accessModel": obj.get("accessModel"),
            "active": obj.get("active") if obj.get("active") is not None else True,
            "activeFrom": obj.get("activeFrom"),
            "activeUntil": obj.get("activeUntil"),
            "smartkeyModelName": obj.get("smartkeyModelName"),
            "isOiiUser": obj.get("isOiiUser"),
            "isOiiUserKpUser": obj.get("isOiiUserKpUser"),
            "language": obj.get("language"),
            "passcodeChngRqd": obj.get("passcodeChngRqd"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "passcode": obj.get("passcode"),
            "smartkeyAccessType": obj.get("smartkeyAccessType"),
            "smartkeyToken": obj.get("smartkeyToken"),
            "oiiUsername": obj.get("oiiUsername"),
            "oiiPassword": obj.get("oiiPassword"),
            "useExtendedDelay": obj.get("useExtendedDelay"),
            "encryptedSecrets": obj.get("encryptedSecrets") if obj.get("encryptedSecrets") is not None else False,
            "duressOffset": obj.get("duressOffset") if obj.get("duressOffset") is not None else 1
        })
        return _obj


