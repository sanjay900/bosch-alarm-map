# bosch_alarm_map.NtpApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ntp**](NtpApi.md#get_ntp) | **GET** /ntp | Get NTP state
[**post_ntp**](NtpApi.md#post_ntp) | **POST** /ntp | Configure NTP


# **get_ntp**
> NtpGet get_ntp()

Get NTP state

The Network Time Protocol (NTP) resource provides insight into current NTP state.

Configured NTP synchronization is done upon a panel reboot and repeated once per 7 days.


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.ntp_get import NtpGet
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
    api_instance = bosch_alarm_map.NtpApi(api_client)

    try:
        # Get NTP state
        api_response = api_instance.get_ntp()
        print("The response of NtpApi->get_ntp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NtpApi->get_ntp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NtpGet**](NtpGet.md)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success  |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**500** | Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ntp**
> post_ntp(ntp_post)

Configure NTP

Network Time Protocol (NTP) can be configured to use both or either fixed publicly available NTP servers and custom NTP servers. Custom NTP servers take priority if both are enabled.


### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.ntp_post import NtpPost
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
    api_instance = bosch_alarm_map.NtpApi(api_client)
    ntp_post = bosch_alarm_map.NtpPost() # NtpPost | 

    try:
        # Configure NTP
        api_instance.post_ntp(ntp_post)
    except Exception as e:
        print("Exception when calling NtpApi->post_ntp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ntp_post** | [**NtpPost**](NtpPost.md)|  | 

### Return type

void (empty response body)

### Authorization

[digest](../README.md#digest)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized &lt;br&gt; This response code indicates that the client does not have the appropriate access rights to execute the requested action on the server. It indicates that an authorization needs to be done for the request.  |  -  |
**500** | Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

