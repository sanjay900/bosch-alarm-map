# coding: utf-8

"""
    REST-API_basic

    # Overview   This document specifies the MAP REST-API (OII) - **O**pen **I**ntrusion **I**nterface (**OII**).  The REST-API (former known as **O**pen **I**ntrusion **I**nterface [**OII**]), is implemented on the MAP system. This document is fully valid to the MAP panel firmware Version: <br> <br> **MAP_Update.1.4.0272.tar.bz2**<br>  To be backward compatible, all \"/get\", \"/post\" and other commands which includes \"OII\", will be still \"OII\".  New implemented features will be named as \"REST-API\" instead of \"OII\".  Please note that the following rules have been ignored when checking the OpenAPI documentation file against errors and warnings:   - [no-identical-paths](https://redocly.com/docs/cli/rules/no-identical-paths/)   - [no-ambiguous-paths](https://redocly.com/docs/cli/rules/no-ambiguous-paths/)   - [spec](https://redocly.com/docs/cli/rules/spec/)  The OpenAPI file is structured in the following groups: 1. REST-API_basic 2. REST-API_MUM  ## 1: REST-API_basic  All URLs described under this group contain all functions of released MAP panel firmware version 1.4.0176 All REST-API (OII) functions are also described in the following previous documents (PDF):     - ApplicationNotes.pdf   - BaseSpecification.pdf   - ResourceModel.pdf  This previous REST-API (OII) documentation can be downloaded [here](https://media.boschsecurity.com/fs/media/pb/media/extranet/map_partners/2019_oii_openintrusioninterface.zip). <br>   New features: - *Memory Info & statistics*     This feature is available from the MAP panel firmware version *<1.4.0xxx ToDo, replace*   - *NTP*  This feature is available from the MAP panel firmware version *<1.4.0xxx ToDo, replace*  - *supportfiles*     This feature is available from the MAP panel firmware version 1.4.0231  ## 2: REST-API_MUM  All URLs described in this group contain the features, which are added by the firmware version 1.4.0245   New Features: - *VDS2252 permissions*    Updated internal permissions with both mayClearMainPowerFailure and mayClearATS   ## HTTPS server certificates The MAP system is using so named \"unique self signed server certificates\" for HTTPS. The certificate files are created during the MAP panel start, if not already existing. Due to missing entropy and hardware resources, 2048-bit certificates are created. The MAP system guarantees those certificates will not change uncontrolled during lifetime. This guarantee is fullfilled by automated test during development.  ## General client requests   The MAP systems are **strongly limited** in hardware and software resources. This is why there are **limitations** using the MAP REST-API which **must** be considered to avoid erroneous behavior and a poor user experience.<br> - Use a ping to check the network availability **before** sending HTTP requests to the MAP panel. - The MAP panel can handle parallel requests. However, it is strongly recommended that a single client makes only serial requests.  - Parallel processing of many multiple requests will typically fail with negative response codes and overload the system. - Multiple requests to the same MAP panel must be serialized with a delay of at least 1 second between the last response and the next request. - The MAP panel might return the response codes 500 or a 503 or other response codes in case of overload. - Requests with HTTP Content-Length higher than 30000 bytes are not supported, HTTP Error Code 411 will be raised. - Receiving negative response codes caused by overload require a 60 seconds communication delay. - If the MAP panel does not (anymore) response at all, a delay of at least 5 minutes must be considered. - It is strongly recommended to use a connection pool for better HTTPS performance as well as lower CPU load on the MAP panel. - If the connection is cancelled or runs into timeout it is undefined whether the request will still be processed or not.  - After connection errors, the HTTPS connection must be closed and it is necessary again to check network availability by ping. - Cyclic request, e.g. ping, getting synchronization states and performing a time synchronization are allowed. - Cyclic request must not be more frequent than every 5 minutes. - Enabled **User Passcode Tamper** feature will prevent potential bruteforce attack. Retry count and lockout time is configurable via RPS for MAP. During the lockout any request will return code 401 for attacking IP. - In case of negative response codes, the client side should provide request and response logging to a file, with milliseconds timestamps, to support further analyses. - In case of interface errors or unexpected behaviour, the client side must provide request and response logging to a file, with milliseconds timestamps, e.g. activated by a client side debug level. - The MAP panel itself logs all database modifications, per default, to the history.log, what is strongly limited in number of entries and content. - The MAP panel itself does not log all HTTPS request and responses because of file system limitations. - TCP keepalive is enabled, lost connections will be dropped after 25 seconds.   ## HTTPS server limitations  Due to limited resources, MAP system generally does not process HTTPS requests simultaneously.  However, there are exceptions that are processed simultaneously: - **/syncstatus** - **/panel** - **/sub** - **/sub/\\*** - **/history**  All other URLs are executed sequentially.  Requests are queued and executed once execution units are available.  Simultaneous execution is limited to 3 simultaneous requests, processing time will be slower for multiple simultaneous requests.  Overloading REST-API can make MAP less responsive, in case of overload, the REST-API will generally respond with HTTP code 503, or, in case of heavy overload, will immediately close TCP socket without any response.    ## Response time guarantees  The following URLs have a guaranteed time, only if one HTTPS client connection at the same time.  The following URLs are guaranteed to execute their requests within 120 seconds: - **/history** - **/supportfile** - **/points** - **/couplers** - **/lsnauxs**  The following URLs are guaranteed to execute their requests within 60 seconds: - **/network** - **/syncstatus** - **/usermodellist** - **/outputs** - **/user** - **/mains** - **/groundfaults**  All other REST-API requests are guaranteed to be executed within 10 seconds.  ## License  Following URLs are only accessible with a valid MUM software license and only with a MAP-COM panel: - usermodel - usermodel/* - usermodellist - daymodel - daymodel/* - daymodellist - timemodel - timemodel/* - timemodellist - specialdaymodel - specialdaymodel/* - specialdaymodellist - smartkeymodel - smartkeymodel/* - smartkeymodellist - areaandtimemodel - areaandtimemodel/* - areaandtimemodellist - accessmodel - accessmodel/* - accessmodellist - permissionmodel - permissionmodel/* - permissionmodellist - mumusergroup - sharedkey - statistics - statistics/oii - statistics/db  Missing license will lead to HTTP 403 plain-text response, for example \"License missing MUM/usermodel\"  ## Security  Supported cipher suites:  **TLS1.3** (**recommended**) - TLS_AES_256_GCM_SHA384 - TLS_CHACHA20_POLY1305_SHA256 - TLS_AES_128_GCM_SHA256  **TLS1.2** - ECDHE-RSA-AES128-SHA256 - ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-RSA-AES256-SHA384 - ECDHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-SHA256 - DHE-RSA-AES128-GCM-SHA256 - DHE-RSA-AES256-SHA256 - DHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-SHA  **TLS1.0** (**deprecated**! Not recommended to be used, has to be manually enabled in MAP panel configuration via RPS for MAP) - AES128-SHA - AES256-SHA

    The version of the OpenAPI document: 1.4.0272, 18.09.2024
    Contact: intrusion.emea@de.bosch.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from bosch_alarm_map.models.fetch_events import FetchEvents
from bosch_alarm_map.models.fetched_events import FetchedEvents
from bosch_alarm_map.models.sub import Sub

from bosch_alarm_map.api_client import ApiClient, RequestSerialized
from bosch_alarm_map.api_response import ApiResponse
from bosch_alarm_map.rest import RESTResponseType


class SubSIIDApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def delete_sub_siid(
        self,
        sub_siid: Annotated[StrictStr, Field(description="Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Unsubscribe

        This operation cancels a subscription. The MAP panel will free the event buffer associated to this subscription.

        :param sub_siid: Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  (required)
        :type sub_siid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_sub_siid_serialize(
            sub_siid=sub_siid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '401': None,
            '403': None,
            '409': None,
            '414': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_sub_siid_with_http_info(
        self,
        sub_siid: Annotated[StrictStr, Field(description="Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Unsubscribe

        This operation cancels a subscription. The MAP panel will free the event buffer associated to this subscription.

        :param sub_siid: Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  (required)
        :type sub_siid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_sub_siid_serialize(
            sub_siid=sub_siid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '401': None,
            '403': None,
            '409': None,
            '414': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_sub_siid_without_preload_content(
        self,
        sub_siid: Annotated[StrictStr, Field(description="Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Unsubscribe

        This operation cancels a subscription. The MAP panel will free the event buffer associated to this subscription.

        :param sub_siid: Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  (required)
        :type sub_siid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_sub_siid_serialize(
            sub_siid=sub_siid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '401': None,
            '403': None,
            '409': None,
            '414': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_sub_siid_serialize(
        self,
        sub_siid,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if sub_siid is not None:
            _path_params['sub_SIID'] = sub_siid
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'digest'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/sub/{sub_SIID}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_sub_siid(
        self,
        sub_siid: Annotated[StrictStr, Field(description="Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Sub:
        """Individual subscription resource

        The MAP panel provides event notifications for all resources. This *GET* function is used, to get a specific subscription resource.  ### Subscription Resource (/sub/*)  A resource representing individual, valid subscription of a client. This resource can be used to inspect the information about the current subscription, to fetch the events as well as to cancel the subscription. The link to the individual subscription is provided in the response to a subscription request. This resource is dynamically created and deleted during runtime. The MAP panel assures that the subscription resource URL is unique even over power cycles of the MAP panel. The URL shall be treated as an opaque identifier for the individual subscription. No semantics or sequence information shall be assumed by the client. 

        :param sub_siid: Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  (required)
        :type sub_siid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_sub_siid_serialize(
            sub_siid=sub_siid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Sub",
            '401': None,
            '403': None,
            '409': None,
            '414': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_sub_siid_with_http_info(
        self,
        sub_siid: Annotated[StrictStr, Field(description="Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Sub]:
        """Individual subscription resource

        The MAP panel provides event notifications for all resources. This *GET* function is used, to get a specific subscription resource.  ### Subscription Resource (/sub/*)  A resource representing individual, valid subscription of a client. This resource can be used to inspect the information about the current subscription, to fetch the events as well as to cancel the subscription. The link to the individual subscription is provided in the response to a subscription request. This resource is dynamically created and deleted during runtime. The MAP panel assures that the subscription resource URL is unique even over power cycles of the MAP panel. The URL shall be treated as an opaque identifier for the individual subscription. No semantics or sequence information shall be assumed by the client. 

        :param sub_siid: Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  (required)
        :type sub_siid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_sub_siid_serialize(
            sub_siid=sub_siid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Sub",
            '401': None,
            '403': None,
            '409': None,
            '414': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_sub_siid_without_preload_content(
        self,
        sub_siid: Annotated[StrictStr, Field(description="Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub ")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Individual subscription resource

        The MAP panel provides event notifications for all resources. This *GET* function is used, to get a specific subscription resource.  ### Subscription Resource (/sub/*)  A resource representing individual, valid subscription of a client. This resource can be used to inspect the information about the current subscription, to fetch the events as well as to cancel the subscription. The link to the individual subscription is provided in the response to a subscription request. This resource is dynamically created and deleted during runtime. The MAP panel assures that the subscription resource URL is unique even over power cycles of the MAP panel. The URL shall be treated as an opaque identifier for the individual subscription. No semantics or sequence information shall be assumed by the client. 

        :param sub_siid: Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  (required)
        :type sub_siid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_sub_siid_serialize(
            sub_siid=sub_siid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Sub",
            '401': None,
            '403': None,
            '409': None,
            '414': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_sub_siid_serialize(
        self,
        sub_siid,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if sub_siid is not None:
            _path_params['sub_SIID'] = sub_siid
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'digest'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/sub/{sub_SIID}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def post_sub_siid(
        self,
        sub_siid: Annotated[StrictStr, Field(description="Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub ")],
        fetch_events: FetchEvents,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> FetchedEvents:
        """Fetch events

        A client fetches events from the buffer of this subscription by using a POST request with the defined, optional parameters in the body of the request. Once events are successfully delivered to the client, they will be deleted from the internal event buffer. Thus events can only be fetched once.  Fetching the events is done by sending a POST request. <br> Parameters are defined to allow to control on the event delivery to the client. The available parameters are:  #### maxEvents  The maximum number of events contained in the answer to this request. If maxEvents is omitted, the number of events is set to the bufferSize of the subscription. maxEvents is used to assure that the client only fetches as much events as it can process in one batch.  #### minEvents  The minimum number of events contained in the answer to this request, i.e. a request will return when at least minEvents is available. If minEvents is omitted or minEvents is specified as 0, minEvents has the same value as maxEvents (at maximum the bufferSize of the subscription).  #### maxTime  The maximum time in seconds a request will block. When maxTime expires, the MAP panel will reply with the currently available events. If no events are available, an empty event list will be provided. The default value of maxTime is 0. Thus, if maxTime is omitted or set to 0 the request will return immediately with the available events (up to maxEvents). The maximum possible value for maxTime is 100. Thus the call will never block longer than for 100 seconds.<br><br>   The MAP panel will respond to a POST request as soon as the first of the previously specified conditions is fulfilled. Thus, in case minEvents is not reached, the answer will return after maxTime. In case minEvents is reached, the response is send immediately. By adjusting maxEvents, minEvents and maxTime the client has the opportunity to optimize the poling behaviour to its need. For example, when the client expects events rarely (e.g. alarm messages) it could set “minEvents”: 1 and “maxTime”: 100. Thereby, the client is notified as soon as a single event comes in. Using a long maxTime ensures that the poll request does not need to be repeated often. Similarly, if it is expected that many events come in (e.g. state changes in a disarmed area), the throughput can be improved by choosing a large minEvents number e.g. “minEvents”: 100 to make sure that the data is transmitted efficiently. maxEvents can be defined to ensure that not too many events are fetched which may not be possible to be handled by the client e.g “maxEvents”:200. In addition, a client can extend its lease by sending a request with “maxEvents” set to 0. Thereby, the lease is extended and the response does not contain any events. This is particularly useful, if the client is currently not able to process any events but wants to keep its subscription on the MAP panel. 

        :param sub_siid: Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  (required)
        :type sub_siid: str
        :param fetch_events: (required)
        :type fetch_events: FetchEvents
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_sub_siid_serialize(
            sub_siid=sub_siid,
            fetch_events=fetch_events,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FetchedEvents",
            '401': None,
            '403': None,
            '409': None,
            '414': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def post_sub_siid_with_http_info(
        self,
        sub_siid: Annotated[StrictStr, Field(description="Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub ")],
        fetch_events: FetchEvents,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[FetchedEvents]:
        """Fetch events

        A client fetches events from the buffer of this subscription by using a POST request with the defined, optional parameters in the body of the request. Once events are successfully delivered to the client, they will be deleted from the internal event buffer. Thus events can only be fetched once.  Fetching the events is done by sending a POST request. <br> Parameters are defined to allow to control on the event delivery to the client. The available parameters are:  #### maxEvents  The maximum number of events contained in the answer to this request. If maxEvents is omitted, the number of events is set to the bufferSize of the subscription. maxEvents is used to assure that the client only fetches as much events as it can process in one batch.  #### minEvents  The minimum number of events contained in the answer to this request, i.e. a request will return when at least minEvents is available. If minEvents is omitted or minEvents is specified as 0, minEvents has the same value as maxEvents (at maximum the bufferSize of the subscription).  #### maxTime  The maximum time in seconds a request will block. When maxTime expires, the MAP panel will reply with the currently available events. If no events are available, an empty event list will be provided. The default value of maxTime is 0. Thus, if maxTime is omitted or set to 0 the request will return immediately with the available events (up to maxEvents). The maximum possible value for maxTime is 100. Thus the call will never block longer than for 100 seconds.<br><br>   The MAP panel will respond to a POST request as soon as the first of the previously specified conditions is fulfilled. Thus, in case minEvents is not reached, the answer will return after maxTime. In case minEvents is reached, the response is send immediately. By adjusting maxEvents, minEvents and maxTime the client has the opportunity to optimize the poling behaviour to its need. For example, when the client expects events rarely (e.g. alarm messages) it could set “minEvents”: 1 and “maxTime”: 100. Thereby, the client is notified as soon as a single event comes in. Using a long maxTime ensures that the poll request does not need to be repeated often. Similarly, if it is expected that many events come in (e.g. state changes in a disarmed area), the throughput can be improved by choosing a large minEvents number e.g. “minEvents”: 100 to make sure that the data is transmitted efficiently. maxEvents can be defined to ensure that not too many events are fetched which may not be possible to be handled by the client e.g “maxEvents”:200. In addition, a client can extend its lease by sending a request with “maxEvents” set to 0. Thereby, the lease is extended and the response does not contain any events. This is particularly useful, if the client is currently not able to process any events but wants to keep its subscription on the MAP panel. 

        :param sub_siid: Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  (required)
        :type sub_siid: str
        :param fetch_events: (required)
        :type fetch_events: FetchEvents
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_sub_siid_serialize(
            sub_siid=sub_siid,
            fetch_events=fetch_events,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FetchedEvents",
            '401': None,
            '403': None,
            '409': None,
            '414': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def post_sub_siid_without_preload_content(
        self,
        sub_siid: Annotated[StrictStr, Field(description="Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub ")],
        fetch_events: FetchEvents,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Fetch events

        A client fetches events from the buffer of this subscription by using a POST request with the defined, optional parameters in the body of the request. Once events are successfully delivered to the client, they will be deleted from the internal event buffer. Thus events can only be fetched once.  Fetching the events is done by sending a POST request. <br> Parameters are defined to allow to control on the event delivery to the client. The available parameters are:  #### maxEvents  The maximum number of events contained in the answer to this request. If maxEvents is omitted, the number of events is set to the bufferSize of the subscription. maxEvents is used to assure that the client only fetches as much events as it can process in one batch.  #### minEvents  The minimum number of events contained in the answer to this request, i.e. a request will return when at least minEvents is available. If minEvents is omitted or minEvents is specified as 0, minEvents has the same value as maxEvents (at maximum the bufferSize of the subscription).  #### maxTime  The maximum time in seconds a request will block. When maxTime expires, the MAP panel will reply with the currently available events. If no events are available, an empty event list will be provided. The default value of maxTime is 0. Thus, if maxTime is omitted or set to 0 the request will return immediately with the available events (up to maxEvents). The maximum possible value for maxTime is 100. Thus the call will never block longer than for 100 seconds.<br><br>   The MAP panel will respond to a POST request as soon as the first of the previously specified conditions is fulfilled. Thus, in case minEvents is not reached, the answer will return after maxTime. In case minEvents is reached, the response is send immediately. By adjusting maxEvents, minEvents and maxTime the client has the opportunity to optimize the poling behaviour to its need. For example, when the client expects events rarely (e.g. alarm messages) it could set “minEvents”: 1 and “maxTime”: 100. Thereby, the client is notified as soon as a single event comes in. Using a long maxTime ensures that the poll request does not need to be repeated often. Similarly, if it is expected that many events come in (e.g. state changes in a disarmed area), the throughput can be improved by choosing a large minEvents number e.g. “minEvents”: 100 to make sure that the data is transmitted efficiently. maxEvents can be defined to ensure that not too many events are fetched which may not be possible to be handled by the client e.g “maxEvents”:200. In addition, a client can extend its lease by sending a request with “maxEvents” set to 0. Thereby, the lease is extended and the response does not contain any events. This is particularly useful, if the client is currently not able to process any events but wants to keep its subscription on the MAP panel. 

        :param sub_siid: Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  (required)
        :type sub_siid: str
        :param fetch_events: (required)
        :type fetch_events: FetchEvents
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_sub_siid_serialize(
            sub_siid=sub_siid,
            fetch_events=fetch_events,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FetchedEvents",
            '401': None,
            '403': None,
            '409': None,
            '414': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _post_sub_siid_serialize(
        self,
        sub_siid,
        fetch_events,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if sub_siid is not None:
            _path_params['sub_SIID'] = sub_siid
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if fetch_events is not None:
            _body_params = fetch_events


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'digest'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/sub/{sub_SIID}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


