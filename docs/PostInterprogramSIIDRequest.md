# PostInterprogramSIIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | This command provides information about the reasons why the internal program cannot be activated. It provides the list of related device urls that prevent the internal program from being activated. | [optional] 

## Example

```python
from openapi_client.models.post_interprogram_siid_request import PostInterprogramSIIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostInterprogramSIIDRequest from a JSON string
post_interprogram_siid_request_instance = PostInterprogramSIIDRequest.from_json(json)
# print the JSON string representation of the object
print(PostInterprogramSIIDRequest.to_json())

# convert the object into a dict
post_interprogram_siid_request_dict = post_interprogram_siid_request_instance.to_dict()
# create an instance of PostInterprogramSIIDRequest from a dict
post_interprogram_siid_request_from_dict = PostInterprogramSIIDRequest.from_dict(post_interprogram_siid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


