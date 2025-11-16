# bosch_alarm_map.PowerDeviceSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getpower_device_siid**](PowerDeviceSIIDApi.md#getpower_device_siid) | **GET** /{powerDevice_SIID} | Individual non BDB power device


# **getpower_device_siid**
> getpower_device_siid(power_device_siid)

Individual non BDB power device

The type powerdevice lists power devices configured on couplers on the LSN. It
provides the same interface as device type. It can be disabled.
It cannot be bypassed or walktested.
The resource structure will contain attributes of device and disable.


### Example


```python
import bosch_alarm_map
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
    api_instance = bosch_alarm_map.PowerDeviceSIIDApi(api_client)
    power_device_siid = 'power_device_siid_example' # str | Unique powerDevice SIID. You can get all existing powerDevices IDs with the command GET /powerDevices

    try:
        # Individual non BDB power device
        api_instance.getpower_device_siid(power_device_siid)
    except Exception as e:
        print("Exception when calling PowerDeviceSIIDApi->getpower_device_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **power_device_siid** | **str**| Unique powerDevice SIID. You can get all existing powerDevices IDs with the command GET /powerDevices | 

### Return type

void (empty response body)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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

