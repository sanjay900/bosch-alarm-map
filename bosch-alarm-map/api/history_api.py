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

from bosch-alarm-map.models.history import History

from bosch-alarm-map.api_client import ApiClient, RequestSerialized
from bosch-alarm-map.api_response import ApiResponse
from bosch-alarm-map.rest import RESTResponseType


class HistoryApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_history(
        self,
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
    ) -> History:
        """The history log consists of events in the MAP panel configured to be logged.

        The history resource provides access to the MAP panel history data base. Each entry in the history describes an event in the MAP panel that has been configured to be logged in the history. As the history consists of a large amount of entries, dedicated filters are defined that allow paged access to the history. Thus, a client does not need to fetch the complete history in one GET request. Due to its size, the history data resource does not create any events. MAP panel provides two separate history data bases: - main history, consists of events in the panel configured to be logged. - IPCHistory (IP Communicator History), consists only of events related to reporting over IP. IPCHistory is applicable only if the MAP panel has been configured to report over IP. Events in IPCHistory will not be logged in panel main history. A client will have to fetch events from main history and IPCHistory separately. The history in the MAP panel is implemented as a ring buffer causing older events to be deleted when the buffer is full. Thus, a client that wants to archive all events need to read out the history regularly to make sure that no events get overwritten before they could be fetched. Each history entry is following a fixed structure of: - Event id: Unique ID for this event - Timestamp: Time when the event occurred. Timestamp is ISO8601 compliant but not REST-API date time compliant as time zone is not included. - Event name: Human readable string describing the event - SIID: Id of the system element that triggered that event - Parameters: Additional information on the event in a key value fashion. Each key and value are separated by a “ = “ (two whitespaces + = ). Multiple key value pairs are separated by a “\\n”, which is a JSON reserved character. For example, the keys IsMandatory and ModifierUser_ID are represented as IsMandatory = No\\nModifierUser_ID = 2\\n The history resource is represented as a JSON structure which contains an array of history entries. Each history entry contains the above defined fields separated by a semicolon “;”. For example: \"883953013;2014-07-24T13:24:13.256;RPS Accessed the System;TA_OCCUR;1.1.System.4.1;IsMandatory = No\\n\" 

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

        _param = self._get_history_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "History",
            '401': None,
            '403': None,
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
    def get_history_with_http_info(
        self,
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
    ) -> ApiResponse[History]:
        """The history log consists of events in the MAP panel configured to be logged.

        The history resource provides access to the MAP panel history data base. Each entry in the history describes an event in the MAP panel that has been configured to be logged in the history. As the history consists of a large amount of entries, dedicated filters are defined that allow paged access to the history. Thus, a client does not need to fetch the complete history in one GET request. Due to its size, the history data resource does not create any events. MAP panel provides two separate history data bases: - main history, consists of events in the panel configured to be logged. - IPCHistory (IP Communicator History), consists only of events related to reporting over IP. IPCHistory is applicable only if the MAP panel has been configured to report over IP. Events in IPCHistory will not be logged in panel main history. A client will have to fetch events from main history and IPCHistory separately. The history in the MAP panel is implemented as a ring buffer causing older events to be deleted when the buffer is full. Thus, a client that wants to archive all events need to read out the history regularly to make sure that no events get overwritten before they could be fetched. Each history entry is following a fixed structure of: - Event id: Unique ID for this event - Timestamp: Time when the event occurred. Timestamp is ISO8601 compliant but not REST-API date time compliant as time zone is not included. - Event name: Human readable string describing the event - SIID: Id of the system element that triggered that event - Parameters: Additional information on the event in a key value fashion. Each key and value are separated by a “ = “ (two whitespaces + = ). Multiple key value pairs are separated by a “\\n”, which is a JSON reserved character. For example, the keys IsMandatory and ModifierUser_ID are represented as IsMandatory = No\\nModifierUser_ID = 2\\n The history resource is represented as a JSON structure which contains an array of history entries. Each history entry contains the above defined fields separated by a semicolon “;”. For example: \"883953013;2014-07-24T13:24:13.256;RPS Accessed the System;TA_OCCUR;1.1.System.4.1;IsMandatory = No\\n\" 

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

        _param = self._get_history_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "History",
            '401': None,
            '403': None,
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
    def get_history_without_preload_content(
        self,
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
        """The history log consists of events in the MAP panel configured to be logged.

        The history resource provides access to the MAP panel history data base. Each entry in the history describes an event in the MAP panel that has been configured to be logged in the history. As the history consists of a large amount of entries, dedicated filters are defined that allow paged access to the history. Thus, a client does not need to fetch the complete history in one GET request. Due to its size, the history data resource does not create any events. MAP panel provides two separate history data bases: - main history, consists of events in the panel configured to be logged. - IPCHistory (IP Communicator History), consists only of events related to reporting over IP. IPCHistory is applicable only if the MAP panel has been configured to report over IP. Events in IPCHistory will not be logged in panel main history. A client will have to fetch events from main history and IPCHistory separately. The history in the MAP panel is implemented as a ring buffer causing older events to be deleted when the buffer is full. Thus, a client that wants to archive all events need to read out the history regularly to make sure that no events get overwritten before they could be fetched. Each history entry is following a fixed structure of: - Event id: Unique ID for this event - Timestamp: Time when the event occurred. Timestamp is ISO8601 compliant but not REST-API date time compliant as time zone is not included. - Event name: Human readable string describing the event - SIID: Id of the system element that triggered that event - Parameters: Additional information on the event in a key value fashion. Each key and value are separated by a “ = “ (two whitespaces + = ). Multiple key value pairs are separated by a “\\n”, which is a JSON reserved character. For example, the keys IsMandatory and ModifierUser_ID are represented as IsMandatory = No\\nModifierUser_ID = 2\\n The history resource is represented as a JSON structure which contains an array of history entries. Each history entry contains the above defined fields separated by a semicolon “;”. For example: \"883953013;2014-07-24T13:24:13.256;RPS Accessed the System;TA_OCCUR;1.1.System.4.1;IsMandatory = No\\n\" 

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

        _param = self._get_history_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "History",
            '401': None,
            '403': None,
            '414': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_history_serialize(
        self,
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
            resource_path='/history',
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


