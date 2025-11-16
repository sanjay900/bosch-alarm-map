# TimeModelID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_model_id** | **str** | Unique Name of the Time model. The name is used to identify the item on the MAP System. The following characters are forbidden in identifier name: \&quot; @ ;  | 

## Example

```python
from bosch-alarm-map.models.time_model_id import TimeModelID

# TODO update the JSON string below
json = "{}"
# create an instance of TimeModelID from a JSON string
time_model_id_instance = TimeModelID.from_json(json)
# print the JSON string representation of the object
print(TimeModelID.to_json())

# convert the object into a dict
time_model_id_dict = time_model_id_instance.to_dict()
# create an instance of TimeModelID from a dict
time_model_id_from_dict = TimeModelID.from_dict(time_model_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


