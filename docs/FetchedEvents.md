# FetchedEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evts** | [**List[Evts]**](Evts.md) | List of current subscriptions (respecting the access rights of the user) | [optional] 

## Example

```python
from bosch-alarm-map.models.fetched_events import FetchedEvents

# TODO update the JSON string below
json = "{}"
# create an instance of FetchedEvents from a JSON string
fetched_events_instance = FetchedEvents.from_json(json)
# print the JSON string representation of the object
print(FetchedEvents.to_json())

# convert the object into a dict
fetched_events_dict = fetched_events_instance.to_dict()
# create an instance of FetchedEvents from a dict
fetched_events_from_dict = FetchedEvents.from_dict(fetched_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


