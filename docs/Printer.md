# Printer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**cover_open** | **bool** | True if printer cover is open, otherwise false | [optional] 
**paper_low** | **bool** | True if printer is low on paper | [optional] 

## Example

```python
from bosch_alarm_map.models.printer import Printer

# TODO update the JSON string below
json = "{}"
# create an instance of Printer from a JSON string
printer_instance = Printer.from_json(json)
# print the JSON string representation of the object
print(Printer.to_json())

# convert the object into a dict
printer_dict = printer_instance.to_dict()
# create an instance of Printer from a dict
printer_from_dict = Printer.from_dict(printer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


