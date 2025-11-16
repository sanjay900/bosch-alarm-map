# openapi_client.TimeApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_time**](TimeApi.md#get_time) | **GET** /time | Get System Time
[**post_time**](TimeApi.md#post_time) | **POST** /time | Set System Time


# **get_time**
> TimeOut get_time()

Get System Time

The time resource provides information on the current system time of the MAP panel including time
zone. A client can also use this resource to set the time of the MAP panel.
The time is given in precision of milliseconds.


### Example


```python
import openapi_client
from openapi_client.models.time_out import TimeOut
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
    api_instance = openapi_client.TimeApi(api_client)

    try:
        # Get System Time
        api_response = api_instance.get_time()
        print("The response of TimeApi->get_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeApi->get_time: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TimeOut**](TimeOut.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. This response code indicates a successful transaction. It will be returned for a successful GET request. The response will contain the resource representation. PUT, POST or DELETE will return 201, *Created* after successful execution or 202 after successful acceptance or 204 *No Content* after successful execution.  |  -  |
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**409** | Conflict &lt;br&gt; This command code is returned when a command is not executed due to application specific reasons. The body of the error response will contain further information on why the command was not executed. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. The body of the response will contain the list of resource URLs which prevented execution of the command.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time**
> post_time(time_in)

Set System Time

It is possible to set the date and time of the panel over the REST-API. This can be used for
commissioning purposes or for time synchronization, where a client sets the time in regular
intervals to assure a desired synchronization of its internal clock to the clock of the MAP panel.
Currently the time zone is only configurable via RPSforMAP and cannot be set via the REST-API. This is
considered to be appropriate, as the MAP system needs to be configured over RPS and the time zone
should not change over time, as the installation location of the MAP panel is fixed.
The time that is provided in the request is interpreted as UTC time. This means, even if the date
time is including time zone information, for example 2014-07-20T16:11:42+02:00, the actual UTC time is
calculated from that, for example 2014-07-20T14:11:42Z and the internal clock’s UTC is set accordingly.
When fetching the time using a GET, the local time reflecting the configured time zone will be
provided as described in get /time.


### Example


```python
import openapi_client
from openapi_client.models.time_in import TimeIn
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
    api_instance = openapi_client.TimeApi(api_client)
    time_in = {"@cmd":"SETTIME","utcDateTime":"2021-07-20T16:11:42Z"} # TimeIn | 

    try:
        # Set System Time
        api_instance.post_time(time_in)
    except Exception as e:
        print("Exception when calling TimeApi->post_time: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_in** | [**TimeIn**](TimeIn.md)|  | 

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
**409** | Conflict &lt;br&gt; This command code is returned when a command is not executed due to application specific reasons. The body of the error response will contain further information on why the command was not executed. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. The body of the response will contain the list of resource URLs which prevented execution of the command.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

