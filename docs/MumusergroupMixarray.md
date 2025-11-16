# MumusergroupMixarray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mumusergroup_sync_id** | **int** | Synchronization ID for MUM user group. Will be changed for each change in the MUM user group. | 
**user_ids** | [**List[MumusergroupMixarrayAllOfUserIds]**](MumusergroupMixarrayAllOfUserIds.md) |  | [optional] 

## Example

```python
from openapi_client.models.mumusergroup_mixarray import MumusergroupMixarray

# TODO update the JSON string below
json = "{}"
# create an instance of MumusergroupMixarray from a JSON string
mumusergroup_mixarray_instance = MumusergroupMixarray.from_json(json)
# print the JSON string representation of the object
print(MumusergroupMixarray.to_json())

# convert the object into a dict
mumusergroup_mixarray_dict = mumusergroup_mixarray_instance.to_dict()
# create an instance of MumusergroupMixarray from a dict
mumusergroup_mixarray_from_dict = MumusergroupMixarray.from_dict(mumusergroup_mixarray_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


