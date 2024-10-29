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



from pydantic import BaseModel, Field, StrictStr
from geoengine_openapi_client.models.color_param import ColorParam
from geoengine_openapi_client.models.stroke_param import StrokeParam

class TextSymbology(BaseModel):
    """
    TextSymbology
    """
    attribute: StrictStr = Field(...)
    fill_color: ColorParam = Field(..., alias="fillColor")
    stroke: StrokeParam = Field(...)
    __properties = ["attribute", "fillColor", "stroke"]

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
    def from_json(cls, json_str: str) -> TextSymbology:
        """Create an instance of TextSymbology from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of fill_color
        if self.fill_color:
            _dict['fillColor'] = self.fill_color.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stroke
        if self.stroke:
            _dict['stroke'] = self.stroke.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TextSymbology:
        """Create an instance of TextSymbology from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TextSymbology.parse_obj(obj)

        _obj = TextSymbology.parse_obj({
            "attribute": obj.get("attribute"),
            "fill_color": ColorParam.from_dict(obj.get("fillColor")) if obj.get("fillColor") is not None else None,
            "stroke": StrokeParam.from_dict(obj.get("stroke")) if obj.get("stroke") is not None else None
        })
        return _obj


