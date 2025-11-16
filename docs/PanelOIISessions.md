# PanelOIISessions

Information about memory usage for REST-API sessions in bytes, sessions can have no buffer, indicated with size of zero. Sessions are a pre-allocated memory object, they do not represent active clients, however they are correlated. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_memory_usage** | **int** | Total memory allocation for REST-API buffers | [optional] 
**per_session_usage** | **List[int]** | Memory allocation per session | [optional] 

## Example

```python
from bosch-alarm-map.models.panel_oii_sessions import PanelOIISessions

# TODO update the JSON string below
json = "{}"
# create an instance of PanelOIISessions from a JSON string
panel_oii_sessions_instance = PanelOIISessions.from_json(json)
# print the JSON string representation of the object
print(PanelOIISessions.to_json())

# convert the object into a dict
panel_oii_sessions_dict = panel_oii_sessions_instance.to_dict()
# create an instance of PanelOIISessions from a dict
panel_oii_sessions_from_dict = PanelOIISessions.from_dict(panel_oii_sessions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


