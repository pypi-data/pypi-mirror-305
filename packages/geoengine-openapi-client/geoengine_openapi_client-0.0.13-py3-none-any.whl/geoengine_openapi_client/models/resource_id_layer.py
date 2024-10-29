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



from pydantic import BaseModel, Field, StrictStr, validator

class ResourceIdLayer(BaseModel):
    """
    ResourceIdLayer
    """
    id: StrictStr = Field(...)
    type: StrictStr = Field(...)
    __properties = ["id", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Layer', 'LayerCollection', 'Project', 'DatasetId', 'MlModel'):
            raise ValueError("must be one of enum values ('Layer', 'LayerCollection', 'Project', 'DatasetId', 'MlModel')")
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
    def from_json(cls, json_str: str) -> ResourceIdLayer:
        """Create an instance of ResourceIdLayer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResourceIdLayer:
        """Create an instance of ResourceIdLayer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResourceIdLayer.parse_obj(obj)

        _obj = ResourceIdLayer.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type")
        })
        return _obj


