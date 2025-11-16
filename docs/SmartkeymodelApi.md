# openapi_client.SmartkeymodelApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_smartkeymodel**](SmartkeymodelApi.md#get_smartkeymodel) | **GET** /smartkeymodel/{SmartkeyModelID} | Get a specific Smartkey model from the MAP system
[**post_smartkeymodel**](SmartkeymodelApi.md#post_smartkeymodel) | **POST** /smartkeymodel | Create a new Smartkey model on the MAP System


# **get_smartkeymodel**
> GetSmartkeymodel200Response get_smartkeymodel(smartkey_model_id)

Get a specific Smartkey model from the MAP system

This function returns a list with all Smartkey models and their parameters on a MAP system.

### Example


```python
import openapi_client
from openapi_client.models.get_smartkeymodel200_response import GetSmartkeymodel200Response
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
    api_instance = openapi_client.SmartkeymodelApi(api_client)
    smartkey_model_id = 'SuperSmartKeyAccess' # str | Unique Smartkey model name

    try:
        # Get a specific Smartkey model from the MAP system
        api_response = api_instance.get_smartkeymodel(smartkey_model_id)
        print("The response of SmartkeymodelApi->get_smartkeymodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartkeymodelApi->get_smartkeymodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smartkey_model_id** | **str**| Unique Smartkey model name | 

### Return type

[**GetSmartkeymodel200Response**](GetSmartkeymodel200Response.md)

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

# **post_smartkeymodel**
> SmartkeyModelSyncID post_smartkeymodel(post_smartkeymodel_request)

Create a new Smartkey model on the MAP System

This function is used to create, modify or deletes Smartkey models on a MAP system from the REST-API interface. It has the same functionalities like the RPS for MAP. This URL is designed to be used from a system, that controls remotely the user and system parameters of several MAP system. <br>
To use the functions, every POST request needs a valid smartkeyModelSyncID. The initial smartkeyModelSyncID can be get from the commands GET /syncstatus or GET /smartkeymodellist. After a successful operation, you get a new valid areaAndTimeModelSyncID back. It is recommended to use this ID, if you want to create, modify or delete several smartkey models.<br>
A Smartkey model can be assigned to one or several users. Do not delete the used Smartkey model, if it has a dependency to a user.

### Create smartkey model

To create a new Smartkey model on a MAP system, the client must ensure that the key value *smartkeyModelID* is not already used on the system. Further a valid smartkeyModelSyncID is required.
The example *createSmartkeyModel* shows an example how to create a Smartkey model.

### Modify smartkey smartkeyModelSyncID

To modify an existing Smartkey model on a MAP system, the client needs a valid *smartkeyModelSyncID*.
The example *modifySmartkeyModel* shows an example how to modify a Smartkey model.

### Delete smartkey model

To delete an existing Smartkey model on a MAP system, the client needs also a valid *smartkeyModelSyncID*.
The example *deleteSmartkeyModel* shows an example how to delete a Smartkey model.


### Example


```python
import openapi_client
from openapi_client.models.post_smartkeymodel_request import PostSmartkeymodelRequest
from openapi_client.models.smartkey_model_sync_id import SmartkeyModelSyncID
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
    api_instance = openapi_client.SmartkeymodelApi(api_client)
    post_smartkeymodel_request = {"@cmd":"CREATE","smartkeyModelID":"Basic SmartkeyProfile 1","areaScopeList":["Control Panel Area","Area 1"],"armAuthority":"CanArmAnyTime","disarmAuthority":"CanDisarm","timeModelUsedForDisarming":"6 Days (No Sundays)","smartkeyModelSyncID":156} # PostSmartkeymodelRequest | 

    try:
        # Create a new Smartkey model on the MAP System
        api_response = api_instance.post_smartkeymodel(post_smartkeymodel_request)
        print("The response of SmartkeymodelApi->post_smartkeymodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartkeymodelApi->post_smartkeymodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_smartkeymodel_request** | [**PostSmartkeymodelRequest**](PostSmartkeymodelRequest.md)|  | 

### Return type

[**SmartkeyModelSyncID**](SmartkeyModelSyncID.md)

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

