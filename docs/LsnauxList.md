# LsnauxList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Lsnaux]**](Lsnaux.md) | List of all lsnauxs | [optional] 

## Example

```python
from openapi_client.models.lsnaux_list import LsnauxList

# TODO update the JSON string below
json = "{}"
# create an instance of LsnauxList from a JSON string
lsnaux_list_instance = LsnauxList.from_json(json)
# print the JSON string representation of the object
print(LsnauxList.to_json())

# convert the object into a dict
lsnaux_list_dict = lsnaux_list_instance.to_dict()
# create an instance of LsnauxList from a dict
lsnaux_list_from_dict = LsnauxList.from_dict(lsnaux_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


