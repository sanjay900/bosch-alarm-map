# bosch-alarm-map.SyncstatusApi

All URIs are relative to *https://169.254.10.10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_syncstatus**](SyncstatusApi.md#get_syncstatus) | **GET** /syncstatus | Get all synchronization IDs


# **get_syncstatus**
> SynchronizationIDs get_syncstatus()

Get all synchronization IDs

Synchronization IDs are implemented to track changes in the MAP system database.
Any change to corresponding model will increase its synchronization ID value by 1. System reboot will increase all synchronization IDs.
Initial value of synchronization IDs is 0. Synchronization values are not directly modifiable and are managed internally.

### Uptime & Restart counter

Uptime and restart counter help to properly manage Synchronization IDs.

### Most frequent cases of /syncstatus usage detailed:

- SyncIDs did not change
- Uptime has increased
- Restart counter did not change
- No changes were made to the MAP system. Synchronization is not required.

### —

- SyncIDs have changed
- Uptime has increased
- Restart counter did not change
- Changes were made to the MAP system, either partial GETMODIFIEDLIST or full synchronization is possible.

### —

- Restart counter has changed or uptime has decreased
- System was rebooted, full synchronization is required. GETMODIFIEDLIST output will be incomplete.


### —

The IDs are only reset if the MAP database is deleted or overwritten. Possible cases are:

### MAP software update

A system update is supplied with a default database. Synchronization IDs are always reset during a MAP panel firmware installation. MAP panel firmware can only be updated using RPS for MAP.

Recommended workflow is:

Backup MAP panel configuration using RPS for MAP. Update MAP panel firmware. Restore configuration from backup. Note: synchronization IDs are not part of a backup.

### Failsafe mode

In the case of a critical system error, the system goes into the failsafe mode. This usually results in an alarm being sent directly to a higher-level reporting station, like a security office, a fire department or the police.
Furthermore the MAP panel database is then replaced. To switch back from the failsafe mode to the normal operation state, a new installation of the current MAP panel firmware is required. This will install the default MAP database.


### Example


```python
import bosch-alarm-map
from bosch-alarm-map.models.synchronization_ids import SynchronizationIDs
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
    api_instance = bosch-alarm-map.SyncstatusApi(api_client)

    try:
        # Get all synchronization IDs
        api_response = api_instance.get_syncstatus()
        print("The response of SyncstatusApi->get_syncstatus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncstatusApi->get_syncstatus: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SynchronizationIDs**](SynchronizationIDs.md)

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

