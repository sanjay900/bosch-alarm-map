# bosch-alarm-map.LsnauxSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lsnaux_siid**](LsnauxSIIDApi.md#get_lsnaux_siid) | **GET** /{lsnaux_SIID} | Individual LSN aux
[**post_lsnaus_siid**](LsnauxSIIDApi.md#post_lsnaus_siid) | **POST** /{lsnaux_SIID} | Enable/Disable a lsnaux


# **get_lsnaux_siid**
> Lsnaux get_lsnaux_siid(lsnaux_siid)

Individual LSN aux

The resource type lsnAux lists the LSN Aux power on the LSN Gateway. It extends
device resource type. This resource type can be disabled. This resource type cannot be bypassed or walktested. The resource structure will
contain attributes of disable.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.lsnaux import Lsnaux
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
    api_instance = bosch-alarm-map.LsnauxSIIDApi(api_client)
    lsnaux_siid = '/1.1.Gateway.8001.702' # str | Unique lsnaux SIID. You can get all existing lsnauxs IDs with the command GET /lsnauxs

    try:
        # Individual LSN aux
        api_response = api_instance.get_lsnaux_siid(lsnaux_siid)
        print("The response of LsnauxSIIDApi->get_lsnaux_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LsnauxSIIDApi->get_lsnaux_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lsnaux_siid** | **str**| Unique lsnaux SIID. You can get all existing lsnauxs IDs with the command GET /lsnauxs | 

### Return type

[**Lsnaux**](Lsnaux.md)

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

# **post_lsnaus_siid**
> post_lsnaus_siid(lsnaux_siid, device_enable_disable)

Enable/Disable a lsnaux

The resource type lsnAux lists the LSN Aux power on the LSN Gateway. It extends
device resource type. This resource type can be disabled. This resource type cannot be bypassed or walktested. The resource structure will
contain attributes of disable.


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
    api_instance = bosch-alarm-map.LsnauxSIIDApi(api_client)
    lsnaux_siid = '/1.1.Gateway.8001.702' # str | 
    device_enable_disable = {"@cmd":"ENABLE"} # DeviceEnableDisable | 

    try:
        # Enable/Disable a lsnaux
        api_instance.post_lsnaus_siid(lsnaux_siid, device_enable_disable)
    except Exception as e:
        print("Exception when calling LsnauxSIIDApi->post_lsnaus_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lsnaux_siid** | **str**|  | 
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

