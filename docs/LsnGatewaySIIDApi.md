# bosch-alarm-map.LsnGatewaySIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lsn_gateway_siid**](LsnGatewaySIIDApi.md#get_lsn_gateway_siid) | **GET** /{lsnGateway_SIID} | Individual LSN gateway
[**postlsn_gateway_siid**](LsnGatewaySIIDApi.md#postlsn_gateway_siid) | **POST** /{lsnGateway_SIID} | Enable/Disable, get Firmware Version of a lsnGateway


# **get_lsn_gateway_siid**
> LsnGateway get_lsn_gateway_siid(lsn_gateway_siid)

Individual LSN gateway

The resource type lsnGateways extends the device resource type with an additional
firmware version command. It lists all LSN Gateways. It can be disabled. This resource type cannot be bypassed or walktested. The resource structure
will contain attributes of device and disable.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.lsn_gateway import LsnGateway
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
    api_instance = bosch-alarm-map.LsnGatewaySIIDApi(api_client)
    lsn_gateway_siid = '/1.1.Gateway.8001.1' # str | Unique lsnGateway SIID. You can get all existing lsnGateways IDs with the command GET /lsnGateways

    try:
        # Individual LSN gateway
        api_response = api_instance.get_lsn_gateway_siid(lsn_gateway_siid)
        print("The response of LsnGatewaySIIDApi->get_lsn_gateway_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LsnGatewaySIIDApi->get_lsn_gateway_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lsn_gateway_siid** | **str**| Unique lsnGateway SIID. You can get all existing lsnGateways IDs with the command GET /lsnGateways | 

### Return type

[**LsnGateway**](LsnGateway.md)

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

# **postlsn_gateway_siid**
> DevicefirmwareVersion postlsn_gateway_siid(lsn_gateway_siid, postlsn_gateway_siid_request)

Enable/Disable, get Firmware Version of a lsnGateway

The resource type lsnGateways extends the device resource type with an additional
firmware version command. It lists all LSN Gateways. It can be disabled. This resource type cannot be bypassed or walktested. The resource structure
will contain attributes of device and disable.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.devicefirmware_version import DevicefirmwareVersion
from bosch-alarm-map.models.postlsn_gateway_siid_request import PostlsnGatewaySIIDRequest
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
    api_instance = bosch-alarm-map.LsnGatewaySIIDApi(api_client)
    lsn_gateway_siid = '/1.1.Gateway.8001.1' # str | 
    postlsn_gateway_siid_request = {"@cmd":"ENABLE"} # PostlsnGatewaySIIDRequest | 

    try:
        # Enable/Disable, get Firmware Version of a lsnGateway
        api_response = api_instance.postlsn_gateway_siid(lsn_gateway_siid, postlsn_gateway_siid_request)
        print("The response of LsnGatewaySIIDApi->postlsn_gateway_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LsnGatewaySIIDApi->postlsn_gateway_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lsn_gateway_siid** | **str**|  | 
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
**202** | Successful operation. ENABLE/DISABLE or ACTIVATE/DEACTIVATE device |  -  |
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

