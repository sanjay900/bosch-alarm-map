# openapi_client.LsnbusSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lsnbus_siid**](LsnbusSIIDApi.md#get_lsnbus_siid) | **GET** /{lsnbus_SIID} | Individual LSN Bus
[**post_lsnbus_siid**](LsnbusSIIDApi.md#post_lsnbus_siid) | **POST** /{lsnbus_SIID} | Enable/Disable a LSN Bus


# **get_lsnbus_siid**
> Lsnbus get_lsnbus_siid(lsnbus_siid)

Individual LSN Bus

The resource type lsnBus lists the LSN loop and LSN Stub on the LSN Gateway.
It provides the same interface as the resource type device.
The resource structure will contain attributes of device and disable.


### Example


```python
import openapi_client
from openapi_client.models.lsnbus import Lsnbus
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://169.254.10.10
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://169.254.10.10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LsnbusSIIDApi(api_client)
    lsnbus_siid = '/1.1.Gateway.8001.2' # str | Unique lsnbus SIID. You can get all existing lsnbuses IDs with the command GET /lsnbuses

    try:
        # Individual LSN Bus
        api_response = api_instance.get_lsnbus_siid(lsnbus_siid)
        print("The response of LsnbusSIIDApi->get_lsnbus_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LsnbusSIIDApi->get_lsnbus_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lsnbus_siid** | **str**| Unique lsnbus SIID. You can get all existing lsnbuses IDs with the command GET /lsnbuses | 

### Return type

[**Lsnbus**](Lsnbus.md)

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

# **post_lsnbus_siid**
> post_lsnbus_siid(lsnbus_siid, device_enable_disable)

Enable/Disable a LSN Bus

The resource type lsnBus lists the LSN loop and LSN Stub on the LSN Gateway.
It provides the same interface as the resource type device. This resource type can be disabled. This resource type cannot be bypassed or walktested.
The resource structure will contain attributes of device and disable.


### Example


```python
import openapi_client
from openapi_client.models.device_enable_disable import DeviceEnableDisable
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://169.254.10.10
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://169.254.10.10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LsnbusSIIDApi(api_client)
    lsnbus_siid = '/1.1.Gateway.8001.2' # str | 
    device_enable_disable = {"@cmd":"ENABLE"} # DeviceEnableDisable | 

    try:
        # Enable/Disable a LSN Bus
        api_instance.post_lsnbus_siid(lsnbus_siid, device_enable_disable)
    except Exception as e:
        print("Exception when calling LsnbusSIIDApi->post_lsnbus_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lsnbus_siid** | **str**|  | 
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
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

