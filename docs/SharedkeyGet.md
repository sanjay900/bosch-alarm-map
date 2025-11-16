# SharedkeyGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **str** | Shared Key checksum | [optional] 
**encrypted** | **str** | Encrypted Shared Key data | [optional] 
**timestamp** | **str** | Shared Key timestamp | [optional] 

## Example

```python
from openapi_client.models.sharedkey_get import SharedkeyGet

# TODO update the JSON string below
json = "{}"
# create an instance of SharedkeyGet from a JSON string
sharedkey_get_instance = SharedkeyGet.from_json(json)
# print the JSON string representation of the object
print(SharedkeyGet.to_json())

# convert the object into a dict
sharedkey_get_dict = sharedkey_get_instance.to_dict()
# create an instance of SharedkeyGet from a dict
sharedkey_get_from_dict = SharedkeyGet.from_dict(sharedkey_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


