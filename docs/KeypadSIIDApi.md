# bosch-alarm-map.KeypadSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_keypad_siid**](KeypadSIIDApi.md#get_keypad_siid) | **GET** /{keypad_SIID} | Individual keypad
[**post_keypad_siid**](KeypadSIIDApi.md#post_keypad_siid) | **POST** /{keypad_SIID} | Enable/Disable, Activate/Deactivate, get firmware Version of a Keypad


# **get_keypad_siid**
> Keypad get_keypad_siid(keypad_siid)

Individual keypad

This lists the system Keypad of the MAP system. It extends device resource type
with additional statuses and commands specific to the Keypad. It supports a firmware version
command to retrieve the firmware version running on the Keypad. It can be disabled. This resource type cannot be bypassed or walktested.
The resource structure will contain attributes of device and disable.
Note: In addition to the behaviour of a disabled device, disabling a
Keypad results in the Keypad being locked. The LEDs do not change their state. The screen is
not turned off but no user can log in. A logged in user will be logged out.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.keypad import Keypad
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
    api_instance = bosch-alarm-map.KeypadSIIDApi(api_client)
    keypad_siid = '/1.1.SystemKeypad.12001.1' # str | Unique Keypad SIID. You can get all existing Keypads IDs with the command GET /keypads

    try:
        # Individual keypad
        api_response = api_instance.get_keypad_siid(keypad_siid)
        print("The response of KeypadSIIDApi->get_keypad_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeypadSIIDApi->get_keypad_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypad_siid** | **str**| Unique Keypad SIID. You can get all existing Keypads IDs with the command GET /keypads | 

### Return type

[**Keypad**](Keypad.md)

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

# **post_keypad_siid**
> DevicefirmwareVersion post_keypad_siid(keypad_siid, post_keypad_siid_request)

Enable/Disable, Activate/Deactivate, get firmware Version of a Keypad

This lists the system Keypad of the MAP system. It extends device resource type
with additional statuses and commands specific to the Keypad. It supports a firmware version
command to retrieve the firmware version running on the Keypad. It can be disabled. This resource type cannot be bypassed or walktested.
The resource structure will contain attributes of device and disable.
Note: In addition to the behaviour of a disabled device, disabling a
Keypad results in the Keypad being locked. The LEDs do not change their state. The screen is
not turned off but no user can log in. A logged in user will be logged out.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.devicefirmware_version import DevicefirmwareVersion
from bosch-alarm-map.models.post_keypad_siid_request import PostKeypadSIIDRequest
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
    api_instance = bosch-alarm-map.KeypadSIIDApi(api_client)
    keypad_siid = '/1.1.SystemKeypad.12001.1' # str | 
    post_keypad_siid_request = {"@cmd":"ENABLE"} # PostKeypadSIIDRequest | 

    try:
        # Enable/Disable, Activate/Deactivate, get firmware Version of a Keypad
        api_response = api_instance.post_keypad_siid(keypad_siid, post_keypad_siid_request)
        print("The response of KeypadSIIDApi->post_keypad_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeypadSIIDApi->post_keypad_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keypad_siid** | **str**|  | 
 **post_keypad_siid_request** | [**PostKeypadSIIDRequest**](PostKeypadSIIDRequest.md)|  | 

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
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**409** | Conflict (Keypad disabled / Keypad deactivated) |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

