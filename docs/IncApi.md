# openapi_client.IncApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inc**](IncApi.md#get_inc) | **GET** /inc | List of all incidents in the MAP
[**post_inc**](IncApi.md#post_inc) | **POST** /inc | Handle, or silence a list of incidents


# **get_inc**
> IncList get_inc()

List of all incidents in the MAP

Alarms and troubles of the MAP system are modelled as so called incidents. In difference to other
resources like area or point, an incident resource will not always exist, but will be created when
an alarm/trouble appears in the system. The incident resource will also be removed from the REST-API
when the alarm/trouble is resolved and disappears from the Keypad.

### General Concept

The REST-API includes an event notification mechanism that allows spontaneous transmission of state
changes (e.g. closing of a door contact) and occurrence of incidents (e.g. intrusion alarms). The
notification mechanism uses a publish-subscribe pattern, where a client has to register with the
MAP panel to specify which events it is interested in. This allows to custom tailor the events collected
for each individual client. For example, a client may subscribe only for incidents in the system.
In this case, it will only be notified about alarms and troubles but will not be notified about state
changes of peripherals, significantly reducing the amount of events to be communicated.
Once a subscription has been successfully created, the MAP panel will internally store the events for
the client in a ring buffer with a defined size. It is the task of the client to fetch the events by
issuing a request to a subscription specific URL.

#### Event delivery

The delivery of the events is done using a so called long polling mechanism. This means that
an incoming request to fetch events will not return an answer until either a sufficient amount of
events is available or a timer expires. A client specifies for each request how much events shall
be included in the response as a minimum (minEvents), as a maximum (maxEvents) and how
long the call is allowed to block at most (maxTime).
In general, a client needs to fetch its events periodically to make sure that all events are
received. The MAP panel will store only a limited amount of events for the client. In case events are
not fetched in time, the oldest events in the buffer are overridden (ring buffer). A client can
inspect the event id to recognize a buffer overflow. Even after a buffer overflow, MAP panel will
continue to collect events. It is the choice of a client if an overflow is acceptable or not. If not, a
client can unsubscribe to free the buffer and create a new subscription.

#### Lease time

A client also needs to ensure to poll for new events periodically, as the MAP panel will delete
subscriptions that have been inactive for a given time (lease time negotiated during
subscription). In cases where a client is not able to continuously poll events e.g. due to overload
conditions, a client can fetch events with maxEvents set to 0. Such a request will be interpreted
as subscription renewal but no events will be sent to the client.


#### Event structure

The system will create events in case of creation of a new resource, a state change of an
existing resource or on deletion of a resource. Each event will have a unique ID, a timestamp
which marks the time of occurrence, a type (created/changed/deleted) and the complete
resource representation. In addition, a list of property keys is included in a state change event
to indicate the properties that have changed in the resource.

The incident resource itself contains all relevant information about the alarm. In particular, it
conveys who has acknowledged or handled the alarm. Creation, deletion and state changes of
an incident are communicated via events.
The incidents are located under the root resource “/inc”. This resource acts as an incident list,
where all pending incidents in the system can be accessed. The individual incidents are located
under /inc with the following structure:
/inc/[Area ID]/[incident ID]


### Example


```python
import openapi_client
from openapi_client.models.inc_list import IncList
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
    api_instance = openapi_client.IncApi(api_client)

    try:
        # List of all incidents in the MAP
        api_response = api_instance.get_inc()
        print("The response of IncApi->get_inc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncApi->get_inc: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IncList**](IncList.md)

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

# **post_inc**
> post_inc(incident_resource)

Handle, or silence a list of incidents

Depending on the device type and incident type, the life cycle of the incident varies. The
interface provides information on what the client is expected to do. The “Handling Required”
attribute of the incident resource indicates whether a user needs to handle/acknowledge the
incident via the REST-API or the Keypad before it can get resolved and deleted.
Usually incident can only be handled when area is disarmed. However there is a configuration
option to explicitly allow handling in armed areas (“Allow Reset of Armed Areas”).
Some types of incidents (e.g. LSN Loop tamper) require to be handled after the device is back
to normal, thus “Handling Required” will remain true even if it was already handled. User has to
retry handling until the incident is deleted.


### Example


```python
import openapi_client
from openapi_client.models.incident_resource import IncidentResource
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
    api_instance = openapi_client.IncApi(api_client)
    incident_resource = {"@cmd":"HANDLE"} # IncidentResource | 

    try:
        # Handle, or silence a list of incidents
        api_instance.post_inc(incident_resource)
    except Exception as e:
        print("Exception when calling IncApi->post_inc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_resource** | [**IncidentResource**](IncidentResource.md)|  | 

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
**409** | Conflict. Execution of the command was not possible. Possible Resons: List of resource urls which prevented the command from being executed when ATOMIC is TRUE or the string describing that application rules prevented execution of the command on any element of the list. It will be only retrurned when atomic is false.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

