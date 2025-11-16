# Error409


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The error code 409 is returned by the server if a sent vaule will create a conflict with the current state of the resources. Set of possible error states: &lt;br&gt; * SyncError - This error code represents the conflict, if a syncid value conflicts with the current state of the resources. * DependencyConflict - This errorcode represents the Conflict, if a deletion on a model is requested, which is used by another model. Can occur during deletion or deactivation of users or models. This error code is also shown, if the last User with REST-API authorization should be deleted or deactivated. * AlreadyExists -  This errorcode represents the Conflict, that a USERID or the Model_ID already exits on the Panel database. Can occur during creation or modification of Users or Models.  | 
**target** | **str** | The key-value/name, which is responsible for the error. | [optional] 
**message** | **str** | Universal JSON object/ value,  which causes the error. Output starts all time with: \&quot;Conflict caused by: &lt;value&gt;\&quot;  | [optional] 

## Example

```python
from openapi_client.models.error409 import Error409

# TODO update the JSON string below
json = "{}"
# create an instance of Error409 from a JSON string
error409_instance = Error409.from_json(json)
# print the JSON string representation of the object
print(Error409.to_json())

# convert the object into a dict
error409_dict = error409_instance.to_dict()
# create an instance of Error409 from a dict
error409_from_dict = Error409.from_dict(error409_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


