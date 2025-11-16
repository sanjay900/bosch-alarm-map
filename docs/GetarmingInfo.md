# GetarmingInfo

This command is used to to get ARMING infos

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.getarming_info import GetarmingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetarmingInfo from a JSON string
getarming_info_instance = GetarmingInfo.from_json(json)
# print the JSON string representation of the object
print(GetarmingInfo.to_json())

# convert the object into a dict
getarming_info_dict = getarming_info_instance.to_dict()
# create an instance of GetarmingInfo from a dict
getarming_info_from_dict = GetarmingInfo.from_dict(getarming_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


