# StatisticsDbAllOfDatabasesPathToDatabase

Database information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_kb** | **int** | Size of History Database in Kilobytes | [optional] 
**handles** | [**StatisticsDbAllOfDatabasesPathToDatabaseHandles**](StatisticsDbAllOfDatabasesPathToDatabaseHandles.md) |  | [optional] 
**counters** | [**StatisticsDbAllOfDatabasesPathToDatabaseCounters**](StatisticsDbAllOfDatabasesPathToDatabaseCounters.md) |  | [optional] 

## Example

```python
from bosch-alarm-map.models.statistics_db_all_of_databases_path_to_database import StatisticsDbAllOfDatabasesPathToDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsDbAllOfDatabasesPathToDatabase from a JSON string
statistics_db_all_of_databases_path_to_database_instance = StatisticsDbAllOfDatabasesPathToDatabase.from_json(json)
# print the JSON string representation of the object
print(StatisticsDbAllOfDatabasesPathToDatabase.to_json())

# convert the object into a dict
statistics_db_all_of_databases_path_to_database_dict = statistics_db_all_of_databases_path_to_database_instance.to_dict()
# create an instance of StatisticsDbAllOfDatabasesPathToDatabase from a dict
statistics_db_all_of_databases_path_to_database_from_dict = StatisticsDbAllOfDatabasesPathToDatabase.from_dict(statistics_db_all_of_databases_path_to_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


