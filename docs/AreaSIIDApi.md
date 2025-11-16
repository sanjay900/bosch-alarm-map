# bosch_alarm_map.AreaSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_area_siid**](AreaSIIDApi.md#get_area_siid) | **GET** /{area_SIID} | Status retrieval of an individual area
[**post_area_siid**](AreaSIIDApi.md#post_area_siid) | **POST** /{area_SIID} | Control individual area


# **get_area_siid**
> Area get_area_siid(area_siid)

Status retrieval of an individual area

The area resource represents an individual area that is configured with the MAP system. Clients that
are not aware of the available areas can use the AreaList resource /areas , to inspect the
areas that are configured with MAP system. In the current version of the specification each area is
accessible at a location corresponding to its SIID. For example, an area with the SIID
1.1.Area.2.5 is accessible under /1.1.Area.2.5.
The area resource itself provides information about the current area state including whether it
can be armed or disarmed. Further, arming and disarming of an area is supported, as well as
control over test modes and the chime mode. <br>


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.area import Area
from bosch_alarm_map.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://169.254.10.10
# See configuration.py for a list of all supported configuration parameters.
configuration = bosch_alarm_map.Configuration(
    host = "https://169.254.10.10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with bosch_alarm_map.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bosch_alarm_map.AreaSIIDApi(api_client)
    area_siid = '/1.1.Area.2.2' # str | Unique area SIID. You can get all existing area SIIDs with the command GET /areas 

    try:
        # Status retrieval of an individual area
        api_response = api_instance.get_area_siid(area_siid)
        print("The response of AreaSIIDApi->get_area_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AreaSIIDApi->get_area_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_siid** | **str**| Unique area SIID. You can get all existing area SIIDs with the command GET /areas  | 

### Return type

[**Area**](Area.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_area_siid**
> AreaPostResponses post_area_siid(area_siid, post_area_siid_request)

Control individual area

The area resource represents an individual area that is configured with the MAP system. Clients that
are not aware of the available areas can use the AreaList resource /areas, to inspect the
areas that are configured with MAP panel. In the current version of the specification each area is
accessible at a location corresponding to its SIID. For example, an area with the SIID
1.1.Area.2.5 is accessible under /1.1.Area.2.5.
The area resource itself provides information about the current area state including whether it
can be armed or disarmed. Further, arming and disarming of an area is supported, as well as
control over test modes and the chime mode. For the following area functions an example with explanation is attached: <br>

- Arm area
- Disarm area
- Start Walktest
- Stop Walktest
- start motion detector test
- Stop Motion Detector Test
- Start Chime Mode
- Stop Chime Mode
- Start Bell Test
- ArmingInfo


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.area_post_responses import AreaPostResponses
from bosch_alarm_map.models.post_area_siid_request import PostAreaSIIDRequest
from bosch_alarm_map.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://169.254.10.10
# See configuration.py for a list of all supported configuration parameters.
configuration = bosch_alarm_map.Configuration(
    host = "https://169.254.10.10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with bosch_alarm_map.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bosch_alarm_map.AreaSIIDApi(api_client)
    area_siid = '/1.1.Area.2.2' # str | Unique area SIID.
    post_area_siid_request = {"@cmd":"ARM","bypassOffNormalDevices":false,"exitDelay":"ZERO"} # PostAreaSIIDRequest | 

    try:
        # Control individual area
        api_response = api_instance.post_area_siid(area_siid, post_area_siid_request)
        print("The response of AreaSIIDApi->post_area_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AreaSIIDApi->post_area_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_siid** | **str**| Unique area SIID. | 
 **post_area_siid_request** | [**PostAreaSIIDRequest**](PostAreaSIIDRequest.md)|  | 

### Return type

[**AreaPostResponses**](AreaPostResponses.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**202** | Accepted &lt;br&gt; This response code indicates that the request has been accepted but the processing has not been completed. The request may or may not succeed.  |  -  |
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**409** | Conflict. This command code is returned when a command is not executed due to application specific reasons. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. Trying to start a walktest in an area which is currently running a walktest is rejected with a 409 return code and the defined String content (not JSON). The currently running walktest remains unchanged and running. In case a client wants to restart a walktest, it needs to first stop the walktest and then start a new one.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

