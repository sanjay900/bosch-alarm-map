# AccessModelistPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 
**access_model_sync_id** | **int** | Synchronization ID for the access table. Will be changed for each change in the access database table. | 

## Example

```python
from openapi_client.models.access_modelist_post import AccessModelistPost

# TODO update the JSON string below
json = "{}"
# create an instance of AccessModelistPost from a JSON string
access_modelist_post_instance = AccessModelistPost.from_json(json)
# print the JSON string representation of the object
print(AccessModelistPost.to_json())

# convert the object into a dict
access_modelist_post_dict = access_modelist_post_instance.to_dict()
# create an instance of AccessModelistPost from a dict
access_modelist_post_from_dict = AccessModelistPost.from_dict(access_modelist_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


