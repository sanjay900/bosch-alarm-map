# GetSmartkeymodel200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smartkey_model_id** | **str** | Unique name of a Smartkey Model. The name is used to identify the item on the MAP system. The following charaters are forbidden by the choose of the identifier name: \&quot; @ ; | 
**area_scope_list** | **List[str]** | List of areas in the scope of the Smartkey profile | [optional] 
**arm_authority** | **str** | Arm Authority of a Smartkey user during the configured time model | [optional] 
**disarm_authority** | **str** | Disarm authority of a Smartkey user during the configured time model | [optional] 
**time_model_used_for_disarming** | **str** | Related time model for disarming. Set no time model if the Smartkey model is not restricted by a time model. | [optional] 
**smartkey_model_sync_id** | **int** | Synchronization ID for the smart key database table. Will be changed for each change in the smart key database table. | 

## Example

```python
from openapi_client.models.get_smartkeymodel200_response import GetSmartkeymodel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSmartkeymodel200Response from a JSON string
get_smartkeymodel200_response_instance = GetSmartkeymodel200Response.from_json(json)
# print the JSON string representation of the object
print(GetSmartkeymodel200Response.to_json())

# convert the object into a dict
get_smartkeymodel200_response_dict = get_smartkeymodel200_response_instance.to_dict()
# create an instance of GetSmartkeymodel200Response from a dict
get_smartkeymodel200_response_from_dict = GetSmartkeymodel200Response.from_dict(get_smartkeymodel200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


