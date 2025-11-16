# bosch_alarm_map.PermissionmodelApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permissionmodel**](PermissionmodelApi.md#get_permissionmodel) | **GET** /permissionmodel/{PermissionModelID} | Get a specific permission model from the MAP system
[**post_permisionmodel**](PermissionmodelApi.md#post_permisionmodel) | **POST** /permissionmodel | Create a new permission model on the MAP system


# **get_permissionmodel**
> GetPermissionmodel200Response get_permissionmodel(permission_model_id)

Get a specific permission model from the MAP system

Get a model by ID

### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.get_permissionmodel200_response import GetPermissionmodel200Response
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
    api_instance = bosch_alarm_map.PermissionmodelApi(api_client)
    permission_model_id = 'Installer Permission' # str | Unique permission model name

    try:
        # Get a specific permission model from the MAP system
        api_response = api_instance.get_permissionmodel(permission_model_id)
        print("The response of PermissionmodelApi->get_permissionmodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionmodelApi->get_permissionmodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_model_id** | **str**| Unique permission model name | 

### Return type

[**GetPermissionmodel200Response**](GetPermissionmodel200Response.md)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation, update daymodel |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**404** | Not found. The request URL with the specified parameter was not found.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_permisionmodel**
> PermissionModelSyncID post_permisionmodel(post_permisionmodel_request)

Create a new permission model on the MAP system

This function is used to create, modify or delete a permission model on a MAP system from the REST-API interface. It has the same functionalities like the RPS for MAP. This URL is designed to be used from a system, that controls remotely the user and system parameters of several MAP systems. <br>
To use the functions, every POST request needs a valid permissionModelSyncID. The initial permissionModelSyncID can be get from the commands GET /syncstatus or GET /permissionmodellist. After a successful operation, you get a new valid permissionModelSyncID back. It is recommended to use this ID, if you want to create, modify or delete several AreaAndTime models.<br>
A permission model can be assigned to Area and Time Model. Do not delete the used permission model, if it has a dependency to a Area and Time Model.

### Create permission model

To create a new permission model on a MAP system, the client must ensure that the key value *permissionModelSyncID* is not already used on the system. Further a valid accesspermissionModelSyncID is required.
The example *createPermissionModel* shows how to create a permission model:

### Modify permission model

To modify an existing permission model on a MAP system, the client needs a valid *permissionModelSyncID*.
The example *modifyPermissionModel** shows how to modify a permission model:

### Delete permission model

To delete an existing access model on a MAP system, the client needs also a valid *permissionModelSyncID*.
The example *deletePermissionModel* shows how to delete a permission model:


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.permission_model_sync_id import PermissionModelSyncID
from bosch_alarm_map.models.post_permisionmodel_request import PostPermisionmodelRequest
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
    api_instance = bosch_alarm_map.PermissionmodelApi(api_client)
    post_permisionmodel_request = {"@cmd":"CREATE","permissionModelID":"Installer Permission","armCategoryPermissions":{"mayArmArea":true,"mayArmWithActiveTamper":true,"mayDisarmArea":true,"mayDisarmOnlyFromAlarm":true,"mayBypassDetector":true,"mayForceBypassDetectorsInArea":true,"mayUnBypassDetector":true,"mayUnBypassforciblybypassedDetectorsInAr":true,"maySwitchInternalProgramOn/Off":true},"EventCategoryPermissions":{"mayClearInternalAlarm":true,"mayClearExternalAlarm":true,"mayClearTamper":true,"mayClearTrouble":true,"mayClearBatteryTrouble":true,"maySilence":true,"mayClearMainPowerFailure":true,"mayClearATS":true},"maintenanceCategoryPermissions":{"mayAdjustControlCenterVolume/Backlight":true,"mayChangeOutputState":true,"maySetDateTime":true,"mayTestBell":true,"mayTestMotionDetectors":true,"mayWalkTestAutomaticPoints":true,"mayWalkTestPoints":true,"mayChangeNetworkSetting":true},"operationsCategoryPermissions":{"mayDisableDevice":true,"mayEnableDevice":true,"mayTurnChimeOn/Off":true,"mayChangeSchedule":true,"mayEditBlockingTime":true},"remoteServiceCategoryPermissions":{"mayAuthorizeManufacturerUser":true,"mayAuthorizeRPSUser":true},"statusCategoryPermissions":{"mayViewAreaStatus":true,"mayViewDeviceStatus":true,"mayViewDuressAlarm":true,"mayViewAlarmCount":true,"mayViewEventMemory":true,"mayViewControlPanelHistory":true,"mayPrintControlPanelHistory":true,"mayViewControlPanelVersion":true},"userCategoryPermissions":{"mayAddUser":true,"mayDeleteUser":true,"mayChangeUserPasscode":true},"permissionModelSyncID":156} # PostPermisionmodelRequest | 

    try:
        # Create a new permission model on the MAP system
        api_response = api_instance.post_permisionmodel(post_permisionmodel_request)
        print("The response of PermissionmodelApi->post_permisionmodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionmodelApi->post_permisionmodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_permisionmodel_request** | [**PostPermisionmodelRequest**](PostPermisionmodelRequest.md)|  | 

### Return type

[**PermissionModelSyncID**](PermissionModelSyncID.md)

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

