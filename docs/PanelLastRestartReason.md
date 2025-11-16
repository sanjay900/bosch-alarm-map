# PanelLastRestartReason

Panel restart reason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Restart reason code | [optional] 
**description** | **str** | Restart reason description | [optional] 
**time** | **str** | Restart reason timestamp | [optional] 

## Example

```python
from openapi_client.models.panel_last_restart_reason import PanelLastRestartReason

# TODO update the JSON string below
json = "{}"
# create an instance of PanelLastRestartReason from a JSON string
panel_last_restart_reason_instance = PanelLastRestartReason.from_json(json)
# print the JSON string representation of the object
print(PanelLastRestartReason.to_json())

# convert the object into a dict
panel_last_restart_reason_dict = panel_last_restart_reason_instance.to_dict()
# create an instance of PanelLastRestartReason from a dict
panel_last_restart_reason_from_dict = PanelLastRestartReason.from_dict(panel_last_restart_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


