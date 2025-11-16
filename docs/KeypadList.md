# KeypadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Keypad]**](Keypad.md) | List of all keypads | [optional] 

## Example

```python
from bosch-alarm-map.models.keypad_list import KeypadList

# TODO update the JSON string below
json = "{}"
# create an instance of KeypadList from a JSON string
keypad_list_instance = KeypadList.from_json(json)
# print the JSON string representation of the object
print(KeypadList.to_json())

# convert the object into a dict
keypad_list_dict = keypad_list_instance.to_dict()
# create an instance of KeypadList from a dict
keypad_list_from_dict = KeypadList.from_dict(keypad_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


