# StatisticsGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Start date | [optional] 
**last** | **str** | Last update date | [optional] 
**duration** | **str** | Amount of time between start of statistics and last statistic update | [optional] 
**interval** | **str** | Frequency interval, on average how often statistic is appended | [optional] 
**counter** | **int** | Update counter, number of changes made to statistic module | [optional] 
**oii** | **object** |  | [optional] 
**db** | **object** |  | [optional] 

## Example

```python
from bosch-alarm-map.models.statistics_get import StatisticsGet

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsGet from a JSON string
statistics_get_instance = StatisticsGet.from_json(json)
# print the JSON string representation of the object
print(StatisticsGet.to_json())

# convert the object into a dict
statistics_get_dict = statistics_get_instance.to_dict()
# create an instance of StatisticsGet from a dict
statistics_get_from_dict = StatisticsGet.from_dict(statistics_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


