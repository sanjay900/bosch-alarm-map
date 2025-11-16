# StatisticsOiiAllOfClientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Start date | [optional] 
**last** | **str** | Last update date | [optional] 
**duration** | **str** | Amount of time between start of statistics and last statistic update | [optional] 
**interval** | **str** | Frequency interval, on average how often statistic is appended | [optional] 
**delay** | **str** | Delay between clients requests, minimum, average, maximum | [optional] 
**requests** | **int** | Number of requests made by client | [optional] 
**responses** | **int** | Number of responses sent to client | [optional] 
**positive** | **int** | Number of positive responses sent to client | [optional] 
**negative** | **int** | Number of positive negative sent to client | [optional] 

## Example

```python
from bosch_alarm_map.models.statistics_oii_all_of_clients_inner import StatisticsOiiAllOfClientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsOiiAllOfClientsInner from a JSON string
statistics_oii_all_of_clients_inner_instance = StatisticsOiiAllOfClientsInner.from_json(json)
# print the JSON string representation of the object
print(StatisticsOiiAllOfClientsInner.to_json())

# convert the object into a dict
statistics_oii_all_of_clients_inner_dict = statistics_oii_all_of_clients_inner_instance.to_dict()
# create an instance of StatisticsOiiAllOfClientsInner from a dict
statistics_oii_all_of_clients_inner_from_dict = StatisticsOiiAllOfClientsInner.from_dict(statistics_oii_all_of_clients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


