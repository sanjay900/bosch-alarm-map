# StatisticsCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Start date | [optional] 
**last** | **str** | Last update date | [optional] 
**duration** | **str** | Amount of time between start of statistics and last statistic update | [optional] 
**interval** | **str** | Frequency interval, on average how often statistic is appended | [optional] 

## Example

```python
from bosch-alarm-map.models.statistics_common import StatisticsCommon

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsCommon from a JSON string
statistics_common_instance = StatisticsCommon.from_json(json)
# print the JSON string representation of the object
print(StatisticsCommon.to_json())

# convert the object into a dict
statistics_common_dict = statistics_common_instance.to_dict()
# create an instance of StatisticsCommon from a dict
statistics_common_from_dict = StatisticsCommon.from_dict(statistics_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


