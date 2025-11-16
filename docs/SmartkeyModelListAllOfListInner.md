# SmartkeyModelListAllOfListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smartkey_model_id** | **str** | Unique name of a Smartkey Model. The name is used to identify the item on the MAP system. The following charaters are forbidden by the choose of the identifier name: \&quot; @ ; | 
**area_scope_list** | **List[str]** | List of areas in the scope of the Smartkey profile | [optional] 
**arm_authority** | **str** | Arm Authority of a Smartkey user during the configured time model | [optional] 
**disarm_authority** | **str** | Disarm authority of a Smartkey user during the configured time model | [optional] 
**time_model_used_for_disarming** | **str** | Related time model for disarming. Set no time model if the Smartkey model is not restricted by a time model. | [optional] 

## Example

```python
from openapi_client.models.smartkey_model_list_all_of_list_inner import SmartkeyModelListAllOfListInner

# TODO update the JSON string below
json = "{}"
# create an instance of SmartkeyModelListAllOfListInner from a JSON string
smartkey_model_list_all_of_list_inner_instance = SmartkeyModelListAllOfListInner.from_json(json)
# print the JSON string representation of the object
print(SmartkeyModelListAllOfListInner.to_json())

# convert the object into a dict
smartkey_model_list_all_of_list_inner_dict = smartkey_model_list_all_of_list_inner_instance.to_dict()
# create an instance of SmartkeyModelListAllOfListInner from a dict
smartkey_model_list_all_of_list_inner_from_dict = SmartkeyModelListAllOfListInner.from_dict(smartkey_model_list_all_of_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


