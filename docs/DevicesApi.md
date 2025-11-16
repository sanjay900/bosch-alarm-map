# openapi_client.DevicesApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getdevices**](DevicesApi.md#getdevices) | **GET** /devices | List of all devices configured in the MAP system.


# **getdevices**
> DevicesList getdevices()

List of all devices configured in the MAP system.

The /devices resource provides a list of all configured devices of the MAP system together with the individual resource types of all supported devices.
This resource type is the basic resource type for all MAP system devices (except for a few specific devices). It thus includes the commonly available properties and commands for devices in the MAP system.
To allow batch operations on devices of the same type, MAP panel supports list resources for each of the of the defined device types.


### Example


```python
import openapi_client
from openapi_client.models.devices_list import DevicesList
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
    api_instance = openapi_client.DevicesApi(api_client)

    try:
        # List of all devices configured in the MAP system.
        api_response = api_instance.getdevices()
        print("The response of DevicesApi->getdevices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->getdevices: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DevicesList**](DevicesList.md)

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

