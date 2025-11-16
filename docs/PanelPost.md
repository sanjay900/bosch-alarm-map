# PanelPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | This operation initiates restarting the panel or to get the panel support files. The functions with the support files is still a developer function. No guarantee that these develers all logs | [optional] 
**persist_data** | **bool** | Indicates whether to persist persistent data or not, by default persistent data is purged | [optional] [default to False]

## Example

```python
from openapi_client.models.panel_post import PanelPost

# TODO update the JSON string below
json = "{}"
# create an instance of PanelPost from a JSON string
panel_post_instance = PanelPost.from_json(json)
# print the JSON string representation of the object
print(PanelPost.to_json())

# convert the object into a dict
panel_post_dict = panel_post_instance.to_dict()
# create an instance of PanelPost from a dict
panel_post_from_dict = PanelPost.from_dict(panel_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


