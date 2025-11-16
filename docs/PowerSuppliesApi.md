# bosch-alarm-map.PowerSuppliesApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_powersupplies**](PowerSuppliesApi.md#get_powersupplies) | **GET** /powerSupplies | List of all MAP power supplies
[**post_powersupplies**](PowerSuppliesApi.md#post_powersupplies) | **POST** /powerSupplies | Parametrize all MAP system power supplies


# **get_powersupplies**
> PowerSupplyList get_powersupplies()

List of all MAP power supplies

Get a List of all MAP system power supplies

### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.power_supply_list import PowerSupplyList
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
    api_instance = bosch-alarm-map.PowerSuppliesApi(api_client)

    try:
        # List of all MAP power supplies
        api_response = api_instance.get_powersupplies()
        print("The response of PowerSuppliesApi->get_powersupplies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerSuppliesApi->get_powersupplies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PowerSupplyList**](PowerSupplyList.md)

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

# **post_powersupplies**
> post_powersupplies(device_enable_disable)

Parametrize all MAP system power supplies

Enable/Disable, Activate/Deactivate all powerSupplies

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
    api_instance = bosch-alarm-map.PowerSuppliesApi(api_client)
    device_enable_disable = {"@cmd":"ENABLE"} # DeviceEnableDisable | 

    try:
        # Parametrize all MAP system power supplies
        api_instance.post_powersupplies(device_enable_disable)
    except Exception as e:
        print("Exception when calling PowerSuppliesApi->post_powersupplies: %s\n" % e)
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
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**409** | Conflict (Power supplies disabled / Power supplies deactivated) |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

