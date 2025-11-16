# StatisticsOii


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Start date | [optional] 
**last** | **str** | Last update date | [optional] 
**duration** | **str** | Amount of time between start of statistics and last statistic update | [optional] 
**interval** | **str** | Frequency interval, on average how often statistic is appended | [optional] 
**counter** | **int** | Update counter, number of changes made to statistic module | [optional] 
**requests** | **int** | Number of REST-API requests | [optional] 
**responses** | **int** | Number of REST-API responses | [optional] 
**positive** | **int** | Number of positive REST-API responses | [optional] 
**positive** | **int** | Percent of positive REST-API responses | [optional] 
**negative** | **int** | Number of negative REST-API responses | [optional] 
**negative** | **int** | Percent of negative REST-API responses | [optional] 
**positive_responses** | **List[str]** | List of used REST-API endpoints that returned positive response with:   - endpoint URL   - request type   - request command (if available)   - number of responses   - minimum time to respond in milliseconds   - average time to respond in milliseconds   - maximum time to respond in milliseconds  | [optional] 
**negative_responses** | **List[str]** | List of used REST-API endpoints that returned negative response with:   - endpoint URL   - request type   - http code   - count of responses  | [optional] 
**clients** | [**List[StatisticsOiiAllOfClientsInner]**](StatisticsOiiAllOfClientsInner.md) | List of REST-API clients (client name format: USERID@IP, e.g. \&quot;005@127.0.0.1\&quot;) with client statistic:   - date and time of the first request received   - date and time of the last request received   - time duration between last request and first   - interval, on average how often statistic is appended   - delay between requests (minimum, average, maximum)   - number of requests   - number of responses sent   - number of positive responses sent   - number of negative responses sent  | [optional] 

## Example

```python
from bosch_alarm_map.models.statistics_oii import StatisticsOii

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsOii from a JSON string
statistics_oii_instance = StatisticsOii.from_json(json)
# print the JSON string representation of the object
print(StatisticsOii.to_json())

# convert the object into a dict
statistics_oii_dict = statistics_oii_instance.to_dict()
# create an instance of StatisticsOii from a dict
statistics_oii_from_dict = StatisticsOii.from_dict(statistics_oii_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


