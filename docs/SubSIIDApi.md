# openapi_client.SubSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sub_siid**](SubSIIDApi.md#delete_sub_siid) | **DELETE** /sub/{sub_SIID} | Unsubscribe
[**get_sub_siid**](SubSIIDApi.md#get_sub_siid) | **GET** /sub/{sub_SIID} | Individual subscription resource
[**post_sub_siid**](SubSIIDApi.md#post_sub_siid) | **POST** /sub/{sub_SIID} | Fetch events


# **delete_sub_siid**
> delete_sub_siid(sub_siid)

Unsubscribe

This operation cancels a subscription. The MAP panel will free the event buffer associated to this subscription.

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
    api_instance = openapi_client.SubSIIDApi(api_client)
    sub_siid = '/EDB1122914E14962A8BDCBD75B9ABA92' # str | Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub 

    try:
        # Unsubscribe
        api_instance.delete_sub_siid(sub_siid)
    except Exception as e:
        print("Exception when calling SubSIIDApi->delete_sub_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_siid** | **str**| Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  | 

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
**204** | No Content |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**409** | Conflict &lt;br&gt; This command code is returned when a command is not executed due to application specific reasons. The body of the error response will contain further information on why the command was not executed. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. The body of the response will contain the list of resource URLs which prevented execution of the command.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_siid**
> Sub get_sub_siid(sub_siid)

Individual subscription resource

The MAP panel provides event notifications for all resources.
This *GET* function is used, to get a specific subscription resource.

### Subscription Resource (/sub/*)

A resource representing individual, valid subscription
of a client. This resource can be used to inspect the information about the current
subscription, to fetch the events as well as to cancel the subscription. The link to the
individual subscription is provided in the response to a subscription request. This
resource is dynamically created and deleted during runtime. The MAP panel assures that the
subscription resource URL is unique even over power cycles of the MAP panel. The URL
shall be treated as an opaque identifier for the individual subscription. No semantics or
sequence information shall be assumed by the client.


### Example


```python
import openapi_client
from openapi_client.models.sub import Sub
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
    api_instance = openapi_client.SubSIIDApi(api_client)
    sub_siid = '/538D759E63DA4E64A687F58C22793435' # str | Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub 

    try:
        # Individual subscription resource
        api_response = api_instance.get_sub_siid(sub_siid)
        print("The response of SubSIIDApi->get_sub_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubSIIDApi->get_sub_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_siid** | **str**| Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  | 

### Return type

[**Sub**](Sub.md)

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
**409** | Conflict &lt;br&gt; This command code is returned when a command is not executed due to application specific reasons. The body of the error response will contain further information on why the command was not executed. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. The body of the response will contain the list of resource URLs which prevented execution of the command.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sub_siid**
> FetchedEvents post_sub_siid(sub_siid, fetch_events)

Fetch events

A client fetches events from the buffer of this subscription by using a POST request with the defined, optional parameters in the body of the request.
Once events are successfully delivered to the client, they will be deleted from the internal event buffer. Thus events can only be fetched once.

Fetching the events is done by sending a POST request. <br>
Parameters are defined to allow to control on the event delivery to the client. The available parameters are:

#### maxEvents

The maximum number of events contained in the answer to this request. If
maxEvents is omitted, the number of events is set to the bufferSize of the subscription.
maxEvents is used to assure that the client only fetches as much events as it can
process in one batch.

#### minEvents

The minimum number of events contained in the answer to this request, i.e.
a request will return when at least minEvents is available. If minEvents is omitted or
minEvents is specified as 0, minEvents has the same value as maxEvents (at maximum
the bufferSize of the subscription).

#### maxTime

The maximum time in seconds a request will block. When maxTime expires,
the MAP panel will reply with the currently available events. If no events are available, an
empty event list will be provided. The default value of maxTime is 0. Thus, if maxTime is
omitted or set to 0 the request will return immediately with the available events (up to
maxEvents). The maximum possible value for maxTime is 100. Thus the call will never
block longer than for 100 seconds.<br><br>


The MAP panel will respond to a POST request as soon as the first of the previously specified
conditions is fulfilled. Thus, in case minEvents is not reached, the answer will return after
maxTime. In case minEvents is reached, the response is send immediately.
By adjusting maxEvents, minEvents and maxTime the client has the opportunity to optimize the
poling behaviour to its need. For example, when the client expects events rarely (e.g. alarm
messages) it could set “minEvents”: 1 and “maxTime”: 100. Thereby, the client is notified as
soon as a single event comes in. Using a long maxTime ensures that the poll request does not
need to be repeated often. Similarly, if it is expected that many events come in (e.g. state
changes in a disarmed area), the throughput can be improved by choosing a large minEvents
number e.g. “minEvents”: 100 to make sure that the data is transmitted efficiently. maxEvents
can be defined to ensure that not too many events are fetched which may not be possible to be
handled by the client e.g “maxEvents”:200.
In addition, a client can extend its lease by sending a request with “maxEvents” set to 0.
Thereby, the lease is extended and the response does not contain any events. This is
particularly useful, if the client is currently not able to process any events but wants to keep its
subscription on the MAP panel.


### Example


```python
import openapi_client
from openapi_client.models.fetch_events import FetchEvents
from openapi_client.models.fetched_events import FetchedEvents
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
    api_instance = openapi_client.SubSIIDApi(api_client)
    sub_siid = '/EDB1122914E14962A8BDCBD75B9ABA92' # str | Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub 
    fetch_events = {"@cmd":"FETCHEVENTS","maxEvents":100,"minEvents":1,"maxTime":50} # FetchEvents | 

    try:
        # Fetch events
        api_response = api_instance.post_sub_siid(sub_siid, fetch_events)
        print("The response of SubSIIDApi->post_sub_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubSIIDApi->post_sub_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_siid** | **str**| Unique subscription SIID. You can get all existing subscriptions SIIDs with the command GET /sub  | 
 **fetch_events** | [**FetchEvents**](FetchEvents.md)|  | 

### Return type

[**FetchedEvents**](FetchedEvents.md)

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
**409** | Conflict &lt;br&gt; This command code is returned when a command is not executed due to application specific reasons. The body of the error response will contain further information on why the command was not executed. This response code is also returned when a command on a list resource was issued with an “atomic” parameter. The code indicates that the execution of the command was not possible. The body of the response will contain the list of resource URLs which prevented execution of the command.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

