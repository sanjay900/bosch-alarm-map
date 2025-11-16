# bosch-alarm-map.HistoryApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_history**](HistoryApi.md#get_history) | **GET** /history | The history log consists of events in the MAP panel configured to be logged.


# **get_history**
> History get_history()

The history log consists of events in the MAP panel configured to be logged.

The history resource provides access to the MAP panel history data base. Each entry in the history
describes an event in the MAP panel that has been configured to be logged in the history. As the
history consists of a large amount of entries, dedicated filters are defined that allow paged
access to the history. Thus, a client does not need to fetch the complete history in one GET
request. Due to its size, the history data resource does not create any events.
MAP panel provides two separate history data bases:
- main history, consists of events in the panel configured to be logged.
- IPCHistory (IP Communicator History), consists only of events related to reporting over IP.
IPCHistory is applicable only if the MAP panel has been configured to report over IP. Events in IPCHistory will not be logged in panel main history.
A client will have to fetch events from main history and IPCHistory separately.
The history in the MAP panel is implemented as a ring buffer causing older events to be deleted when
the buffer is full. Thus, a client that wants to archive all events need to read out the history
regularly to make sure that no events get overwritten before they could be fetched.
Each history entry is following a fixed structure of:
- Event id: Unique ID for this event
- Timestamp: Time when the event occurred. Timestamp is ISO8601 compliant but not REST-API date time compliant as time zone is not included.
- Event name: Human readable string describing the event
- SIID: Id of the system element that triggered that event
- Parameters: Additional information on the event in a key value fashion. Each key and
value are separated by a “ = “ (two whitespaces + = ). Multiple key value pairs are
separated by a “\n”, which is a JSON reserved character. For example, the keys
IsMandatory and ModifierUser_ID are represented as
IsMandatory = No\nModifierUser_ID = 2\n
The history resource is represented as a JSON structure which contains an array of history
entries. Each history entry contains the above defined fields separated by a semicolon “;”. For
example:
"883953013;2014-07-24T13:24:13.256;RPS Accessed the System;TA_OCCUR;1.1.System.4.1;IsMandatory = No\n"


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.history import History
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
    api_instance = bosch-alarm-map.HistoryApi(api_client)

    try:
        # The history log consists of events in the MAP panel configured to be logged.
        api_response = api_instance.get_history()
        print("The response of HistoryApi->get_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->get_history: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**History**](History.md)

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

