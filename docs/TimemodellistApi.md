# openapi_client.TimemodellistApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_timemodellist**](TimemodellistApi.md#get_timemodellist) | **GET** /timemodellist | Get all time models of the MAP system
[**posttimemodellist**](TimemodellistApi.md#posttimemodellist) | **POST** /timemodellist | Get list of time models that were changed after specified syncID


# **get_timemodellist**
> TimeModelList get_timemodellist()

Get all time models of the MAP system

This function returns a list of all timemodels saved in the MAP panel database, including all model attributes.

### Example


```python
import openapi_client
from openapi_client.models.time_model_list import TimeModelList
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
    api_instance = openapi_client.TimemodellistApi(api_client)

    try:
        # Get all time models of the MAP system
        api_response = api_instance.get_timemodellist()
        print("The response of TimemodellistApi->get_timemodellist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimemodellistApi->get_timemodellist: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TimeModelList**](TimeModelList.md)

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
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **posttimemodellist**
> TimeModelList posttimemodellist(time_modellist_post=time_modellist_post)

Get list of time models that were changed after specified syncID

The POST function is used to send only necessary modifications to a client. It is designed to transport only changes of the timemodel attributes, which are related to a previous timeModelSyncID. This will improve the performance and reduce the network load significantly for the normal use cases. <br>
Normal case means, that typically models are configured when the system is set up. Only minor adjustments are made afterwards.<br>
A client transmits to a MAP system its last timeModelSyncID, which it has stored. The MAP system responds a list that included all used IDs.
Only the timemodels, where a modification happened between the received timeModelSyncID from the client and the current one of the MAP system will be sent with all user attributes. For all the other timemodels, only the timemodel ID without any other attributes is added.
The client system takes the modifications from the body and can check for timemodels that are deleted, because deleted timemodels do not appear anymore in the response body.<br>

### Remarks:

- If the client sends a *timeModelSyncID* that is exactly the same as the timeModelSyncID from the database, only the IDs without attributes are sent in the response, as there is no modification to be reported.
- If the client sends a *timeModelSyncID* that is higher than the ID in the database of the MAP system, an error is returned. The same applies when a negative dtimeModelSyncID is sent by the client.
- If the client sends a timeModelSyncID that is exactly 0, the response will contain all information fully.
- The MAP system saves always the latest timeModelSyncID as an extra attribute named *timeModelModificationSyncID* into the RAM when a timeModel was modified. A write to the existing database would break the existing database structure and does not perform good enough.
- By a (re-)boot the timeModelSyncID (URL /syncstatus) is increased by one and all *timemodelModificationSyncID* entries in the RAM with this increased *timeModelSyncID*.
- If RPS for MAP updates the configuration on a MAP system, this will typically also cause a reboot. It is fine and the syncIDs are increased, to be sure a fully synchronization is processed from all REST-API clients.
- The increase of the timeModelSyncID invalidates all timemodelSyncID that are saved by all REST-API clients and ensures all data will be synchronized if a reboot happens.


### Example


```python
import openapi_client
from openapi_client.models.time_model_list import TimeModelList
from openapi_client.models.time_modellist_post import TimeModellistPost
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
    api_instance = openapi_client.TimemodellistApi(api_client)
    time_modellist_post = {"@cmd":"GETMODIFIEDLIST","timeModelSyncID":572} # TimeModellistPost |  (optional)

    try:
        # Get list of time models that were changed after specified syncID
        api_response = api_instance.posttimemodellist(time_modellist_post=time_modellist_post)
        print("The response of TimemodellistApi->posttimemodellist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimemodellistApi->posttimemodellist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_modellist_post** | [**TimeModellistPost**](TimeModellistPost.md)|  | [optional] 

### Return type

[**TimeModelList**](TimeModelList.md)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | The request could not be completed due to a conflict with the current state of the SyncID. The client SHOULD NOT repeat the request without modifications. |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**404** | Not found. The request URL with the specified parameter was not found.  |  -  |
**409** | The request could not be completed due to a conflict with the current state of the SyncID. The client SHOULD NOT repeat the request without modifications. |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

