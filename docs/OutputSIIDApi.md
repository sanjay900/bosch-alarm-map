# bosch-alarm-map.OutputSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_output_siid**](OutputSIIDApi.md#get_output_siid) | **GET** /{output_SIID} | Individual output
[**post_output_siid**](OutputSIIDApi.md#post_output_siid) | **POST** /{output_SIID} | Enable/Disable an output


# **get_output_siid**
> Output get_output_siid(output_siid)

Individual output

The resource type output extends the type device with additional output state information and commands to turn on/off.

### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.output import Output
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
    api_instance = bosch-alarm-map.OutputSIIDApi(api_client)
    output_siid = '/1.1.Output.3002.12' # str | Unique output SIID. You can get all existing outputs IDs with the command GET /outputs

    try:
        # Individual output
        api_response = api_instance.get_output_siid(output_siid)
        print("The response of OutputSIIDApi->get_output_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutputSIIDApi->get_output_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_siid** | **str**| Unique output SIID. You can get all existing outputs IDs with the command GET /outputs | 

### Return type

[**Output**](Output.md)

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

# **post_output_siid**
> post_output_siid(output_siid, post_outputs_request)

Enable/Disable an output

The resource type output can be disabled.
This resource type cannot be bypassed or walktested. The resource structure will contain
attributes of device and disable.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.post_outputs_request import PostOutputsRequest
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
    api_instance = bosch-alarm-map.OutputSIIDApi(api_client)
    output_siid = '/1.1.Output.3002.12' # str | 
    post_outputs_request = {"@cmd":"ENABLE"} # PostOutputsRequest | 

    try:
        # Enable/Disable an output
        api_instance.post_output_siid(output_siid, post_outputs_request)
    except Exception as e:
        print("Exception when calling OutputSIIDApi->post_output_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_siid** | **str**|  | 
 **post_outputs_request** | [**PostOutputsRequest**](PostOutputsRequest.md)|  | 

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
**409** | Conflict. Each output must be assigned to an area. To solve this, assign an area to the output using the RPS for MAP. |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

