# bosch-alarm-map.FireDetectorSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firedetector_siid**](FireDetectorSIIDApi.md#firedetector_siid) | **POST** /{fireDetector_SIID} | Enable/Disable a fireDetector
[**get_firedetector**](FireDetectorSIIDApi.md#get_firedetector) | **GET** /{fireDetector_SIID} | Individual fire detector


# **firedetector_siid**
> firedetector_siid(fire_detector_siid, device_enable_disable)

Enable/Disable a fireDetector

Fire detector is an extension to the point type and is used to model fire detectors in the MAP
system. It adds details on the triggered sensor in the scope of a walktest. This resource type can
be disabled.
Similar as a point, a fire detector may be configured to be walktestable or bypassable. Thus, the
walktest and bypass interface may be supported by an individual resource depending on the
panel configuration. The resource structure will contain attributes of device, disable and
point in addition to the attributes mentioned below. If configured to be bypassed and
walktested, it will also contain attributes of bypass and walktest respectively.


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
    api_instance = bosch-alarm-map.FireDetectorSIIDApi(api_client)
    fire_detector_siid = '/1.1.Point.01001.006' # str | 
    device_enable_disable = {"@cmd":"ENABLE"} # DeviceEnableDisable | 

    try:
        # Enable/Disable a fireDetector
        api_instance.firedetector_siid(fire_detector_siid, device_enable_disable)
    except Exception as e:
        print("Exception when calling FireDetectorSIIDApi->firedetector_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fire_detector_siid** | **str**|  | 
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
**409** | Conflict &lt;br&gt; This command code is returned when a command is not executed due to application specific reasons. The body of the error response will contain further information on why the command was not executed. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. The body of the response will contain the list of resource URLs which prevented execution of the command.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firedetector**
> FireDetector get_firedetector(fire_detector_siid)

Individual fire detector

Fire detector is an extension to the point type and is used to model fire detectors in the MAP
system. It adds details on the triggered sensor in the scope of a walktest. This resource type can
be disabled.
Similar as a point, a fire detector may be configured to be walktestable or bypassable. Thus, the
walktest and bypass interface may be supported by an individual resource depending on the
panel configuration. The resource structure will contain attributes of device, disable and
point in addition to the attributes mentioned below. If configured to be bypassed and
walktested, it will also contain attributes of bypass and walktest respectively.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.fire_detector import FireDetector
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
    api_instance = bosch-alarm-map.FireDetectorSIIDApi(api_client)
    fire_detector_siid = '/1.1.Point.01001.006' # str | 

    try:
        # Individual fire detector
        api_response = api_instance.get_firedetector(fire_detector_siid)
        print("The response of FireDetectorSIIDApi->get_firedetector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FireDetectorSIIDApi->get_firedetector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fire_detector_siid** | **str**|  | 

### Return type

[**FireDetector**](FireDetector.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

