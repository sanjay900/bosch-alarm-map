# Sub


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**lease_time** | **int** | The actual lease time, in which the client has to renew its subscriptions to prevent the subscription and events to be deleted. &lt;br&gt; - Minimum &#x3D; 10 - Maximum &#x3D; 600 | [optional] 
**buffer_size** | **int** | Actual size of the allocated event ring buffer. | [optional] 
**subscriptions** | **List[List[SubscriptionsInner]]** | Detailed information about the description in the same format as given during the subscription request | [optional] 

## Example

```python
from bosch_alarm_map.models.sub import Sub

# TODO update the JSON string below
json = "{}"
# create an instance of Sub from a JSON string
sub_instance = Sub.from_json(json)
# print the JSON string representation of the object
print(Sub.to_json())

# convert the object into a dict
sub_dict = sub_instance.to_dict()
# create an instance of Sub from a dict
sub_from_dict = Sub.from_dict(sub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


