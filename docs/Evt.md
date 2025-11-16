# Evt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**armed** | **bool** |  | [optional] 

## Example

```python
from bosch-alarm-map.models.evt import Evt

# TODO update the JSON string below
json = "{}"
# create an instance of Evt from a JSON string
evt_instance = Evt.from_json(json)
# print the JSON string representation of the object
print(Evt.to_json())

# convert the object into a dict
evt_dict = evt_instance.to_dict()
# create an instance of Evt from a dict
evt_from_dict = Evt.from_dict(evt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


