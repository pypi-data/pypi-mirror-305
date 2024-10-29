# coding: utf-8

"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.8.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field, StrictStr, validator

class TaskStatusFailed(BaseModel):
    """
    TaskStatusFailed
    """
    clean_up: Optional[Any] = Field(..., alias="cleanUp")
    error: Optional[Any] = Field(...)
    status: StrictStr = Field(...)
    __properties = ["cleanUp", "error", "status"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('failed'):
            raise ValueError("must be one of enum values ('failed')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TaskStatusFailed:
        """Create an instance of TaskStatusFailed from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if clean_up (nullable) is None
        # and __fields_set__ contains the field
        if self.clean_up is None and "clean_up" in self.__fields_set__:
            _dict['cleanUp'] = None

        # set to None if error (nullable) is None
        # and __fields_set__ contains the field
        if self.error is None and "error" in self.__fields_set__:
            _dict['error'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskStatusFailed:
        """Create an instance of TaskStatusFailed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskStatusFailed.parse_obj(obj)

        _obj = TaskStatusFailed.parse_obj({
            "clean_up": obj.get("cleanUp"),
            "error": obj.get("error"),
            "status": obj.get("status")
        })
        return _obj


