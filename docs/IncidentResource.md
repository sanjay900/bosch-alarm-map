# IncidentResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | * HANDLE This operation initiates handling the incident * SILENCE This operation initiates silencing the incident  | [optional] 

## Example

```python
from bosch_alarm_map.models.incident_resource import IncidentResource

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentResource from a JSON string
incident_resource_instance = IncidentResource.from_json(json)
# print the JSON string representation of the object
print(IncidentResource.to_json())

# convert the object into a dict
incident_resource_dict = incident_resource_instance.to_dict()
# create an instance of IncidentResource from a dict
incident_resource_from_dict = IncidentResource.from_dict(incident_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


