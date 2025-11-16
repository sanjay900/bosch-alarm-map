# SpecialDayModellistPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 
**special_day_model_sync_id** | **int** | Synchronization ID for the special day database table. Will be changed for each change in the special day database table. | 

## Example

```python
from openapi_client.models.special_day_modellist_post import SpecialDayModellistPost

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialDayModellistPost from a JSON string
special_day_modellist_post_instance = SpecialDayModellistPost.from_json(json)
# print the JSON string representation of the object
print(SpecialDayModellistPost.to_json())

# convert the object into a dict
special_day_modellist_post_dict = special_day_modellist_post_instance.to_dict()
# create an instance of SpecialDayModellistPost from a dict
special_day_modellist_post_from_dict = SpecialDayModellistPost.from_dict(special_day_modellist_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


