# SmartkeyModelID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smartkey_model_id** | **str** | Unique name of a Smartkey Model. The name is used to identify the item on the MAP system. The following charaters are forbidden by the choose of the identifier name: \&quot; @ ; | 

## Example

```python
from openapi_client.models.smartkey_model_id import SmartkeyModelID

# TODO update the JSON string below
json = "{}"
# create an instance of SmartkeyModelID from a JSON string
smartkey_model_id_instance = SmartkeyModelID.from_json(json)
# print the JSON string representation of the object
print(SmartkeyModelID.to_json())

# convert the object into a dict
smartkey_model_id_dict = smartkey_model_id_instance.to_dict()
# create an instance of SmartkeyModelID from a dict
smartkey_model_id_from_dict = SmartkeyModelID.from_dict(smartkey_model_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


