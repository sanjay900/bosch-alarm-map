# openapi_client.LsnApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lsngw_config**](LsnApi.md#get_lsngw_config) | **GET** /lsn | Get current LSN configuration
[**post_lsngw_config**](LsnApi.md#post_lsngw_config) | **POST** /lsn | Create, modify or delete a LSN Gateway configuration


# **get_lsngw_config**
> get_lsngw_config()

Get current LSN configuration

This function is used to get current LSN configuration.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.LsnApi(api_client)

    try:
        # Get current LSN configuration
        api_instance.get_lsngw_config()
    except Exception as e:
        print("Exception when calling LsnApi->get_lsngw_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lsngw_config**
> post_lsngw_config(post_lsngw_config_request=post_lsngw_config_request)

Create, modify or delete a LSN Gateway configuration

This function is used to create, modify or delete LSN GW configuraion.

Each device has a minimal number of required parameters. Other parameters, if not set, will be defaulted to the values from the RPS.

Reporting number parameter will not be respected unless the Panel has Event Reporing configured.

Any successful POST request will automatically reboot the Panel to apply the configuration.
The Panel will reboot within 30 seconds after the request is processed.


### Example


```python
import openapi_client
from openapi_client.models.post_lsngw_config_request import PostLSNGWConfigRequest
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
    api_instance = openapi_client.LsnApi(api_client)
    post_lsngw_config_request = {"@cmd":"CREATE","connection":"internal","name":"[LSN GW 1]","area":"","serialNumber":"90292.60349616210","busMode":"Classic","aux":[{"name":"[AUX 1]","supportsDelayedReporting":true},{"name":"[AUX 2]","supportsDelayedReporting":true}],"loop":{"name":"[LSN GW 1: Loop]","devices":[{"type":"EMK36","name":"EMK36 LSN Device","pointType":"Intrusion (Non Bypassable)","area":"[Control Panel Area]"}]}} # PostLSNGWConfigRequest |  (optional)

    try:
        # Create, modify or delete a LSN Gateway configuration
        api_instance.post_lsngw_config(post_lsngw_config_request=post_lsngw_config_request)
    except Exception as e:
        print("Exception when calling LsnApi->post_lsngw_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_lsngw_config_request** | [**PostLSNGWConfigRequest**](PostLSNGWConfigRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. The request succeeded, and resource was either created, modified or deleted.  |  -  |
**400** | Bad request &lt;br&gt; Query parameters are unknown or malformed.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**404** | Not found. The request URL with the specified parameter was not found.  |  -  |
**409** | Already exists &lt;br&gt; Maximum number of LSN GW reached  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

