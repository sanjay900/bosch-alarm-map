# bosch-alarm-map.CouplerSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coupler_siid**](CouplerSIIDApi.md#get_coupler_siid) | **GET** /{coupler_SIID} | Individual coupler
[**post_coupler_siid**](CouplerSIIDApi.md#post_coupler_siid) | **POST** /{coupler_SIID} | Enable/Disable a coupler


# **get_coupler_siid**
> Coupler get_coupler_siid(coupler_siid)

Individual coupler

The type coupler_SIID lists the couplers and provides the same interface as device type.
It can be disabled. It cannot be bypassed or walktested.
The resource structure will contain attributes of device and disable.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.coupler import Coupler
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
    api_instance = bosch-alarm-map.CouplerSIIDApi(api_client)
    coupler_siid = '/1.1.Module.3001.6' # str | Unique coupler SIID. You can get all existing couplers SIIDs with the command GET /couplers

    try:
        # Individual coupler
        api_response = api_instance.get_coupler_siid(coupler_siid)
        print("The response of CouplerSIIDApi->get_coupler_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CouplerSIIDApi->get_coupler_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupler_siid** | **str**| Unique coupler SIID. You can get all existing couplers SIIDs with the command GET /couplers | 

### Return type

[**Coupler**](Coupler.md)

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

# **post_coupler_siid**
> post_coupler_siid(coupler_siid, device_enable_disable)

Enable/Disable a coupler

The type coupler_SIID lists the couplers and provides the same interface as device type.
It can be disabled. It cannot be bypassed or walktested.
The resource structure will contain attributes of device and disable.


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
    api_instance = bosch-alarm-map.CouplerSIIDApi(api_client)
    coupler_siid = '/1.1.Module.3001.6' # str | Unique coupler SIID. You can get all existing couplers SIIDs with the command GET /couplers
    device_enable_disable = {"@cmd":"ENABLE"} # DeviceEnableDisable | 

    try:
        # Enable/Disable a coupler
        api_instance.post_coupler_siid(coupler_siid, device_enable_disable)
    except Exception as e:
        print("Exception when calling CouplerSIIDApi->post_coupler_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupler_siid** | **str**| Unique coupler SIID. You can get all existing couplers SIIDs with the command GET /couplers | 
 **device_enable_disable** | [**DeviceEnableDisable**](DeviceEnableDisable.md)|  | 

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
**409** | Conflict &lt;br&gt; This command code is returned when a command is not executed due to application specific reasons. The body of the error response will contain further information on why the command was not executed. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. The body of the response will contain the list of resource URLs which prevented execution of the command.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

