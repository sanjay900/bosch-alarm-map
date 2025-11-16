# TimeOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** |  | [optional] 
**time_zone** | **str** | Time zone following the IANA Time Zone Database (also known as Olson database) name  | [optional] 
**date_time** | **str** | Time and date in REST-API base specification compliant format including milliseconds. A client can extract local as well as UTC date time from this string | [optional] 

## Example

```python
from openapi_client.models.time_out import TimeOut

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOut from a JSON string
time_out_instance = TimeOut.from_json(json)
# print the JSON string representation of the object
print(TimeOut.to_json())

# convert the object into a dict
time_out_dict = time_out_instance.to_dict()
# create an instance of TimeOut from a dict
time_out_from_dict = TimeOut.from_dict(time_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


