# bosch-alarm-map.UsermodelApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usermodel_by_id**](UsermodelApi.md#get_usermodel_by_id) | **GET** /usermodel/{id} | Get all parameters of specific user from MAP system
[**post_usermodel**](UsermodelApi.md#post_usermodel) | **POST** /usermodel | Create, modify or delete a user on the MAP system


# **get_usermodel_by_id**
> GetUsermodelById200Response get_usermodel_by_id(id)

Get all parameters of specific user from MAP system

This function returns all parameters of a defined user. The passcode of the user is encrypted.

### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.get_usermodel_by_id200_response import GetUsermodelById200Response
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
    api_instance = bosch-alarm-map.UsermodelApi(api_client)
    id = '/004' # str | Unique user ID of each MAP system user. Possible user IDs are in the range from 4 to 998.

    try:
        # Get all parameters of specific user from MAP system
        api_response = api_instance.get_usermodel_by_id(id)
        print("The response of UsermodelApi->get_usermodel_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsermodelApi->get_usermodel_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique user ID of each MAP system user. Possible user IDs are in the range from 4 to 998. | 

### Return type

[**GetUsermodelById200Response**](GetUsermodelById200Response.md)

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

# **post_usermodel**
> UserModelSyncID post_usermodel(user_model_post=user_model_post)

Create, modify or delete a user on the MAP system

This function is used to create, modify or delete users on a MAP system from the REST-API interface. It has the same functionalities like the RPS for MAP. This URL is designed to be used from a system, that controls remotely the user of several MAP systems. <br>
To use the functions, every POST request needs a valid userModelSyncID.
The initial userModelSyncID can be get from the commands GET /syncstatus or GET /usermodellist.
After a successful operation, you get a new valid userModelSyncID back. It is recommended to use this ID, if you want to create, modify or delete several users.

### Create User

To create a new user on a MAP system, the client must ensure that the key value *id* is not already used on the system. Further a valid userModelSyncID is required.
The following examples shows how a user can be created:
  - createUserWithMinimalParameters
  - createUserWithSmartkeyProfile
  - createUserFullConfig

### Modify User

To modify an existing user on a MAP system, the client needs also a valid userModelSyncID.
When modifying, all user parameters must be specified completely in the requested body schema.
The example *modifyUser* shows how to modify a user.

### Delete User

To delete an existing user on a MAP system, the client needs also a valid userModelSyncID.
The example *deleteUser* shows how to delete a user.

### Smartkey Profile

Smartkey Profile is an optional attribute set with up to 3 attributes: Name, Access Type, Token.  Name and Access Type must be specified together. 'Token Only' and 'Token And PINpad' Access Types require Token.

### User Secrets Encryption

User attributes: passcode, oiiPassword, smartkeyToken are considered as user secrets.

User secrets are encrypted in GET output if shared key is available. Missing shared key will lead to plaintext output in GET.

User secrets encryption significantly affects performance of GET LIST, making it around 25% slower. POST and GET are slowed by a very small margin.

Shared Key change will trigger encryption on the first GET operation, making it slower by around a second for very large amount of secrets (~3000 secrets). For smaller databases encryption it will be proportionally faster.

In POST encryptedSecrets boolean attribute enables encrypted secret fields in POST payload. Encrypted data is mainly used for MAP panel synchronization, it is not intended for a consumer to encrypt secrets themselves.

If encryptedSecrets=true all secrets must be provided encrypted. If only one secret need to be modified in plain text, it is valid to omit the other secrets in the request.

In GET encryptedSecrets will be true in case user secrets are encrypted.

To have a successful decryption: Shared Key must be the same between device that encrypts and device that decrypts. Encrypted data cannot be shared between different userIDs, which means a valid encrypted secret for user 005 won't be accepted for any other userID.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.user_model_post import UserModelPost
from bosch-alarm-map.models.user_model_sync_id import UserModelSyncID
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
    api_instance = bosch-alarm-map.UsermodelApi(api_client)
    user_model_post = {"@cmd":"CREATE","id":"008","userType":"User:Standard","firstName":"Jan","lastName":"Jansen","passcode":"888888","accessModel":"Basic Profile","userModelSyncID":156} # UserModelPost |  (optional)

    try:
        # Create, modify or delete a user on the MAP system
        api_response = api_instance.post_usermodel(user_model_post=user_model_post)
        print("The response of UsermodelApi->post_usermodel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsermodelApi->post_usermodel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_model_post** | [**UserModelPost**](UserModelPost.md)|  | [optional] 

### Return type

[**UserModelSyncID**](UserModelSyncID.md)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. The request succeeded, and resource was either created, modified or deleted. |  -  |
**400** | Bad request. The request could not be understood by the server due to incorrect syntax in the requested body. The client SHOULD NOT repeat the request without modifications.  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Required license not found. Server response indicates missing license type.  |  -  |
**404** | Not found. The request URL with the specified parameter was not found.  |  -  |
**409** | The request could not be completed due to a conflict with the current state of the resource. The client SHOULD NOT repeat the request without modifications. |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

