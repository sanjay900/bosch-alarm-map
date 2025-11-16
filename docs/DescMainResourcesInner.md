# DescMainResourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**ref** | **str** | Link for the main resources. The links are relative links. The absolute link can be created by prepending the baseURL to the given relative link of the resource. | [optional] 

## Example

```python
from bosch-alarm-map.models.desc_main_resources_inner import DescMainResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DescMainResourcesInner from a JSON string
desc_main_resources_inner_instance = DescMainResourcesInner.from_json(json)
# print the JSON string representation of the object
print(DescMainResourcesInner.to_json())

# convert the object into a dict
desc_main_resources_inner_dict = desc_main_resources_inner_instance.to_dict()
# create an instance of DescMainResourcesInner from a dict
desc_main_resources_inner_from_dict = DescMainResourcesInner.from_dict(desc_main_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


