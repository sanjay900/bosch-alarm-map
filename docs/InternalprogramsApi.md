# bosch-alarm-map.InternalprogramsApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_internalprograms**](InternalprogramsApi.md#get_internalprograms) | **GET** /internalprograms | List all internal programs configured. 
[**post_internalprograms**](InternalprogramsApi.md#post_internalprograms) | **POST** /internalprograms | Activate/Deactivate all internal programs


# **get_internalprograms**
> InternalProgramList get_internalprograms()

List all internal programs configured. 

The internal program resource allows investigating the status of internal programs configured in
the MAP system and allows activating or deactivating the internal program. In case an alarm occurs, the
alarm will be referenced by the area in which it occurred not at the internal program. Similarly,
the incident will not indicate the internal program but the area that detected the alarm.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.internal_program_list import InternalProgramList
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
    api_instance = bosch-alarm-map.InternalprogramsApi(api_client)

    try:
        # List all internal programs configured. 
        api_response = api_instance.get_internalprograms()
        print("The response of InternalprogramsApi->get_internalprograms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalprogramsApi->get_internalprograms: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InternalProgramList**](InternalProgramList.md)

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

# **post_internalprograms**
> post_internalprograms(device_activate_deactivate)

Activate/Deactivate all internal programs

The internal program resource allows investigating the status of internal programs configured in
the MAP system and allows activating or deactivating the internal program. In case an alarm occurs, the
alarm will be referenced by the area in which it occurred not at the internal program. Similarly,
the incident will not indicate the internal program but the area that detected the alarm.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.device_activate_deactivate import DeviceActivateDeactivate
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
    api_instance = bosch-alarm-map.InternalprogramsApi(api_client)
    device_activate_deactivate = {"@cmd":"ACTIVATE"} # DeviceActivateDeactivate | 

    try:
        # Activate/Deactivate all internal programs
        api_instance.post_internalprograms(device_activate_deactivate)
    except Exception as e:
        print("Exception when calling InternalprogramsApi->post_internalprograms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_activate_deactivate** | [**DeviceActivateDeactivate**](DeviceActivateDeactivate.md)|  | 

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
**409** | Conflict &lt;br&gt; This command code is returned when a command is not executed due to application specific reasons. The body of the error response will contain further information on why the command was not executed. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. The body of the response will contain the list of resource URLs which prevented execution of the command.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

