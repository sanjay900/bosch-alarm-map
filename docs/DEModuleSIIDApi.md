# openapi_client.DEModuleSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_de_module_siid**](DEModuleSIIDApi.md#get_de_module_siid) | **GET** /{DEModule_SIID} | DE Module of the MAP system
[**post_de_module_siid**](DEModuleSIIDApi.md#post_de_module_siid) | **POST** /{DEModule_SIID} | Enable/disable, get firmware version


# **get_de_module_siid**
> DEModule get_de_module_siid(de_module_siid)

DE Module of the MAP system

The resource type deModule extends the device resource type with an additional
command of firmware version. It list the DE-Module. It can be disabled. The resource structure will contain the attributes of device and disable.
It cannot be bypassed or walktested.


### Example


```python
import openapi_client
from openapi_client.models.de_module import DEModule
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
    api_instance = openapi_client.DEModuleSIIDApi(api_client)
    de_module_siid = '/1.1.Gateway.15001.1' # str | Unique DEModule SIID

    try:
        # DE Module of the MAP system
        api_response = api_instance.get_de_module_siid(de_module_siid)
        print("The response of DEModuleSIIDApi->get_de_module_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DEModuleSIIDApi->get_de_module_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **de_module_siid** | **str**| Unique DEModule SIID | 

### Return type

[**DEModule**](DEModule.md)

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

# **post_de_module_siid**
> DevicefirmwareVersion post_de_module_siid(de_module_siid, postlsn_gateway_siid_request)

Enable/disable, get firmware version

Enable ore disable the DEModule over the REST-API interface. It is also possible to read out the firmware version of a running DE Module.


### Example


```python
import openapi_client
from openapi_client.models.devicefirmware_version import DevicefirmwareVersion
from openapi_client.models.postlsn_gateway_siid_request import PostlsnGatewaySIIDRequest
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
    api_instance = openapi_client.DEModuleSIIDApi(api_client)
    de_module_siid = '/1.1.Gateway.15001.1' # str | 
    postlsn_gateway_siid_request = {"@cmd":"ENABLE"} # PostlsnGatewaySIIDRequest | 

    try:
        # Enable/disable, get firmware version
        api_response = api_instance.post_de_module_siid(de_module_siid, postlsn_gateway_siid_request)
        print("The response of DEModuleSIIDApi->post_de_module_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DEModuleSIIDApi->post_de_module_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **de_module_siid** | **str**|  | 
 **postlsn_gateway_siid_request** | [**PostlsnGatewaySIIDRequest**](PostlsnGatewaySIIDRequest.md)|  | 

### Return type

[**DevicefirmwareVersion**](DevicefirmwareVersion.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation, get firmware version |  -  |
**202** | Successful operation. ENABLE/DISABLE device |  -  |
**400** | Bad request (Command not correct) |  -  |
**403** | A valid request was sent, but the user is not allowed to conduct the requested operation. |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

