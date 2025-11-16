# bosch_alarm_map.AreaandtimemodellistApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_areaandtimemodellist**](AreaandtimemodellistApi.md#get_areaandtimemodellist) | **GET** /areaandtimemodellist | Get all area and time models of the MAP system
[**postareaandtimemodellist**](AreaandtimemodellistApi.md#postareaandtimemodellist) | **POST** /areaandtimemodellist | Get list of area and time models that were changed after specified syncID


# **get_areaandtimemodellist**
> AreaAndTimeModelList get_areaandtimemodellist()

Get all area and time models of the MAP system

This function returns a list of all areaandtimemodels saved in the MAP panel database, including all model attributes.

### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.area_and_time_model_list import AreaAndTimeModelList
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
    api_instance = bosch_alarm_map.AreaandtimemodellistApi(api_client)

    try:
        # Get all area and time models of the MAP system
        api_response = api_instance.get_areaandtimemodellist()
        print("The response of AreaandtimemodellistApi->get_areaandtimemodellist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AreaandtimemodellistApi->get_areaandtimemodellist: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AreaAndTimeModelList**](AreaAndTimeModelList.md)

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
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postareaandtimemodellist**
> AreaAndTimeModelList postareaandtimemodellist(area_and_time_modellist_post=area_and_time_modellist_post)

Get list of area and time models that were changed after specified syncID

The POST function is used to send only necassary modifications to a client. It is designed to transport only changes of the areaandtimemodel attributes, which are related to a previous areaandtimeModelSyncID. This will improve the performance and reduce the network load significantly for the normal use cases. <br>
Normal case means, that typically models are configured when the system is set up. Only minor adjustments are made afterwards.<br>
A client transmits to a MAP system its last areaandtimeModelSyncID, which it has stored. The MAP system responds a list, that included all used IDs.
Only the areaandtimemodels, where a modification happened between the received areaandtimeModelSyncID from the client and the current one of the MAP system will be sent with all user attributes. For all the other areaandtimemodels, only the areaandtimeModel ID without any other attributes is added.
The client system takes the modifications from the body and can check for areaandtimemodels that are deleted, because deleted areaandtimemodels do not appear anymore in the response body.<br>

### Remarks:

- If the client sends an *areaandtimeModelSyncID* that is exactly the same as the areaandtimeModelSyncID from the database, only the IDs without attributes are sent in the response, as there is no modification to be reported.
- If the client sends an *areaandtimeModelSyncID* that is higher than the ID in the database of the MAP system, an error is returned. The same applies when a negative areaandtimeModelSyncID is sent by the client.
- If the client sends an areaandtimeModelSyncID that is exactly 0, the response will contain all information fully.
- The MAP system saves always the latest areaandtimeModelSyncID as an extra attribute named *areaandtimeModelSyncIDModificationSyncID* into the RAM  when a areaandtimeModel was modified. A write to the existing database would break the existing database structure and does not perform good enough.
- By a (re-)boot the areaandtimeModelSyncID (URL /syncstatus) is increased by one and all *areaandtimeModelSyncIDModificationSyncID* entries in the RAM with this increased *areaandtimeModelSyncID*.
- If RPS for MAP updates the configuration on a MAP system,  this will typically also cause a reboot. It is fine and the syncIDs are increased, to be sure a fully synchronization is processed from all REST-API clients.
- The increase of the areaandtimeModelSyncID invalidates all areaandtimeModelSyncID which are saved by all REST-API clients and ensures all data will be synchronized if a reboot happens.


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.area_and_time_model_list import AreaAndTimeModelList
from bosch_alarm_map.models.area_and_time_modellist_post import AreaAndTimeModellistPost
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
    api_instance = bosch_alarm_map.AreaandtimemodellistApi(api_client)
    area_and_time_modellist_post = {"@cmd":"GETMODIFIEDLIST","areaAndTimeModelSyncID":572} # AreaAndTimeModellistPost |  (optional)

    try:
        # Get list of area and time models that were changed after specified syncID
        api_response = api_instance.postareaandtimemodellist(area_and_time_modellist_post=area_and_time_modellist_post)
        print("The response of AreaandtimemodellistApi->postareaandtimemodellist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AreaandtimemodellistApi->postareaandtimemodellist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_and_time_modellist_post** | [**AreaAndTimeModellistPost**](AreaAndTimeModellistPost.md)|  | [optional] 

### Return type

[**AreaAndTimeModelList**](AreaAndTimeModelList.md)

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

