# bosch_alarm_map.PsCanOpSIIDApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ps_can_op_siid**](PsCanOpSIIDApi.md#get_ps_can_op_siid) | **GET** /{psCanOp_SIID} | Power supply CAN-Bus


# **get_ps_can_op_siid**
> PsCanOp get_ps_can_op_siid(ps_can_op_siid)

Power supply CAN-Bus

Get informations of a specific Can power supply output resource

### Example


```python
import bosch_alarm_map
from bosch_alarm_map.models.ps_can_op import PsCanOp
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
    api_instance = bosch_alarm_map.PsCanOpSIIDApi(api_client)
    ps_can_op_siid = '/1.1.PowerSupply.13001.6' # str | Unique psCanOp SIID. You can get all psCanOps IDs with the command GET /psCanOpList

    try:
        # Power supply CAN-Bus
        api_response = api_instance.get_ps_can_op_siid(ps_can_op_siid)
        print("The response of PsCanOpSIIDApi->get_ps_can_op_siid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PsCanOpSIIDApi->get_ps_can_op_siid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ps_can_op_siid** | **str**| Unique psCanOp SIID. You can get all psCanOps IDs with the command GET /psCanOpList | 

### Return type

[**PsCanOp**](PsCanOp.md)

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

