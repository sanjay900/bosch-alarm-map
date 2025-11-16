# WalktestStop

This command is used to stop the walktest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 

## Example

```python
from bosch_alarm_map.models.walktest_stop import WalktestStop

# TODO update the JSON string below
json = "{}"
# create an instance of WalktestStop from a JSON string
walktest_stop_instance = WalktestStop.from_json(json)
# print the JSON string representation of the object
print(WalktestStop.to_json())

# convert the object into a dict
walktest_stop_dict = walktest_stop_instance.to_dict()
# create an instance of WalktestStop from a dict
walktest_stop_from_dict = WalktestStop.from_dict(walktest_stop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


