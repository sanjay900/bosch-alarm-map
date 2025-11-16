# openapi_client.StatisticsApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getstatistics**](StatisticsApi.md#getstatistics) | **GET** /statistics | Get MAP internal statistics


# **getstatistics**
> StatisticsGet getstatistics()

Get MAP internal statistics

MAP statistics are available for REST-API (OII) and Database (DB).

Get all statistic modules:
- /statistics

It is possible to partially get statistics for a specific module:
- /statistics/oii
- /statistics/db


### Example


```python
import openapi_client
from openapi_client.models.statistics_get import StatisticsGet
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
    api_instance = openapi_client.StatisticsApi(api_client)

    try:
        # Get MAP internal statistics
        api_response = api_instance.getstatistics()
        print("The response of StatisticsApi->getstatistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->getstatistics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatisticsGet**](StatisticsGet.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**500** | Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

