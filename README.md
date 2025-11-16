# bosch-alarm-map
# Overview 

This document specifies the MAP REST-API (OII) - **O**pen **I**ntrusion **I**nterface (**OII**). 
The REST-API (former known as **O**pen **I**ntrusion **I**nterface [**OII**]), is implemented on the MAP system. This document is fully valid to the MAP panel firmware Version: <br> <br>
**MAP_Update.1.4.0272.tar.bz2**<br> 
To be backward compatible, all \"/get\", \"/post\" and other commands which includes \"OII\", will be still \"OII\". 
New implemented features will be named as \"REST-API\" instead of \"OII\".

Please note that the following rules have been ignored when checking the OpenAPI documentation file against errors and warnings:
  - [no-identical-paths](https://redocly.com/docs/cli/rules/no-identical-paths/)
  - [no-ambiguous-paths](https://redocly.com/docs/cli/rules/no-ambiguous-paths/)
  - [spec](https://redocly.com/docs/cli/rules/spec/)

The OpenAPI file is structured in the following groups:
1. REST-API_basic
2. REST-API_MUM

## 1: REST-API_basic

All URLs described under this group contain all functions of released MAP panel firmware version 1.4.0176
All REST-API (OII) functions are also described in the following previous documents (PDF):  
  - ApplicationNotes.pdf
  - BaseSpecification.pdf
  - ResourceModel.pdf

This previous REST-API (OII) documentation can be downloaded [here](https://media.boschsecurity.com/fs/media/pb/media/extranet/map_partners/2019_oii_openintrusioninterface.zip). <br> 

New features:
- *Memory Info & statistics*
    This feature is available from the MAP panel firmware version *<1.4.0xxx ToDo, replace*
 
- *NTP*
 This feature is available from the MAP panel firmware version *<1.4.0xxx ToDo, replace*

- *supportfiles* 
   This feature is available from the MAP panel firmware version 1.4.0231

## 2: REST-API_MUM

All URLs described in this group contain the features, which are added by the firmware version 1.4.0245 

New Features:
- *VDS2252 permissions*
   Updated internal permissions with both mayClearMainPowerFailure and mayClearATS


## HTTPS server certificates
The MAP system is using so named \"unique self signed server certificates\" for HTTPS.
The certificate files are created during the MAP panel start, if not already existing.
Due to missing entropy and hardware resources, 2048-bit certificates are created.
The MAP system guarantees those certificates will not change uncontrolled during lifetime.
This guarantee is fullfilled by automated test during development.

## General client requests 

The MAP systems are **strongly limited** in hardware and software resources. This is why there are **limitations** using the MAP REST-API which **must** be considered to avoid erroneous behavior and a poor user experience.<br>
- Use a ping to check the network availability **before** sending HTTP requests to the MAP panel.
- The MAP panel can handle parallel requests. However, it is strongly recommended that a single client makes only serial requests. 
- Parallel processing of many multiple requests will typically fail with negative response codes and overload the system.
- Multiple requests to the same MAP panel must be serialized with a delay of at least 1 second between the last response and the next request.
- The MAP panel might return the response codes 500 or a 503 or other response codes in case of overload.
- Requests with HTTP Content-Length higher than 30000 bytes are not supported, HTTP Error Code 411 will be raised.
- Receiving negative response codes caused by overload require a 60 seconds communication delay.
- If the MAP panel does not (anymore) response at all, a delay of at least 5 minutes must be considered.
- It is strongly recommended to use a connection pool for better HTTPS performance as well as lower CPU load on the MAP panel.
- If the connection is cancelled or runs into timeout it is undefined whether the request will still be processed or not. 
- After connection errors, the HTTPS connection must be closed and it is necessary again to check network availability by ping.
- Cyclic request, e.g. ping, getting synchronization states and performing a time synchronization are allowed.
- Cyclic request must not be more frequent than every 5 minutes.
- Enabled **User Passcode Tamper** feature will prevent potential bruteforce attack. Retry count and lockout time is configurable via RPS for MAP. During the lockout any request will return code 401 for attacking IP.
- In case of negative response codes, the client side should provide request and response logging to a file, with milliseconds timestamps, to support further analyses.
- In case of interface errors or unexpected behaviour, the client side must provide request and response logging to a file, with milliseconds timestamps, e.g. activated by a client side debug level.
- The MAP panel itself logs all database modifications, per default, to the history.log, what is strongly limited in number of entries and content.
- The MAP panel itself does not log all HTTPS request and responses because of file system limitations.
- TCP keepalive is enabled, lost connections will be dropped after 25 seconds.


## HTTPS server limitations

Due to limited resources, MAP system generally does not process HTTPS requests simultaneously.

However, there are exceptions that are processed simultaneously:
- **/syncstatus**
- **/panel**
- **/sub**
- **/sub/\\***
- **/history**

All other URLs are executed sequentially.

Requests are queued and executed once execution units are available.

Simultaneous execution is limited to 3 simultaneous requests, processing time will be slower for multiple simultaneous requests.

Overloading REST-API can make MAP less responsive, in case of overload, the REST-API will generally respond with HTTP code 503, or, in case of heavy overload, will immediately close TCP socket without any response.



## Response time guarantees

The following URLs have a guaranteed time, only if one HTTPS client connection at the same time.

The following URLs are guaranteed to execute their requests within 120 seconds:
- **/history**
- **/supportfile**
- **/points**
- **/couplers**
- **/lsnauxs**

The following URLs are guaranteed to execute their requests within 60 seconds:
- **/network**
- **/syncstatus**
- **/usermodellist**
- **/outputs**
- **/user**
- **/mains**
- **/groundfaults**

All other REST-API requests are guaranteed to be executed within 10 seconds.

## License

Following URLs are only accessible with a valid MUM software license and only with a MAP-COM panel:
- usermodel
- usermodel/*
- usermodellist
- daymodel
- daymodel/*
- daymodellist
- timemodel
- timemodel/*
- timemodellist
- specialdaymodel
- specialdaymodel/*
- specialdaymodellist
- smartkeymodel
- smartkeymodel/*
- smartkeymodellist
- areaandtimemodel
- areaandtimemodel/*
- areaandtimemodellist
- accessmodel
- accessmodel/*
- accessmodellist
- permissionmodel
- permissionmodel/*
- permissionmodellist
- mumusergroup
- sharedkey
- statistics
- statistics/oii
- statistics/db

Missing license will lead to HTTP 403 plain-text response, for example \"License missing MUM/usermodel\"

## Security

Supported cipher suites:

**TLS1.3** (**recommended**)
- TLS_AES_256_GCM_SHA384
- TLS_CHACHA20_POLY1305_SHA256
- TLS_AES_128_GCM_SHA256

**TLS1.2**
- ECDHE-RSA-AES128-SHA256
- ECDHE-RSA-AES128-GCM-SHA256
- ECDHE-RSA-AES256-SHA384
- ECDHE-RSA-AES256-GCM-SHA384
- DHE-RSA-AES128-SHA256
- DHE-RSA-AES128-GCM-SHA256
- DHE-RSA-AES256-SHA256
- DHE-RSA-AES256-GCM-SHA384
- DHE-RSA-AES128-SHA

**TLS1.0** (**deprecated**! Not recommended to be used, has to be manually enabled in MAP panel configuration via RPS for MAP)
- AES128-SHA
- AES256-SHA

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.4.0272, 18.09.2024
- Package version: 1.0.0
- Generator version: 7.17.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.boschsecurity.com/xc/en/extranet/map-partners/](https://www.boschsecurity.com/xc/en/extranet/map-partners/)

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import bosch_alarm_map
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bosch_alarm_map
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import bosch_alarm_map
from bosch_alarm_map.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://169.254.10.10
# See configuration.py for a list of all supported configuration parameters.
configuration = bosch_alarm_map.Configuration(
    host = "https://169.254.10.10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.


# Enter a context with an instance of the API client
with bosch_alarm_map.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bosch_alarm_map.DEModuleSIIDApi(api_client)
    de_module_siid = '/1.1.Gateway.15001.1' # str | Unique DEModule SIID

    try:
        # DE Module of the MAP system
        api_response = api_instance.get_de_module_siid(de_module_siid)
        print("The response of DEModuleSIIDApi->get_de_module_siid:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DEModuleSIIDApi->get_de_module_siid: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://169.254.10.10*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DEModuleSIIDApi* | [**get_de_module_siid**](docs/DEModuleSIIDApi.md#get_de_module_siid) | **GET** /{DEModule_SIID} | DE Module of the MAP system
*DEModuleSIIDApi* | [**post_de_module_siid**](docs/DEModuleSIIDApi.md#post_de_module_siid) | **POST** /{DEModule_SIID} | Enable/disable, get firmware version
*AccessmodelApi* | [**get_accessmodel**](docs/AccessmodelApi.md#get_accessmodel) | **GET** /accessmodel/{AccessModelID} | Get a specific accessmodel from the MAP system
*AccessmodelApi* | [**post_accessmodel**](docs/AccessmodelApi.md#post_accessmodel) | **POST** /accessmodel | Create a new access model on the MAP system
*AccessmodellistApi* | [**get_accessmodellist**](docs/AccessmodellistApi.md#get_accessmodellist) | **GET** /accessmodellist | Get all access models of the MAP system
*AccessmodellistApi* | [**postaccessmodellist**](docs/AccessmodellistApi.md#postaccessmodellist) | **POST** /accessmodellist | Get list of access models that were changed after specified syncID
*AreaSIIDApi* | [**get_area_siid**](docs/AreaSIIDApi.md#get_area_siid) | **GET** /{area_SIID} | Status retrieval of an individual area
*AreaSIIDApi* | [**post_area_siid**](docs/AreaSIIDApi.md#post_area_siid) | **POST** /{area_SIID} | Control individual area
*AreaandtimemodelApi* | [**get_areaandtimemodel**](docs/AreaandtimemodelApi.md#get_areaandtimemodel) | **GET** /areaandtimemodel/{AreaAndTimeModelID} | Get a specific area and time model from the MAP system
*AreaandtimemodelApi* | [**post_areaandtimemodel**](docs/AreaandtimemodelApi.md#post_areaandtimemodel) | **POST** /areaandtimemodel | Create, modify or delete an area and time model on the MAP system
*AreaandtimemodellistApi* | [**get_areaandtimemodellist**](docs/AreaandtimemodellistApi.md#get_areaandtimemodellist) | **GET** /areaandtimemodellist | Get all area and time models of the MAP system
*AreaandtimemodellistApi* | [**postareaandtimemodellist**](docs/AreaandtimemodellistApi.md#postareaandtimemodellist) | **POST** /areaandtimemodellist | Get list of area and time models that were changed after specified syncID
*AreasApi* | [**get_areas**](docs/AreasApi.md#get_areas) | **GET** /areas | List of all areas configured in the MAP system
*AreasApi* | [**post_areas**](docs/AreasApi.md#post_areas) | **POST** /areas | Operation to multiple areas at the same time: 
*BatteriesApi* | [**get_batteries**](docs/BatteriesApi.md#get_batteries) | **GET** /batteries | List of batteries in the MAP system
*BatteriesApi* | [**post_batteries**](docs/BatteriesApi.md#post_batteries) | **POST** /batteries | Enable/Disable, Bypass/Unbypass all batteries
*BatterySIIDApi* | [**get_battery_siid**](docs/BatterySIIDApi.md#get_battery_siid) | **GET** /{battery_SIID} | Individual battery in the MAP system
*BatterySIIDApi* | [**post_battery_siid**](docs/BatterySIIDApi.md#post_battery_siid) | **POST** /{battery_SIID} | Enable/Disable, Bypass/Unbypass individual battery
*BatterychargerSIIDApi* | [**get_batterycharger_siid**](docs/BatterychargerSIIDApi.md#get_batterycharger_siid) | **GET** /{batterycharger_SIID} | Individual battery charger
*BatterychargerSIIDApi* | [**post_batterycharger_siid**](docs/BatterychargerSIIDApi.md#post_batterycharger_siid) | **POST** /{batterycharger_SIID} | Enable/Disable a batterycharger
*BatterychargersApi* | [**get_batterychargers**](docs/BatterychargersApi.md#get_batterychargers) | **GET** /batterychargers | List of battery chargers in the MAP system
*BatterychargersApi* | [**post_batterychargers**](docs/BatterychargersApi.md#post_batterychargers) | **POST** /batterychargers | Enable/Disable all battery chargers
*BlocklockSIIDApi* | [**get_blocklock_siid**](docs/BlocklockSIIDApi.md#get_blocklock_siid) | **GET** /{blocklock_SIID} | Individual blocklock device
*BlocklockSIIDApi* | [**post_blocklock_siid**](docs/BlocklockSIIDApi.md#post_blocklock_siid) | **POST** /{blocklock_SIID} | Enable/Disable a blocklock
*BlocklocksApi* | [**get_blocklocks**](docs/BlocklocksApi.md#get_blocklocks) | **GET** /blocklocks | List of blocklocks
*BlocklocksApi* | [**post_blocklocks**](docs/BlocklocksApi.md#post_blocklocks) | **POST** /blocklocks | Enable/Disable all blocklocks
*CommunicatorSIIDApi* | [**getcommunicator_siid**](docs/CommunicatorSIIDApi.md#getcommunicator_siid) | **GET** /{communicator_SIID} | Get information from a unique Communicator
*ConfigApi* | [**get_confic**](docs/ConfigApi.md#get_confic) | **GET** /config | View MAP system configuration
*CouplerSIIDApi* | [**get_coupler_siid**](docs/CouplerSIIDApi.md#get_coupler_siid) | **GET** /{coupler_SIID} | Individual coupler
*CouplerSIIDApi* | [**post_coupler_siid**](docs/CouplerSIIDApi.md#post_coupler_siid) | **POST** /{coupler_SIID} | Enable/Disable a coupler
*CouplersApi* | [**get_couplers**](docs/CouplersApi.md#get_couplers) | **GET** /couplers | List of couplers in the MAP system
*CouplersApi* | [**post_couplers**](docs/CouplersApi.md#post_couplers) | **POST** /couplers | Enable/Disable all couplers
*DaymodelApi* | [**get_daymodel**](docs/DaymodelApi.md#get_daymodel) | **GET** /daymodel/{dayModelID} | Get a specific daymodel item from the MAP system
*DaymodelApi* | [**post_day_model**](docs/DaymodelApi.md#post_day_model) | **POST** /daymodel | Create, modify or delete a day model on the MAP System
*DaymodellistApi* | [**get_daymodellist**](docs/DaymodellistApi.md#get_daymodellist) | **GET** /daymodellist | Get a list of all day models
*DaymodellistApi* | [**postdaymodellist**](docs/DaymodellistApi.md#postdaymodellist) | **POST** /daymodellist | Get list of day models that were changed after specified syncID
*DescApi* | [**getdesc**](docs/DescApi.md#getdesc) | **GET** /desc | Descriptive information
*DeviceSIIDApi* | [**get_device_siid**](docs/DeviceSIIDApi.md#get_device_siid) | **GET** /{device_SIID} | Individual device
*DeviceSIIDApi* | [**postdevice_siid**](docs/DeviceSIIDApi.md#postdevice_siid) | **POST** /{device_SIID} | Enable/Disable a device
*DevicesApi* | [**getdevices**](docs/DevicesApi.md#getdevices) | **GET** /devices | List of all devices configured in the MAP system.
*FireDetectorSIIDApi* | [**firedetector_siid**](docs/FireDetectorSIIDApi.md#firedetector_siid) | **POST** /{fireDetector_SIID} | Enable/Disable a fireDetector
*FireDetectorSIIDApi* | [**get_firedetector**](docs/FireDetectorSIIDApi.md#get_firedetector) | **GET** /{fireDetector_SIID} | Individual fire detector
*FireDetectorsApi* | [**getfire_detectors**](docs/FireDetectorsApi.md#getfire_detectors) | **GET** /fireDetectors | List of fire detectors in the MAP system
*FireDetectorsApi* | [**postfire_detectors**](docs/FireDetectorsApi.md#postfire_detectors) | **POST** /fireDetectors | Enable/Disable all fireDetectors
*GroundfaultSIIDApi* | [**get_groundfault_siid**](docs/GroundfaultSIIDApi.md#get_groundfault_siid) | **GET** /{groundfault_SIID} | Individual ground fault resource
*GroundfaultSIIDApi* | [**post_groundfault_siid**](docs/GroundfaultSIIDApi.md#post_groundfault_siid) | **POST** /{groundfault_SIID} | Enable/Disable a groundfault
*GroundfaultsApi* | [**get_groundfaults**](docs/GroundfaultsApi.md#get_groundfaults) | **GET** /groundfaults | List of resources representing the ground faults of a power supply in the MAP system
*GroundfaultsApi* | [**post_groundfaults**](docs/GroundfaultsApi.md#post_groundfaults) | **POST** /groundfaults | Enable/Disable all groundfaults
*HistoryApi* | [**get_history**](docs/HistoryApi.md#get_history) | **GET** /history | The history log consists of events in the MAP panel configured to be logged.
*IncApi* | [**get_inc**](docs/IncApi.md#get_inc) | **GET** /inc | List of all incidents in the MAP
*IncApi* | [**post_inc**](docs/IncApi.md#post_inc) | **POST** /inc | Handle, or silence a list of incidents
*InfrastructureApi* | [**getinfrastructure**](docs/InfrastructureApi.md#getinfrastructure) | **GET** /infrastructure | Get complete MAP device infrastructure
*InfrastructureApi* | [**getinfrastructurebysiid**](docs/InfrastructureApi.md#getinfrastructurebysiid) | **GET** /infrastructure/{DeviceSIID} | Get MAP device infrastructure starting from SIID
*InternalprogramSIIDApi* | [**get_internalprogram_siid**](docs/InternalprogramSIIDApi.md#get_internalprogram_siid) | **GET** /{internalprogram_SIID} | Individual internal program (1 to 14).
*InternalprogramSIIDApi* | [**post_interprogram_siid**](docs/InternalprogramSIIDApi.md#post_interprogram_siid) | **POST** /{internalprogram_SIID} | Activate/Deactivate specified internal program
*InternalprogramsApi* | [**get_internalprograms**](docs/InternalprogramsApi.md#get_internalprograms) | **GET** /internalprograms | List all internal programs configured. 
*InternalprogramsApi* | [**post_internalprograms**](docs/InternalprogramsApi.md#post_internalprograms) | **POST** /internalprograms | Activate/Deactivate all internal programs
*IpchistoryApi* | [**get_ipchistory**](docs/IpchistoryApi.md#get_ipchistory) | **GET** /ipchistory | Get PCHistory (IP Communicator History) Log
*KeypadSIIDApi* | [**get_keypad_siid**](docs/KeypadSIIDApi.md#get_keypad_siid) | **GET** /{keypad_SIID} | Individual keypad
*KeypadSIIDApi* | [**post_keypad_siid**](docs/KeypadSIIDApi.md#post_keypad_siid) | **POST** /{keypad_SIID} | Enable/Disable, Activate/Deactivate, get firmware Version of a Keypad
*KeypadsApi* | [**get_keypads**](docs/KeypadsApi.md#get_keypads) | **GET** /keypads | List of Keypads in the system
*KeypadsApi* | [**post_keypads**](docs/KeypadsApi.md#post_keypads) | **POST** /keypads | Enable/Disable, Activate/Deactivate all Keypads
*KeyswitchSIIDApi* | [**getkeyswitch_siid**](docs/KeyswitchSIIDApi.md#getkeyswitch_siid) | **GET** /{keyswitch_SIID} | Individual keyswitch
*KeyswitchSIIDApi* | [**post_keyswitch_siid**](docs/KeyswitchSIIDApi.md#post_keyswitch_siid) | **POST** /{keyswitch_SIID} | Enable/Disable a keyswitch
*KeyswitchesApi* | [**get_keyswitches**](docs/KeyswitchesApi.md#get_keyswitches) | **GET** /keyswitches | List of keyswitches in the MAP system
*LsnApi* | [**get_lsngw_config**](docs/LsnApi.md#get_lsngw_config) | **GET** /lsn | Get current LSN configuration
*LsnApi* | [**post_lsngw_config**](docs/LsnApi.md#post_lsngw_config) | **POST** /lsn | Create, modify or delete a LSN Gateway configuration
*LsnGatewaySIIDApi* | [**get_lsn_gateway_siid**](docs/LsnGatewaySIIDApi.md#get_lsn_gateway_siid) | **GET** /{lsnGateway_SIID} | Individual LSN gateway
*LsnGatewaySIIDApi* | [**postlsn_gateway_siid**](docs/LsnGatewaySIIDApi.md#postlsn_gateway_siid) | **POST** /{lsnGateway_SIID} | Enable/Disable, get Firmware Version of a lsnGateway
*LsnGatewaysApi* | [**getlsn_gateways**](docs/LsnGatewaysApi.md#getlsn_gateways) | **GET** /lsnGateways | List of LSN gateways in the MAP system
*LsnGatewaysApi* | [**postlsn_gateways**](docs/LsnGatewaysApi.md#postlsn_gateways) | **POST** /lsnGateways | Enable/Disable, Activate/Deactivate all lsnGateways
*LsnauxSIIDApi* | [**get_lsnaux_siid**](docs/LsnauxSIIDApi.md#get_lsnaux_siid) | **GET** /{lsnaux_SIID} | Individual LSN aux
*LsnauxSIIDApi* | [**post_lsnaus_siid**](docs/LsnauxSIIDApi.md#post_lsnaus_siid) | **POST** /{lsnaux_SIID} | Enable/Disable a lsnaux
*LsnauxsApi* | [**get_lsnauxs**](docs/LsnauxsApi.md#get_lsnauxs) | **GET** /lsnauxs | List of LSN auxiliary power outlets in the MAP system
*LsnauxsApi* | [**post_lsnauxs**](docs/LsnauxsApi.md#post_lsnauxs) | **POST** /lsnauxs | Enable/Disable all lsnauxs
*LsnbusSIIDApi* | [**get_lsnbus_siid**](docs/LsnbusSIIDApi.md#get_lsnbus_siid) | **GET** /{lsnbus_SIID} | Individual LSN Bus
*LsnbusSIIDApi* | [**post_lsnbus_siid**](docs/LsnbusSIIDApi.md#post_lsnbus_siid) | **POST** /{lsnbus_SIID} | Enable/Disable a LSN Bus
*LsnbusesApi* | [**get_lsnbuses**](docs/LsnbusesApi.md#get_lsnbuses) | **GET** /lsnbuses | List of LSN Buses (loops and stubs) in the MAP system
*LsnbusesApi* | [**post_lsnbuses**](docs/LsnbusesApi.md#post_lsnbuses) | **POST** /lsnbuses | Enable/Disable all LSN Buses
*MainSIIDApi* | [**get_main_siid**](docs/MainSIIDApi.md#get_main_siid) | **GET** /{main_SIID} | Individual main resource
*MainSIIDApi* | [**post_main_siid**](docs/MainSIIDApi.md#post_main_siid) | **POST** /{main_SIID} | Enable/Disable a main
*MainsApi* | [**get_mains**](docs/MainsApi.md#get_mains) | **GET** /mains | Get list of all alternating current (short: ac ) power supplies 
*MainsApi* | [**post_mains**](docs/MainsApi.md#post_mains) | **POST** /mains | Enable/Disable all mains
*MumusergroupApi* | [**getmumusergroup**](docs/MumusergroupApi.md#getmumusergroup) | **GET** /mumusergroup | Get MUM property for all User IDs
*MumusergroupApi* | [**postmumusergroup**](docs/MumusergroupApi.md#postmumusergroup) | **POST** /mumusergroup | Set MUM property to a set of User IDs 
*NetworkApi* | [**get_network**](docs/NetworkApi.md#get_network) | **GET** /network | Inspect network settings
*NetworkApi* | [**post_network**](docs/NetworkApi.md#post_network) | **POST** /network | Activate/Deactivate DHCP, set IP Address of the MAP panel
*NtpApi* | [**get_ntp**](docs/NtpApi.md#get_ntp) | **GET** /ntp | Get NTP state
*NtpApi* | [**post_ntp**](docs/NtpApi.md#post_ntp) | **POST** /ntp | Configure NTP
*OutputSIIDApi* | [**get_output_siid**](docs/OutputSIIDApi.md#get_output_siid) | **GET** /{output_SIID} | Individual output
*OutputSIIDApi* | [**post_output_siid**](docs/OutputSIIDApi.md#post_output_siid) | **POST** /{output_SIID} | Enable/Disable an output
*OutputsApi* | [**get_outputs**](docs/OutputsApi.md#get_outputs) | **GET** /outputs | List of all outputs
*OutputsApi* | [**post_outputs**](docs/OutputsApi.md#post_outputs) | **POST** /outputs | Enable/Disable all outputs
*PanelApi* | [**get_panel**](docs/PanelApi.md#get_panel) | **GET** /panel | Current MAP panel status
*PanelApi* | [**post_panel**](docs/PanelApi.md#post_panel) | **POST** /panel | Restart the device over REST-API interface.
*PermissionmodelApi* | [**get_permissionmodel**](docs/PermissionmodelApi.md#get_permissionmodel) | **GET** /permissionmodel/{PermissionModelID} | Get a specific permission model from the MAP system
*PermissionmodelApi* | [**post_permisionmodel**](docs/PermissionmodelApi.md#post_permisionmodel) | **POST** /permissionmodel | Create a new permission model on the MAP system
*PermissionmodellistApi* | [**get_permissionmodellist**](docs/PermissionmodellistApi.md#get_permissionmodellist) | **GET** /permissionmodellist | Get all permission models of the MAP system
*PermissionmodellistApi* | [**postpermissionmodellist**](docs/PermissionmodellistApi.md#postpermissionmodellist) | **POST** /permissionmodellist | Get list of permission models that were changed after specified syncID
*PointSIIDApi* | [**get_point_siid**](docs/PointSIIDApi.md#get_point_siid) | **GET** /{point_SIID} | Individual point
*PointSIIDApi* | [**post_point_siid**](docs/PointSIIDApi.md#post_point_siid) | **POST** /{point_SIID} | Enable/Disable  point
*PointsApi* | [**get_points**](docs/PointsApi.md#get_points) | **GET** /points | List of points in the system
*PointsApi* | [**post_points**](docs/PointsApi.md#post_points) | **POST** /points | Enable/Disable all points
*PowerDeviceSIIDApi* | [**getpower_device_siid**](docs/PowerDeviceSIIDApi.md#getpower_device_siid) | **GET** /{powerDevice_SIID} | Individual non BDB power device
*PowerDevicesApi* | [**get_power_devices**](docs/PowerDevicesApi.md#get_power_devices) | **GET** /powerDevices | List of all non BDB power supplies
*PowerSuppliesApi* | [**get_powersupplies**](docs/PowerSuppliesApi.md#get_powersupplies) | **GET** /powerSupplies | List of all MAP power supplies
*PowerSuppliesApi* | [**post_powersupplies**](docs/PowerSuppliesApi.md#post_powersupplies) | **POST** /powerSupplies | Parametrize all MAP system power supplies
*PowerSupplySIIDApi* | [**get_posersupply_siid**](docs/PowerSupplySIIDApi.md#get_posersupply_siid) | **GET** /{powerSupply_SIID} | Individual powersupply
*PowerSupplySIIDApi* | [**post_powersupply_siid**](docs/PowerSupplySIIDApi.md#post_powersupply_siid) | **POST** /{powerSupply_SIID} | Parametrize a MAP system power supply
*PrinterSIIDApi* | [**get_printer_siid**](docs/PrinterSIIDApi.md#get_printer_siid) | **GET** /printer_SIID/{printer_SIID} | Printer of the MAP
*PrinterSIIDApi* | [**post_printer_siid**](docs/PrinterSIIDApi.md#post_printer_siid) | **POST** /printer_SIID/{printer_SIID} | Enable/Disable a printer
*PsCanOpListApi* | [**get_ps_can_op_list**](docs/PsCanOpListApi.md#get_ps_can_op_list) | **GET** /psCanOpList | List of power supply CAN outputs
*PsCanOpSIIDApi* | [**get_ps_can_op_siid**](docs/PsCanOpSIIDApi.md#get_ps_can_op_siid) | **GET** /{psCanOp_SIID} | Power supply CAN-Bus
*SharedkeyApi* | [**getsharedkey**](docs/SharedkeyApi.md#getsharedkey) | **GET** /sharedkey | Get Shared Key
*SharedkeyApi* | [**postsharedkey**](docs/SharedkeyApi.md#postsharedkey) | **POST** /sharedkey | Manage Shared Key 
*SmartkeySIIDApi* | [**get_smartkey_siid**](docs/SmartkeySIIDApi.md#get_smartkey_siid) | **GET** /{smartkey_SIID} | Get individual information of one Smartkey device.
*SmartkeySIIDApi* | [**post_smartkey_siid**](docs/SmartkeySIIDApi.md#post_smartkey_siid) | **POST** /{smartkey_SIID} | Enable/Disable a Smartkey
*SmartkeymodelApi* | [**get_smartkeymodel**](docs/SmartkeymodelApi.md#get_smartkeymodel) | **GET** /smartkeymodel/{SmartkeyModelID} | Get a specific Smartkey model from the MAP system
*SmartkeymodelApi* | [**post_smartkeymodel**](docs/SmartkeymodelApi.md#post_smartkeymodel) | **POST** /smartkeymodel | Create a new Smartkey model on the MAP System
*SmartkeymodellistApi* | [**get_smartkeymodellist**](docs/SmartkeymodellistApi.md#get_smartkeymodellist) | **GET** /smartkeymodellist | Get all Smartkey models of the MAP system
*SmartkeymodellistApi* | [**post_smartkeymodellist**](docs/SmartkeymodellistApi.md#post_smartkeymodellist) | **POST** /smartkeymodellist | Get list of Smartkey models that were changed after specified syncID
*SmartkeysApi* | [**get_smartkeys**](docs/SmartkeysApi.md#get_smartkeys) | **GET** /smartkeys | List of Smartkeys
*SmartkeysApi* | [**post_smartkeys**](docs/SmartkeysApi.md#post_smartkeys) | **POST** /smartkeys | Enable/Disable all Smartkeys
*SpecialdaymodelApi* | [**get_specialdaymodel**](docs/SpecialdaymodelApi.md#get_specialdaymodel) | **GET** /specialdaymodel/{SpecialDayModelID} | Get a special day model from the MAP system
*SpecialdaymodelApi* | [**post_specialdaymodel**](docs/SpecialdaymodelApi.md#post_specialdaymodel) | **POST** /specialdaymodel | Create modify or delete a special day Model on the MAP system
*SpecialdaymodellistApi* | [**get_specialdaymodellist**](docs/SpecialdaymodellistApi.md#get_specialdaymodellist) | **GET** /specialdaymodellist | Get all special day models of the MAP system
*SpecialdaymodellistApi* | [**postspecialdaymodellist**](docs/SpecialdaymodellistApi.md#postspecialdaymodellist) | **POST** /specialdaymodellist | Get list of special day models that were changed after specified syncID
*StatisticsApi* | [**getstatistics**](docs/StatisticsApi.md#getstatistics) | **GET** /statistics | Get MAP internal statistics
*SubApi* | [**get_sub**](docs/SubApi.md#get_sub) | **GET** /sub | List current event subscriptions
*SubApi* | [**post_sub**](docs/SubApi.md#post_sub) | **POST** /sub | Create a subscription
*SubSIIDApi* | [**delete_sub_siid**](docs/SubSIIDApi.md#delete_sub_siid) | **DELETE** /sub/{sub_SIID} | Unsubscribe
*SubSIIDApi* | [**get_sub_siid**](docs/SubSIIDApi.md#get_sub_siid) | **GET** /sub/{sub_SIID} | Individual subscription resource
*SubSIIDApi* | [**post_sub_siid**](docs/SubSIIDApi.md#post_sub_siid) | **POST** /sub/{sub_SIID} | Fetch events
*SupervisedConnsApi* | [**get_supervised_conns**](docs/SupervisedConnsApi.md#get_supervised_conns) | **GET** /supervisedConns | List of Connections to other systems.
*SupervisedConnsSIIDApi* | [**get_supervised_conns_siid**](docs/SupervisedConnsSIIDApi.md#get_supervised_conns_siid) | **GET** /{supervisedConns_SIID} | Individual supervised connection
*SupervisedConnsSIIDApi* | [**post_supervised_conns**](docs/SupervisedConnsSIIDApi.md#post_supervised_conns) | **POST** /{supervisedConns_SIID} | Enable Connections to other systems.
*SupportfileApi* | [**getsupportfile**](docs/SupportfileApi.md#getsupportfile) | **GET** /supportfile | Download MAP panel supportfiles
*SyncstatusApi* | [**get_syncstatus**](docs/SyncstatusApi.md#get_syncstatus) | **GET** /syncstatus | Get all synchronization IDs
*TimeApi* | [**get_time**](docs/TimeApi.md#get_time) | **GET** /time | Get System Time
*TimeApi* | [**post_time**](docs/TimeApi.md#post_time) | **POST** /time | Set System Time
*TimemodelApi* | [**get_timemodel**](docs/TimemodelApi.md#get_timemodel) | **GET** /timemodel/{timeModelID} | Get a specific timemodel item from the MAP system.
*TimemodelApi* | [**post_timemodel**](docs/TimemodelApi.md#post_timemodel) | **POST** /timemodel | Create, modify or delete a new Time Model on the MAP System
*TimemodellistApi* | [**get_timemodellist**](docs/TimemodellistApi.md#get_timemodellist) | **GET** /timemodellist | Get all time models of the MAP system
*TimemodellistApi* | [**posttimemodellist**](docs/TimemodellistApi.md#posttimemodellist) | **POST** /timemodellist | Get list of time models that were changed after specified syncID
*UserApi* | [**get_user_id**](docs/UserApi.md#get_user_id) | **GET** /user/{userID} | Specific user configuration
*UserApi* | [**post_user_id**](docs/UserApi.md#post_user_id) | **POST** /user/{userID} | Activate or Deactivate a specific user on system
*UsermodelApi* | [**get_usermodel_by_id**](docs/UsermodelApi.md#get_usermodel_by_id) | **GET** /usermodel/{id} | Get all parameters of specific user from MAP system
*UsermodelApi* | [**post_usermodel**](docs/UsermodelApi.md#post_usermodel) | **POST** /usermodel | Create, modify or delete a user on the MAP system
*UsermodellistApi* | [**get_usermodellist**](docs/UsermodellistApi.md#get_usermodellist) | **GET** /usermodellist | Get a list of all users
*UsermodellistApi* | [**post_usermodellist**](docs/UsermodellistApi.md#post_usermodellist) | **POST** /usermodellist | Get only all user modifications, related to previous userModelSyncID
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users | Get a list with all user configs from system
*UsersApi* | [**post_users**](docs/UsersApi.md#post_users) | **POST** /users | Activate or Deactivate a set of users on system
*WalktestSIIDApi* | [**delete_walktest_siid**](docs/WalktestSIIDApi.md#delete_walktest_siid) | **DELETE** /walktest/{walktest_SIID} | Stop Walktest
*WalktestSIIDApi* | [**get_walktest_siid**](docs/WalktestSIIDApi.md#get_walktest_siid) | **GET** /walktest/{walktest_SIID} | Individual walktest
*WalktestSIIDApi* | [**post_walktest_siid**](docs/WalktestSIIDApi.md#post_walktest_siid) | **POST** /walktest/{walktest_SIID} | Walktest diagnose
*WalktestsApi* | [**delete_walktests**](docs/WalktestsApi.md#delete_walktests) | **DELETE** /walktests | Stop all Walktests
*WalktestsApi* | [**get_walktests**](docs/WalktestsApi.md#get_walktests) | **GET** /walktests | Show all active walktests


## Documentation For Models

 - [AccessModel](docs/AccessModel.md)
 - [AccessModelID](docs/AccessModelID.md)
 - [AccessModelList](docs/AccessModelList.md)
 - [AccessModelListAllOfListInner](docs/AccessModelListAllOfListInner.md)
 - [AccessModelSyncID](docs/AccessModelSyncID.md)
 - [AccessModelistPost](docs/AccessModelistPost.md)
 - [Area](docs/Area.md)
 - [AreaAndTimeModel](docs/AreaAndTimeModel.md)
 - [AreaAndTimeModelID](docs/AreaAndTimeModelID.md)
 - [AreaAndTimeModelList](docs/AreaAndTimeModelList.md)
 - [AreaAndTimeModelListAllOfListInner](docs/AreaAndTimeModelListAllOfListInner.md)
 - [AreaAndTimeModelSyncID](docs/AreaAndTimeModelSyncID.md)
 - [AreaAndTimeModellistPost](docs/AreaAndTimeModellistPost.md)
 - [AreaArm](docs/AreaArm.md)
 - [AreaConfiguration](docs/AreaConfiguration.md)
 - [AreaDisarm](docs/AreaDisarm.md)
 - [AreaList](docs/AreaList.md)
 - [AreaPostResponses](docs/AreaPostResponses.md)
 - [AreaWalktestStarted](docs/AreaWalktestStarted.md)
 - [ArmingInfo](docs/ArmingInfo.md)
 - [ArmingInfoWhyNotReadyToArm](docs/ArmingInfoWhyNotReadyToArm.md)
 - [ArmingInfoWhyNotReadyToDisarm](docs/ArmingInfoWhyNotReadyToDisarm.md)
 - [ArmingInfoWhyNotReadyToForceArm](docs/ArmingInfoWhyNotReadyToForceArm.md)
 - [Battery](docs/Battery.md)
 - [BatteryList](docs/BatteryList.md)
 - [Batterycharger](docs/Batterycharger.md)
 - [BatterychargerList](docs/BatterychargerList.md)
 - [BellTestStart](docs/BellTestStart.md)
 - [Blocklock](docs/Blocklock.md)
 - [BlocklockList](docs/BlocklockList.md)
 - [ChimeModeStartStop](docs/ChimeModeStartStop.md)
 - [Command](docs/Command.md)
 - [Communicator](docs/Communicator.md)
 - [Config](docs/Config.md)
 - [Coupler](docs/Coupler.md)
 - [CouplerList](docs/CouplerList.md)
 - [CreateSub](docs/CreateSub.md)
 - [CreatedSub](docs/CreatedSub.md)
 - [DEModule](docs/DEModule.md)
 - [DayModel](docs/DayModel.md)
 - [DayModelID](docs/DayModelID.md)
 - [DayModelList](docs/DayModelList.md)
 - [DayModelListAllOfListInner](docs/DayModelListAllOfListInner.md)
 - [DayModelSyncID](docs/DayModelSyncID.md)
 - [DayModellistPost](docs/DayModellistPost.md)
 - [Desc](docs/Desc.md)
 - [DescMainResourcesInner](docs/DescMainResourcesInner.md)
 - [Device](docs/Device.md)
 - [DeviceActivateDeactivate](docs/DeviceActivateDeactivate.md)
 - [DeviceBypassUnbypass](docs/DeviceBypassUnbypass.md)
 - [DeviceConfiguration](docs/DeviceConfiguration.md)
 - [DeviceEnableDisable](docs/DeviceEnableDisable.md)
 - [DeviceFwVersion](docs/DeviceFwVersion.md)
 - [DeviceOnOff](docs/DeviceOnOff.md)
 - [DeviceOpState](docs/DeviceOpState.md)
 - [DeviceUpdate](docs/DeviceUpdate.md)
 - [DeviceWalktest](docs/DeviceWalktest.md)
 - [DevicefirmwareVersion](docs/DevicefirmwareVersion.md)
 - [DevicesList](docs/DevicesList.md)
 - [Diagnose](docs/Diagnose.md)
 - [DiagnoseResponse](docs/DiagnoseResponse.md)
 - [Error400](docs/Error400.md)
 - [Error409](docs/Error409.md)
 - [Evt](docs/Evt.md)
 - [Evts](docs/Evts.md)
 - [FetchEvents](docs/FetchEvents.md)
 - [FetchedEvents](docs/FetchedEvents.md)
 - [FireDetector](docs/FireDetector.md)
 - [FireDetectorList](docs/FireDetectorList.md)
 - [FireDetectorTestedSensorsInner](docs/FireDetectorTestedSensorsInner.md)
 - [GetAccessmodel200Response](docs/GetAccessmodel200Response.md)
 - [GetAreaandtimemodel200Response](docs/GetAreaandtimemodel200Response.md)
 - [GetDaymodel200Response](docs/GetDaymodel200Response.md)
 - [GetPermissionmodel200Response](docs/GetPermissionmodel200Response.md)
 - [GetSmartkeymodel200Response](docs/GetSmartkeymodel200Response.md)
 - [GetSpecialdaymodel200Response](docs/GetSpecialdaymodel200Response.md)
 - [GetSupervisedConnsSIID200Response](docs/GetSupervisedConnsSIID200Response.md)
 - [GetTimemodel200Response](docs/GetTimemodel200Response.md)
 - [GetUsermodelById200Response](docs/GetUsermodelById200Response.md)
 - [GetarmingInfo](docs/GetarmingInfo.md)
 - [Groundfault](docs/Groundfault.md)
 - [GroundfaultList](docs/GroundfaultList.md)
 - [HandlingState](docs/HandlingState.md)
 - [History](docs/History.md)
 - [Inc](docs/Inc.md)
 - [IncList](docs/IncList.md)
 - [IncidentResource](docs/IncidentResource.md)
 - [Infrastructure](docs/Infrastructure.md)
 - [InfrastructureDevice](docs/InfrastructureDevice.md)
 - [InfrastructureDeviceGenericProperty](docs/InfrastructureDeviceGenericProperty.md)
 - [InfrastructureDeviceProperties](docs/InfrastructureDeviceProperties.md)
 - [InfrastructureDeviceRPSProperty](docs/InfrastructureDeviceRPSProperty.md)
 - [InfrastructureDeviceSIType](docs/InfrastructureDeviceSIType.md)
 - [InternalProgram](docs/InternalProgram.md)
 - [InternalProgramIpArmingInfo](docs/InternalProgramIpArmingInfo.md)
 - [InternalProgramList](docs/InternalProgramList.md)
 - [InternalProgramsConfiguration](docs/InternalProgramsConfiguration.md)
 - [IpArmingInfo](docs/IpArmingInfo.md)
 - [Keypad](docs/Keypad.md)
 - [KeypadList](docs/KeypadList.md)
 - [Keyswitch](docs/Keyswitch.md)
 - [Keyswitchlist](docs/Keyswitchlist.md)
 - [LSNAntimaskSensitivityDetectionRangeProperty](docs/LSNAntimaskSensitivityDetectionRangeProperty.md)
 - [LSNAntimaskSensitivityProperty](docs/LSNAntimaskSensitivityProperty.md)
 - [LSNDetectorSensitivityProperty](docs/LSNDetectorSensitivityProperty.md)
 - [LSNEMK36Configuration](docs/LSNEMK36Configuration.md)
 - [LSNEMK36ConfigurationAnyOf](docs/LSNEMK36ConfigurationAnyOf.md)
 - [LSNEMK36SConfiguration](docs/LSNEMK36SConfiguration.md)
 - [LSNGWAUXConfiguration](docs/LSNGWAUXConfiguration.md)
 - [LSNGWConfiguration](docs/LSNGWConfiguration.md)
 - [LSNGWConfigurationCreatePost](docs/LSNGWConfigurationCreatePost.md)
 - [LSNGWConfigurationDeletePost](docs/LSNGWConfigurationDeletePost.md)
 - [LSNGWLoopConfiguration](docs/LSNGWLoopConfiguration.md)
 - [LSNGWLoopConfigurationDevicesInner](docs/LSNGWLoopConfigurationDevicesInner.md)
 - [LSNLoopBypassable24HourIntrusionPointPost](docs/LSNLoopBypassable24HourIntrusionPointPost.md)
 - [LSNLoopBypassableBoltContactPointPost](docs/LSNLoopBypassableBoltContactPointPost.md)
 - [LSNLoopBypassableIntrusionPointPost](docs/LSNLoopBypassableIntrusionPointPost.md)
 - [LSNLoopDevicePost](docs/LSNLoopDevicePost.md)
 - [LSNLoopFailureIndicationProperty](docs/LSNLoopFailureIndicationProperty.md)
 - [LSNLoopLatchingBypassableTechnicalPointPost](docs/LSNLoopLatchingBypassableTechnicalPointPost.md)
 - [LSNLoopNonBypassable24HourIntrusionPointPost](docs/LSNLoopNonBypassable24HourIntrusionPointPost.md)
 - [LSNLoopNonBypassableBoltContactPointPost](docs/LSNLoopNonBypassableBoltContactPointPost.md)
 - [LSNLoopNonBypassableIntrusionPointPost](docs/LSNLoopNonBypassableIntrusionPointPost.md)
 - [LSNLoopNonBypassableTechnicalPointPost](docs/LSNLoopNonBypassableTechnicalPointPost.md)
 - [LSNLoopNonLatchingBypassableTechnicalPointPost](docs/LSNLoopNonLatchingBypassableTechnicalPointPost.md)
 - [LSNLoopNonSilentAmokPointPost](docs/LSNLoopNonSilentAmokPointPost.md)
 - [LSNLoopNonSilentHoldupPointPost](docs/LSNLoopNonSilentHoldupPointPost.md)
 - [LSNLoopRetriggerableBypassableTechnicalPointPost](docs/LSNLoopRetriggerableBypassableTechnicalPointPost.md)
 - [LSNLoopSilentAmokPointPost](docs/LSNLoopSilentAmokPointPost.md)
 - [LSNLoopSilentDuressPointPost](docs/LSNLoopSilentDuressPointPost.md)
 - [LSNLoopSilentHoldupPointPost](docs/LSNLoopSilentHoldupPointPost.md)
 - [LSNND100Configuration](docs/LSNND100Configuration.md)
 - [LSNND100ConfigurationAnyOf](docs/LSNND100ConfigurationAnyOf.md)
 - [LSNND200Configuration](docs/LSNND200Configuration.md)
 - [LSNND200ConfigurationAnyOf](docs/LSNND200ConfigurationAnyOf.md)
 - [LSNPLoopPointDevicePost](docs/LSNPLoopPointDevicePost.md)
 - [LSNSKA100Configuration](docs/LSNSKA100Configuration.md)
 - [LSNSKA100ConfigurationAnyOf](docs/LSNSKA100ConfigurationAnyOf.md)
 - [LSNStdIntr50Configuration](docs/LSNStdIntr50Configuration.md)
 - [LSNStdIntr50ConfigurationAnyOf](docs/LSNStdIntr50ConfigurationAnyOf.md)
 - [LSNStdIntr51Configuration](docs/LSNStdIntr51Configuration.md)
 - [LSNStdIntr51ConfigurationAnyOf](docs/LSNStdIntr51ConfigurationAnyOf.md)
 - [LSNStdIntr52Configuration](docs/LSNStdIntr52Configuration.md)
 - [LSNStdIntr52ConfigurationAnyOf](docs/LSNStdIntr52ConfigurationAnyOf.md)
 - [LSNStdIntr53Configuration](docs/LSNStdIntr53Configuration.md)
 - [LSNStdIntr53ConfigurationAnyOf](docs/LSNStdIntr53ConfigurationAnyOf.md)
 - [LSNStdIntr54Configuration](docs/LSNStdIntr54Configuration.md)
 - [LSNStdIntr54ConfigurationAnyOf](docs/LSNStdIntr54ConfigurationAnyOf.md)
 - [LSNStdIntr55Configuration](docs/LSNStdIntr55Configuration.md)
 - [LSNStdIntr55ConfigurationAnyOf](docs/LSNStdIntr55ConfigurationAnyOf.md)
 - [LSNStdIntr56Configuration](docs/LSNStdIntr56Configuration.md)
 - [LSNStdIntr56ConfigurationAnyOf](docs/LSNStdIntr56ConfigurationAnyOf.md)
 - [LSNUP370TConfiguration](docs/LSNUP370TConfiguration.md)
 - [LSNUP370TConfigurationAnyOf](docs/LSNUP370TConfigurationAnyOf.md)
 - [LSNWalktestCategoryProperty](docs/LSNWalktestCategoryProperty.md)
 - [LSNWalktestTriggerFrequencyProperty](docs/LSNWalktestTriggerFrequencyProperty.md)
 - [LsnGateway](docs/LsnGateway.md)
 - [LsnGatewayList](docs/LsnGatewayList.md)
 - [Lsnaux](docs/Lsnaux.md)
 - [LsnauxList](docs/LsnauxList.md)
 - [Lsnbus](docs/Lsnbus.md)
 - [LsnbusList](docs/LsnbusList.md)
 - [Main](docs/Main.md)
 - [MainList](docs/MainList.md)
 - [ModelListcommand](docs/ModelListcommand.md)
 - [MotionDetectorTestStartStop](docs/MotionDetectorTestStartStop.md)
 - [MumusergroupMixarray](docs/MumusergroupMixarray.md)
 - [MumusergroupMixarrayAllOfUserIds](docs/MumusergroupMixarrayAllOfUserIds.md)
 - [MumusergroupSyncID](docs/MumusergroupSyncID.md)
 - [NetworkGet](docs/NetworkGet.md)
 - [NetworkPost](docs/NetworkPost.md)
 - [NtpGet](docs/NtpGet.md)
 - [NtpGetCustom](docs/NtpGetCustom.md)
 - [NtpGetPublic](docs/NtpGetPublic.md)
 - [NtpPost](docs/NtpPost.md)
 - [Output](docs/Output.md)
 - [OutputList](docs/OutputList.md)
 - [Panel](docs/Panel.md)
 - [PanelCpuUsage](docs/PanelCpuUsage.md)
 - [PanelCpuUsageAverages](docs/PanelCpuUsageAverages.md)
 - [PanelDisk](docs/PanelDisk.md)
 - [PanelLastRestartReason](docs/PanelLastRestartReason.md)
 - [PanelMeminfo](docs/PanelMeminfo.md)
 - [PanelOIISessions](docs/PanelOIISessions.md)
 - [PanelPanel](docs/PanelPanel.md)
 - [PanelPost](docs/PanelPost.md)
 - [PermissionModel](docs/PermissionModel.md)
 - [PermissionModelArmCategoryPermissions](docs/PermissionModelArmCategoryPermissions.md)
 - [PermissionModelEventCategoryPermissions](docs/PermissionModelEventCategoryPermissions.md)
 - [PermissionModelID](docs/PermissionModelID.md)
 - [PermissionModelList](docs/PermissionModelList.md)
 - [PermissionModelListAllOfListInner](docs/PermissionModelListAllOfListInner.md)
 - [PermissionModelMaintenanceCategoryPermissions](docs/PermissionModelMaintenanceCategoryPermissions.md)
 - [PermissionModelOperationsCategoryPermissions](docs/PermissionModelOperationsCategoryPermissions.md)
 - [PermissionModelRemoteServiceCategoryPermissions](docs/PermissionModelRemoteServiceCategoryPermissions.md)
 - [PermissionModelStatusCategoryPermissions](docs/PermissionModelStatusCategoryPermissions.md)
 - [PermissionModelSyncID](docs/PermissionModelSyncID.md)
 - [PermissionModelUserCategoryPermissions](docs/PermissionModelUserCategoryPermissions.md)
 - [PermissionModellistPost](docs/PermissionModellistPost.md)
 - [Point](docs/Point.md)
 - [PointList](docs/PointList.md)
 - [PostAccessmodelRequest](docs/PostAccessmodelRequest.md)
 - [PostAreaSIIDRequest](docs/PostAreaSIIDRequest.md)
 - [PostAreaandtimemodelRequest](docs/PostAreaandtimemodelRequest.md)
 - [PostAreasRequest](docs/PostAreasRequest.md)
 - [PostBatteriesRequest](docs/PostBatteriesRequest.md)
 - [PostDayModelRequest](docs/PostDayModelRequest.md)
 - [PostInterprogramSIIDRequest](docs/PostInterprogramSIIDRequest.md)
 - [PostKeypadSIIDRequest](docs/PostKeypadSIIDRequest.md)
 - [PostKeypadsRequest](docs/PostKeypadsRequest.md)
 - [PostLSNGWConfigRequest](docs/PostLSNGWConfigRequest.md)
 - [PostOutputsRequest](docs/PostOutputsRequest.md)
 - [PostPermisionmodelRequest](docs/PostPermisionmodelRequest.md)
 - [PostSmartkeymodelRequest](docs/PostSmartkeymodelRequest.md)
 - [PostSpecialdaymodelRequest](docs/PostSpecialdaymodelRequest.md)
 - [PostTimemodelRequest](docs/PostTimemodelRequest.md)
 - [PostlsnGatewaySIIDRequest](docs/PostlsnGatewaySIIDRequest.md)
 - [PowerSupply](docs/PowerSupply.md)
 - [PowerSupplyList](docs/PowerSupplyList.md)
 - [Printer](docs/Printer.md)
 - [PsCanOp](docs/PsCanOp.md)
 - [PsCanOpList](docs/PsCanOpList.md)
 - [SharedkeyGet](docs/SharedkeyGet.md)
 - [SharedkeyPost](docs/SharedkeyPost.md)
 - [Smartkey](docs/Smartkey.md)
 - [SmartkeyList](docs/SmartkeyList.md)
 - [SmartkeyModel](docs/SmartkeyModel.md)
 - [SmartkeyModelID](docs/SmartkeyModelID.md)
 - [SmartkeyModelList](docs/SmartkeyModelList.md)
 - [SmartkeyModelListAllOfListInner](docs/SmartkeyModelListAllOfListInner.md)
 - [SmartkeyModelListPost](docs/SmartkeyModelListPost.md)
 - [SmartkeyModelSyncID](docs/SmartkeyModelSyncID.md)
 - [SpecialDayModel](docs/SpecialDayModel.md)
 - [SpecialDayModelID](docs/SpecialDayModelID.md)
 - [SpecialDayModelList](docs/SpecialDayModelList.md)
 - [SpecialDayModelListAllOfListInner](docs/SpecialDayModelListAllOfListInner.md)
 - [SpecialDayModelSyncID](docs/SpecialDayModelSyncID.md)
 - [SpecialDayModellistPost](docs/SpecialDayModellistPost.md)
 - [StatisticsCommon](docs/StatisticsCommon.md)
 - [StatisticsDb](docs/StatisticsDb.md)
 - [StatisticsDbAllOfDatabases](docs/StatisticsDbAllOfDatabases.md)
 - [StatisticsDbAllOfDatabasesPathToDatabase](docs/StatisticsDbAllOfDatabasesPathToDatabase.md)
 - [StatisticsDbAllOfDatabasesPathToDatabaseCounters](docs/StatisticsDbAllOfDatabasesPathToDatabaseCounters.md)
 - [StatisticsDbAllOfDatabasesPathToDatabaseHandles](docs/StatisticsDbAllOfDatabasesPathToDatabaseHandles.md)
 - [StatisticsGeneral](docs/StatisticsGeneral.md)
 - [StatisticsGet](docs/StatisticsGet.md)
 - [StatisticsOii](docs/StatisticsOii.md)
 - [StatisticsOiiAllOfClientsInner](docs/StatisticsOiiAllOfClientsInner.md)
 - [Sub](docs/Sub.md)
 - [SubList](docs/SubList.md)
 - [SubscriptionsInner](docs/SubscriptionsInner.md)
 - [SupervisedConns](docs/SupervisedConns.md)
 - [SupervisedConnsList](docs/SupervisedConnsList.md)
 - [SupervisedIPC](docs/SupervisedIPC.md)
 - [SynchronizationIDs](docs/SynchronizationIDs.md)
 - [SyncstatusAllowSendingUserDBIfArmed](docs/SyncstatusAllowSendingUserDBIfArmed.md)
 - [SyncstatusKeysData](docs/SyncstatusKeysData.md)
 - [SyncstatusRestartCounter](docs/SyncstatusRestartCounter.md)
 - [SyncstatusUptime](docs/SyncstatusUptime.md)
 - [TimeIn](docs/TimeIn.md)
 - [TimeModel](docs/TimeModel.md)
 - [TimeModelID](docs/TimeModelID.md)
 - [TimeModelList](docs/TimeModelList.md)
 - [TimeModelListAllOfListInner](docs/TimeModelListAllOfListInner.md)
 - [TimeModelPeriodInDaysInner](docs/TimeModelPeriodInDaysInner.md)
 - [TimeModelSyncID](docs/TimeModelSyncID.md)
 - [TimeModellistPost](docs/TimeModellistPost.md)
 - [TimeOut](docs/TimeOut.md)
 - [User](docs/User.md)
 - [UserActivate](docs/UserActivate.md)
 - [UserBasicData](docs/UserBasicData.md)
 - [UserID](docs/UserID.md)
 - [UserModel](docs/UserModel.md)
 - [UserModelList](docs/UserModelList.md)
 - [UserModelListAllOfListInner](docs/UserModelListAllOfListInner.md)
 - [UserModelPost](docs/UserModelPost.md)
 - [UserModelSyncID](docs/UserModelSyncID.md)
 - [UserModellistPost](docs/UserModellistPost.md)
 - [Users](docs/Users.md)
 - [Walktest](docs/Walktest.md)
 - [WalktestList](docs/WalktestList.md)
 - [WalktestStart](docs/WalktestStart.md)
 - [WalktestStop](docs/WalktestStop.md)
 - [WalktestWtInner](docs/WalktestWtInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="digest"></a>
### digest


<a id="clientCert"></a>
### clientCert



## Author

intrusion.emea@de.bosch.com


