# Panel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**failsafe** | **bool** | Indicates if the MAP panel is in failsafe | [optional] 
**installer_mode** | **bool** | True if MAP panel is in installer mode | [optional] 
**cfg_status** | **str** | &#39;The configuration status of the panel: - *default*:    MAP panel is running default configuration - *latest*:     MAP panel is running the latest configuration sent to it - *last-good*:  MAP panel is running the last good configuration  | [optional] 
**last_cfg_updt** | **str** | Date and time of the last configuration update on the MAP panel | [optional] 
**last_user_db_updt** | **str** | Date and time of the last user database update on the panel from RPS (remote configuration tool) | [optional] 
**is_panel_loaded** | **bool** | Indicates the MAP panel is in a temporary busy state (resulting in possible delays for responses over REST-API. No data loss is expected.) | [optional] 
**restart_imminent** | **bool** | Indicates that the MAP panel is overloaded, due to which the MAP panel will restart. | [optional] 
**firmware_version** | **str** | Installed firmware version | [optional] 
**model_name** | **str** | MAP model name | [optional] 
**udn** | **str** | Unique Device Name | [optional] 
**last_restart_reason** | [**PanelLastRestartReason**](PanelLastRestartReason.md) |  | [optional] 
**meminfo** | [**PanelMeminfo**](PanelMeminfo.md) |  | [optional] 
**cpu_usage** | [**PanelCpuUsage**](PanelCpuUsage.md) |  | [optional] 
**disk** | [**PanelDisk**](PanelDisk.md) |  | [optional] 
**panel** | [**PanelPanel**](PanelPanel.md) |  | [optional] 
**oii_sessions** | [**PanelOIISessions**](PanelOIISessions.md) |  | [optional] 

## Example

```python
from bosch-alarm-map.models.panel import Panel

# TODO update the JSON string below
json = "{}"
# create an instance of Panel from a JSON string
panel_instance = Panel.from_json(json)
# print the JSON string representation of the object
print(Panel.to_json())

# convert the object into a dict
panel_dict = panel_instance.to_dict()
# create an instance of Panel from a dict
panel_from_dict = Panel.from_dict(panel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


