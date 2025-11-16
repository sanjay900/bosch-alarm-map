# bosch_alarm_map.AreasApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_areas**](AreasApi.md#get_areas) | **GET** /areas | List of all areas configured in the MAP system
[**post_areas**](AreasApi.md#post_areas) | **POST** /areas | Operation to multiple areas at the same time: 


# **get_areas**
> AreaList get_areas()

List of all areas configured in the MAP system

The AreaList resource wraps a list of areas, to provide status of and access to multiple areas at
the same time. The area list allows retrieval of status information of multiple areas. The areas that are to be
fetched are selected using query parameters (url). If no parameters are specified, the status of
all areas is provided.


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.area_list import AreaList
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
    api_instance = bosch_alarm_map.AreasApi(api_client)

    try:
        # List of all areas configured in the MAP system
        api_response = api_instance.get_areas()
        print("The response of AreasApi->get_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AreasApi->get_areas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AreaList**](AreaList.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AreaList object structure. The list object will only contain resources which match the defined filters given in the query parameters. |  -  |
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**409** | Conflict &lt;br&gt; This command code is returned when a command is not executed due to application specific reasons. The body of the error response will contain further information on why the command was not executed. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. The body of the response will contain the list of resource URLs which prevented execution of the command.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_areas**
> post_areas(post_areas_request)

Operation to multiple areas at the same time: 

The AreaList resource wraps a list of areas, to provide status of and access to multiple areas at
the same time. The area list allows retrieval of status information of multiple areas. The areas that are to be
fetched are selected using query parameters (url). If no parameters are specified, the status of
all areas is provided. For the following area functions an example with explanation is attached:
- Arm areas
- Disarm areas
- Start walktests
- Stop walktests
- Start motion detector tests
- Stop motion detector tests
- Start chime mode
- Stop chime mode
- Start bell test


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.post_areas_request import PostAreasRequest
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
    api_instance = bosch_alarm_map.AreasApi(api_client)
    post_areas_request = {"@cmd":"ARM","bypassOffNormalDevices":false,"exitDelay":"ZERO"} # PostAreasRequest | 

    try:
        # Operation to multiple areas at the same time: 
        api_instance.post_areas(post_areas_request)
    except Exception as e:
        print("Exception when calling AreasApi->post_areas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_areas_request** | [**PostAreasRequest**](PostAreasRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted &lt;br&gt; This response code indicates that the request has been accepted but the processing has not been completed. The request may or may not succeed.  |  -  |
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**409** | Conflict. Eexecution of the command was not possible. Possible Reasons: List of resource urls which prevented the command from being executed when ATOMIC is TRUE or the string describing that application rules prevented execution of the command on any element of the list. Will be only retrurned when atomic is false.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

