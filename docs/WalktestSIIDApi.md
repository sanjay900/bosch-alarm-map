# bosch_alarm_map.WalktestSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_walktest_siid**](WalktestSIIDApi.md#delete_walktest_siid) | **DELETE** /walktest/{walktest_SIID} | Stop Walktest
[**get_walktest_siid**](WalktestSIIDApi.md#get_walktest_siid) | **GET** /walktest/{walktest_SIID} | Individual walktest
[**post_walktest_siid**](WalktestSIIDApi.md#post_walktest_siid) | **POST** /walktest/{walktest_SIID} | Walktest diagnose


# **delete_walktest_siid**
> delete_walktest_siid(walktest_siid)

Stop Walktest

This operation stops the walktest in all related areas and points that are part of this test

### Example


```python
import bosch_alarm_map
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
    api_instance = bosch_alarm_map.WalktestSIIDApi(api_client)
    walktest_siid = '/274F1EC2086C40AB8601DF998431DA46' # str | Unique walktest SIID. You can get all existing walktest SIIDs with the command GET /walktests 

    try:
        # Stop Walktest
        api_instance.delete_walktest_siid(walktest_siid)
    except Exception as e:
        print("Exception when calling WalktestSIIDApi->delete_walktest_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **walktest_siid** | **str**| Unique walktest SIID. You can get all existing walktest SIIDs with the command GET /walktests  | 

### Return type

void (empty response body)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_walktest_siid**
> Walktest get_walktest_siid(walktest_siid)

Individual walktest

The walktest resource represents a walktest that contains one or multiple areas. A walktest
resource is created during runtime when a client or a user starts a walktest. The walktest contains
information which areas should participate in the walktest and if the walktest has already stared
in that area. Additionally, it allows stopping the walktest. Walktests are started via the area or
area list resource. Each walktest is referenced by a walktest list.


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.walktest import Walktest
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
    api_instance = bosch_alarm_map.WalktestSIIDApi(api_client)
    walktest_siid = '/274F1EC2086C40AB8601DF998431DA46' # str | Unique walktest SIID. You can get all existing walktest SIIDs with the command GET /walktests 

    try:
        # Individual walktest
        api_response = api_instance.get_walktest_siid(walktest_siid)
        print("The response of WalktestSIIDApi->get_walktest_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalktestSIIDApi->get_walktest_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **walktest_siid** | **str**| Unique walktest SIID. You can get all existing walktest SIIDs with the command GET /walktests  | 

### Return type

[**Walktest**](Walktest.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Walktest object structure |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_walktest_siid**
> DiagnoseResponse post_walktest_siid(walktest_siid, diagnose)

Walktest diagnose

A walktestable device provides some diagnostic information that can be fetched using the
diagnose command. (This information has not been included as a property of the resource as it
changes only rarely and is usually only used in preparation of a walktest. Thus, moving it into
a command allows to save bandwidth in most scenarios.)


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.diagnose import Diagnose
from bosch_alarm_map.models.diagnose_response import DiagnoseResponse
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
    api_instance = bosch_alarm_map.WalktestSIIDApi(api_client)
    walktest_siid = '/274F1EC2086C40AB8601DF998431DA46' # str | Unique walktest SIID. You can get all existing walktest SIIDs with the command GET /walktests 
    diagnose = bosch_alarm_map.Diagnose() # Diagnose | 

    try:
        # Walktest diagnose
        api_response = api_instance.post_walktest_siid(walktest_siid, diagnose)
        print("The response of WalktestSIIDApi->post_walktest_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalktestSIIDApi->post_walktest_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **walktest_siid** | **str**| Unique walktest SIID. You can get all existing walktest SIIDs with the command GET /walktests  | 
 **diagnose** | [**Diagnose**](Diagnose.md)|  | 

### Return type

[**DiagnoseResponse**](DiagnoseResponse.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: application/json
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

