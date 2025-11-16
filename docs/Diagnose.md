# Diagnose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | Retrieves diagnostic information of the device.  Only walktestable device provides some diagnostic information that can be fetched using the diagnose command. (This information has not been included as a property of the resource as it changes only rarely and is usually only used in preparation of a walktest. Thus, moving it into a command allows to save bandwidth in most scenarios.)  | [optional] 

## Example

```python
from bosch_alarm_map.models.diagnose import Diagnose

# TODO update the JSON string below
json = "{}"
# create an instance of Diagnose from a JSON string
diagnose_instance = Diagnose.from_json(json)
# print the JSON string representation of the object
print(Diagnose.to_json())

# convert the object into a dict
diagnose_dict = diagnose_instance.to_dict()
# create an instance of Diagnose from a dict
diagnose_from_dict = Diagnose.from_dict(diagnose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


