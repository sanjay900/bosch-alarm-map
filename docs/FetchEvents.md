# FetchEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | Fetch events from the buffer of this subscription | [optional] 
**max_events** | **int** | Optional. Default value is “unlimited”. | [optional] 
**min_events** | **int** | Optional. If not specified or specified as 0, minEvents &#x3D; maxEvents. If a request specifies minEvents bigger than maxEvents, minEvents will be set to maxEvents. | [optional] 
**max_time** | **int** | Optional. Maximum number of seconds the call will block. Maximum value is 100. Minimum is 0. | [optional] 

## Example

```python
from bosch-alarm-map.models.fetch_events import FetchEvents

# TODO update the JSON string below
json = "{}"
# create an instance of FetchEvents from a JSON string
fetch_events_instance = FetchEvents.from_json(json)
# print the JSON string representation of the object
print(FetchEvents.to_json())

# convert the object into a dict
fetch_events_dict = fetch_events_instance.to_dict()
# create an instance of FetchEvents from a dict
fetch_events_from_dict = FetchEvents.from_dict(fetch_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


