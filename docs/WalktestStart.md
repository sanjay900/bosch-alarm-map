# WalktestStart

This command is used to start the walktest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 
**included_points** | **str** | Specifies which points should be put into test mode. | [optional] 

## Example

```python
from openapi_client.models.walktest_start import WalktestStart

# TODO update the JSON string below
json = "{}"
# create an instance of WalktestStart from a JSON string
walktest_start_instance = WalktestStart.from_json(json)
# print the JSON string representation of the object
print(WalktestStart.to_json())

# convert the object into a dict
walktest_start_dict = walktest_start_instance.to_dict()
# create an instance of WalktestStart from a dict
walktest_start_from_dict = WalktestStart.from_dict(walktest_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


