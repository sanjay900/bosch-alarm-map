# DeviceConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of device as configured in RPS for MAP. | [optional] 
**siid** | **str** | Auto generated unique Identifier. A, B, C and D are integer values. | [optional] 
**type** | **str** | &lt;table&gt;   &lt;tr&gt;     &lt;td&gt;----&lt;/td&gt;     &lt;td&gt;----------&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;TYPE&lt;/td&gt;     &lt;td&gt;SUBTYPE(S)&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;----&lt;/td&gt;     &lt;td&gt;----------&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;POINT&lt;/td&gt;     &lt;td&gt;ONBOARD,TAMPER, LSNEXPANDER, PIR, SEISMIC, GLASSBREAK, CONTACT, PANIC, UNIVERSAL, MCP, VIRTUAL&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;FIREDETECTOR&lt;/td&gt;     &lt;td&gt;O, OT, OC, OTC, T&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;OUTPUT&lt;/td&gt;     &lt;td&gt;CONTROL, LED, SIREN,STROBE, KPSPEAKER (Keypad Speaker), VIRTUAL&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;LSNBUS&lt;/td&gt;     &lt;td&gt;LOOP,STUB&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;KEYSWITCH&lt;/td&gt;     &lt;td&gt;STATIC,DYNAMIC, VIRTUALSTATIC, VIRTUALDYNAMIC&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;COMMUNICATOR&lt;/td&gt;     &lt;td&gt;AT2000, AT3000&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;COUPLER&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;LSNAUX&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;GROUNDFAULT&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;BATTERYCHARGER&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;BATTERY&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;MAINS&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;PSCANOUTPUT&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;POWERDEVICE&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;PRINTER&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;BLOCKLOCK&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;SMARTKEY&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;DEMODULE&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;POWERSUPPLY&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;LSNGATEWAY&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;KEYPAD&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;OII&lt;/td&gt;     &lt;td&gt;-&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;SUPERV&lt;/td&gt;     &lt;td&gt;BIS,IPC,OII&lt;/td&gt;   &lt;/tr&gt; &lt;/table&gt;  | [optional] 
**part_of_walktest** | **bool** | Indicates whether this device is part of a walktest. If true, the resource will implement the walktest interface. | [optional] 
**bypassable** | **bool** | Indicates whether device can be bypassed. If true, the resource implements the bypass interface. | [optional] 
**parent_siid** | **str** | Parent Device SIID. This will be “&lt;Empty&gt;” if no parent Device. This would indicate where the device is configured. For such as On board, internal CAN etc A, B, C and D are integer values. | [optional] 

## Example

```python
from bosch_alarm_map.models.device_configuration import DeviceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceConfiguration from a JSON string
device_configuration_instance = DeviceConfiguration.from_json(json)
# print the JSON string representation of the object
print(DeviceConfiguration.to_json())

# convert the object into a dict
device_configuration_dict = device_configuration_instance.to_dict()
# create an instance of DeviceConfiguration from a dict
device_configuration_from_dict = DeviceConfiguration.from_dict(device_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


