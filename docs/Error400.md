# Error400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The error code 400 is returned by the server if there is a semantic error in the requested body. Possible error states are: &lt;br&gt; * MissingArgument - Error case, if a required variable was not sent from the client * TooLong - Error case, if a sent variable by the client is too long. A variable may consist of a maximum of 64 characters. Exceptions are the attributes *firstName* and *lastName* of the command POST /usermodel. A maximum of 32 characters may be used here. * BadValue - Basic error case, caused by the client:   + Wrong data type or unexpected value   - Reference not existing   - Value with forbidden special characters:     - \\     - &#39;     - \&quot;     - @     - ;  | 
**target** | **str** | The target value, which is responsible for the error. | [optional] 
**message** | **str** | Universal generic JSON object to specify the error case. Starts with string: \&quot;Conflict caused by:  | [optional] 

## Example

```python
from bosch-alarm-map.models.error400 import Error400

# TODO update the JSON string below
json = "{}"
# create an instance of Error400 from a JSON string
error400_instance = Error400.from_json(json)
# print the JSON string representation of the object
print(Error400.to_json())

# convert the object into a dict
error400_dict = error400_instance.to_dict()
# create an instance of Error400 from a dict
error400_from_dict = Error400.from_dict(error400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


