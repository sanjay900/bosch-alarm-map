# openapi_client.SupportfileApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getsupportfile**](SupportfileApi.md#getsupportfile) | **GET** /supportfile | Download MAP panel supportfiles


# **getsupportfile**
> object getsupportfile()

Download MAP panel supportfiles

Receive a compressed bundle of support files from MAP panel. This data should be provided to Bosch support as additional debug information in case of system problems.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.SupportfileApi(api_client)

    try:
        # Download MAP panel supportfiles
        api_response = api_instance.getsupportfile()
        print("The response of SupportfileApi->getsupportfile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportfileApi->getsupportfile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-bzip2

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | debug.tar.bz2 Support File |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**500** | Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

