# GetSpecialdaymodel200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_day_model_id** | **str** | Unique Name of the Special day. The name is used to identify the item on the MAP System. The following characters are forbidden in identifier name: \&quot; @ ;  | 
**day_model_id** | **str** | Unique name (ID) of an existing Access Model | [optional] 
**priority** | **int** | If more than one time model is configured at the same date, the time model with the highest priority will be executed (1 &#x3D; highest, 100 lowest) | [optional] 
**next_occurrence** | **str** | Yearly repeating Date of the Special day. The date of nextOccurrence must be today or in the future. | [optional] 
**repeat_policy** | **str** | Final date, up to the specialmodel is guilty. It is optional in custom and easterBased. Date must be today or in the future. | [optional] 
**custom_rule** | **str** | The Custom rules are constructed with 2 or 3 words. The words are separated with a space. Allowed parameters for index, day and month: &lt;br&gt; The index value can be: &lt;br&gt;   - FIRST   - SECOND   - THIRD   - FOURTH   - FIFTH  the day value can be:&lt;br&gt;   - MONDAY   - TUESDAY   - WEDNESDAY   - THURSDAY   - FRIDAY   - SATURDAY   - SUNDAY  The month value can by: &lt;br&gt; - JANUARY - FEBRUARY - MARCH - APRIL - MAY - JUNE - JULY - AUGUST - SEPTEMBER - OCTOBER - NOVEMBER - DECEMBER  #### Custom rules 2 words:  **Index Day** or &lt;br&gt; **Index Month** &lt;br&gt;  Example *2 word rule* (each week, every month)&lt;br&gt; \&quot;SECOND FRIDAY\&quot;&lt;br&gt; That means that this special day occurs on every second Friday of every month.&lt;br&gt;  Example *2 word rule* (particular month, every year)&lt;br&gt; \&quot;FIRST JUNE\&quot;&lt;br&gt; That means that this special day occurs on every first June of every year.&lt;br&gt;  #### Custom rules 3 words:  **INDEX DAY MONTH** Example 3 word rule (defined day, particular month, every year&lt;br&gt; \&quot;FIRST SUNDAY MARCH\&quot;&lt;br&gt; That means that this special day occurs on first Sunday of each March.&lt;br&gt;  | [optional] 
**easter_offset** | **str** | The vaule is required only for easterBase. | [optional] 
**repeat_until** | **str** | The date of nextOccurrence must be today or in the future. | [optional] 
**special_day_model_sync_id** | **int** | Synchronization ID for the special day database table. Will be changed for each change in the special day database table. | 

## Example

```python
from bosch-alarm-map.models.get_specialdaymodel200_response import GetSpecialdaymodel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpecialdaymodel200Response from a JSON string
get_specialdaymodel200_response_instance = GetSpecialdaymodel200Response.from_json(json)
# print the JSON string representation of the object
print(GetSpecialdaymodel200Response.to_json())

# convert the object into a dict
get_specialdaymodel200_response_dict = get_specialdaymodel200_response_instance.to_dict()
# create an instance of GetSpecialdaymodel200Response from a dict
get_specialdaymodel200_response_from_dict = GetSpecialdaymodel200Response.from_dict(get_specialdaymodel200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


