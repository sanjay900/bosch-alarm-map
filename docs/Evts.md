# Evts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of this event consisting of panel and local subscriber id. &lt;br&gt; **Panel Event ID**: Panelwide, unique ID for this event. A client shall treat this ID as an opaque string and should not assume any particular semantics of the panel ID value. The panel event ID is independent of the individual subscription and unique even over a power cycle of the MAP panel. &lt;br&gt; **SubscriptionSequenceNumber**: An integer that identifies an event in the context of the subscription. The sequence number will be incremented for each event that is stored for a specific subscription (starting with 0). A client can inspect the sequence number of an event to deduct whether events have been lost i.e. MAP panel has overridden an event as the ring buffer is full. The number ranges from 0 to 65535. In case this range is exceeded, the number is reset to 0 and continued to be incremented from then on. From this follows that a client needs to be prepared to expect a sequence number of 0 as a valid successor to 65535. | [optional] 
**time** | **str** | Local date time including time zone information for when the event occurred. | [optional] 
**type** | **str** | Event type classifier | [optional] 
**props** | **List[str]** | A list of property keys whose value has changed. The list contains at least a single entry for an event of type CHANGED. In all other cases the list will be empty. | [optional] 
**evt** | [**Evt**](Evt.md) | The resource representation as would be provided using a GET on that resource directly after the event happened. | [optional] 

## Example

```python
from bosch_alarm_map.models.evts import Evts

# TODO update the JSON string below
json = "{}"
# create an instance of Evts from a JSON string
evts_instance = Evts.from_json(json)
# print the JSON string representation of the object
print(Evts.to_json())

# convert the object into a dict
evts_dict = evts_instance.to_dict()
# create an instance of Evts from a dict
evts_from_dict = Evts.from_dict(evts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


