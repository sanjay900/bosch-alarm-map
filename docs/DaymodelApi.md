# bosch_alarm_map.DaymodelApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_daymodel**](DaymodelApi.md#get_daymodel) | **GET** /daymodel/{dayModelID} | Get a specific daymodel item from the MAP system
[**post_day_model**](DaymodelApi.md#post_day_model) | **POST** /daymodel | Create, modify or delete a day model on the MAP System


# **get_daymodel**
> GetDaymodel200Response get_daymodel(day_model_id)

Get a specific daymodel item from the MAP system

Get a model by ID

### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.get_daymodel200_response import GetDaymodel200Response
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
    api_instance = bosch_alarm_map.DaymodelApi(api_client)
    day_model_id = '24-Hour' # str | Unique name of a DayModel item. The name is used to identify the item on the MAP system

    try:
        # Get a specific daymodel item from the MAP system
        api_response = api_instance.get_daymodel(day_model_id)
        print("The response of DaymodelApi->get_daymodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DaymodelApi->get_daymodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day_model_id** | **str**| Unique name of a DayModel item. The name is used to identify the item on the MAP system | 

### Return type

[**GetDaymodel200Response**](GetDaymodel200Response.md)

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

# **post_day_model**
> DayModelSyncID post_day_model(post_day_model_request)

Create, modify or delete a day model on the MAP System

This function is used to create, modify or delete day model on a MAP system from the REST-API interface. It has the same functionalities like the RPS for MAP. This URL is designed to be used from a system, that controls remotely the user and system parameters of several MAP systems. <br>
To use the functions, every POST request needs a valid dayModelSyncID. The initial dayModelSyncID can be get from the command GET /syncstatus or GET /daymodellist. After a successful operation, you get a new valid dayModelSyncID back. It is recommended to use this ID, if you want to create, modify or delete several day models.<br>
By the creation or modification of the *interval* array, the client must ensure that the previous interval value is set. The client must also ensure that the intervals are not overlapped and that the start time is earlier than the end time.
A day model can be used from a time model and/or a specialday model. Do not delete the used daymodel, if it has a dependency to a time model or specialday model.

### Create day model

To create a new daymodel on a MAP system, the client must ensure that the key value *dayModelID* is not already used on the system. Further a valid dayModelSyncID is required.
The example *createDayModel* shows how to create a daymodel:

### Modify day model

To modify a existing day model on a MAP system, the client needs a valid dayModelSyncID.
The example *modifyDayModel* shows how to modify a day model:

### Delete day model

To delete a existing day model on a MAP system, the client needs also a valid dayModelSyncID.
The example *deleteDayModel* shows how to delete a day model:


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.day_model_sync_id import DayModelSyncID
from bosch_alarm_map.models.post_day_model_request import PostDayModelRequest
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
    api_instance = bosch_alarm_map.DaymodelApi(api_client)
    post_day_model_request = {"@cmd":"CREATE","dayModelID":"Cleaning/ Service Time","interval":["06:00:00 - 08:00:00","16:00:00 - 20:00:00","00:00:00 - 00:00:00"],"dayModelSyncID":156} # PostDayModelRequest | 

    try:
        # Create, modify or delete a day model on the MAP System
        api_response = api_instance.post_day_model(post_day_model_request)
        print("The response of DaymodelApi->post_day_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DaymodelApi->post_day_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_day_model_request** | [**PostDayModelRequest**](PostDayModelRequest.md)|  | 

### Return type

[**DayModelSyncID**](DayModelSyncID.md)

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
**409** | The request could not be completed due to a conflict with the current state of the resource. The client SHOULD NOT repeat the request without modifications. |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

