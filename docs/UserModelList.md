# UserModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_model_sync_id** | **int** | Synchronization ID for the user database table. Will be changed for each change in the user database table. | 
**list** | [**List[UserModelListAllOfListInner]**](UserModelListAllOfListInner.md) | List of users | [optional] 

## Example

```python
from openapi_client.models.user_model_list import UserModelList

# TODO update the JSON string below
json = "{}"
# create an instance of UserModelList from a JSON string
user_model_list_instance = UserModelList.from_json(json)
# print the JSON string representation of the object
print(UserModelList.to_json())

# convert the object into a dict
user_model_list_dict = user_model_list_instance.to_dict()
# create an instance of UserModelList from a dict
user_model_list_from_dict = UserModelList.from_dict(user_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


