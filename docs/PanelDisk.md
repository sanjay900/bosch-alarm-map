# PanelDisk

Disk (NAND flash) usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total disk capacity in kilobytes | [optional] 
**free** | **int** | Free disk capacity in kilobytes | [optional] 
**usage** | **int** | Used disk capacity in kilobytes | [optional] 
**badblocks** | **int** | Number of bad blocks of NAND flash | [optional] 

## Example

```python
from bosch-alarm-map.models.panel_disk import PanelDisk

# TODO update the JSON string below
json = "{}"
# create an instance of PanelDisk from a JSON string
panel_disk_instance = PanelDisk.from_json(json)
# print the JSON string representation of the object
print(PanelDisk.to_json())

# convert the object into a dict
panel_disk_dict = panel_disk_instance.to_dict()
# create an instance of PanelDisk from a dict
panel_disk_from_dict = PanelDisk.from_dict(panel_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


