# StatisticsDb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Start date | [optional] 
**last** | **str** | Last update date | [optional] 
**duration** | **str** | Amount of time between start of statistics and last statistic update | [optional] 
**interval** | **str** | Frequency interval, on average how often statistic is appended | [optional] 
**counter** | **int** | Update counter, number of changes made to statistic module | [optional] 
**databases** | [**StatisticsDbAllOfDatabases**](StatisticsDbAllOfDatabases.md) |  | [optional] 

## Example

```python
from bosch_alarm_map.models.statistics_db import StatisticsDb

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsDb from a JSON string
statistics_db_instance = StatisticsDb.from_json(json)
# print the JSON string representation of the object
print(StatisticsDb.to_json())

# convert the object into a dict
statistics_db_dict = statistics_db_instance.to_dict()
# create an instance of StatisticsDb from a dict
statistics_db_from_dict = StatisticsDb.from_dict(statistics_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


