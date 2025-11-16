# bosch_alarm_map.DescApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getdesc**](DescApi.md#getdesc) | **GET** /desc | Descriptive information


# **getdesc**
> Desc getdesc()

Descriptive information

The description of the MAP panel is provided under “/desc”.
The field mainResources will contain the links to the resources listed in the example.


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.desc import Desc
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
    api_instance = bosch_alarm_map.DescApi(api_client)

    try:
        # Descriptive information
        api_response = api_instance.getdesc()
        print("The response of DescApi->getdesc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DescApi->getdesc: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Desc**](Desc.md)

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

