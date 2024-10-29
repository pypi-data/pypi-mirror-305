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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cdo_sdk_python.models.application_context_class_loader_parent_unnamed_module_class_loader import ApplicationContextClassLoaderParentUnnamedModuleClassLoader
from cdo_sdk_python.models.redirect_view_servlet_context_filter_registrations_value import RedirectViewServletContextFilterRegistrationsValue
from cdo_sdk_python.models.redirect_view_servlet_context_jsp_config_descriptor import RedirectViewServletContextJspConfigDescriptor
from cdo_sdk_python.models.redirect_view_servlet_context_servlet_registrations_value import RedirectViewServletContextServletRegistrationsValue
from cdo_sdk_python.models.redirect_view_servlet_context_session_cookie_config import RedirectViewServletContextSessionCookieConfig
from typing import Optional, Set
from typing_extensions import Self

class RedirectViewServletContext(BaseModel):
    """
    RedirectViewServletContext
    """ # noqa: E501
    session_timeout: Optional[StrictInt] = Field(default=None, alias="sessionTimeout")
    class_loader: Optional[ApplicationContextClassLoaderParentUnnamedModuleClassLoader] = Field(default=None, alias="classLoader")
    major_version: Optional[StrictInt] = Field(default=None, alias="majorVersion")
    minor_version: Optional[StrictInt] = Field(default=None, alias="minorVersion")
    attribute_names: Optional[Dict[str, Any]] = Field(default=None, alias="attributeNames")
    context_path: Optional[StrictStr] = Field(default=None, alias="contextPath")
    init_parameter_names: Optional[Dict[str, Any]] = Field(default=None, alias="initParameterNames")
    session_tracking_modes: Optional[List[StrictStr]] = Field(default=None, alias="sessionTrackingModes")
    servlet_names: Optional[Dict[str, Any]] = Field(default=None, alias="servletNames")
    effective_major_version: Optional[StrictInt] = Field(default=None, alias="effectiveMajorVersion")
    effective_minor_version: Optional[StrictInt] = Field(default=None, alias="effectiveMinorVersion")
    servlets: Optional[Dict[str, Any]] = None
    server_info: Optional[StrictStr] = Field(default=None, alias="serverInfo")
    servlet_context_name: Optional[StrictStr] = Field(default=None, alias="servletContextName")
    filter_registrations: Optional[Dict[str, RedirectViewServletContextFilterRegistrationsValue]] = Field(default=None, alias="filterRegistrations")
    session_cookie_config: Optional[RedirectViewServletContextSessionCookieConfig] = Field(default=None, alias="sessionCookieConfig")
    default_session_tracking_modes: Optional[List[StrictStr]] = Field(default=None, alias="defaultSessionTrackingModes")
    effective_session_tracking_modes: Optional[List[StrictStr]] = Field(default=None, alias="effectiveSessionTrackingModes")
    jsp_config_descriptor: Optional[RedirectViewServletContextJspConfigDescriptor] = Field(default=None, alias="jspConfigDescriptor")
    virtual_server_name: Optional[StrictStr] = Field(default=None, alias="virtualServerName")
    request_character_encoding: Optional[StrictStr] = Field(default=None, alias="requestCharacterEncoding")
    response_character_encoding: Optional[StrictStr] = Field(default=None, alias="responseCharacterEncoding")
    servlet_registrations: Optional[Dict[str, RedirectViewServletContextServletRegistrationsValue]] = Field(default=None, alias="servletRegistrations")
    __properties: ClassVar[List[str]] = ["sessionTimeout", "classLoader", "majorVersion", "minorVersion", "attributeNames", "contextPath", "initParameterNames", "sessionTrackingModes", "servletNames", "effectiveMajorVersion", "effectiveMinorVersion", "servlets", "serverInfo", "servletContextName", "filterRegistrations", "sessionCookieConfig", "defaultSessionTrackingModes", "effectiveSessionTrackingModes", "jspConfigDescriptor", "virtualServerName", "requestCharacterEncoding", "responseCharacterEncoding", "servletRegistrations"]

    @field_validator('session_tracking_modes')
    def session_tracking_modes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['COOKIE', 'URL', 'SSL']):
                raise ValueError("each list item must be one of ('COOKIE', 'URL', 'SSL')")
        return value

    @field_validator('default_session_tracking_modes')
    def default_session_tracking_modes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['COOKIE', 'URL', 'SSL']):
                raise ValueError("each list item must be one of ('COOKIE', 'URL', 'SSL')")
        return value

    @field_validator('effective_session_tracking_modes')
    def effective_session_tracking_modes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['COOKIE', 'URL', 'SSL']):
                raise ValueError("each list item must be one of ('COOKIE', 'URL', 'SSL')")
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
        """Create an instance of RedirectViewServletContext from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of class_loader
        if self.class_loader:
            _dict['classLoader'] = self.class_loader.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in filter_registrations (dict)
        _field_dict = {}
        if self.filter_registrations:
            for _key in self.filter_registrations:
                if self.filter_registrations[_key]:
                    _field_dict[_key] = self.filter_registrations[_key].to_dict()
            _dict['filterRegistrations'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of session_cookie_config
        if self.session_cookie_config:
            _dict['sessionCookieConfig'] = self.session_cookie_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of jsp_config_descriptor
        if self.jsp_config_descriptor:
            _dict['jspConfigDescriptor'] = self.jsp_config_descriptor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in servlet_registrations (dict)
        _field_dict = {}
        if self.servlet_registrations:
            for _key in self.servlet_registrations:
                if self.servlet_registrations[_key]:
                    _field_dict[_key] = self.servlet_registrations[_key].to_dict()
            _dict['servletRegistrations'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RedirectViewServletContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sessionTimeout": obj.get("sessionTimeout"),
            "classLoader": ApplicationContextClassLoaderParentUnnamedModuleClassLoader.from_dict(obj["classLoader"]) if obj.get("classLoader") is not None else None,
            "majorVersion": obj.get("majorVersion"),
            "minorVersion": obj.get("minorVersion"),
            "attributeNames": obj.get("attributeNames"),
            "contextPath": obj.get("contextPath"),
            "initParameterNames": obj.get("initParameterNames"),
            "sessionTrackingModes": obj.get("sessionTrackingModes"),
            "servletNames": obj.get("servletNames"),
            "effectiveMajorVersion": obj.get("effectiveMajorVersion"),
            "effectiveMinorVersion": obj.get("effectiveMinorVersion"),
            "servlets": obj.get("servlets"),
            "serverInfo": obj.get("serverInfo"),
            "servletContextName": obj.get("servletContextName"),
            "filterRegistrations": dict(
                (_k, RedirectViewServletContextFilterRegistrationsValue.from_dict(_v))
                for _k, _v in obj["filterRegistrations"].items()
            )
            if obj.get("filterRegistrations") is not None
            else None,
            "sessionCookieConfig": RedirectViewServletContextSessionCookieConfig.from_dict(obj["sessionCookieConfig"]) if obj.get("sessionCookieConfig") is not None else None,
            "defaultSessionTrackingModes": obj.get("defaultSessionTrackingModes"),
            "effectiveSessionTrackingModes": obj.get("effectiveSessionTrackingModes"),
            "jspConfigDescriptor": RedirectViewServletContextJspConfigDescriptor.from_dict(obj["jspConfigDescriptor"]) if obj.get("jspConfigDescriptor") is not None else None,
            "virtualServerName": obj.get("virtualServerName"),
            "requestCharacterEncoding": obj.get("requestCharacterEncoding"),
            "responseCharacterEncoding": obj.get("responseCharacterEncoding"),
            "servletRegistrations": dict(
                (_k, RedirectViewServletContextServletRegistrationsValue.from_dict(_v))
                for _k, _v in obj["servletRegistrations"].items()
            )
            if obj.get("servletRegistrations") is not None
            else None
        })
        return _obj


