# FireDetectorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[FireDetector]**](FireDetector.md) | List of all fireDetectors | [optional] 

## Example

```python
from openapi_client.models.fire_detector_list import FireDetectorList

# TODO update the JSON string below
json = "{}"
# create an instance of FireDetectorList from a JSON string
fire_detector_list_instance = FireDetectorList.from_json(json)
# print the JSON string representation of the object
print(FireDetectorList.to_json())

# convert the object into a dict
fire_detector_list_dict = fire_detector_list_instance.to_dict()
# create an instance of FireDetectorList from a dict
fire_detector_list_from_dict = FireDetectorList.from_dict(fire_detector_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


