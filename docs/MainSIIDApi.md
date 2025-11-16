# openapi_client.MainSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_main_siid**](MainSIIDApi.md#get_main_siid) | **GET** /{main_SIID} | Individual main resource
[**post_main_siid**](MainSIIDApi.md#post_main_siid) | **POST** /{main_SIID} | Enable/Disable a main


# **get_main_siid**
> Main get_main_siid(main_siid)

Individual main resource

The resource type mains lists the alternating current (short: ac ) input of the power supply. It provides the same
interface as the resource type device.


### Example


```python
import openapi_client
from openapi_client.models.main import Main
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
    api_instance = openapi_client.MainSIIDApi(api_client)
    main_siid = '/1.1.PowerSupply.13001.4' # str | Unique main SIID. You can get all existing mains IDs with the command GET /mains

    try:
        # Individual main resource
        api_response = api_instance.get_main_siid(main_siid)
        print("The response of MainSIIDApi->get_main_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainSIIDApi->get_main_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main_siid** | **str**| Unique main SIID. You can get all existing mains IDs with the command GET /mains | 

### Return type

[**Main**](Main.md)

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

# **post_main_siid**
> post_main_siid(main_siid, post_batteries_request)

Enable/Disable a main

The resource type mains lists the alternating current (AC) input of the power supply. It provides the same interface as the resource type device.

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
    api_instance = openapi_client.MainSIIDApi(api_client)
    main_siid = '/1.1.PowerSupply.13001.4' # str | 
    post_batteries_request = {"@cmd":"ENABLE"} # PostBatteriesRequest | 

    try:
        # Enable/Disable a main
        api_instance.post_main_siid(main_siid, post_batteries_request)
    except Exception as e:
        print("Exception when calling MainSIIDApi->post_main_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main_siid** | **str**|  | 
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
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

