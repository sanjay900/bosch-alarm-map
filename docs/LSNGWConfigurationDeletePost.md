# LSNGWConfigurationDeletePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | POST request command. | 
**siid** | **str** | LSN GW device SIID. | 

## Example

```python
from openapi_client.models.lsngw_configuration_delete_post import LSNGWConfigurationDeletePost

# TODO update the JSON string below
json = "{}"
# create an instance of LSNGWConfigurationDeletePost from a JSON string
lsngw_configuration_delete_post_instance = LSNGWConfigurationDeletePost.from_json(json)
# print the JSON string representation of the object
print(LSNGWConfigurationDeletePost.to_json())

# convert the object into a dict
lsngw_configuration_delete_post_dict = lsngw_configuration_delete_post_instance.to_dict()
# create an instance of LSNGWConfigurationDeletePost from a dict
lsngw_configuration_delete_post_from_dict = LSNGWConfigurationDeletePost.from_dict(lsngw_configuration_delete_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


