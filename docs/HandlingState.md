# HandlingState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | (MAP system currently supports only NONE and HANDLED) | [optional] 
**user** | **str** | The MAP system user that handled the incident | [optional] 
**interface** | **str** | The interface that was used to handle the incident (i.e. REST-API or Keypad) | [optional] 

## Example

```python
from bosch_alarm_map.models.handling_state import HandlingState

# TODO update the JSON string below
json = "{}"
# create an instance of HandlingState from a JSON string
handling_state_instance = HandlingState.from_json(json)
# print the JSON string representation of the object
print(HandlingState.to_json())

# convert the object into a dict
handling_state_dict = handling_state_instance.to_dict()
# create an instance of HandlingState from a dict
handling_state_from_dict = HandlingState.from_dict(handling_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


