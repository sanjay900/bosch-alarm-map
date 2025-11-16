# bosch-alarm-map.ConfigApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_confic**](ConfigApi.md#get_confic) | **GET** /config | View MAP system configuration


# **get_confic**
> Config get_confic()

View MAP system configuration

A configuration file is provided that describes the areas, internal programs, devices and their
relationship. A client can download the configuration on start up to understand which items are
configured in the MAP system. In particular, the relationship between areas and devices as
well as among devices is given in this resource. The relationship information is only given with the
configuration. The resources themselves do not have links between each other, as the
relationships cannot change during runtime. <br>
**Object Structure** <br>
The configuration object has three major parts. <br>
1. Configured areas <br>
In the first part of the configuration the list of all configured areas and their properties is provided. In addition, each area contains a list of all devices that are part of this area. <br>
2. Internal programs <br>
The second part of the configuration is the internal program configuration which provides list of configured internal programs and the devices that are configured for these internal programs. <br>
3. Device configuration <br>
The third part of the configuration is the device configuration. This part includes details about the devices.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.config import Config
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
    api_instance = bosch-alarm-map.ConfigApi(api_client)

    try:
        # View MAP system configuration
        api_response = api_instance.get_confic()
        print("The response of ConfigApi->get_confic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->get_confic: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Config**](Config.md)

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

