# CreatedSub


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_url** | **str** | A URL to the location of the newly created subscription. | [optional] 
**lease_time** | **int** | Actual lease time | [optional] 
**buffer_size** | **int** | Actual, allocated buffer size | [optional] 

## Example

```python
from openapi_client.models.created_sub import CreatedSub

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedSub from a JSON string
created_sub_instance = CreatedSub.from_json(json)
# print the JSON string representation of the object
print(CreatedSub.to_json())

# convert the object into a dict
created_sub_dict = created_sub_instance.to_dict()
# create an instance of CreatedSub from a dict
created_sub_from_dict = CreatedSub.from_dict(created_sub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


