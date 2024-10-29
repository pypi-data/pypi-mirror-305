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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cdo_sdk_python.models.access_rule_details_content import AccessRuleDetailsContent
from cdo_sdk_python.models.log_settings import LogSettings
from typing import Optional, Set
from typing_extensions import Self

class AccessRule(BaseModel):
    """
    AccessRule
    """ # noqa: E501
    uid: StrictStr = Field(description="The unique identifier, represented as a UUID, of Access Rule in CDO.")
    access_group_uid: StrictStr = Field(description="The unique identifier, represented as a UUID, of the Access Group associated with the Access Rule.", alias="accessGroupUid")
    shared_access_group_uid: Optional[StrictStr] = Field(default=None, description="Optional unique identifier for the shared Access Group associated with a shared Access Rule.", alias="sharedAccessGroupUid")
    entity_uid: StrictStr = Field(description="The unique identifier, represented as a UUID, of the device/manager associated with the Access Rule. Points to shared Access Group in case of shared Rule", alias="entityUid")
    index: StrictInt = Field(description="Access rule index position in Access Group ordered rule list.")
    rule_type: Optional[StrictStr] = Field(default=None, description="The L3 level rule type. L3, L7 or CONTENT_FILTERING. Defaults to L3.", alias="ruleType")
    rule_action: StrictStr = Field(description="The rule's action: PERMIT or DENY.", alias="ruleAction")
    protocol: Optional[AccessRuleDetailsContent] = None
    source_port: Optional[AccessRuleDetailsContent] = Field(default=None, alias="sourcePort")
    destination_port: Optional[AccessRuleDetailsContent] = Field(default=None, alias="destinationPort")
    source_network: Optional[AccessRuleDetailsContent] = Field(default=None, alias="sourceNetwork")
    destination_network: Optional[AccessRuleDetailsContent] = Field(default=None, alias="destinationNetwork")
    source_dynamic_object: Optional[AccessRuleDetailsContent] = Field(default=None, alias="sourceDynamicObject")
    destination_dynamic_object: Optional[AccessRuleDetailsContent] = Field(default=None, alias="destinationDynamicObject")
    log_settings: Optional[LogSettings] = Field(default=None, alias="logSettings")
    rule_time_range: Optional[AccessRuleDetailsContent] = Field(default=None, alias="ruleTimeRange")
    remark: Optional[StrictStr] = Field(default=None, description="A remark.")
    issue: Optional[StrictStr] = Field(default=None, description="Issues. SHADOWED or null.")
    is_active_rule: Optional[StrictBool] = Field(default=None, description="Is active. True by default", alias="isActiveRule")
    created_date: Optional[datetime] = Field(default=None, description="The time (in UTC) at which Access Rule was created, represented using the RFC-3339 standard.", alias="createdDate")
    updated_date: Optional[datetime] = Field(default=None, description="The time (in UTC) at which Access Rule was updated, represented using the RFC-3339 standard.", alias="updatedDate")
    __properties: ClassVar[List[str]] = ["uid", "accessGroupUid", "sharedAccessGroupUid", "entityUid", "index", "ruleType", "ruleAction", "protocol", "sourcePort", "destinationPort", "sourceNetwork", "destinationNetwork", "sourceDynamicObject", "destinationDynamicObject", "logSettings", "ruleTimeRange", "remark", "issue", "isActiveRule", "createdDate", "updatedDate"]

    @field_validator('rule_action')
    def rule_action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PERMIT', 'DENY']):
            raise ValueError("must be one of enum values ('PERMIT', 'DENY')")
        return value

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
        """Create an instance of AccessRule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of protocol
        if self.protocol:
            _dict['protocol'] = self.protocol.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_port
        if self.source_port:
            _dict['sourcePort'] = self.source_port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_port
        if self.destination_port:
            _dict['destinationPort'] = self.destination_port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_network
        if self.source_network:
            _dict['sourceNetwork'] = self.source_network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_network
        if self.destination_network:
            _dict['destinationNetwork'] = self.destination_network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_dynamic_object
        if self.source_dynamic_object:
            _dict['sourceDynamicObject'] = self.source_dynamic_object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_dynamic_object
        if self.destination_dynamic_object:
            _dict['destinationDynamicObject'] = self.destination_dynamic_object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of log_settings
        if self.log_settings:
            _dict['logSettings'] = self.log_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rule_time_range
        if self.rule_time_range:
            _dict['ruleTimeRange'] = self.rule_time_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uid": obj.get("uid"),
            "accessGroupUid": obj.get("accessGroupUid"),
            "sharedAccessGroupUid": obj.get("sharedAccessGroupUid"),
            "entityUid": obj.get("entityUid"),
            "index": obj.get("index"),
            "ruleType": obj.get("ruleType"),
            "ruleAction": obj.get("ruleAction"),
            "protocol": AccessRuleDetailsContent.from_dict(obj["protocol"]) if obj.get("protocol") is not None else None,
            "sourcePort": AccessRuleDetailsContent.from_dict(obj["sourcePort"]) if obj.get("sourcePort") is not None else None,
            "destinationPort": AccessRuleDetailsContent.from_dict(obj["destinationPort"]) if obj.get("destinationPort") is not None else None,
            "sourceNetwork": AccessRuleDetailsContent.from_dict(obj["sourceNetwork"]) if obj.get("sourceNetwork") is not None else None,
            "destinationNetwork": AccessRuleDetailsContent.from_dict(obj["destinationNetwork"]) if obj.get("destinationNetwork") is not None else None,
            "sourceDynamicObject": AccessRuleDetailsContent.from_dict(obj["sourceDynamicObject"]) if obj.get("sourceDynamicObject") is not None else None,
            "destinationDynamicObject": AccessRuleDetailsContent.from_dict(obj["destinationDynamicObject"]) if obj.get("destinationDynamicObject") is not None else None,
            "logSettings": LogSettings.from_dict(obj["logSettings"]) if obj.get("logSettings") is not None else None,
            "ruleTimeRange": AccessRuleDetailsContent.from_dict(obj["ruleTimeRange"]) if obj.get("ruleTimeRange") is not None else None,
            "remark": obj.get("remark"),
            "issue": obj.get("issue"),
            "isActiveRule": obj.get("isActiveRule"),
            "createdDate": obj.get("createdDate"),
            "updatedDate": obj.get("updatedDate")
        })
        return _obj


