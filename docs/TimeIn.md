# TimeIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | Fixed String identifier for this command | 
**utc_date_time** | **str** | Date as defined above including timezone but in second precision. If no time zone is specified (e.g. +02:00 or Z), the request will be rejected. second fraction, e.g. millie seconds are not allowed. Actually this is supports a simple time synchronization that is not that accurate and what depends on the TCP transporting time. | 

## Example

```python
from bosch-alarm-map.models.time_in import TimeIn

# TODO update the JSON string below
json = "{}"
# create an instance of TimeIn from a JSON string
time_in_instance = TimeIn.from_json(json)
# print the JSON string representation of the object
print(TimeIn.to_json())

# convert the object into a dict
time_in_dict = time_in_instance.to_dict()
# create an instance of TimeIn from a dict
time_in_from_dict = TimeIn.from_dict(time_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


