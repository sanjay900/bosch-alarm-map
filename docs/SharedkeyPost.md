# SharedkeyPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | 
**checksum** | **str** | Shared Key checksum | [optional] 
**encrypted** | **str** | Encrypted Shared Key data | [optional] 
**timestamp** | **str** | Shared Key timestamp | [optional] 

## Example

```python
from bosch-alarm-map.models.sharedkey_post import SharedkeyPost

# TODO update the JSON string below
json = "{}"
# create an instance of SharedkeyPost from a JSON string
sharedkey_post_instance = SharedkeyPost.from_json(json)
# print the JSON string representation of the object
print(SharedkeyPost.to_json())

# convert the object into a dict
sharedkey_post_dict = sharedkey_post_instance.to_dict()
# create an instance of SharedkeyPost from a dict
sharedkey_post_from_dict = SharedkeyPost.from_dict(sharedkey_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


