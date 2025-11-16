# bosch_alarm_map.AccessmodelApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accessmodel**](AccessmodelApi.md#get_accessmodel) | **GET** /accessmodel/{AccessModelID} | Get a specific accessmodel from the MAP system
[**post_accessmodel**](AccessmodelApi.md#post_accessmodel) | **POST** /accessmodel | Create a new access model on the MAP system


# **get_accessmodel**
> GetAccessmodel200Response get_accessmodel(access_model_id)

Get a specific accessmodel from the MAP system

Get a model by ID

### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.get_accessmodel200_response import GetAccessmodel200Response
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
    api_instance = bosch_alarm_map.AccessmodelApi(api_client)
    access_model_id = 'Installer Profile' # str | Unique accessmodel name

    try:
        # Get a specific accessmodel from the MAP system
        api_response = api_instance.get_accessmodel(access_model_id)
        print("The response of AccessmodelApi->get_accessmodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessmodelApi->get_accessmodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_model_id** | **str**| Unique accessmodel name | 

### Return type

[**GetAccessmodel200Response**](GetAccessmodel200Response.md)

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

# **post_accessmodel**
> AccessModelSyncID post_accessmodel(post_accessmodel_request)

Create a new access model on the MAP system

This function is used to create, modify or delete an access model on a MAP system from the REST-API interface. It has the same functionalities like the RPS for MAP. This URL is designed to be used from a system, that controls remotely the user and system parameters of several MAP systems. <br>
To use the functions, every POST request needs a valid accessModelSyncID. The initial areaAndTimeModelSyncID can be get from the commands GET /syncstatus or GET /accesmodellist. After a successful operation, you get a new valid accessModelSyncID back. It is recommended to use this ID, if you want to create, modify or delete several AreaAndTime models.<br>
An access model can be assigned to users. Do not delete the used access model, if it has a dependency to a user.

### Create Access Model

To create a new access model on a MAP system, the client must ensure that the key value *accessModelID* is not already used on the system. Further a valid accessModelSyncID is required.
The example *createAccessModel* shows how to create an access model.

### Modify Access Model

To modify an existing access model on a MAP system, the client needs a valid *areaAndTimeModelSyncID*.
The example *modifyAccessModel* shows how to modify an access model.


### Delete Access Model

To delete an existing access model on a MAP system, the client needs also a valid *accessModelSyncID*.
The example *deleteAccessModel** shows how to delete an access model:


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.access_model_sync_id import AccessModelSyncID
from bosch_alarm_map.models.post_accessmodel_request import PostAccessmodelRequest
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
    api_instance = bosch_alarm_map.AccessmodelApi(api_client)
    post_accessmodel_request = {"@cmd":"CREATE","accessModelID":"Installer Profile","accessProfileLevel":1,"areaAndTimeModelList":["Installer Model","Owner/Facility Manager Model"],"accessModelSyncID":156} # PostAccessmodelRequest | 

    try:
        # Create a new access model on the MAP system
        api_response = api_instance.post_accessmodel(post_accessmodel_request)
        print("The response of AccessmodelApi->post_accessmodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessmodelApi->post_accessmodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_accessmodel_request** | [**PostAccessmodelRequest**](PostAccessmodelRequest.md)|  | 

### Return type

[**AccessModelSyncID**](AccessModelSyncID.md)

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

