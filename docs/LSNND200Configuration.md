# LSNND200Configuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of a device. | 
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**point_type** | **str** | Point device type. | 
**supports_delayed_reporting** | **bool** | Delayed reporting support. | [optional] 
**walktest_category** | [**LSNWalktestCategoryProperty**](LSNWalktestCategoryProperty.md) |  | [optional] 
**reporting_number** | **int** | LSN device reporting number. | [optional] 

## Example

```python
from bosch-alarm-map.models.lsnnd200_configuration import LSNND200Configuration

# TODO update the JSON string below
json = "{}"
# create an instance of LSNND200Configuration from a JSON string
lsnnd200_configuration_instance = LSNND200Configuration.from_json(json)
# print the JSON string representation of the object
print(LSNND200Configuration.to_json())

# convert the object into a dict
lsnnd200_configuration_dict = lsnnd200_configuration_instance.to_dict()
# create an instance of LSNND200Configuration from a dict
lsnnd200_configuration_from_dict = LSNND200Configuration.from_dict(lsnnd200_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


