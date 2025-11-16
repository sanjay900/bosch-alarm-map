# bosch_alarm_map.KeyswitchSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getkeyswitch_siid**](KeyswitchSIIDApi.md#getkeyswitch_siid) | **GET** /{keyswitch_SIID} | Individual keyswitch
[**post_keyswitch_siid**](KeyswitchSIIDApi.md#post_keyswitch_siid) | **POST** /{keyswitch_SIID} | Enable/Disable a keyswitch


# **getkeyswitch_siid**
> Keyswitch getkeyswitch_siid(keyswitch_siid)

Individual keyswitch

The keyswitch resource type extends the device type with additional property of active.
It can be disabled. Keyswitches are not bypassable. Walktest of keyswitches is currently not supported by
MAP system.
The resource structure will contain attributes of device and disable.


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.keyswitch import Keyswitch
from bosch_alarm_map.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://169.254.10.10
# See configuration.py for a list of all supported configuration parameters.
configuration = bosch_alarm_map.Configuration(
    host = "https://169.254.10.10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with bosch_alarm_map.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bosch_alarm_map.KeyswitchSIIDApi(api_client)
    keyswitch_siid = '/1.1.Keyswitch.3002.13' # str | Unique keyswitch SIID. You can get all existing keyswitchs IDs with the command GET /keyswitches

    try:
        # Individual keyswitch
        api_response = api_instance.getkeyswitch_siid(keyswitch_siid)
        print("The response of KeyswitchSIIDApi->getkeyswitch_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyswitchSIIDApi->getkeyswitch_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyswitch_siid** | **str**| Unique keyswitch SIID. You can get all existing keyswitchs IDs with the command GET /keyswitches | 

### Return type

[**Keyswitch**](Keyswitch.md)

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

# **post_keyswitch_siid**
> post_keyswitch_siid(keyswitch_siid, device_enable_disable)

Enable/Disable a keyswitch

The keyswitch extends the basic device type with the additional property of active.
A keyswitch can be disabled. Keyswitches are not bypassable and the walktest function of keyswitches is currently not supported


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.device_enable_disable import DeviceEnableDisable
from bosch_alarm_map.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://169.254.10.10
# See configuration.py for a list of all supported configuration parameters.
configuration = bosch_alarm_map.Configuration(
    host = "https://169.254.10.10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with bosch_alarm_map.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bosch_alarm_map.KeyswitchSIIDApi(api_client)
    keyswitch_siid = '/1.1.Keyswitch.3002.13' # str | Unique keyswitch SIID. You can get all existing keyswitchs IDs with the command GET /keyswitches
    device_enable_disable = {"@cmd":"ENABLE"} # DeviceEnableDisable | 

    try:
        # Enable/Disable a keyswitch
        api_instance.post_keyswitch_siid(keyswitch_siid, device_enable_disable)
    except Exception as e:
        print("Exception when calling KeyswitchSIIDApi->post_keyswitch_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyswitch_siid** | **str**| Unique keyswitch SIID. You can get all existing keyswitchs IDs with the command GET /keyswitches | 
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
**202** | Successful operation. |  -  |
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

