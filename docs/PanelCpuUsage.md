# PanelCpuUsage

CPU usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **float** | Current CPU usage percentage (5 seconds average) | [optional] 
**averages** | [**PanelCpuUsageAverages**](PanelCpuUsageAverages.md) |  | [optional] 

## Example

```python
from openapi_client.models.panel_cpu_usage import PanelCpuUsage

# TODO update the JSON string below
json = "{}"
# create an instance of PanelCpuUsage from a JSON string
panel_cpu_usage_instance = PanelCpuUsage.from_json(json)
# print the JSON string representation of the object
print(PanelCpuUsage.to_json())

# convert the object into a dict
panel_cpu_usage_dict = panel_cpu_usage_instance.to_dict()
# create an instance of PanelCpuUsage from a dict
panel_cpu_usage_from_dict = PanelCpuUsage.from_dict(panel_cpu_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


