# PanelPanel

Information about MAP Panel application itself

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_size** | **int** | Virtual RAM usage in kilobytes | [optional] 
**vm_rss** | **int** | Physical RAM usage in kilobytes | [optional] 
**threads** | **int** | Number of threads used | [optional] 

## Example

```python
from openapi_client.models.panel_panel import PanelPanel

# TODO update the JSON string below
json = "{}"
# create an instance of PanelPanel from a JSON string
panel_panel_instance = PanelPanel.from_json(json)
# print the JSON string representation of the object
print(PanelPanel.to_json())

# convert the object into a dict
panel_panel_dict = panel_panel_instance.to_dict()
# create an instance of PanelPanel from a dict
panel_panel_from_dict = PanelPanel.from_dict(panel_panel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


