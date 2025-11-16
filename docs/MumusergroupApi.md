# bosch-alarm-map.MumusergroupApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getmumusergroup**](MumusergroupApi.md#getmumusergroup) | **GET** /mumusergroup | Get MUM property for all User IDs
[**postmumusergroup**](MumusergroupApi.md#postmumusergroup) | **POST** /mumusergroup | Set MUM property to a set of User IDs 


# **getmumusergroup**
> MumusergroupMixarray getmumusergroup()

Get MUM property for all User IDs

The response body of this URL returns all User IDs, that are controlled by the MUM application. All User IDs will returned in a mixed array. An ID range is shown as tuple. A single controlled ID is shown as integer.

### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.mumusergroup_mixarray import MumusergroupMixarray
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
    api_instance = bosch-alarm-map.MumusergroupApi(api_client)

    try:
        # Get MUM property for all User IDs
        api_response = api_instance.getmumusergroup()
        print("The response of MumusergroupApi->getmumusergroup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MumusergroupApi->getmumusergroup: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MumusergroupMixarray**](MumusergroupMixarray.md)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of User IDs with MUM property |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**404** | Not found. The request URL with the specified parameter was not found.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postmumusergroup**
> postmumusergroup(mumusergroup_mixarray=mumusergroup_mixarray)

Set MUM property to a set of User IDs 

From this URL it is possible to reserve a set of UserIDs on a MAP system. The reserved IDs are managed and controlled by a user management system like the
MUM application. If the mumusergroup flag is set to a User ID, the IDs defined in the mumusergroup are not anymore controllable and shown on the MAP Keypads, which are connected to the MAP system.<br>

### Define user group

To assign users to the group, either individual IDs or ID ranges can be defined. The examples under the content type *setsingleIds* shows examples, how a set single user IDs into the
MUM user group. The following examples show, how to create a mum group with a single userid or with 3 userids:
  - setsingleUserID
  - setsingleUserIDs

To remove the group, send an empty array. See example:
  - deletegroup

The examples under the content type *setmixedgroup* demonstrate, how to create a group via a userID range. The example:
  - setfullrange

demonstrates the way how to create a group, where all users on a MAP system are managed by the MUM application.

In the example:
  - setmixUserIdgroup

only the users with IDs { 4, 5, 70,71,72,...,89,90, 100, 200,201, ...,299,300 } are managed by the user application.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.mumusergroup_mixarray import MumusergroupMixarray
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
    api_instance = bosch-alarm-map.MumusergroupApi(api_client)
    mumusergroup_mixarray = {"userIds":[5],"mumusergroupSyncID":52} # MumusergroupMixarray |  (optional)

    try:
        # Set MUM property to a set of User IDs 
        api_instance.postmumusergroup(mumusergroup_mixarray=mumusergroup_mixarray)
    except Exception as e:
        print("Exception when calling MumusergroupApi->postmumusergroup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mumusergroup_mixarray** | [**MumusergroupMixarray**](MumusergroupMixarray.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[clientCert](../README.md#clientCert)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. The request succeeded, and resource was either created, modified or deleted.  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**404** | Not found. The request URL with the specified parameter was not found.  |  -  |
**500** | Internal Server Error  |  -  |
**503** | Service Unavailable &lt;br&gt; This response code indicates that the server is in a temporary overload condition and thus unable to serve the request. The client can retry the request at a later point in time.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

