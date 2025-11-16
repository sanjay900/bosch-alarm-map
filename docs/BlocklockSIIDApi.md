# openapi_client.BlocklockSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_blocklock_siid**](BlocklockSIIDApi.md#get_blocklock_siid) | **GET** /{blocklock_SIID} | Individual blocklock device
[**post_blocklock_siid**](BlocklockSIIDApi.md#post_blocklock_siid) | **POST** /{blocklock_SIID} | Enable/Disable a blocklock


# **get_blocklock_siid**
> Blocklock get_blocklock_siid(blocklock_siid)

Individual blocklock device

The type blocklocks is an additional resource type which provides the same interface as the
armingDevice type and models the blocklock on MAP system. It can be disabled and
bypassed. This resource type cannot be walktested.
The resource structure will contain attributes of device, disable, bypassed and armingDevice.


### Example


```python
import openapi_client
from openapi_client.models.blocklock import Blocklock
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
    api_instance = openapi_client.BlocklockSIIDApi(api_client)
    blocklock_siid = '/1.1.ArmingDevice.3001.26' # str | Unique blocklock SIID. You can get all existing blocklocks SIIDs with the command GET /blocklocks

    try:
        # Individual blocklock device
        api_response = api_instance.get_blocklock_siid(blocklock_siid)
        print("The response of BlocklockSIIDApi->get_blocklock_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlocklockSIIDApi->get_blocklock_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocklock_siid** | **str**| Unique blocklock SIID. You can get all existing blocklocks SIIDs with the command GET /blocklocks | 

### Return type

[**Blocklock**](Blocklock.md)

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
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_blocklock_siid**
> post_blocklock_siid(blocklock_siid, post_batteries_request)

Enable/Disable a blocklock

The type blocklock_SIID is an additional resource type which provides the same interface as the
armingDevice type and models the blocklock on MAP system. It can be disabled and
bypassed. This resource type cannot be walktested.
The resource structure will contain attributes of device, disable, bypassed and armingDevice.


### Example


```python
import openapi_client
from openapi_client.models.post_batteries_request import PostBatteriesRequest
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
    api_instance = openapi_client.BlocklockSIIDApi(api_client)
    blocklock_siid = '/1.1.ArmingDevice.3001.26' # str | Unique blocklock SIID. You can get all existing blocklocks SIIDs with the command GET /blocklocks
    post_batteries_request = {"@cmd":"ENABLE"} # PostBatteriesRequest | 

    try:
        # Enable/Disable a blocklock
        api_instance.post_blocklock_siid(blocklock_siid, post_batteries_request)
    except Exception as e:
        print("Exception when calling BlocklockSIIDApi->post_blocklock_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocklock_siid** | **str**| Unique blocklock SIID. You can get all existing blocklocks SIIDs with the command GET /blocklocks | 
 **post_batteries_request** | [**PostBatteriesRequest**](PostBatteriesRequest.md)|  | 

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

