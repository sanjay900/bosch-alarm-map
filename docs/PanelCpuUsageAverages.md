# PanelCpuUsageAverages

Average CPU usage percentage over period (exponential moving average)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_1min** | **float** | Average over 1 minute | [optional] 
**var_5min** | **float** | Average over 5 minutes | [optional] 
**var_30min** | **float** | Average over 30 minutes | [optional] 

## Example

```python
from bosch-alarm-map.models.panel_cpu_usage_averages import PanelCpuUsageAverages

# TODO update the JSON string below
json = "{}"
# create an instance of PanelCpuUsageAverages from a JSON string
panel_cpu_usage_averages_instance = PanelCpuUsageAverages.from_json(json)
# print the JSON string representation of the object
print(PanelCpuUsageAverages.to_json())

# convert the object into a dict
panel_cpu_usage_averages_dict = panel_cpu_usage_averages_instance.to_dict()
# create an instance of PanelCpuUsageAverages from a dict
panel_cpu_usage_averages_from_dict = PanelCpuUsageAverages.from_dict(panel_cpu_usage_averages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


