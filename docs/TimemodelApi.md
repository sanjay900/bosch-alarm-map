# bosch_alarm_map.TimemodelApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_timemodel**](TimemodelApi.md#get_timemodel) | **GET** /timemodel/{timeModelID} | Get a specific timemodel item from the MAP system.
[**post_timemodel**](TimemodelApi.md#post_timemodel) | **POST** /timemodel | Create, modify or delete a new Time Model on the MAP System


# **get_timemodel**
> GetTimemodel200Response get_timemodel(time_model_id)

Get a specific timemodel item from the MAP system.

Get a model by ID

### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.get_timemodel200_response import GetTimemodel200Response
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
    api_instance = bosch_alarm_map.TimemodelApi(api_client)
    time_model_id = '24-Hour' # str | Unique name of a time model

    try:
        # Get a specific timemodel item from the MAP system.
        api_response = api_instance.get_timemodel(time_model_id)
        print("The response of TimemodelApi->get_timemodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimemodelApi->get_timemodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_model_id** | **str**| Unique name of a time model | 

### Return type

[**GetTimemodel200Response**](GetTimemodel200Response.md)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**404** | Not found. The request URL with the specified parameter was not found.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_timemodel**
> TimeModelSyncID post_timemodel(post_timemodel_request)

Create, modify or delete a new Time Model on the MAP System

This function is used to create, modify or delete a time model on a MAP system from the REST-API interface. It has the same functionalities like the RPS for MAP. This URL is designed to be used from a MAP system, that controls remotely the user and system parameters of several MAP systems. <br>
To use the functions, every POST request needs a valid timeModelSyncID. The initial timeModelSyncID can be get from the commands GET /syncstatus or GET timemodellist. After a successful operation, you get a new valid dayModelSyncID back. It is recommended to use this ID, if you want to create, modify or delete several day models.<br>
A time model can be used from an area and time model or a Smartkey model. Do not delete the time model, if it has a dependency to an area and time model or a Smartkey model.

### Create time model

To create a new time model on a MAP system, the client must ensure that the key value *timeModelID* is not already used on the system. Further a valid timeModelSyncID is required.
The example *createTimeModel* shows how to create a time model:

### Modify time model

To modify an existing day model on a MAP system, the client needs a valid dayModelSyncID.
The example *modifyTimeModel* shows how to modify a time model:

### Delete time model

To delete an existing day model on a MAP system, the client needs also a valid dayModelSyncID.
The example  *deleteTimeModel* shows how to delete a time model:


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.post_timemodel_request import PostTimemodelRequest
from bosch_alarm_map.models.time_model_sync_id import TimeModelSyncID
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
    api_instance = bosch_alarm_map.TimemodelApi(api_client)
    post_timemodel_request = {"@cmd":"CREATE","timeModelID":"6 Days (No Sundays)","referenceDate":"2011-10-11","ignoreSpecialDays":false,"periodInDays":[{"dayModelID":"Normal Work Day","priority":1},{"dayModelID":"Normal Work Day","priority":1},{"dayModelID":"Normal Work Day","priority":1},{"dayModelID":"Normal Work Day","priority":1},{"dayModelID":"Friday Work Day","priority":1},{"dayModelID":"Saturday Work Day","priority":1},{"dayModelID":"No Access","priority":1}],"specialDays":["New Year's Day","Christmas"],"timeModelSyncID":156} # PostTimemodelRequest | 

    try:
        # Create, modify or delete a new Time Model on the MAP System
        api_response = api_instance.post_timemodel(post_timemodel_request)
        print("The response of TimemodelApi->post_timemodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimemodelApi->post_timemodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_timemodel_request** | [**PostTimemodelRequest**](PostTimemodelRequest.md)|  | 

### Return type

[**TimeModelSyncID**](TimeModelSyncID.md)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. The request succeeded, and resource was either created, modified or deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**404** | Not found. The request URL with the specified parameter was not found.  |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

