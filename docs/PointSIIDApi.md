# bosch-alarm-map.PointSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_point_siid**](PointSIIDApi.md#get_point_siid) | **GET** /{point_SIID} | Individual point
[**post_point_siid**](PointSIIDApi.md#post_point_siid) | **POST** /{point_SIID} | Enable/Disable  point


# **get_point_siid**
> Point get_point_siid(point_siid)

Individual point

Get all information from a specific point in the system

### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.point import Point
from bosch-alarm-map.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://169.254.10.10
# See configuration.py for a list of all supported configuration parameters.
configuration = bosch-alarm-map.Configuration(
    host = "https://169.254.10.10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with bosch-alarm-map.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bosch-alarm-map.PointSIIDApi(api_client)
    point_siid = '/1.1.Point.1001.9' # str | Unique point SIID. You can get all existing points IDs with the command GET /points

    try:
        # Individual point
        api_response = api_instance.get_point_siid(point_siid)
        print("The response of PointSIIDApi->get_point_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointSIIDApi->get_point_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point_siid** | **str**| Unique point SIID. You can get all existing points IDs with the command GET /points | 

### Return type

[**Point**](Point.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_point_siid**
> post_point_siid(point_siid, device_enable_disable)

Enable/Disable  point

Enable/Disable a specific point in the system

### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.device_enable_disable import DeviceEnableDisable
from bosch-alarm-map.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://169.254.10.10
# See configuration.py for a list of all supported configuration parameters.
configuration = bosch-alarm-map.Configuration(
    host = "https://169.254.10.10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with bosch-alarm-map.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bosch-alarm-map.PointSIIDApi(api_client)
    point_siid = '/1.1.Point.1001.9' # str | 
    device_enable_disable = {"@cmd":"ENABLE"} # DeviceEnableDisable | 

    try:
        # Enable/Disable  point
        api_instance.post_point_siid(point_siid, device_enable_disable)
    except Exception as e:
        print("Exception when calling PointSIIDApi->post_point_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point_siid** | **str**|  | 
 **device_enable_disable** | [**DeviceEnableDisable**](DeviceEnableDisable.md)|  | 

### Return type

void (empty response body)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted &lt;br&gt; This response code indicates that the request has been accepted but the processing has not been completed. The request may or may not succeed.  |  -  |
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**409** | Conflict. Each point must be assigned to an area. To solve this, assign an area to the point using the RPS for MAP. |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

