# bosch_alarm_map.UserApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_id**](UserApi.md#get_user_id) | **GET** /user/{userID} | Specific user configuration
[**post_user_id**](UserApi.md#post_user_id) | **POST** /user/{userID} | Activate or Deactivate a specific user on system


# **get_user_id**
> User get_user_id(user_id)

Specific user configuration

This resource handles a MAP panel user. It provides information about its ID, activation / deactivation status and other parameters. It includes NOT the personal user attributes like passcode.

### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.user import User
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
    api_instance = bosch_alarm_map.UserApi(api_client)
    user_id = '/004' # str | Unique user ID of each MAP panel user. User ID range is 004 - 999.

    try:
        # Specific user configuration
        api_response = api_instance.get_user_id(user_id)
        print("The response of UserApi->get_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Unique user ID of each MAP panel user. User ID range is 004 - 999. | 

### Return type

[**User**](User.md)

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
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_id**
> post_user_id(user_id, user_activate)

Activate or Deactivate a specific user on system

This resource is used to activation or deactivation a MAP system user. With the URL it is not possible to modify or set all parameters of a user. To be able to modify all user parameters, the URL POST / usermodel must be used.

### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.user_activate import UserActivate
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
    api_instance = bosch_alarm_map.UserApi(api_client)
    user_id = '/004' # str | Unique user ID of each MAP system user. User ID range is 004 - 999.
    user_activate = {"@cmd":"ACTIVATE"} # UserActivate | 

    try:
        # Activate or Deactivate a specific user on system
        api_instance.post_user_id(user_id, user_activate)
    except Exception as e:
        print("Exception when calling UserApi->post_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Unique user ID of each MAP system user. User ID range is 004 - 999. | 
 **user_activate** | [**UserActivate**](UserActivate.md)|  | 

### Return type

void (empty response body)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation, but device is already set to DHCP |  -  |
**204** | Successful operation |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**403** | Forbidden &lt;br&gt; A valid request was sent, but the user is not allowed to conduct the requested operation.  |  -  |
**414** | Response code is used if the URI exceeds the maximum supported size (255 bytes). In the context of the REST-API are intended to be kept short, but a client may increase the size of a URI by adding query parameters. String matching can be used to reduce the query length.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

