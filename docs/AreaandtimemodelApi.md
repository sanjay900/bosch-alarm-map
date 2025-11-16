# openapi_client.AreaandtimemodelApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_areaandtimemodel**](AreaandtimemodelApi.md#get_areaandtimemodel) | **GET** /areaandtimemodel/{AreaAndTimeModelID} | Get a specific area and time model from the MAP system
[**post_areaandtimemodel**](AreaandtimemodelApi.md#post_areaandtimemodel) | **POST** /areaandtimemodel | Create, modify or delete an area and time model on the MAP system


# **get_areaandtimemodel**
> GetAreaandtimemodel200Response get_areaandtimemodel(area_and_time_model_id)

Get a specific area and time model from the MAP system

This function returns all parameters of a defined area and time model.


### Example


```python
import openapi_client
from openapi_client.models.get_areaandtimemodel200_response import GetAreaandtimemodel200Response
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
    api_instance = openapi_client.AreaandtimemodelApi(api_client)
    area_and_time_model_id = 'Installer Model, All Areas, Anytime' # str | Unique area and time model name

    try:
        # Get a specific area and time model from the MAP system
        api_response = api_instance.get_areaandtimemodel(area_and_time_model_id)
        print("The response of AreaandtimemodelApi->get_areaandtimemodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AreaandtimemodelApi->get_areaandtimemodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_and_time_model_id** | **str**| Unique area and time model name | 

### Return type

[**GetAreaandtimemodel200Response**](GetAreaandtimemodel200Response.md)

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
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**404** | Not found. The request URL with the specified parameter was not found.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_areaandtimemodel**
> AreaAndTimeModelSyncID post_areaandtimemodel(post_areaandtimemodel_request)

Create, modify or delete an area and time model on the MAP system

This function is used to create, modify or delete an AreaAndTime Model on a MAP system from the REST-API interface. It has the same functionalities like the RPS for MAP. This URL is designed to be used from a system, that controls remotely the user and system parameters of several MAP systems. <br>
To use the functions, every POST request needs a valid areaAndTimeModelSyncID. The initial areaAndTimeModelSyncID can be get from the commands GET /syncstatus or GET /areaandtimemodellist. After a successful operation, you get a new valid areaAndTimeModelSyncID back. It is recommended to use this ID, if you want to create, modify or delete several AreaAndTime models.<br>
A AreaAndTime Model can be assigned to access models. Do not delete the used AreaAndTime Model, if it has a dependency to an access model.

### Create AreaAndTime Model

To create a new AreaAndTime model on a MAP system, the client must ensure that the key value *areaAndTimeModelID* is not already used on the system. Further a valid areaAndTimeModelSyncID is required.
The example **createAreaAndTimeModel** shows how to create an AreaAndTime Model.

### Modify AreaAndTime Model

To modify an existing AreaAndTime model on a MAP system, the client needs a valid *areaAndTimeModelSyncID*.
The example *modifyAreaAndTimeModel* shows how to modify an AreaAndTime Model.


### Delete AreaAndTime Model

To delete an existing AreaAndTime model on a MAP system, the client needs also a valid *areaAndTimeModelSyncID*.
The example *deleteAreaAndTimeModel* shows how to delete an AreaAndTime Model.


### Example


```python
import openapi_client
from openapi_client.models.area_and_time_model_sync_id import AreaAndTimeModelSyncID
from openapi_client.models.post_areaandtimemodel_request import PostAreaandtimemodelRequest
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
    api_instance = openapi_client.AreaandtimemodelApi(api_client)
    post_areaandtimemodel_request = {"@cmd":"CREATE","areaAndTimeModelID":"Installer Model, All Areas, Anytime","alwaysAllowedPermissionSet":"Super User Permission","restrictedByAreaPermissionSet":"","restrictedByTimePermissionSet":"","restrictedByAreaAndTimePermissionSet":"","areaList":[],"timeModelID":"","areaAndTimeModelSyncID":145} # PostAreaandtimemodelRequest | 

    try:
        # Create, modify or delete an area and time model on the MAP system
        api_response = api_instance.post_areaandtimemodel(post_areaandtimemodel_request)
        print("The response of AreaandtimemodelApi->post_areaandtimemodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AreaandtimemodelApi->post_areaandtimemodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_areaandtimemodel_request** | [**PostAreaandtimemodelRequest**](PostAreaandtimemodelRequest.md)|  | 

### Return type

[**AreaAndTimeModelSyncID**](AreaAndTimeModelSyncID.md)

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

