# WalktestWtInner

area: URL to the area that is part of this walktest. <br>  wtStatus: Walktest status of the area. Possible values are PENDING (walktest requested but not started), STARTED, FAILED (walktest requested but area did not start test, e.g. because of area being armed)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **str** | URL to the area that is part of this walktest | [optional] 
**wt_status** | **str** | Walktest status of the area. Possible values are: - PENDING: walktest requested but not started - STARTED: walktest active - FAILED: walktest requested but area did not start test, e.g. because of area being armed  | [optional] 

## Example

```python
from bosch-alarm-map.models.walktest_wt_inner import WalktestWtInner

# TODO update the JSON string below
json = "{}"
# create an instance of WalktestWtInner from a JSON string
walktest_wt_inner_instance = WalktestWtInner.from_json(json)
# print the JSON string representation of the object
print(WalktestWtInner.to_json())

# convert the object into a dict
walktest_wt_inner_dict = walktest_wt_inner_instance.to_dict()
# create an instance of WalktestWtInner from a dict
walktest_wt_inner_from_dict = WalktestWtInner.from_dict(walktest_wt_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


