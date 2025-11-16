# InternalProgramsConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of internal program as configured in RPS for MAP. | [optional] 
**siid** | **str** | Auto generated unique Identifier. A, B, C and D are integer values. | [optional] 
**device_list** | **List[str]** | List of SIIDs of all devices configured for the internal program. | [optional] 

## Example

```python
from openapi_client.models.internal_programs_configuration import InternalProgramsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of InternalProgramsConfiguration from a JSON string
internal_programs_configuration_instance = InternalProgramsConfiguration.from_json(json)
# print the JSON string representation of the object
print(InternalProgramsConfiguration.to_json())

# convert the object into a dict
internal_programs_configuration_dict = internal_programs_configuration_instance.to_dict()
# create an instance of InternalProgramsConfiguration from a dict
internal_programs_configuration_from_dict = InternalProgramsConfiguration.from_dict(internal_programs_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


