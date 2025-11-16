# UserID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique numeric user identification (user ID). | 

## Example

```python
from bosch_alarm_map.models.user_id import UserID

# TODO update the JSON string below
json = "{}"
# create an instance of UserID from a JSON string
user_id_instance = UserID.from_json(json)
# print the JSON string representation of the object
print(UserID.to_json())

# convert the object into a dict
user_id_dict = user_id_instance.to_dict()
# create an instance of UserID from a dict
user_id_from_dict = UserID.from_dict(user_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


