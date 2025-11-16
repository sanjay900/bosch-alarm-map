# StatisticsDbAllOfDatabasesPathToDatabaseHandles

SQL database handle statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alloc** | **int** | Number of created (allocated) SQL handles | [optional] 
**dealloc** | **int** | Number of deleted (deallocated) SQL handles | [optional] 
**usage** | **int** | Number of SQL handles in use | [optional] 

## Example

```python
from bosch-alarm-map.models.statistics_db_all_of_databases_path_to_database_handles import StatisticsDbAllOfDatabasesPathToDatabaseHandles

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsDbAllOfDatabasesPathToDatabaseHandles from a JSON string
statistics_db_all_of_databases_path_to_database_handles_instance = StatisticsDbAllOfDatabasesPathToDatabaseHandles.from_json(json)
# print the JSON string representation of the object
print(StatisticsDbAllOfDatabasesPathToDatabaseHandles.to_json())

# convert the object into a dict
statistics_db_all_of_databases_path_to_database_handles_dict = statistics_db_all_of_databases_path_to_database_handles_instance.to_dict()
# create an instance of StatisticsDbAllOfDatabasesPathToDatabaseHandles from a dict
statistics_db_all_of_databases_path_to_database_handles_from_dict = StatisticsDbAllOfDatabasesPathToDatabaseHandles.from_dict(statistics_db_all_of_databases_path_to_database_handles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


