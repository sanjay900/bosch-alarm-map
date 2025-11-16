# PostSmartkeymodelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | 
**smartkey_model_id** | **str** | Unique name of a Smartkey Model. The name is used to identify the item on the MAP system. The following charaters are forbidden by the choose of the identifier name: \&quot; @ ; | 
**area_scope_list** | **List[str]** | List of areas in the scope of the Smartkey profile | [optional] 
**arm_authority** | **str** | Arm Authority of a Smartkey user during the configured time model | [optional] 
**disarm_authority** | **str** | Disarm authority of a Smartkey user during the configured time model | [optional] 
**time_model_used_for_disarming** | **str** | Related time model for disarming. Set no time model if the Smartkey model is not restricted by a time model. | [optional] 
**smartkey_model_sync_id** | **int** | Synchronization ID for the smart key database table. Will be changed for each change in the smart key database table. | 

## Example

```python
from bosch_alarm_map.models.post_smartkeymodel_request import PostSmartkeymodelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSmartkeymodelRequest from a JSON string
post_smartkeymodel_request_instance = PostSmartkeymodelRequest.from_json(json)
# print the JSON string representation of the object
print(PostSmartkeymodelRequest.to_json())

# convert the object into a dict
post_smartkeymodel_request_dict = post_smartkeymodel_request_instance.to_dict()
# create an instance of PostSmartkeymodelRequest from a dict
post_smartkeymodel_request_from_dict = PostSmartkeymodelRequest.from_dict(post_smartkeymodel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


