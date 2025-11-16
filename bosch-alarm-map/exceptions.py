# coding: utf-8

"""
    REST-API_basic

    # Overview   This document specifies the MAP REST-API (OII) - **O**pen **I**ntrusion **I**nterface (**OII**).  The REST-API (former known as **O**pen **I**ntrusion **I**nterface [**OII**]), is implemented on the MAP system. This document is fully valid to the MAP panel firmware Version: <br> <br> **MAP_Update.1.4.0272.tar.bz2**<br>  To be backward compatible, all \"/get\", \"/post\" and other commands which includes \"OII\", will be still \"OII\".  New implemented features will be named as \"REST-API\" instead of \"OII\".  Please note that the following rules have been ignored when checking the OpenAPI documentation file against errors and warnings:   - [no-identical-paths](https://redocly.com/docs/cli/rules/no-identical-paths/)   - [no-ambiguous-paths](https://redocly.com/docs/cli/rules/no-ambiguous-paths/)   - [spec](https://redocly.com/docs/cli/rules/spec/)  The OpenAPI file is structured in the following groups: 1. REST-API_basic 2. REST-API_MUM  ## 1: REST-API_basic  All URLs described under this group contain all functions of released MAP panel firmware version 1.4.0176 All REST-API (OII) functions are also described in the following previous documents (PDF):     - ApplicationNotes.pdf   - BaseSpecification.pdf   - ResourceModel.pdf  This previous REST-API (OII) documentation can be downloaded [here](https://media.boschsecurity.com/fs/media/pb/media/extranet/map_partners/2019_oii_openintrusioninterface.zip). <br>   New features: - *Memory Info & statistics*     This feature is available from the MAP panel firmware version *<1.4.0xxx ToDo, replace*   - *NTP*  This feature is available from the MAP panel firmware version *<1.4.0xxx ToDo, replace*  - *supportfiles*     This feature is available from the MAP panel firmware version 1.4.0231  ## 2: REST-API_MUM  All URLs described in this group contain the features, which are added by the firmware version 1.4.0245   New Features: - *VDS2252 permissions*    Updated internal permissions with both mayClearMainPowerFailure and mayClearATS   ## HTTPS server certificates The MAP system is using so named \"unique self signed server certificates\" for HTTPS. The certificate files are created during the MAP panel start, if not already existing. Due to missing entropy and hardware resources, 2048-bit certificates are created. The MAP system guarantees those certificates will not change uncontrolled during lifetime. This guarantee is fullfilled by automated test during development.  ## General client requests   The MAP systems are **strongly limited** in hardware and software resources. This is why there are **limitations** using the MAP REST-API which **must** be considered to avoid erroneous behavior and a poor user experience.<br> - Use a ping to check the network availability **before** sending HTTP requests to the MAP panel. - The MAP panel can handle parallel requests. However, it is strongly recommended that a single client makes only serial requests.  - Parallel processing of many multiple requests will typically fail with negative response codes and overload the system. - Multiple requests to the same MAP panel must be serialized with a delay of at least 1 second between the last response and the next request. - The MAP panel might return the response codes 500 or a 503 or other response codes in case of overload. - Requests with HTTP Content-Length higher than 30000 bytes are not supported, HTTP Error Code 411 will be raised. - Receiving negative response codes caused by overload require a 60 seconds communication delay. - If the MAP panel does not (anymore) response at all, a delay of at least 5 minutes must be considered. - It is strongly recommended to use a connection pool for better HTTPS performance as well as lower CPU load on the MAP panel. - If the connection is cancelled or runs into timeout it is undefined whether the request will still be processed or not.  - After connection errors, the HTTPS connection must be closed and it is necessary again to check network availability by ping. - Cyclic request, e.g. ping, getting synchronization states and performing a time synchronization are allowed. - Cyclic request must not be more frequent than every 5 minutes. - Enabled **User Passcode Tamper** feature will prevent potential bruteforce attack. Retry count and lockout time is configurable via RPS for MAP. During the lockout any request will return code 401 for attacking IP. - In case of negative response codes, the client side should provide request and response logging to a file, with milliseconds timestamps, to support further analyses. - In case of interface errors or unexpected behaviour, the client side must provide request and response logging to a file, with milliseconds timestamps, e.g. activated by a client side debug level. - The MAP panel itself logs all database modifications, per default, to the history.log, what is strongly limited in number of entries and content. - The MAP panel itself does not log all HTTPS request and responses because of file system limitations. - TCP keepalive is enabled, lost connections will be dropped after 25 seconds.   ## HTTPS server limitations  Due to limited resources, MAP system generally does not process HTTPS requests simultaneously.  However, there are exceptions that are processed simultaneously: - **/syncstatus** - **/panel** - **/sub** - **/sub/\\*** - **/history**  All other URLs are executed sequentially.  Requests are queued and executed once execution units are available.  Simultaneous execution is limited to 3 simultaneous requests, processing time will be slower for multiple simultaneous requests.  Overloading REST-API can make MAP less responsive, in case of overload, the REST-API will generally respond with HTTP code 503, or, in case of heavy overload, will immediately close TCP socket without any response.    ## Response time guarantees  The following URLs have a guaranteed time, only if one HTTPS client connection at the same time.  The following URLs are guaranteed to execute their requests within 120 seconds: - **/history** - **/supportfile** - **/points** - **/couplers** - **/lsnauxs**  The following URLs are guaranteed to execute their requests within 60 seconds: - **/network** - **/syncstatus** - **/usermodellist** - **/outputs** - **/user** - **/mains** - **/groundfaults**  All other REST-API requests are guaranteed to be executed within 10 seconds.  ## License  Following URLs are only accessible with a valid MUM software license and only with a MAP-COM panel: - usermodel - usermodel/* - usermodellist - daymodel - daymodel/* - daymodellist - timemodel - timemodel/* - timemodellist - specialdaymodel - specialdaymodel/* - specialdaymodellist - smartkeymodel - smartkeymodel/* - smartkeymodellist - areaandtimemodel - areaandtimemodel/* - areaandtimemodellist - accessmodel - accessmodel/* - accessmodellist - permissionmodel - permissionmodel/* - permissionmodellist - mumusergroup - sharedkey - statistics - statistics/oii - statistics/db  Missing license will lead to HTTP 403 plain-text response, for example \"License missing MUM/usermodel\"  ## Security  Supported cipher suites:  **TLS1.3** (**recommended**) - TLS_AES_256_GCM_SHA384 - TLS_CHACHA20_POLY1305_SHA256 - TLS_AES_128_GCM_SHA256  **TLS1.2** - ECDHE-RSA-AES128-SHA256 - ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-RSA-AES256-SHA384 - ECDHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-SHA256 - DHE-RSA-AES128-GCM-SHA256 - DHE-RSA-AES256-SHA256 - DHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-SHA  **TLS1.0** (**deprecated**! Not recommended to be used, has to be manually enabled in MAP panel configuration via RPS for MAP) - AES128-SHA - AES256-SHA

    The version of the OpenAPI document: 1.4.0272, 18.09.2024
    Contact: intrusion.emea@de.bosch.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from typing import Any, Optional
from typing_extensions import Self

class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None,
                 key_type=None) -> None:
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiAttributeError(OpenApiException, AttributeError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Raised when an attribute reference or assignment fails.

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiAttributeError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(OpenApiException):

    def __init__(
        self, 
        status=None, 
        reason=None, 
        http_resp=None,
        *,
        body: Optional[str] = None,
        data: Optional[Any] = None,
    ) -> None:
        self.status = status
        self.reason = reason
        self.body = body
        self.data = data
        self.headers = None

        if http_resp:
            if self.status is None:
                self.status = http_resp.status
            if self.reason is None:
                self.reason = http_resp.reason
            if self.body is None:
                try:
                    self.body = http_resp.data.decode('utf-8')
                except Exception:
                    pass
            self.headers = http_resp.getheaders()

    @classmethod
    def from_response(
        cls, 
        *, 
        http_resp, 
        body: Optional[str], 
        data: Optional[Any],
    ) -> Self:
        if http_resp.status == 400:
            raise BadRequestException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 401:
            raise UnauthorizedException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 403:
            raise ForbiddenException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 404:
            raise NotFoundException(http_resp=http_resp, body=body, data=data)

        # Added new conditions for 409 and 422
        if http_resp.status == 409:
            raise ConflictException(http_resp=http_resp, body=body, data=data)

        if http_resp.status == 422:
            raise UnprocessableEntityException(http_resp=http_resp, body=body, data=data)

        if 500 <= http_resp.status <= 599:
            raise ServiceException(http_resp=http_resp, body=body, data=data)
        raise ApiException(http_resp=http_resp, body=body, data=data)

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.data or self.body:
            error_message += "HTTP response body: {0}\n".format(self.data or self.body)

        return error_message


class BadRequestException(ApiException):
    pass


class NotFoundException(ApiException):
    pass


class UnauthorizedException(ApiException):
    pass


class ForbiddenException(ApiException):
    pass


class ServiceException(ApiException):
    pass


class ConflictException(ApiException):
    """Exception for HTTP 409 Conflict."""
    pass


class UnprocessableEntityException(ApiException):
    """Exception for HTTP 422 Unprocessable Entity."""
    pass


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
