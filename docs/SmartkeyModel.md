# SmartkeyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_scope_list** | **List[str]** | List of areas in the scope of the Smartkey profile | [optional] 
**arm_authority** | **str** | Arm Authority of a Smartkey user during the configured time model | [optional] 
**disarm_authority** | **str** | Disarm authority of a Smartkey user during the configured time model | [optional] 
**time_model_used_for_disarming** | **str** | Related time model for disarming. Set no time model if the Smartkey model is not restricted by a time model. | [optional] 

## Example

```python
from openapi_client.models.smartkey_model import SmartkeyModel

# TODO update the JSON string below
json = "{}"
# create an instance of SmartkeyModel from a JSON string
smartkey_model_instance = SmartkeyModel.from_json(json)
# print the JSON string representation of the object
print(SmartkeyModel.to_json())

# convert the object into a dict
smartkey_model_dict = smartkey_model_instance.to_dict()
# create an instance of SmartkeyModel from a dict
smartkey_model_from_dict = SmartkeyModel.from_dict(smartkey_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


