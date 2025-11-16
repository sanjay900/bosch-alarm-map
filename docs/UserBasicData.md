# UserBasicData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_type** | **str** | The userType value classifies users in two ways. - First, an Installer user has per default more privileges than a standard user. This rights are needed for example for maintenance work one the system. - Second, the userType defines if the user account is time-limited (*One-Time-Use* or *Temporary*) or not (*Standard*).   The User type *Standard* is active over the full system time, which is defined from 01.01.1970 to 19.01.2038.   Time-limited users are only active in a defined time period. To define this period the key values *activeFrom* and *activeUntil* are used to set a time interval.   The time period must be between 01.01.1970 - 19.01.2038.  | [optional] 
**access_model** | **str** | Name of an existing access Model | [optional] 
**active** | **bool** | Identifies if the user is currently active and can access the MAP system. | [optional] [default to True]
**active_from** | **str** | Start date when user will be activated and can access the MAP system. If active is true the attribute activeFrom must not be used.  | [optional] 
**active_until** | **str** | Date when the users access to the System expires. Used for Temporary User Types  | [optional] 
**smartkey_model_name** | **str** | Name of an existing Smartkey Model, a part of Smartkey Profile set. Smartkey Profile is an optional attribute set, it up to 3 attributes Name - Access Type, Token. Name and Access Type must be specified together. &#39;Token Only&#39; and &#39;Token And PINpad&#39; Access Types require Token.  | [optional] 
**is_oii_user** | **bool** | User have permission for REST-API (OII)  | [optional] 
**is_oii_user_kp_user** | **bool** | User have permission for login from MAP Keypad  | [optional] 
**language** | **str** | The Language shown on the MAP Keypad when this user logs into the MAP system. Supported Languages: - English: en-US - German: de-DE - French: fr-FR - Dutch: nl-NL - Hungarian: hu-HU - Polish: pl-PL - Italian: it-IT - Russian: ru-RU - Spanish: es-ES - Czech: cs-CZ - Portuguese: pt-PT - Latvian: lv-LV - Romanian: ro-RO - Lithuanian: lt-LT - Ukrainian: uk-UK  | [optional] 
**passcode_chng_rqd** | **bool** | Defines whether the user has to change the passcode at the next Login | [optional] 

## Example

```python
from bosch-alarm-map.models.user_basic_data import UserBasicData

# TODO update the JSON string below
json = "{}"
# create an instance of UserBasicData from a JSON string
user_basic_data_instance = UserBasicData.from_json(json)
# print the JSON string representation of the object
print(UserBasicData.to_json())

# convert the object into a dict
user_basic_data_dict = user_basic_data_instance.to_dict()
# create an instance of UserBasicData from a dict
user_basic_data_from_dict = UserBasicData.from_dict(user_basic_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


