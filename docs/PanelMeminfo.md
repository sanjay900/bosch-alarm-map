# PanelMeminfo

/proc/meminfo output, all values are in kilobytes. Please refer to Linux manual page for detailed explanation of the output

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mem_total** | **int** | Kilobytes | [optional] 
**mem_free** | **int** | Kilobytes | [optional] 
**buffers** | **int** | Kilobytes | [optional] 
**cached** | **int** | Kilobytes | [optional] 
**active** | **int** | Kilobytes | [optional] 
**inactive** | **int** | Kilobytes | [optional] 
**swap_total** | **int** | Kilobytes | [optional] 
**swap_free** | **int** | Kilobytes | [optional] 
**dirty** | **int** | Kilobytes | [optional] 
**writeback** | **int** | Kilobytes | [optional] 

## Example

```python
from openapi_client.models.panel_meminfo import PanelMeminfo

# TODO update the JSON string below
json = "{}"
# create an instance of PanelMeminfo from a JSON string
panel_meminfo_instance = PanelMeminfo.from_json(json)
# print the JSON string representation of the object
print(PanelMeminfo.to_json())

# convert the object into a dict
panel_meminfo_dict = panel_meminfo_instance.to_dict()
# create an instance of PanelMeminfo from a dict
panel_meminfo_from_dict = PanelMeminfo.from_dict(panel_meminfo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


