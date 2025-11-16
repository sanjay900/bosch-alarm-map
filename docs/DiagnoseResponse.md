# DiagnoseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_since_last_activity** | **int** | Number of days since the last activity from the device | [optional] 
**last_walktest_date** | **str** | Time and date | [optional] 
**walktest_recommended** | **bool** | True if a walktest is recommended for the device | [optional] 

## Example

```python
from openapi_client.models.diagnose_response import DiagnoseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnoseResponse from a JSON string
diagnose_response_instance = DiagnoseResponse.from_json(json)
# print the JSON string representation of the object
print(DiagnoseResponse.to_json())

# convert the object into a dict
diagnose_response_dict = diagnose_response_instance.to_dict()
# create an instance of DiagnoseResponse from a dict
diagnose_response_from_dict = DiagnoseResponse.from_dict(diagnose_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


