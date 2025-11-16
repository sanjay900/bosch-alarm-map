# GetDaymodel200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_model_id** | **str** | Unique name of a DayModel. The name is used to identify the item on the MAP System. The following characters are forbidden in identifier name: \&quot; @ ;  | 
**interval** | **List[str]** | Define up to three timezones of the Daymodel. | [optional] 
**day_model_sync_id** | **int** | Synchronization ID for the day database table. Will be changed for each change in the day database table. | 

## Example

```python
from openapi_client.models.get_daymodel200_response import GetDaymodel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDaymodel200Response from a JSON string
get_daymodel200_response_instance = GetDaymodel200Response.from_json(json)
# print the JSON string representation of the object
print(GetDaymodel200Response.to_json())

# convert the object into a dict
get_daymodel200_response_dict = get_daymodel200_response_instance.to_dict()
# create an instance of GetDaymodel200Response from a dict
get_daymodel200_response_from_dict = GetDaymodel200Response.from_dict(get_daymodel200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


