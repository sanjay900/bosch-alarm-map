# coding: utf-8

# flake8: noqa

"""
    REST-API_basic

    # Overview   This document specifies the MAP REST-API (OII) - **O**pen **I**ntrusion **I**nterface (**OII**).  The REST-API (former known as **O**pen **I**ntrusion **I**nterface [**OII**]), is implemented on the MAP system. This document is fully valid to the MAP panel firmware Version: <br> <br> **MAP_Update.1.4.0272.tar.bz2**<br>  To be backward compatible, all \"/get\", \"/post\" and other commands which includes \"OII\", will be still \"OII\".  New implemented features will be named as \"REST-API\" instead of \"OII\".  Please note that the following rules have been ignored when checking the OpenAPI documentation file against errors and warnings:   - [no-identical-paths](https://redocly.com/docs/cli/rules/no-identical-paths/)   - [no-ambiguous-paths](https://redocly.com/docs/cli/rules/no-ambiguous-paths/)   - [spec](https://redocly.com/docs/cli/rules/spec/)  The OpenAPI file is structured in the following groups: 1. REST-API_basic 2. REST-API_MUM  ## 1: REST-API_basic  All URLs described under this group contain all functions of released MAP panel firmware version 1.4.0176 All REST-API (OII) functions are also described in the following previous documents (PDF):     - ApplicationNotes.pdf   - BaseSpecification.pdf   - ResourceModel.pdf  This previous REST-API (OII) documentation can be downloaded [here](https://media.boschsecurity.com/fs/media/pb/media/extranet/map_partners/2019_oii_openintrusioninterface.zip). <br>   New features: - *Memory Info & statistics*     This feature is available from the MAP panel firmware version *<1.4.0xxx ToDo, replace*   - *NTP*  This feature is available from the MAP panel firmware version *<1.4.0xxx ToDo, replace*  - *supportfiles*     This feature is available from the MAP panel firmware version 1.4.0231  ## 2: REST-API_MUM  All URLs described in this group contain the features, which are added by the firmware version 1.4.0245   New Features: - *VDS2252 permissions*    Updated internal permissions with both mayClearMainPowerFailure and mayClearATS   ## HTTPS server certificates The MAP system is using so named \"unique self signed server certificates\" for HTTPS. The certificate files are created during the MAP panel start, if not already existing. Due to missing entropy and hardware resources, 2048-bit certificates are created. The MAP system guarantees those certificates will not change uncontrolled during lifetime. This guarantee is fullfilled by automated test during development.  ## General client requests   The MAP systems are **strongly limited** in hardware and software resources. This is why there are **limitations** using the MAP REST-API which **must** be considered to avoid erroneous behavior and a poor user experience.<br> - Use a ping to check the network availability **before** sending HTTP requests to the MAP panel. - The MAP panel can handle parallel requests. However, it is strongly recommended that a single client makes only serial requests.  - Parallel processing of many multiple requests will typically fail with negative response codes and overload the system. - Multiple requests to the same MAP panel must be serialized with a delay of at least 1 second between the last response and the next request. - The MAP panel might return the response codes 500 or a 503 or other response codes in case of overload. - Requests with HTTP Content-Length higher than 30000 bytes are not supported, HTTP Error Code 411 will be raised. - Receiving negative response codes caused by overload require a 60 seconds communication delay. - If the MAP panel does not (anymore) response at all, a delay of at least 5 minutes must be considered. - It is strongly recommended to use a connection pool for better HTTPS performance as well as lower CPU load on the MAP panel. - If the connection is cancelled or runs into timeout it is undefined whether the request will still be processed or not.  - After connection errors, the HTTPS connection must be closed and it is necessary again to check network availability by ping. - Cyclic request, e.g. ping, getting synchronization states and performing a time synchronization are allowed. - Cyclic request must not be more frequent than every 5 minutes. - Enabled **User Passcode Tamper** feature will prevent potential bruteforce attack. Retry count and lockout time is configurable via RPS for MAP. During the lockout any request will return code 401 for attacking IP. - In case of negative response codes, the client side should provide request and response logging to a file, with milliseconds timestamps, to support further analyses. - In case of interface errors or unexpected behaviour, the client side must provide request and response logging to a file, with milliseconds timestamps, e.g. activated by a client side debug level. - The MAP panel itself logs all database modifications, per default, to the history.log, what is strongly limited in number of entries and content. - The MAP panel itself does not log all HTTPS request and responses because of file system limitations. - TCP keepalive is enabled, lost connections will be dropped after 25 seconds.   ## HTTPS server limitations  Due to limited resources, MAP system generally does not process HTTPS requests simultaneously.  However, there are exceptions that are processed simultaneously: - **/syncstatus** - **/panel** - **/sub** - **/sub/\\*** - **/history**  All other URLs are executed sequentially.  Requests are queued and executed once execution units are available.  Simultaneous execution is limited to 3 simultaneous requests, processing time will be slower for multiple simultaneous requests.  Overloading REST-API can make MAP less responsive, in case of overload, the REST-API will generally respond with HTTP code 503, or, in case of heavy overload, will immediately close TCP socket without any response.    ## Response time guarantees  The following URLs have a guaranteed time, only if one HTTPS client connection at the same time.  The following URLs are guaranteed to execute their requests within 120 seconds: - **/history** - **/supportfile** - **/points** - **/couplers** - **/lsnauxs**  The following URLs are guaranteed to execute their requests within 60 seconds: - **/network** - **/syncstatus** - **/usermodellist** - **/outputs** - **/user** - **/mains** - **/groundfaults**  All other REST-API requests are guaranteed to be executed within 10 seconds.  ## License  Following URLs are only accessible with a valid MUM software license and only with a MAP-COM panel: - usermodel - usermodel/* - usermodellist - daymodel - daymodel/* - daymodellist - timemodel - timemodel/* - timemodellist - specialdaymodel - specialdaymodel/* - specialdaymodellist - smartkeymodel - smartkeymodel/* - smartkeymodellist - areaandtimemodel - areaandtimemodel/* - areaandtimemodellist - accessmodel - accessmodel/* - accessmodellist - permissionmodel - permissionmodel/* - permissionmodellist - mumusergroup - sharedkey - statistics - statistics/oii - statistics/db  Missing license will lead to HTTP 403 plain-text response, for example \"License missing MUM/usermodel\"  ## Security  Supported cipher suites:  **TLS1.3** (**recommended**) - TLS_AES_256_GCM_SHA384 - TLS_CHACHA20_POLY1305_SHA256 - TLS_AES_128_GCM_SHA256  **TLS1.2** - ECDHE-RSA-AES128-SHA256 - ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-RSA-AES256-SHA384 - ECDHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-SHA256 - DHE-RSA-AES128-GCM-SHA256 - DHE-RSA-AES256-SHA256 - DHE-RSA-AES256-GCM-SHA384 - DHE-RSA-AES128-SHA  **TLS1.0** (**deprecated**! Not recommended to be used, has to be manually enabled in MAP panel configuration via RPS for MAP) - AES128-SHA - AES256-SHA

    The version of the OpenAPI document: 1.4.0272, 18.09.2024
    Contact: intrusion.emea@de.bosch.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "DEModuleSIIDApi",
    "AccessmodelApi",
    "AccessmodellistApi",
    "AreaSIIDApi",
    "AreaandtimemodelApi",
    "AreaandtimemodellistApi",
    "AreasApi",
    "BatteriesApi",
    "BatterySIIDApi",
    "BatterychargerSIIDApi",
    "BatterychargersApi",
    "BlocklockSIIDApi",
    "BlocklocksApi",
    "CommunicatorSIIDApi",
    "ConfigApi",
    "CouplerSIIDApi",
    "CouplersApi",
    "DaymodelApi",
    "DaymodellistApi",
    "DescApi",
    "DeviceSIIDApi",
    "DevicesApi",
    "FireDetectorSIIDApi",
    "FireDetectorsApi",
    "GroundfaultSIIDApi",
    "GroundfaultsApi",
    "HistoryApi",
    "IncApi",
    "InfrastructureApi",
    "InternalprogramSIIDApi",
    "InternalprogramsApi",
    "IpchistoryApi",
    "KeypadSIIDApi",
    "KeypadsApi",
    "KeyswitchSIIDApi",
    "KeyswitchesApi",
    "LsnApi",
    "LsnGatewaySIIDApi",
    "LsnGatewaysApi",
    "LsnauxSIIDApi",
    "LsnauxsApi",
    "LsnbusSIIDApi",
    "LsnbusesApi",
    "MainSIIDApi",
    "MainsApi",
    "MumusergroupApi",
    "NetworkApi",
    "NtpApi",
    "OutputSIIDApi",
    "OutputsApi",
    "PanelApi",
    "PermissionmodelApi",
    "PermissionmodellistApi",
    "PointSIIDApi",
    "PointsApi",
    "PowerDeviceSIIDApi",
    "PowerDevicesApi",
    "PowerSuppliesApi",
    "PowerSupplySIIDApi",
    "PrinterSIIDApi",
    "PsCanOpListApi",
    "PsCanOpSIIDApi",
    "SharedkeyApi",
    "SmartkeySIIDApi",
    "SmartkeymodelApi",
    "SmartkeymodellistApi",
    "SmartkeysApi",
    "SpecialdaymodelApi",
    "SpecialdaymodellistApi",
    "StatisticsApi",
    "SubApi",
    "SubSIIDApi",
    "SupervisedConnsApi",
    "SupervisedConnsSIIDApi",
    "SupportfileApi",
    "SyncstatusApi",
    "TimeApi",
    "TimemodelApi",
    "TimemodellistApi",
    "UserApi",
    "UsermodelApi",
    "UsermodellistApi",
    "UsersApi",
    "WalktestSIIDApi",
    "WalktestsApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "AccessModel",
    "AccessModelID",
    "AccessModelList",
    "AccessModelListAllOfListInner",
    "AccessModelSyncID",
    "AccessModelistPost",
    "Area",
    "AreaAndTimeModel",
    "AreaAndTimeModelID",
    "AreaAndTimeModelList",
    "AreaAndTimeModelListAllOfListInner",
    "AreaAndTimeModelSyncID",
    "AreaAndTimeModellistPost",
    "AreaArm",
    "AreaConfiguration",
    "AreaDisarm",
    "AreaList",
    "AreaPostResponses",
    "AreaWalktestStarted",
    "ArmingInfo",
    "ArmingInfoWhyNotReadyToArm",
    "ArmingInfoWhyNotReadyToDisarm",
    "ArmingInfoWhyNotReadyToForceArm",
    "Battery",
    "BatteryList",
    "Batterycharger",
    "BatterychargerList",
    "BellTestStart",
    "Blocklock",
    "BlocklockList",
    "ChimeModeStartStop",
    "Command",
    "Communicator",
    "Config",
    "Coupler",
    "CouplerList",
    "CreateSub",
    "CreatedSub",
    "DEModule",
    "DayModel",
    "DayModelID",
    "DayModelList",
    "DayModelListAllOfListInner",
    "DayModelSyncID",
    "DayModellistPost",
    "Desc",
    "DescMainResourcesInner",
    "Device",
    "DeviceActivateDeactivate",
    "DeviceBypassUnbypass",
    "DeviceConfiguration",
    "DeviceEnableDisable",
    "DeviceFwVersion",
    "DeviceOnOff",
    "DeviceOpState",
    "DeviceUpdate",
    "DeviceWalktest",
    "DevicefirmwareVersion",
    "DevicesList",
    "Diagnose",
    "DiagnoseResponse",
    "Error400",
    "Error409",
    "Evt",
    "Evts",
    "FetchEvents",
    "FetchedEvents",
    "FireDetector",
    "FireDetectorList",
    "FireDetectorTestedSensorsInner",
    "GetAccessmodel200Response",
    "GetAreaandtimemodel200Response",
    "GetDaymodel200Response",
    "GetPermissionmodel200Response",
    "GetSmartkeymodel200Response",
    "GetSpecialdaymodel200Response",
    "GetSupervisedConnsSIID200Response",
    "GetTimemodel200Response",
    "GetUsermodelById200Response",
    "GetarmingInfo",
    "Groundfault",
    "GroundfaultList",
    "HandlingState",
    "History",
    "Inc",
    "IncList",
    "IncidentResource",
    "Infrastructure",
    "InfrastructureDevice",
    "InfrastructureDeviceGenericProperty",
    "InfrastructureDeviceProperties",
    "InfrastructureDeviceRPSProperty",
    "InfrastructureDeviceSIType",
    "InternalProgram",
    "InternalProgramIpArmingInfo",
    "InternalProgramList",
    "InternalProgramsConfiguration",
    "IpArmingInfo",
    "Keypad",
    "KeypadList",
    "Keyswitch",
    "Keyswitchlist",
    "LSNAntimaskSensitivityDetectionRangeProperty",
    "LSNAntimaskSensitivityProperty",
    "LSNDetectorSensitivityProperty",
    "LSNEMK36Configuration",
    "LSNEMK36ConfigurationAnyOf",
    "LSNEMK36SConfiguration",
    "LSNGWAUXConfiguration",
    "LSNGWConfiguration",
    "LSNGWConfigurationCreatePost",
    "LSNGWConfigurationDeletePost",
    "LSNGWLoopConfiguration",
    "LSNGWLoopConfigurationDevicesInner",
    "LSNLoopBypassable24HourIntrusionPointPost",
    "LSNLoopBypassableBoltContactPointPost",
    "LSNLoopBypassableIntrusionPointPost",
    "LSNLoopDevicePost",
    "LSNLoopFailureIndicationProperty",
    "LSNLoopLatchingBypassableTechnicalPointPost",
    "LSNLoopNonBypassable24HourIntrusionPointPost",
    "LSNLoopNonBypassableBoltContactPointPost",
    "LSNLoopNonBypassableIntrusionPointPost",
    "LSNLoopNonBypassableTechnicalPointPost",
    "LSNLoopNonLatchingBypassableTechnicalPointPost",
    "LSNLoopNonSilentAmokPointPost",
    "LSNLoopNonSilentHoldupPointPost",
    "LSNLoopRetriggerableBypassableTechnicalPointPost",
    "LSNLoopSilentAmokPointPost",
    "LSNLoopSilentDuressPointPost",
    "LSNLoopSilentHoldupPointPost",
    "LSNND100Configuration",
    "LSNND100ConfigurationAnyOf",
    "LSNND200Configuration",
    "LSNND200ConfigurationAnyOf",
    "LSNPLoopPointDevicePost",
    "LSNSKA100Configuration",
    "LSNSKA100ConfigurationAnyOf",
    "LSNStdIntr50Configuration",
    "LSNStdIntr50ConfigurationAnyOf",
    "LSNStdIntr51Configuration",
    "LSNStdIntr51ConfigurationAnyOf",
    "LSNStdIntr52Configuration",
    "LSNStdIntr52ConfigurationAnyOf",
    "LSNStdIntr53Configuration",
    "LSNStdIntr53ConfigurationAnyOf",
    "LSNStdIntr54Configuration",
    "LSNStdIntr54ConfigurationAnyOf",
    "LSNStdIntr55Configuration",
    "LSNStdIntr55ConfigurationAnyOf",
    "LSNStdIntr56Configuration",
    "LSNStdIntr56ConfigurationAnyOf",
    "LSNUP370TConfiguration",
    "LSNUP370TConfigurationAnyOf",
    "LSNWalktestCategoryProperty",
    "LSNWalktestTriggerFrequencyProperty",
    "LsnGateway",
    "LsnGatewayList",
    "Lsnaux",
    "LsnauxList",
    "Lsnbus",
    "LsnbusList",
    "Main",
    "MainList",
    "ModelListcommand",
    "MotionDetectorTestStartStop",
    "MumusergroupMixarray",
    "MumusergroupMixarrayAllOfUserIds",
    "MumusergroupSyncID",
    "NetworkGet",
    "NetworkPost",
    "NtpGet",
    "NtpGetCustom",
    "NtpGetPublic",
    "NtpPost",
    "Output",
    "OutputList",
    "Panel",
    "PanelCpuUsage",
    "PanelCpuUsageAverages",
    "PanelDisk",
    "PanelLastRestartReason",
    "PanelMeminfo",
    "PanelOIISessions",
    "PanelPanel",
    "PanelPost",
    "PermissionModel",
    "PermissionModelArmCategoryPermissions",
    "PermissionModelEventCategoryPermissions",
    "PermissionModelID",
    "PermissionModelList",
    "PermissionModelListAllOfListInner",
    "PermissionModelMaintenanceCategoryPermissions",
    "PermissionModelOperationsCategoryPermissions",
    "PermissionModelRemoteServiceCategoryPermissions",
    "PermissionModelStatusCategoryPermissions",
    "PermissionModelSyncID",
    "PermissionModelUserCategoryPermissions",
    "PermissionModellistPost",
    "Point",
    "PointList",
    "PostAccessmodelRequest",
    "PostAreaSIIDRequest",
    "PostAreaandtimemodelRequest",
    "PostAreasRequest",
    "PostBatteriesRequest",
    "PostDayModelRequest",
    "PostInterprogramSIIDRequest",
    "PostKeypadSIIDRequest",
    "PostKeypadsRequest",
    "PostLSNGWConfigRequest",
    "PostOutputsRequest",
    "PostPermisionmodelRequest",
    "PostSmartkeymodelRequest",
    "PostSpecialdaymodelRequest",
    "PostTimemodelRequest",
    "PostlsnGatewaySIIDRequest",
    "PowerSupply",
    "PowerSupplyList",
    "Printer",
    "PsCanOp",
    "PsCanOpList",
    "SharedkeyGet",
    "SharedkeyPost",
    "Smartkey",
    "SmartkeyList",
    "SmartkeyModel",
    "SmartkeyModelID",
    "SmartkeyModelList",
    "SmartkeyModelListAllOfListInner",
    "SmartkeyModelListPost",
    "SmartkeyModelSyncID",
    "SpecialDayModel",
    "SpecialDayModelID",
    "SpecialDayModelList",
    "SpecialDayModelListAllOfListInner",
    "SpecialDayModelSyncID",
    "SpecialDayModellistPost",
    "StatisticsCommon",
    "StatisticsDb",
    "StatisticsDbAllOfDatabases",
    "StatisticsDbAllOfDatabasesPathToDatabase",
    "StatisticsDbAllOfDatabasesPathToDatabaseCounters",
    "StatisticsDbAllOfDatabasesPathToDatabaseHandles",
    "StatisticsGeneral",
    "StatisticsGet",
    "StatisticsOii",
    "StatisticsOiiAllOfClientsInner",
    "Sub",
    "SubList",
    "SubscriptionsInner",
    "SupervisedConns",
    "SupervisedConnsList",
    "SupervisedIPC",
    "SynchronizationIDs",
    "SyncstatusAllowSendingUserDBIfArmed",
    "SyncstatusKeysData",
    "SyncstatusRestartCounter",
    "SyncstatusUptime",
    "TimeIn",
    "TimeModel",
    "TimeModelID",
    "TimeModelList",
    "TimeModelListAllOfListInner",
    "TimeModelPeriodInDaysInner",
    "TimeModelSyncID",
    "TimeModellistPost",
    "TimeOut",
    "User",
    "UserActivate",
    "UserBasicData",
    "UserID",
    "UserModel",
    "UserModelList",
    "UserModelListAllOfListInner",
    "UserModelPost",
    "UserModelSyncID",
    "UserModellistPost",
    "Users",
    "Walktest",
    "WalktestList",
    "WalktestStart",
    "WalktestStop",
    "WalktestWtInner",
]

# import apis into sdk package
from bosch-alarm-map.api.de_module_siid_api import DEModuleSIIDApi as DEModuleSIIDApi
from bosch-alarm-map.api.accessmodel_api import AccessmodelApi as AccessmodelApi
from bosch-alarm-map.api.accessmodellist_api import AccessmodellistApi as AccessmodellistApi
from bosch-alarm-map.api.area_siid_api import AreaSIIDApi as AreaSIIDApi
from bosch-alarm-map.api.areaandtimemodel_api import AreaandtimemodelApi as AreaandtimemodelApi
from bosch-alarm-map.api.areaandtimemodellist_api import AreaandtimemodellistApi as AreaandtimemodellistApi
from bosch-alarm-map.api.areas_api import AreasApi as AreasApi
from bosch-alarm-map.api.batteries_api import BatteriesApi as BatteriesApi
from bosch-alarm-map.api.battery_siid_api import BatterySIIDApi as BatterySIIDApi
from bosch-alarm-map.api.batterycharger_siid_api import BatterychargerSIIDApi as BatterychargerSIIDApi
from bosch-alarm-map.api.batterychargers_api import BatterychargersApi as BatterychargersApi
from bosch-alarm-map.api.blocklock_siid_api import BlocklockSIIDApi as BlocklockSIIDApi
from bosch-alarm-map.api.blocklocks_api import BlocklocksApi as BlocklocksApi
from bosch-alarm-map.api.communicator_siid_api import CommunicatorSIIDApi as CommunicatorSIIDApi
from bosch-alarm-map.api.config_api import ConfigApi as ConfigApi
from bosch-alarm-map.api.coupler_siid_api import CouplerSIIDApi as CouplerSIIDApi
from bosch-alarm-map.api.couplers_api import CouplersApi as CouplersApi
from bosch-alarm-map.api.daymodel_api import DaymodelApi as DaymodelApi
from bosch-alarm-map.api.daymodellist_api import DaymodellistApi as DaymodellistApi
from bosch-alarm-map.api.desc_api import DescApi as DescApi
from bosch-alarm-map.api.device_siid_api import DeviceSIIDApi as DeviceSIIDApi
from bosch-alarm-map.api.devices_api import DevicesApi as DevicesApi
from bosch-alarm-map.api.fire_detector_siid_api import FireDetectorSIIDApi as FireDetectorSIIDApi
from bosch-alarm-map.api.fire_detectors_api import FireDetectorsApi as FireDetectorsApi
from bosch-alarm-map.api.groundfault_siid_api import GroundfaultSIIDApi as GroundfaultSIIDApi
from bosch-alarm-map.api.groundfaults_api import GroundfaultsApi as GroundfaultsApi
from bosch-alarm-map.api.history_api import HistoryApi as HistoryApi
from bosch-alarm-map.api.inc_api import IncApi as IncApi
from bosch-alarm-map.api.infrastructure_api import InfrastructureApi as InfrastructureApi
from bosch-alarm-map.api.internalprogram_siid_api import InternalprogramSIIDApi as InternalprogramSIIDApi
from bosch-alarm-map.api.internalprograms_api import InternalprogramsApi as InternalprogramsApi
from bosch-alarm-map.api.ipchistory_api import IpchistoryApi as IpchistoryApi
from bosch-alarm-map.api.keypad_siid_api import KeypadSIIDApi as KeypadSIIDApi
from bosch-alarm-map.api.keypads_api import KeypadsApi as KeypadsApi
from bosch-alarm-map.api.keyswitch_siid_api import KeyswitchSIIDApi as KeyswitchSIIDApi
from bosch-alarm-map.api.keyswitches_api import KeyswitchesApi as KeyswitchesApi
from bosch-alarm-map.api.lsn_api import LsnApi as LsnApi
from bosch-alarm-map.api.lsn_gateway_siid_api import LsnGatewaySIIDApi as LsnGatewaySIIDApi
from bosch-alarm-map.api.lsn_gateways_api import LsnGatewaysApi as LsnGatewaysApi
from bosch-alarm-map.api.lsnaux_siid_api import LsnauxSIIDApi as LsnauxSIIDApi
from bosch-alarm-map.api.lsnauxs_api import LsnauxsApi as LsnauxsApi
from bosch-alarm-map.api.lsnbus_siid_api import LsnbusSIIDApi as LsnbusSIIDApi
from bosch-alarm-map.api.lsnbuses_api import LsnbusesApi as LsnbusesApi
from bosch-alarm-map.api.main_siid_api import MainSIIDApi as MainSIIDApi
from bosch-alarm-map.api.mains_api import MainsApi as MainsApi
from bosch-alarm-map.api.mumusergroup_api import MumusergroupApi as MumusergroupApi
from bosch-alarm-map.api.network_api import NetworkApi as NetworkApi
from bosch-alarm-map.api.ntp_api import NtpApi as NtpApi
from bosch-alarm-map.api.output_siid_api import OutputSIIDApi as OutputSIIDApi
from bosch-alarm-map.api.outputs_api import OutputsApi as OutputsApi
from bosch-alarm-map.api.panel_api import PanelApi as PanelApi
from bosch-alarm-map.api.permissionmodel_api import PermissionmodelApi as PermissionmodelApi
from bosch-alarm-map.api.permissionmodellist_api import PermissionmodellistApi as PermissionmodellistApi
from bosch-alarm-map.api.point_siid_api import PointSIIDApi as PointSIIDApi
from bosch-alarm-map.api.points_api import PointsApi as PointsApi
from bosch-alarm-map.api.power_device_siid_api import PowerDeviceSIIDApi as PowerDeviceSIIDApi
from bosch-alarm-map.api.power_devices_api import PowerDevicesApi as PowerDevicesApi
from bosch-alarm-map.api.power_supplies_api import PowerSuppliesApi as PowerSuppliesApi
from bosch-alarm-map.api.power_supply_siid_api import PowerSupplySIIDApi as PowerSupplySIIDApi
from bosch-alarm-map.api.printer_siid_api import PrinterSIIDApi as PrinterSIIDApi
from bosch-alarm-map.api.ps_can_op_list_api import PsCanOpListApi as PsCanOpListApi
from bosch-alarm-map.api.ps_can_op_siid_api import PsCanOpSIIDApi as PsCanOpSIIDApi
from bosch-alarm-map.api.sharedkey_api import SharedkeyApi as SharedkeyApi
from bosch-alarm-map.api.smartkey_siid_api import SmartkeySIIDApi as SmartkeySIIDApi
from bosch-alarm-map.api.smartkeymodel_api import SmartkeymodelApi as SmartkeymodelApi
from bosch-alarm-map.api.smartkeymodellist_api import SmartkeymodellistApi as SmartkeymodellistApi
from bosch-alarm-map.api.smartkeys_api import SmartkeysApi as SmartkeysApi
from bosch-alarm-map.api.specialdaymodel_api import SpecialdaymodelApi as SpecialdaymodelApi
from bosch-alarm-map.api.specialdaymodellist_api import SpecialdaymodellistApi as SpecialdaymodellistApi
from bosch-alarm-map.api.statistics_api import StatisticsApi as StatisticsApi
from bosch-alarm-map.api.sub_api import SubApi as SubApi
from bosch-alarm-map.api.sub_siid_api import SubSIIDApi as SubSIIDApi
from bosch-alarm-map.api.supervised_conns_api import SupervisedConnsApi as SupervisedConnsApi
from bosch-alarm-map.api.supervised_conns_siid_api import SupervisedConnsSIIDApi as SupervisedConnsSIIDApi
from bosch-alarm-map.api.supportfile_api import SupportfileApi as SupportfileApi
from bosch-alarm-map.api.syncstatus_api import SyncstatusApi as SyncstatusApi
from bosch-alarm-map.api.time_api import TimeApi as TimeApi
from bosch-alarm-map.api.timemodel_api import TimemodelApi as TimemodelApi
from bosch-alarm-map.api.timemodellist_api import TimemodellistApi as TimemodellistApi
from bosch-alarm-map.api.user_api import UserApi as UserApi
from bosch-alarm-map.api.usermodel_api import UsermodelApi as UsermodelApi
from bosch-alarm-map.api.usermodellist_api import UsermodellistApi as UsermodellistApi
from bosch-alarm-map.api.users_api import UsersApi as UsersApi
from bosch-alarm-map.api.walktest_siid_api import WalktestSIIDApi as WalktestSIIDApi
from bosch-alarm-map.api.walktests_api import WalktestsApi as WalktestsApi

# import ApiClient
from bosch-alarm-map.api_response import ApiResponse as ApiResponse
from bosch-alarm-map.api_client import ApiClient as ApiClient
from bosch-alarm-map.configuration import Configuration as Configuration
from bosch-alarm-map.exceptions import OpenApiException as OpenApiException
from bosch-alarm-map.exceptions import ApiTypeError as ApiTypeError
from bosch-alarm-map.exceptions import ApiValueError as ApiValueError
from bosch-alarm-map.exceptions import ApiKeyError as ApiKeyError
from bosch-alarm-map.exceptions import ApiAttributeError as ApiAttributeError
from bosch-alarm-map.exceptions import ApiException as ApiException

# import models into sdk package
from bosch-alarm-map.models.access_model import AccessModel as AccessModel
from bosch-alarm-map.models.access_model_id import AccessModelID as AccessModelID
from bosch-alarm-map.models.access_model_list import AccessModelList as AccessModelList
from bosch-alarm-map.models.access_model_list_all_of_list_inner import AccessModelListAllOfListInner as AccessModelListAllOfListInner
from bosch-alarm-map.models.access_model_sync_id import AccessModelSyncID as AccessModelSyncID
from bosch-alarm-map.models.access_modelist_post import AccessModelistPost as AccessModelistPost
from bosch-alarm-map.models.area import Area as Area
from bosch-alarm-map.models.area_and_time_model import AreaAndTimeModel as AreaAndTimeModel
from bosch-alarm-map.models.area_and_time_model_id import AreaAndTimeModelID as AreaAndTimeModelID
from bosch-alarm-map.models.area_and_time_model_list import AreaAndTimeModelList as AreaAndTimeModelList
from bosch-alarm-map.models.area_and_time_model_list_all_of_list_inner import AreaAndTimeModelListAllOfListInner as AreaAndTimeModelListAllOfListInner
from bosch-alarm-map.models.area_and_time_model_sync_id import AreaAndTimeModelSyncID as AreaAndTimeModelSyncID
from bosch-alarm-map.models.area_and_time_modellist_post import AreaAndTimeModellistPost as AreaAndTimeModellistPost
from bosch-alarm-map.models.area_arm import AreaArm as AreaArm
from bosch-alarm-map.models.area_configuration import AreaConfiguration as AreaConfiguration
from bosch-alarm-map.models.area_disarm import AreaDisarm as AreaDisarm
from bosch-alarm-map.models.area_list import AreaList as AreaList
from bosch-alarm-map.models.area_post_responses import AreaPostResponses as AreaPostResponses
from bosch-alarm-map.models.area_walktest_started import AreaWalktestStarted as AreaWalktestStarted
from bosch-alarm-map.models.arming_info import ArmingInfo as ArmingInfo
from bosch-alarm-map.models.arming_info_why_not_ready_to_arm import ArmingInfoWhyNotReadyToArm as ArmingInfoWhyNotReadyToArm
from bosch-alarm-map.models.arming_info_why_not_ready_to_disarm import ArmingInfoWhyNotReadyToDisarm as ArmingInfoWhyNotReadyToDisarm
from bosch-alarm-map.models.arming_info_why_not_ready_to_force_arm import ArmingInfoWhyNotReadyToForceArm as ArmingInfoWhyNotReadyToForceArm
from bosch-alarm-map.models.battery import Battery as Battery
from bosch-alarm-map.models.battery_list import BatteryList as BatteryList
from bosch-alarm-map.models.batterycharger import Batterycharger as Batterycharger
from bosch-alarm-map.models.batterycharger_list import BatterychargerList as BatterychargerList
from bosch-alarm-map.models.bell_test_start import BellTestStart as BellTestStart
from bosch-alarm-map.models.blocklock import Blocklock as Blocklock
from bosch-alarm-map.models.blocklock_list import BlocklockList as BlocklockList
from bosch-alarm-map.models.chime_mode_start_stop import ChimeModeStartStop as ChimeModeStartStop
from bosch-alarm-map.models.command import Command as Command
from bosch-alarm-map.models.communicator import Communicator as Communicator
from bosch-alarm-map.models.config import Config as Config
from bosch-alarm-map.models.coupler import Coupler as Coupler
from bosch-alarm-map.models.coupler_list import CouplerList as CouplerList
from bosch-alarm-map.models.create_sub import CreateSub as CreateSub
from bosch-alarm-map.models.created_sub import CreatedSub as CreatedSub
from bosch-alarm-map.models.de_module import DEModule as DEModule
from bosch-alarm-map.models.day_model import DayModel as DayModel
from bosch-alarm-map.models.day_model_id import DayModelID as DayModelID
from bosch-alarm-map.models.day_model_list import DayModelList as DayModelList
from bosch-alarm-map.models.day_model_list_all_of_list_inner import DayModelListAllOfListInner as DayModelListAllOfListInner
from bosch-alarm-map.models.day_model_sync_id import DayModelSyncID as DayModelSyncID
from bosch-alarm-map.models.day_modellist_post import DayModellistPost as DayModellistPost
from bosch-alarm-map.models.desc import Desc as Desc
from bosch-alarm-map.models.desc_main_resources_inner import DescMainResourcesInner as DescMainResourcesInner
from bosch-alarm-map.models.device import Device as Device
from bosch-alarm-map.models.device_activate_deactivate import DeviceActivateDeactivate as DeviceActivateDeactivate
from bosch-alarm-map.models.device_bypass_unbypass import DeviceBypassUnbypass as DeviceBypassUnbypass
from bosch-alarm-map.models.device_configuration import DeviceConfiguration as DeviceConfiguration
from bosch-alarm-map.models.device_enable_disable import DeviceEnableDisable as DeviceEnableDisable
from bosch-alarm-map.models.device_fw_version import DeviceFwVersion as DeviceFwVersion
from bosch-alarm-map.models.device_on_off import DeviceOnOff as DeviceOnOff
from bosch-alarm-map.models.device_op_state import DeviceOpState as DeviceOpState
from bosch-alarm-map.models.device_update import DeviceUpdate as DeviceUpdate
from bosch-alarm-map.models.device_walktest import DeviceWalktest as DeviceWalktest
from bosch-alarm-map.models.devicefirmware_version import DevicefirmwareVersion as DevicefirmwareVersion
from bosch-alarm-map.models.devices_list import DevicesList as DevicesList
from bosch-alarm-map.models.diagnose import Diagnose as Diagnose
from bosch-alarm-map.models.diagnose_response import DiagnoseResponse as DiagnoseResponse
from bosch-alarm-map.models.error400 import Error400 as Error400
from bosch-alarm-map.models.error409 import Error409 as Error409
from bosch-alarm-map.models.evt import Evt as Evt
from bosch-alarm-map.models.evts import Evts as Evts
from bosch-alarm-map.models.fetch_events import FetchEvents as FetchEvents
from bosch-alarm-map.models.fetched_events import FetchedEvents as FetchedEvents
from bosch-alarm-map.models.fire_detector import FireDetector as FireDetector
from bosch-alarm-map.models.fire_detector_list import FireDetectorList as FireDetectorList
from bosch-alarm-map.models.fire_detector_tested_sensors_inner import FireDetectorTestedSensorsInner as FireDetectorTestedSensorsInner
from bosch-alarm-map.models.get_accessmodel200_response import GetAccessmodel200Response as GetAccessmodel200Response
from bosch-alarm-map.models.get_areaandtimemodel200_response import GetAreaandtimemodel200Response as GetAreaandtimemodel200Response
from bosch-alarm-map.models.get_daymodel200_response import GetDaymodel200Response as GetDaymodel200Response
from bosch-alarm-map.models.get_permissionmodel200_response import GetPermissionmodel200Response as GetPermissionmodel200Response
from bosch-alarm-map.models.get_smartkeymodel200_response import GetSmartkeymodel200Response as GetSmartkeymodel200Response
from bosch-alarm-map.models.get_specialdaymodel200_response import GetSpecialdaymodel200Response as GetSpecialdaymodel200Response
from bosch-alarm-map.models.get_supervised_conns_siid200_response import GetSupervisedConnsSIID200Response as GetSupervisedConnsSIID200Response
from bosch-alarm-map.models.get_timemodel200_response import GetTimemodel200Response as GetTimemodel200Response
from bosch-alarm-map.models.get_usermodel_by_id200_response import GetUsermodelById200Response as GetUsermodelById200Response
from bosch-alarm-map.models.getarming_info import GetarmingInfo as GetarmingInfo
from bosch-alarm-map.models.groundfault import Groundfault as Groundfault
from bosch-alarm-map.models.groundfault_list import GroundfaultList as GroundfaultList
from bosch-alarm-map.models.handling_state import HandlingState as HandlingState
from bosch-alarm-map.models.history import History as History
from bosch-alarm-map.models.inc import Inc as Inc
from bosch-alarm-map.models.inc_list import IncList as IncList
from bosch-alarm-map.models.incident_resource import IncidentResource as IncidentResource
from bosch-alarm-map.models.infrastructure import Infrastructure as Infrastructure
from bosch-alarm-map.models.infrastructure_device import InfrastructureDevice as InfrastructureDevice
from bosch-alarm-map.models.infrastructure_device_generic_property import InfrastructureDeviceGenericProperty as InfrastructureDeviceGenericProperty
from bosch-alarm-map.models.infrastructure_device_properties import InfrastructureDeviceProperties as InfrastructureDeviceProperties
from bosch-alarm-map.models.infrastructure_device_rps_property import InfrastructureDeviceRPSProperty as InfrastructureDeviceRPSProperty
from bosch-alarm-map.models.infrastructure_device_si_type import InfrastructureDeviceSIType as InfrastructureDeviceSIType
from bosch-alarm-map.models.internal_program import InternalProgram as InternalProgram
from bosch-alarm-map.models.internal_program_ip_arming_info import InternalProgramIpArmingInfo as InternalProgramIpArmingInfo
from bosch-alarm-map.models.internal_program_list import InternalProgramList as InternalProgramList
from bosch-alarm-map.models.internal_programs_configuration import InternalProgramsConfiguration as InternalProgramsConfiguration
from bosch-alarm-map.models.ip_arming_info import IpArmingInfo as IpArmingInfo
from bosch-alarm-map.models.keypad import Keypad as Keypad
from bosch-alarm-map.models.keypad_list import KeypadList as KeypadList
from bosch-alarm-map.models.keyswitch import Keyswitch as Keyswitch
from bosch-alarm-map.models.keyswitchlist import Keyswitchlist as Keyswitchlist
from bosch-alarm-map.models.lsn_antimask_sensitivity_detection_range_property import LSNAntimaskSensitivityDetectionRangeProperty as LSNAntimaskSensitivityDetectionRangeProperty
from bosch-alarm-map.models.lsn_antimask_sensitivity_property import LSNAntimaskSensitivityProperty as LSNAntimaskSensitivityProperty
from bosch-alarm-map.models.lsn_detector_sensitivity_property import LSNDetectorSensitivityProperty as LSNDetectorSensitivityProperty
from bosch-alarm-map.models.lsnemk36_configuration import LSNEMK36Configuration as LSNEMK36Configuration
from bosch-alarm-map.models.lsnemk36_configuration_any_of import LSNEMK36ConfigurationAnyOf as LSNEMK36ConfigurationAnyOf
from bosch-alarm-map.models.lsnemk36_s_configuration import LSNEMK36SConfiguration as LSNEMK36SConfiguration
from bosch-alarm-map.models.lsngwaux_configuration import LSNGWAUXConfiguration as LSNGWAUXConfiguration
from bosch-alarm-map.models.lsngw_configuration import LSNGWConfiguration as LSNGWConfiguration
from bosch-alarm-map.models.lsngw_configuration_create_post import LSNGWConfigurationCreatePost as LSNGWConfigurationCreatePost
from bosch-alarm-map.models.lsngw_configuration_delete_post import LSNGWConfigurationDeletePost as LSNGWConfigurationDeletePost
from bosch-alarm-map.models.lsngw_loop_configuration import LSNGWLoopConfiguration as LSNGWLoopConfiguration
from bosch-alarm-map.models.lsngw_loop_configuration_devices_inner import LSNGWLoopConfigurationDevicesInner as LSNGWLoopConfigurationDevicesInner
from bosch-alarm-map.models.lsn_loop_bypassable24_hour_intrusion_point_post import LSNLoopBypassable24HourIntrusionPointPost as LSNLoopBypassable24HourIntrusionPointPost
from bosch-alarm-map.models.lsn_loop_bypassable_bolt_contact_point_post import LSNLoopBypassableBoltContactPointPost as LSNLoopBypassableBoltContactPointPost
from bosch-alarm-map.models.lsn_loop_bypassable_intrusion_point_post import LSNLoopBypassableIntrusionPointPost as LSNLoopBypassableIntrusionPointPost
from bosch-alarm-map.models.lsn_loop_device_post import LSNLoopDevicePost as LSNLoopDevicePost
from bosch-alarm-map.models.lsn_loop_failure_indication_property import LSNLoopFailureIndicationProperty as LSNLoopFailureIndicationProperty
from bosch-alarm-map.models.lsn_loop_latching_bypassable_technical_point_post import LSNLoopLatchingBypassableTechnicalPointPost as LSNLoopLatchingBypassableTechnicalPointPost
from bosch-alarm-map.models.lsn_loop_non_bypassable24_hour_intrusion_point_post import LSNLoopNonBypassable24HourIntrusionPointPost as LSNLoopNonBypassable24HourIntrusionPointPost
from bosch-alarm-map.models.lsn_loop_non_bypassable_bolt_contact_point_post import LSNLoopNonBypassableBoltContactPointPost as LSNLoopNonBypassableBoltContactPointPost
from bosch-alarm-map.models.lsn_loop_non_bypassable_intrusion_point_post import LSNLoopNonBypassableIntrusionPointPost as LSNLoopNonBypassableIntrusionPointPost
from bosch-alarm-map.models.lsn_loop_non_bypassable_technical_point_post import LSNLoopNonBypassableTechnicalPointPost as LSNLoopNonBypassableTechnicalPointPost
from bosch-alarm-map.models.lsn_loop_non_latching_bypassable_technical_point_post import LSNLoopNonLatchingBypassableTechnicalPointPost as LSNLoopNonLatchingBypassableTechnicalPointPost
from bosch-alarm-map.models.lsn_loop_non_silent_amok_point_post import LSNLoopNonSilentAmokPointPost as LSNLoopNonSilentAmokPointPost
from bosch-alarm-map.models.lsn_loop_non_silent_holdup_point_post import LSNLoopNonSilentHoldupPointPost as LSNLoopNonSilentHoldupPointPost
from bosch-alarm-map.models.lsn_loop_retriggerable_bypassable_technical_point_post import LSNLoopRetriggerableBypassableTechnicalPointPost as LSNLoopRetriggerableBypassableTechnicalPointPost
from bosch-alarm-map.models.lsn_loop_silent_amok_point_post import LSNLoopSilentAmokPointPost as LSNLoopSilentAmokPointPost
from bosch-alarm-map.models.lsn_loop_silent_duress_point_post import LSNLoopSilentDuressPointPost as LSNLoopSilentDuressPointPost
from bosch-alarm-map.models.lsn_loop_silent_holdup_point_post import LSNLoopSilentHoldupPointPost as LSNLoopSilentHoldupPointPost
from bosch-alarm-map.models.lsnnd100_configuration import LSNND100Configuration as LSNND100Configuration
from bosch-alarm-map.models.lsnnd100_configuration_any_of import LSNND100ConfigurationAnyOf as LSNND100ConfigurationAnyOf
from bosch-alarm-map.models.lsnnd200_configuration import LSNND200Configuration as LSNND200Configuration
from bosch-alarm-map.models.lsnnd200_configuration_any_of import LSNND200ConfigurationAnyOf as LSNND200ConfigurationAnyOf
from bosch-alarm-map.models.lsnp_loop_point_device_post import LSNPLoopPointDevicePost as LSNPLoopPointDevicePost
from bosch-alarm-map.models.lsnska100_configuration import LSNSKA100Configuration as LSNSKA100Configuration
from bosch-alarm-map.models.lsnska100_configuration_any_of import LSNSKA100ConfigurationAnyOf as LSNSKA100ConfigurationAnyOf
from bosch-alarm-map.models.lsn_std_intr50_configuration import LSNStdIntr50Configuration as LSNStdIntr50Configuration
from bosch-alarm-map.models.lsn_std_intr50_configuration_any_of import LSNStdIntr50ConfigurationAnyOf as LSNStdIntr50ConfigurationAnyOf
from bosch-alarm-map.models.lsn_std_intr51_configuration import LSNStdIntr51Configuration as LSNStdIntr51Configuration
from bosch-alarm-map.models.lsn_std_intr51_configuration_any_of import LSNStdIntr51ConfigurationAnyOf as LSNStdIntr51ConfigurationAnyOf
from bosch-alarm-map.models.lsn_std_intr52_configuration import LSNStdIntr52Configuration as LSNStdIntr52Configuration
from bosch-alarm-map.models.lsn_std_intr52_configuration_any_of import LSNStdIntr52ConfigurationAnyOf as LSNStdIntr52ConfigurationAnyOf
from bosch-alarm-map.models.lsn_std_intr53_configuration import LSNStdIntr53Configuration as LSNStdIntr53Configuration
from bosch-alarm-map.models.lsn_std_intr53_configuration_any_of import LSNStdIntr53ConfigurationAnyOf as LSNStdIntr53ConfigurationAnyOf
from bosch-alarm-map.models.lsn_std_intr54_configuration import LSNStdIntr54Configuration as LSNStdIntr54Configuration
from bosch-alarm-map.models.lsn_std_intr54_configuration_any_of import LSNStdIntr54ConfigurationAnyOf as LSNStdIntr54ConfigurationAnyOf
from bosch-alarm-map.models.lsn_std_intr55_configuration import LSNStdIntr55Configuration as LSNStdIntr55Configuration
from bosch-alarm-map.models.lsn_std_intr55_configuration_any_of import LSNStdIntr55ConfigurationAnyOf as LSNStdIntr55ConfigurationAnyOf
from bosch-alarm-map.models.lsn_std_intr56_configuration import LSNStdIntr56Configuration as LSNStdIntr56Configuration
from bosch-alarm-map.models.lsn_std_intr56_configuration_any_of import LSNStdIntr56ConfigurationAnyOf as LSNStdIntr56ConfigurationAnyOf
from bosch-alarm-map.models.lsnup370_t_configuration import LSNUP370TConfiguration as LSNUP370TConfiguration
from bosch-alarm-map.models.lsnup370_t_configuration_any_of import LSNUP370TConfigurationAnyOf as LSNUP370TConfigurationAnyOf
from bosch-alarm-map.models.lsn_walktest_category_property import LSNWalktestCategoryProperty as LSNWalktestCategoryProperty
from bosch-alarm-map.models.lsn_walktest_trigger_frequency_property import LSNWalktestTriggerFrequencyProperty as LSNWalktestTriggerFrequencyProperty
from bosch-alarm-map.models.lsn_gateway import LsnGateway as LsnGateway
from bosch-alarm-map.models.lsn_gateway_list import LsnGatewayList as LsnGatewayList
from bosch-alarm-map.models.lsnaux import Lsnaux as Lsnaux
from bosch-alarm-map.models.lsnaux_list import LsnauxList as LsnauxList
from bosch-alarm-map.models.lsnbus import Lsnbus as Lsnbus
from bosch-alarm-map.models.lsnbus_list import LsnbusList as LsnbusList
from bosch-alarm-map.models.main import Main as Main
from bosch-alarm-map.models.main_list import MainList as MainList
from bosch-alarm-map.models.model_listcommand import ModelListcommand as ModelListcommand
from bosch-alarm-map.models.motion_detector_test_start_stop import MotionDetectorTestStartStop as MotionDetectorTestStartStop
from bosch-alarm-map.models.mumusergroup_mixarray import MumusergroupMixarray as MumusergroupMixarray
from bosch-alarm-map.models.mumusergroup_mixarray_all_of_user_ids import MumusergroupMixarrayAllOfUserIds as MumusergroupMixarrayAllOfUserIds
from bosch-alarm-map.models.mumusergroup_sync_id import MumusergroupSyncID as MumusergroupSyncID
from bosch-alarm-map.models.network_get import NetworkGet as NetworkGet
from bosch-alarm-map.models.network_post import NetworkPost as NetworkPost
from bosch-alarm-map.models.ntp_get import NtpGet as NtpGet
from bosch-alarm-map.models.ntp_get_custom import NtpGetCustom as NtpGetCustom
from bosch-alarm-map.models.ntp_get_public import NtpGetPublic as NtpGetPublic
from bosch-alarm-map.models.ntp_post import NtpPost as NtpPost
from bosch-alarm-map.models.output import Output as Output
from bosch-alarm-map.models.output_list import OutputList as OutputList
from bosch-alarm-map.models.panel import Panel as Panel
from bosch-alarm-map.models.panel_cpu_usage import PanelCpuUsage as PanelCpuUsage
from bosch-alarm-map.models.panel_cpu_usage_averages import PanelCpuUsageAverages as PanelCpuUsageAverages
from bosch-alarm-map.models.panel_disk import PanelDisk as PanelDisk
from bosch-alarm-map.models.panel_last_restart_reason import PanelLastRestartReason as PanelLastRestartReason
from bosch-alarm-map.models.panel_meminfo import PanelMeminfo as PanelMeminfo
from bosch-alarm-map.models.panel_oii_sessions import PanelOIISessions as PanelOIISessions
from bosch-alarm-map.models.panel_panel import PanelPanel as PanelPanel
from bosch-alarm-map.models.panel_post import PanelPost as PanelPost
from bosch-alarm-map.models.permission_model import PermissionModel as PermissionModel
from bosch-alarm-map.models.permission_model_arm_category_permissions import PermissionModelArmCategoryPermissions as PermissionModelArmCategoryPermissions
from bosch-alarm-map.models.permission_model_event_category_permissions import PermissionModelEventCategoryPermissions as PermissionModelEventCategoryPermissions
from bosch-alarm-map.models.permission_model_id import PermissionModelID as PermissionModelID
from bosch-alarm-map.models.permission_model_list import PermissionModelList as PermissionModelList
from bosch-alarm-map.models.permission_model_list_all_of_list_inner import PermissionModelListAllOfListInner as PermissionModelListAllOfListInner
from bosch-alarm-map.models.permission_model_maintenance_category_permissions import PermissionModelMaintenanceCategoryPermissions as PermissionModelMaintenanceCategoryPermissions
from bosch-alarm-map.models.permission_model_operations_category_permissions import PermissionModelOperationsCategoryPermissions as PermissionModelOperationsCategoryPermissions
from bosch-alarm-map.models.permission_model_remote_service_category_permissions import PermissionModelRemoteServiceCategoryPermissions as PermissionModelRemoteServiceCategoryPermissions
from bosch-alarm-map.models.permission_model_status_category_permissions import PermissionModelStatusCategoryPermissions as PermissionModelStatusCategoryPermissions
from bosch-alarm-map.models.permission_model_sync_id import PermissionModelSyncID as PermissionModelSyncID
from bosch-alarm-map.models.permission_model_user_category_permissions import PermissionModelUserCategoryPermissions as PermissionModelUserCategoryPermissions
from bosch-alarm-map.models.permission_modellist_post import PermissionModellistPost as PermissionModellistPost
from bosch-alarm-map.models.point import Point as Point
from bosch-alarm-map.models.point_list import PointList as PointList
from bosch-alarm-map.models.post_accessmodel_request import PostAccessmodelRequest as PostAccessmodelRequest
from bosch-alarm-map.models.post_area_siid_request import PostAreaSIIDRequest as PostAreaSIIDRequest
from bosch-alarm-map.models.post_areaandtimemodel_request import PostAreaandtimemodelRequest as PostAreaandtimemodelRequest
from bosch-alarm-map.models.post_areas_request import PostAreasRequest as PostAreasRequest
from bosch-alarm-map.models.post_batteries_request import PostBatteriesRequest as PostBatteriesRequest
from bosch-alarm-map.models.post_day_model_request import PostDayModelRequest as PostDayModelRequest
from bosch-alarm-map.models.post_interprogram_siid_request import PostInterprogramSIIDRequest as PostInterprogramSIIDRequest
from bosch-alarm-map.models.post_keypad_siid_request import PostKeypadSIIDRequest as PostKeypadSIIDRequest
from bosch-alarm-map.models.post_keypads_request import PostKeypadsRequest as PostKeypadsRequest
from bosch-alarm-map.models.post_lsngw_config_request import PostLSNGWConfigRequest as PostLSNGWConfigRequest
from bosch-alarm-map.models.post_outputs_request import PostOutputsRequest as PostOutputsRequest
from bosch-alarm-map.models.post_permisionmodel_request import PostPermisionmodelRequest as PostPermisionmodelRequest
from bosch-alarm-map.models.post_smartkeymodel_request import PostSmartkeymodelRequest as PostSmartkeymodelRequest
from bosch-alarm-map.models.post_specialdaymodel_request import PostSpecialdaymodelRequest as PostSpecialdaymodelRequest
from bosch-alarm-map.models.post_timemodel_request import PostTimemodelRequest as PostTimemodelRequest
from bosch-alarm-map.models.postlsn_gateway_siid_request import PostlsnGatewaySIIDRequest as PostlsnGatewaySIIDRequest
from bosch-alarm-map.models.power_supply import PowerSupply as PowerSupply
from bosch-alarm-map.models.power_supply_list import PowerSupplyList as PowerSupplyList
from bosch-alarm-map.models.printer import Printer as Printer
from bosch-alarm-map.models.ps_can_op import PsCanOp as PsCanOp
from bosch-alarm-map.models.ps_can_op_list import PsCanOpList as PsCanOpList
from bosch-alarm-map.models.sharedkey_get import SharedkeyGet as SharedkeyGet
from bosch-alarm-map.models.sharedkey_post import SharedkeyPost as SharedkeyPost
from bosch-alarm-map.models.smartkey import Smartkey as Smartkey
from bosch-alarm-map.models.smartkey_list import SmartkeyList as SmartkeyList
from bosch-alarm-map.models.smartkey_model import SmartkeyModel as SmartkeyModel
from bosch-alarm-map.models.smartkey_model_id import SmartkeyModelID as SmartkeyModelID
from bosch-alarm-map.models.smartkey_model_list import SmartkeyModelList as SmartkeyModelList
from bosch-alarm-map.models.smartkey_model_list_all_of_list_inner import SmartkeyModelListAllOfListInner as SmartkeyModelListAllOfListInner
from bosch-alarm-map.models.smartkey_model_list_post import SmartkeyModelListPost as SmartkeyModelListPost
from bosch-alarm-map.models.smartkey_model_sync_id import SmartkeyModelSyncID as SmartkeyModelSyncID
from bosch-alarm-map.models.special_day_model import SpecialDayModel as SpecialDayModel
from bosch-alarm-map.models.special_day_model_id import SpecialDayModelID as SpecialDayModelID
from bosch-alarm-map.models.special_day_model_list import SpecialDayModelList as SpecialDayModelList
from bosch-alarm-map.models.special_day_model_list_all_of_list_inner import SpecialDayModelListAllOfListInner as SpecialDayModelListAllOfListInner
from bosch-alarm-map.models.special_day_model_sync_id import SpecialDayModelSyncID as SpecialDayModelSyncID
from bosch-alarm-map.models.special_day_modellist_post import SpecialDayModellistPost as SpecialDayModellistPost
from bosch-alarm-map.models.statistics_common import StatisticsCommon as StatisticsCommon
from bosch-alarm-map.models.statistics_db import StatisticsDb as StatisticsDb
from bosch-alarm-map.models.statistics_db_all_of_databases import StatisticsDbAllOfDatabases as StatisticsDbAllOfDatabases
from bosch-alarm-map.models.statistics_db_all_of_databases_path_to_database import StatisticsDbAllOfDatabasesPathToDatabase as StatisticsDbAllOfDatabasesPathToDatabase
from bosch-alarm-map.models.statistics_db_all_of_databases_path_to_database_counters import StatisticsDbAllOfDatabasesPathToDatabaseCounters as StatisticsDbAllOfDatabasesPathToDatabaseCounters
from bosch-alarm-map.models.statistics_db_all_of_databases_path_to_database_handles import StatisticsDbAllOfDatabasesPathToDatabaseHandles as StatisticsDbAllOfDatabasesPathToDatabaseHandles
from bosch-alarm-map.models.statistics_general import StatisticsGeneral as StatisticsGeneral
from bosch-alarm-map.models.statistics_get import StatisticsGet as StatisticsGet
from bosch-alarm-map.models.statistics_oii import StatisticsOii as StatisticsOii
from bosch-alarm-map.models.statistics_oii_all_of_clients_inner import StatisticsOiiAllOfClientsInner as StatisticsOiiAllOfClientsInner
from bosch-alarm-map.models.sub import Sub as Sub
from bosch-alarm-map.models.sub_list import SubList as SubList
from bosch-alarm-map.models.subscriptions_inner import SubscriptionsInner as SubscriptionsInner
from bosch-alarm-map.models.supervised_conns import SupervisedConns as SupervisedConns
from bosch-alarm-map.models.supervised_conns_list import SupervisedConnsList as SupervisedConnsList
from bosch-alarm-map.models.supervised_ipc import SupervisedIPC as SupervisedIPC
from bosch-alarm-map.models.synchronization_ids import SynchronizationIDs as SynchronizationIDs
from bosch-alarm-map.models.syncstatus_allow_sending_user_dbif_armed import SyncstatusAllowSendingUserDBIfArmed as SyncstatusAllowSendingUserDBIfArmed
from bosch-alarm-map.models.syncstatus_keys_data import SyncstatusKeysData as SyncstatusKeysData
from bosch-alarm-map.models.syncstatus_restart_counter import SyncstatusRestartCounter as SyncstatusRestartCounter
from bosch-alarm-map.models.syncstatus_uptime import SyncstatusUptime as SyncstatusUptime
from bosch-alarm-map.models.time_in import TimeIn as TimeIn
from bosch-alarm-map.models.time_model import TimeModel as TimeModel
from bosch-alarm-map.models.time_model_id import TimeModelID as TimeModelID
from bosch-alarm-map.models.time_model_list import TimeModelList as TimeModelList
from bosch-alarm-map.models.time_model_list_all_of_list_inner import TimeModelListAllOfListInner as TimeModelListAllOfListInner
from bosch-alarm-map.models.time_model_period_in_days_inner import TimeModelPeriodInDaysInner as TimeModelPeriodInDaysInner
from bosch-alarm-map.models.time_model_sync_id import TimeModelSyncID as TimeModelSyncID
from bosch-alarm-map.models.time_modellist_post import TimeModellistPost as TimeModellistPost
from bosch-alarm-map.models.time_out import TimeOut as TimeOut
from bosch-alarm-map.models.user import User as User
from bosch-alarm-map.models.user_activate import UserActivate as UserActivate
from bosch-alarm-map.models.user_basic_data import UserBasicData as UserBasicData
from bosch-alarm-map.models.user_id import UserID as UserID
from bosch-alarm-map.models.user_model import UserModel as UserModel
from bosch-alarm-map.models.user_model_list import UserModelList as UserModelList
from bosch-alarm-map.models.user_model_list_all_of_list_inner import UserModelListAllOfListInner as UserModelListAllOfListInner
from bosch-alarm-map.models.user_model_post import UserModelPost as UserModelPost
from bosch-alarm-map.models.user_model_sync_id import UserModelSyncID as UserModelSyncID
from bosch-alarm-map.models.user_modellist_post import UserModellistPost as UserModellistPost
from bosch-alarm-map.models.users import Users as Users
from bosch-alarm-map.models.walktest import Walktest as Walktest
from bosch-alarm-map.models.walktest_list import WalktestList as WalktestList
from bosch-alarm-map.models.walktest_start import WalktestStart as WalktestStart
from bosch-alarm-map.models.walktest_stop import WalktestStop as WalktestStop
from bosch-alarm-map.models.walktest_wt_inner import WalktestWtInner as WalktestWtInner

