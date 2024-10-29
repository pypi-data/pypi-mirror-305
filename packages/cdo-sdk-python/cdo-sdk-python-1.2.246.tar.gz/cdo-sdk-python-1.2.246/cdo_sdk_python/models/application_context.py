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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cdo_sdk_python.models.application_context_class_loader import ApplicationContextClassLoader
from cdo_sdk_python.models.environment import Environment
from typing import Optional, Set
from typing_extensions import Self

class ApplicationContext(BaseModel):
    """
    ApplicationContext
    """ # noqa: E501
    parent: Optional[ApplicationContext] = None
    id: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    autowire_capable_bean_factory: Optional[Dict[str, Any]] = Field(default=None, alias="autowireCapableBeanFactory")
    application_name: Optional[StrictStr] = Field(default=None, alias="applicationName")
    startup_date: Optional[StrictInt] = Field(default=None, alias="startupDate")
    environment: Optional[Environment] = None
    bean_definition_count: Optional[StrictInt] = Field(default=None, alias="beanDefinitionCount")
    bean_definition_names: Optional[List[StrictStr]] = Field(default=None, alias="beanDefinitionNames")
    parent_bean_factory: Optional[Dict[str, Any]] = Field(default=None, alias="parentBeanFactory")
    class_loader: Optional[ApplicationContextClassLoader] = Field(default=None, alias="classLoader")
    __properties: ClassVar[List[str]] = ["parent", "id", "displayName", "autowireCapableBeanFactory", "applicationName", "startupDate", "environment", "beanDefinitionCount", "beanDefinitionNames", "parentBeanFactory", "classLoader"]

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
        """Create an instance of ApplicationContext from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of environment
        if self.environment:
            _dict['environment'] = self.environment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of class_loader
        if self.class_loader:
            _dict['classLoader'] = self.class_loader.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parent": ApplicationContext.from_dict(obj["parent"]) if obj.get("parent") is not None else None,
            "id": obj.get("id"),
            "displayName": obj.get("displayName"),
            "autowireCapableBeanFactory": obj.get("autowireCapableBeanFactory"),
            "applicationName": obj.get("applicationName"),
            "startupDate": obj.get("startupDate"),
            "environment": Environment.from_dict(obj["environment"]) if obj.get("environment") is not None else None,
            "beanDefinitionCount": obj.get("beanDefinitionCount"),
            "beanDefinitionNames": obj.get("beanDefinitionNames"),
            "parentBeanFactory": obj.get("parentBeanFactory"),
            "classLoader": ApplicationContextClassLoader.from_dict(obj["classLoader"]) if obj.get("classLoader") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
ApplicationContext.model_rebuild(raise_errors=False)

