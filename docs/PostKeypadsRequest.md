# PostKeypadsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | This operation initiates activating/deactivating the device | [optional] 

## Example

```python
from bosch-alarm-map.models.post_keypads_request import PostKeypadsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostKeypadsRequest from a JSON string
post_keypads_request_instance = PostKeypadsRequest.from_json(json)
# print the JSON string representation of the object
print(PostKeypadsRequest.to_json())

# convert the object into a dict
post_keypads_request_dict = post_keypads_request_instance.to_dict()
# create an instance of PostKeypadsRequest from a dict
post_keypads_request_from_dict = PostKeypadsRequest.from_dict(post_keypads_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


