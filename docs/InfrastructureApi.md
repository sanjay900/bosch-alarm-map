# bosch_alarm_map.InfrastructureApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getinfrastructure**](InfrastructureApi.md#getinfrastructure) | **GET** /infrastructure | Get complete MAP device infrastructure
[**getinfrastructurebysiid**](InfrastructureApi.md#getinfrastructurebysiid) | **GET** /infrastructure/{DeviceSIID} | Get MAP device infrastructure starting from SIID


# **getinfrastructure**
> Infrastructure getinfrastructure()

Get complete MAP device infrastructure

Returns a complete tree of connected devices.

### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.infrastructure import Infrastructure
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
    api_instance = bosch_alarm_map.InfrastructureApi(api_client)

    try:
        # Get complete MAP device infrastructure
        api_response = api_instance.getinfrastructure()
        print("The response of InfrastructureApi->getinfrastructure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->getinfrastructure: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Infrastructure**](Infrastructure.md)

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
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getinfrastructurebysiid**
> InfrastructureDevice getinfrastructurebysiid(device_siid)

Get MAP device infrastructure starting from SIID

Returns a connected devices tree starting from requested SIID.

It is also possible to limit hierarchy depth by specifying depth parameter:
- /infrastructure/{DeviceSIID}?depth={Value}


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.infrastructure_device import InfrastructureDevice
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
    api_instance = bosch_alarm_map.InfrastructureApi(api_client)
    device_siid = '1.1.SystemKeypad.12001.001' # str | SIID of a device

    try:
        # Get MAP device infrastructure starting from SIID
        api_response = api_instance.getinfrastructurebysiid(device_siid)
        print("The response of InfrastructureApi->getinfrastructurebysiid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->getinfrastructurebysiid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_siid** | **str**| SIID of a device | 

### Return type

[**InfrastructureDevice**](InfrastructureDevice.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Represents the error in either in the name of the GET query parameter or in its value.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**404** | Not found. The request URL with the specified parameter was not found.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

