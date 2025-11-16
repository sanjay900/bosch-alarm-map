# openapi_client.LsnauxsApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lsnauxs**](LsnauxsApi.md#get_lsnauxs) | **GET** /lsnauxs | List of LSN auxiliary power outlets in the MAP system
[**post_lsnauxs**](LsnauxsApi.md#post_lsnauxs) | **POST** /lsnauxs | Enable/Disable all lsnauxs


# **get_lsnauxs**
> LsnauxList get_lsnauxs()

List of LSN auxiliary power outlets in the MAP system

The resource type lsnAux lists the LSN Aux power on the LSN Gateway. It extends
device resource type. This resource type can be disabled. This resource type cannot be bypassed or walktested. The resource structure will
contain attributes of disable.


### Example


```python
import openapi_client
from openapi_client.models.lsnaux_list import LsnauxList
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
    api_instance = openapi_client.LsnauxsApi(api_client)

    try:
        # List of LSN auxiliary power outlets in the MAP system
        api_response = api_instance.get_lsnauxs()
        print("The response of LsnauxsApi->get_lsnauxs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LsnauxsApi->get_lsnauxs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LsnauxList**](LsnauxList.md)

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

# **post_lsnauxs**
> post_lsnauxs(device_enable_disable)

Enable/Disable all lsnauxs

The resource type lsnAux lists the LSN Aux power on the LSN Gateway. It extends
device resource type. This resource type can be disabled. This resource type cannot be bypassed or walktested. The resource structure will
contain attributes of disable.


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
    api_instance = openapi_client.LsnauxsApi(api_client)
    device_enable_disable = {"@cmd":"ENABLE"} # DeviceEnableDisable | 

    try:
        # Enable/Disable all lsnauxs
        api_instance.post_lsnauxs(device_enable_disable)
    except Exception as e:
        print("Exception when calling LsnauxsApi->post_lsnauxs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

