# coding: utf-8

"""
    CDO API

    Use the documentation to explore the endpoints CDO has to offer

    The version of the OpenAPI document: 1.5.0
    Contact: cdo.tac@cisco.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CpuHealthMetrics(BaseModel):
    """
    The CPU health metrics for the device. This value will be available only if the health policy on the device has CPU monitoring enabled.
    """ # noqa: E501
    lina_usage_avg: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Measures the average CPU utilisation by the LINA (Cisco's ASA software running natively). Expressed as a percentage value between 0 and 100.", alias="linaUsageAvg")
    snort_usage_avg: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Indicates the average CPU usage by the Snort process, responsible for threat detection, including intrusion prevention and advanced malware protection. Expressed as a percentage value between 0 and 100.", alias="snortUsageAvg")
    system_usage_avg: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Represents the total average CPU load utilised by the FTD system, including both firewall and threat defense mechanisms. Expressed as a percentage value between 0 and 100.", alias="systemUsageAvg")
    __properties: ClassVar[List[str]] = ["linaUsageAvg", "snortUsageAvg", "systemUsageAvg"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CpuHealthMetrics from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CpuHealthMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linaUsageAvg": obj.get("linaUsageAvg"),
            "snortUsageAvg": obj.get("snortUsageAvg"),
            "systemUsageAvg": obj.get("systemUsageAvg")
        })
        return _obj


