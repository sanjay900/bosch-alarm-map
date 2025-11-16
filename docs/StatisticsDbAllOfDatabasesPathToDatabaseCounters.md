# StatisticsDbAllOfDatabasesPathToDatabaseCounters

SQL database performance statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reads** | **int** | Number of database reads | [optional] 
**read_interval** | **str** | Frequency of database reads | [optional] 
**writes** | **int** | Number of database writes | [optional] 
**write_interval** | **str** | Frequency of database writes | [optional] 

## Example

```python
from openapi_client.models.statistics_db_all_of_databases_path_to_database_counters import StatisticsDbAllOfDatabasesPathToDatabaseCounters

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsDbAllOfDatabasesPathToDatabaseCounters from a JSON string
statistics_db_all_of_databases_path_to_database_counters_instance = StatisticsDbAllOfDatabasesPathToDatabaseCounters.from_json(json)
# print the JSON string representation of the object
print(StatisticsDbAllOfDatabasesPathToDatabaseCounters.to_json())

# convert the object into a dict
statistics_db_all_of_databases_path_to_database_counters_dict = statistics_db_all_of_databases_path_to_database_counters_instance.to_dict()
# create an instance of StatisticsDbAllOfDatabasesPathToDatabaseCounters from a dict
statistics_db_all_of_databases_path_to_database_counters_from_dict = StatisticsDbAllOfDatabasesPathToDatabaseCounters.from_dict(statistics_db_all_of_databases_path_to_database_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


