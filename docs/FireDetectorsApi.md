# bosch_alarm_map.FireDetectorsApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getfire_detectors**](FireDetectorsApi.md#getfire_detectors) | **GET** /fireDetectors | List of fire detectors in the MAP system
[**postfire_detectors**](FireDetectorsApi.md#postfire_detectors) | **POST** /fireDetectors | Enable/Disable all fireDetectors


# **getfire_detectors**
> FireDetectorList getfire_detectors()

List of fire detectors in the MAP system

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
import bosch_alarm_map
from bosch_alarm_map.models.fire_detector_list import FireDetectorList
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
    api_instance = bosch_alarm_map.FireDetectorsApi(api_client)

    try:
        # List of fire detectors in the MAP system
        api_response = api_instance.getfire_detectors()
        print("The response of FireDetectorsApi->getfire_detectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FireDetectorsApi->getfire_detectors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FireDetectorList**](FireDetectorList.md)

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

# **postfire_detectors**
> postfire_detectors(device_enable_disable)

Enable/Disable all fireDetectors

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
    api_instance = bosch_alarm_map.FireDetectorsApi(api_client)
    device_enable_disable = {"@cmd":"ENABLE"} # DeviceEnableDisable | 

    try:
        # Enable/Disable all fireDetectors
        api_instance.postfire_detectors(device_enable_disable)
    except Exception as e:
        print("Exception when calling FireDetectorsApi->postfire_detectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**409** | Conflict &lt;br&gt; This command code is returned when a command is not executed due to application specific reasons. The body of the error response will contain further information on why the command was not executed. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. The body of the response will contain the list of resource URLs which prevented execution of the command.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

