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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cdo_sdk_python.models.cd_fmc_object import CdFmcObject
from typing import Optional, Set
from typing_extensions import Self

class CdFmcResult(BaseModel):
    """
    Results from the Cloud-delivered FMC devices, objects or policies that match the search term.
    """ # noqa: E501
    devices: Optional[List[CdFmcObject]] = Field(default=None, description="Devices that match the search term.")
    objects: Optional[List[CdFmcObject]] = Field(default=None, description="Objects that match the search term.")
    policies: Optional[List[CdFmcObject]] = Field(default=None, description="Policies that match the search term.")
    __properties: ClassVar[List[str]] = ["devices", "objects", "policies"]

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
        """Create an instance of CdFmcResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in devices (list)
        _items = []
        if self.devices:
            for _item in self.devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['devices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item in self.objects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in policies (list)
        _items = []
        if self.policies:
            for _item in self.policies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['policies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CdFmcResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "devices": [CdFmcObject.from_dict(_item) for _item in obj["devices"]] if obj.get("devices") is not None else None,
            "objects": [CdFmcObject.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "policies": [CdFmcObject.from_dict(_item) for _item in obj["policies"]] if obj.get("policies") is not None else None
        })
        return _obj


