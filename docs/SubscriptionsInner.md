# SubscriptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** | List of links relative to the MAP system base URL from which events are to be received. The list may contain strings that follow the string matching as defined in *MAPOpenIntrusionInterface_ApplicationNotes.pdf* ,matching to reference multiple resources in a compact way.&lt;br&gt;  Examples: &lt;br&gt; Subscription to all events from all areas - [ \&quot;*\&quot; ]  Subscription to specific area ID - [ /1.1.Area.2.5 ]  | [optional] 
**event_type** | **List[str]** | Array of event types. Possible event types are: - CHANGED - CREATED - DELETED  | [optional] 

## Example

```python
from bosch-alarm-map.models.subscriptions_inner import SubscriptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsInner from a JSON string
subscriptions_inner_instance = SubscriptionsInner.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsInner.to_json())

# convert the object into a dict
subscriptions_inner_dict = subscriptions_inner_instance.to_dict()
# create an instance of SubscriptionsInner from a dict
subscriptions_inner_from_dict = SubscriptionsInner.from_dict(subscriptions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


