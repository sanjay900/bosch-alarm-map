# GetUsermodelById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique numeric user identification (user ID). | 
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
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**passcode** | **str** | 6 digit numerical passcode for login from MAP Keypad | [optional] 
**smartkey_access_type** | **str** | &#39;Token Only&#39; and &#39;Token And PINpad&#39; require Smartkey Token | [optional] 
**smartkey_token** | **str** | Token for the Smartkey. 8 character long hexadecimal value. Must be unique for each user. Requires &#39;Token Only&#39; and &#39;Token And PINpad&#39; Smartkey Access Type | [optional] 
**oii_username** | **str** | Username used for login authentication. It must be at least 8, but no more than 32 characters. It must only consist of characters with ASCII code 33, [ 35, 126]. The used oiiUsername must also be unique on the MAP system. If the selected oiiUsername is already used by another user on the MAP device, a 409 error response message is sent to the client.  | [optional] 
**oii_password** | **str** | Password used to login from REST-API. It must be at least 8, but no more than 16 characters. It must contain at least one UPPERCASE letter. It must contain at least one lowercase letter. It must contain at least one number digit. It must contain at least one special character: [ ! , @ $ % ^ * ? _ ~ - £ ( ) ] | [optional] 
**use_extended_delay** | **bool** | This parameter determines whether the user requires extended entry/exit delay time | [optional] 
**encrypted_secrets** | **bool** | Shows whether secrets are encrypted | [optional] [default to False]
**duress_offset** | **int** | Duress offset configures duress passcode. Duress passcode is not available for Installer User Type. Offset of 0 disables duress for user. To calculate duress passcode, last digit of user&#39;s passcode is ***incremented by offset amount***, incremented digit can wrap around. Example for passcode 123450: offset 1: duress 123451. Example for passcode 123459: offset 2: duress 123451. | [optional] [default to 1]
**user_model_sync_id** | **int** | Synchronization ID for the user database table. Will be changed for each change in the user database table. | 

## Example

```python
from bosch-alarm-map.models.get_usermodel_by_id200_response import GetUsermodelById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsermodelById200Response from a JSON string
get_usermodel_by_id200_response_instance = GetUsermodelById200Response.from_json(json)
# print the JSON string representation of the object
print(GetUsermodelById200Response.to_json())

# convert the object into a dict
get_usermodel_by_id200_response_dict = get_usermodel_by_id200_response_instance.to_dict()
# create an instance of GetUsermodelById200Response from a dict
get_usermodel_by_id200_response_from_dict = GetUsermodelById200Response.from_dict(get_usermodel_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


