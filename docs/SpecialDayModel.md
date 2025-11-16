# SpecialDayModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_model_id** | **str** | Unique name (ID) of an existing Access Model | [optional] 
**priority** | **int** | If more than one time model is configured at the same date, the time model with the highest priority will be executed (1 &#x3D; highest, 100 lowest) | [optional] 
**next_occurrence** | **str** | Yearly repeating Date of the Special day. The date of nextOccurrence must be today or in the future. | [optional] 
**repeat_policy** | **str** | Final date, up to the specialmodel is guilty. It is optional in custom and easterBased. Date must be today or in the future. | [optional] 
**custom_rule** | **str** | The Custom rules are constructed with 2 or 3 words. The words are separated with a space. Allowed parameters for index, day and month: &lt;br&gt; The index value can be: &lt;br&gt;   - FIRST   - SECOND   - THIRD   - FOURTH   - FIFTH  the day value can be:&lt;br&gt;   - MONDAY   - TUESDAY   - WEDNESDAY   - THURSDAY   - FRIDAY   - SATURDAY   - SUNDAY  The month value can by: &lt;br&gt; - JANUARY - FEBRUARY - MARCH - APRIL - MAY - JUNE - JULY - AUGUST - SEPTEMBER - OCTOBER - NOVEMBER - DECEMBER  #### Custom rules 2 words:  **Index Day** or &lt;br&gt; **Index Month** &lt;br&gt;  Example *2 word rule* (each week, every month)&lt;br&gt; \&quot;SECOND FRIDAY\&quot;&lt;br&gt; That means that this special day occurs on every second Friday of every month.&lt;br&gt;  Example *2 word rule* (particular month, every year)&lt;br&gt; \&quot;FIRST JUNE\&quot;&lt;br&gt; That means that this special day occurs on every first June of every year.&lt;br&gt;  #### Custom rules 3 words:  **INDEX DAY MONTH** Example 3 word rule (defined day, particular month, every year&lt;br&gt; \&quot;FIRST SUNDAY MARCH\&quot;&lt;br&gt; That means that this special day occurs on first Sunday of each March.&lt;br&gt;  | [optional] 
**easter_offset** | **str** | The vaule is required only for easterBase. | [optional] 
**repeat_until** | **str** | The date of nextOccurrence must be today or in the future. | [optional] 

## Example

```python
from bosch-alarm-map.models.special_day_model import SpecialDayModel

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialDayModel from a JSON string
special_day_model_instance = SpecialDayModel.from_json(json)
# print the JSON string representation of the object
print(SpecialDayModel.to_json())

# convert the object into a dict
special_day_model_dict = special_day_model_instance.to_dict()
# create an instance of SpecialDayModel from a dict
special_day_model_from_dict = SpecialDayModel.from_dict(special_day_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


