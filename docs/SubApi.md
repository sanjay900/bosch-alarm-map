# bosch_alarm_map.SubApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sub**](SubApi.md#get_sub) | **GET** /sub | List current event subscriptions
[**post_sub**](SubApi.md#post_sub) | **POST** /sub | Create a subscription


# **get_sub**
> SubList get_sub()

List current event subscriptions

The MAP panel provides event notifications for all resources. This *GET* function is used, to get a subscription resource list.
The subscription list resource allows access to all subscriptions. Furthermore, it is the location where a client can create a subscription.

### Subscription Resource List: (/sub) ###

A central resource where a client can create a
subscription. The location of the subscription resource is currently (“/sub”). However, a
client shall not assume the location to be fixed but rather take the location from the
panel description resource, to anticipate changes in future interface versions. The
subscription resource also provides an overview on all existing subscriptions.

A client can decide which events to receive from the panel by setting the appropriate filters for
the subscription. One client can also create multiple subscriptions so that the queue sizes and
fetching behaviour fits to the expected occurrence of events. For example, it can be assumed
that incidents will only occur rarely while device state changes will happen often. Thus, a client
may create two subscriptions; one subscription for incidents only and one subscription for
devices only. Thus, incidents can be prioritized and fetched quicker as if they would be part of
the same subscription.

A client who wants to subscribe to all resources of the panel may specify a filter with all
elements in the subscription list. Please note that the URL of the resources may change over time.
Thus, a client shall look up the URL for the given resource type from the description resource to
be forward compatible.


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.sub_list import SubList
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
    api_instance = bosch_alarm_map.SubApi(api_client)

    try:
        # List current event subscriptions
        api_response = api_instance.get_sub()
        print("The response of SubApi->get_sub:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubApi->get_sub: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SubList**](SubList.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. Subscription List object structure. The list object will only contain resources which match the defined filters given in the query parameters. |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sub**
> CreatedSub post_sub(create_sub)

Create a subscription

In order to create a subscription, a client has to send a POST request to the subscription list
resource. The body of the POST request contains all relevant information about the
subscription.
In case the MAP panel accepts the subscription, it will respond with a 201 ("Created"). The response
will contain further details about the subscription. The subscription will be created only for those
resources to which the client has access rights to.
Please note that the MAP panel may decide to enforce a different leaseTime and bufferSize as
requested by the client. Thus, a client has to adhere to the leaseTime contained in the response
and cannot assume that the originally requested time is going to be used for this subscription.
A subscription may not be accepted due to three main reasons:
- MAP panel is not able to accommodate more subscriptions (e.g. maximum number of subscribers exceeded)
- Subscription request violates access rights
- subscription request is malformed


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.create_sub import CreateSub
from bosch_alarm_map.models.created_sub import CreatedSub
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
    api_instance = bosch_alarm_map.SubApi(api_client)
    create_sub = bosch_alarm_map.CreateSub() # CreateSub | 

    try:
        # Create a subscription
        api_response = api_instance.post_sub(create_sub)
        print("The response of SubApi->post_sub:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubApi->post_sub: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sub** | [**CreateSub**](CreateSub.md)|  | 

### Return type

[**CreatedSub**](CreatedSub.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. The request succeeded, and resource was either created, modified or deleted. |  -  |
**400** | Bad request &lt;br&gt; This response code indicates a malformed or otherwise faulty request.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

