# bosch-alarm-map.SupervisedConnsSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supervised_conns_siid**](SupervisedConnsSIIDApi.md#get_supervised_conns_siid) | **GET** /{supervisedConns_SIID} | Individual supervised connection
[**post_supervised_conns**](SupervisedConnsSIIDApi.md#post_supervised_conns) | **POST** /{supervisedConns_SIID} | Enable Connections to other systems.


# **get_supervised_conns_siid**
> GetSupervisedConnsSIID200Response get_supervised_conns_siid(supervised_conns_siid)

Individual supervised connection

Unique supervised connection SIID of the interface to an other systems like BIS, IPC, or REST-API. You can get all supervised connections IDs with the command GET /supervisedConns


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.get_supervised_conns_siid200_response import GetSupervisedConnsSIID200Response
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
    api_instance = bosch-alarm-map.SupervisedConnsSIIDApi(api_client)
    supervised_conns_siid = '/1.1.System.7.1' # str | 

    try:
        # Individual supervised connection
        api_response = api_instance.get_supervised_conns_siid(supervised_conns_siid)
        print("The response of SupervisedConnsSIIDApi->get_supervised_conns_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupervisedConnsSIIDApi->get_supervised_conns_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supervised_conns_siid** | **str**|  | 

### Return type

[**GetSupervisedConnsSIID200Response**](GetSupervisedConnsSIID200Response.md)

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

# **post_supervised_conns**
> post_supervised_conns(supervised_conns_siid, device_enable_disable=device_enable_disable)

Enable Connections to other systems.

Enable or disable a supervised connection to other systems like BIS, IPC, or REST-API. Please note that the REST-API interface can only be deactivated.
The activation is done via the RPS for MAP software. This resource type cannot be bypassed.


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
    api_instance = bosch-alarm-map.SupervisedConnsSIIDApi(api_client)
    supervised_conns_siid = '/1.1.System.7.1' # str | 
    device_enable_disable = {"@cmd":"ENABLE"} # DeviceEnableDisable |  (optional)

    try:
        # Enable Connections to other systems.
        api_instance.post_supervised_conns(supervised_conns_siid, device_enable_disable=device_enable_disable)
    except Exception as e:
        print("Exception when calling SupervisedConnsSIIDApi->post_supervised_conns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supervised_conns_siid** | **str**|  | 
 **device_enable_disable** | [**DeviceEnableDisable**](DeviceEnableDisable.md)|  | [optional] 

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
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

