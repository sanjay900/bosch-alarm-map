# AccessModelID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_model_id** | **str** | Unique name of an Access Model. The name is used to identify the item on the MAP System. The following characters are forbidden by the choose of the identifier name: \&quot; @ ; | 

## Example

```python
from bosch_alarm_map.models.access_model_id import AccessModelID

# TODO update the JSON string below
json = "{}"
# create an instance of AccessModelID from a JSON string
access_model_id_instance = AccessModelID.from_json(json)
# print the JSON string representation of the object
print(AccessModelID.to_json())

# convert the object into a dict
access_model_id_dict = access_model_id_instance.to_dict()
# create an instance of AccessModelID from a dict
access_model_id_from_dict = AccessModelID.from_dict(access_model_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


