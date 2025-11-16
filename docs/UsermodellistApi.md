# bosch-alarm-map.UsermodellistApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usermodellist**](UsermodellistApi.md#get_usermodellist) | **GET** /usermodellist | Get a list of all users
[**post_usermodellist**](UsermodellistApi.md#post_usermodellist) | **POST** /usermodellist | Get only all user modifications, related to previous userModelSyncID


# **get_usermodellist**
> UserModelList get_usermodellist(var_property=var_property)

Get a list of all users

This function returns a list of all users saved in the MAP panel database, including all user attributes.
Furthermore, with the help of this URL it is possible to display only the users that are managed via a multi-user system.
To use this function, the query parameter *property* must be set with the variable *MUM*.
To assign to a user the property *MUM*, see the URL */mumusergroup*  .<br>

### Example query URL to get all users with the MUM flag:
  /usermodellist?property=MUM


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.user_model_list import UserModelList
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
    api_instance = bosch-alarm-map.UsermodellistApi(api_client)
    var_property = 'var_property_example' # str | Querying by property parameter will filter all existing users with UserID that have specified property flag set. UserID property is a set of flags for each UserID.  List of properties: - MUM: Multi-User-MAP: reserved for MUM usage; MAP Keypad cannot use (create) Users with MUM flagged UserID.  Each UserID has exactly one set of flags attached, UserID can be set in range [4, 998].  (optional)

    try:
        # Get a list of all users
        api_response = api_instance.get_usermodellist(var_property=var_property)
        print("The response of UsermodellistApi->get_usermodellist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsermodellistApi->get_usermodellist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_property** | **str**| Querying by property parameter will filter all existing users with UserID that have specified property flag set. UserID property is a set of flags for each UserID.  List of properties: - MUM: Multi-User-MAP: reserved for MUM usage; MAP Keypad cannot use (create) Users with MUM flagged UserID.  Each UserID has exactly one set of flags attached, UserID can be set in range [4, 998].  | [optional] 

### Return type

[**UserModelList**](UserModelList.md)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request. Query parameters are unknown or malformed.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_usermodellist**
> UserModelList post_usermodellist(user_modellist_post=user_modellist_post)

Get only all user modifications, related to previous userModelSyncID

The POST function is used to send only necessary modifications to a client. It is designed to transport only changes of the user attributes, which are related to a previous userModelSyncID. This will improve the performance and reduce the network load significantly for the normal use cases. <br>
Normal case means, that typically only a few modifications of a few users are done. Such as 1 of 200 users changed the password locally from a MAP Keypad.<br>
A client transmits to a MAP system its last userModelSyncID, which it has stored. The MAP system responds a list that includes all used user IDs.
Only the users, where a modification happened between the received userModelSyncID from the client and the current one of the MAP system will be sent with all user attributes. For all the other users, only the user ID without any other attributes is added.
The client system takes the modifications from the body and can check for users that are deleted, because deleted users do not appear anymore in the response body.<br>

### Remarks:

- If the client sends a *userModelSyncID* that is exactly the same as the userModelSyncID from the database, only the userIDs without attributes are sent in the response, as there is no modification to be reported.
- If the client sends a *userModelSyncID* that is higher than the ID in the database of the MAP system, an error is returned. The same applies when a negative userModelSyncID is sent by the client.
- If the client sends a userModelSyncID that is exactly 0, the response will contain all information fully.
- The MAP system saves always the latest userModelSyncID as an extra attribute named *userModificationSyncID* into the RAM  when a user was modified. A write to the existing database would break the existing database structure and does not perform good enough.
- By a (re-)boot the userModelSyncID (URL /syncstatus) is increased by one and all *userModificationSyncID*  entries in the RAM with this increased *userModelSyncID*.
- If RPS for MAP updates the configuration on a MAP system, this will typically also cause a reboot. It is fine and the syncIDs are increased, to be sure a fully synchronization is processed from all REST-API clients.
- The increase of the userModelSyncID invalidates all userModelSyncID which are saved by all REST-API clients and ensures all data will be synchronized if a reboot happens.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.user_model_list import UserModelList
from bosch-alarm-map.models.user_modellist_post import UserModellistPost
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
    api_instance = bosch-alarm-map.UsermodellistApi(api_client)
    user_modellist_post = {"@cmd":"GETMODIFIEDLIST","userModelSyncID":201} # UserModellistPost |  (optional)

    try:
        # Get only all user modifications, related to previous userModelSyncID
        api_response = api_instance.post_usermodellist(user_modellist_post=user_modellist_post)
        print("The response of UsermodellistApi->post_usermodellist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsermodellistApi->post_usermodellist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_modellist_post** | [**UserModellistPost**](UserModellistPost.md)|  | [optional] 

### Return type

[**UserModelList**](UserModelList.md)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. The request succeeded, and resource was either created, modified or deleted. |  -  |
**400** | The request could not be completed due to a conflict with the current state of the SyncID. The client SHOULD NOT repeat the request without modifications. |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**409** | The request could not be completed due to a conflict with the current state of the SyncID. The client SHOULD NOT repeat the request without modifications. |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

