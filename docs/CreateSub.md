# CreateSub


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | Fixed String to identify this command | [optional] 
**lease_time** | **int** | Maximum number of seconds between two subscription renewal activities i.e. time between two event fetching requests encoded as JSON number. No fractions supported. The actual lease time is decided by the MAP panel. | [optional] 
**buffer_size** | **int** | Requested number of events that will be stored by the MAP panel without overwriting an entry. The actual buffer size is decided by the MAP panel and provided in the response. | [optional] 
**subscriptions** | **List[List[SubscriptionsInner]]** | Detailed information about the description in the same format as given during the subscription request | [optional] 

## Example

```python
from openapi_client.models.create_sub import CreateSub

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSub from a JSON string
create_sub_instance = CreateSub.from_json(json)
# print the JSON string representation of the object
print(CreateSub.to_json())

# convert the object into a dict
create_sub_dict = create_sub_instance.to_dict()
# create an instance of CreateSub from a dict
create_sub_from_dict = CreateSub.from_dict(create_sub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


