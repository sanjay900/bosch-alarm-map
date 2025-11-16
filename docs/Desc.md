# Desc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**base_url** | **str** | Absolute URL to the REST-API server described by this resource | [optional] 
**udn** | **str** | Product ID of the MAP panel | [optional] 
**friendly_name** | **str** | Short description for the end user, e.g. “Intrusion Panel Room 127” | [optional] 
**firmware_version** | **str** | The firmware version running on the MAP panel in format \&quot;Major\&quot;.\&quot;Minor\&quot;.\&quot;Micro\&quot; | [optional] 
**model_name** | **str** | Identification of the MAP5000 panel; e.g. MAP5000, MAP5000-S, MAP5000-COM, MAP5000-SC | [optional] 
**profiles** | **List[str]** | It contains one or more device profile Identifiers (e.g. “MAP5000.1.0”, “MAP5000.2.2”). | [optional] 
**main_resources** | [**List[DescMainResourcesInner]**](DescMainResourcesInner.md) | A list of types and links for all main resources. | [optional] 

## Example

```python
from bosch_alarm_map.models.desc import Desc

# TODO update the JSON string below
json = "{}"
# create an instance of Desc from a JSON string
desc_instance = Desc.from_json(json)
# print the JSON string representation of the object
print(Desc.to_json())

# convert the object into a dict
desc_dict = desc_instance.to_dict()
# create an instance of Desc from a dict
desc_from_dict = Desc.from_dict(desc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


