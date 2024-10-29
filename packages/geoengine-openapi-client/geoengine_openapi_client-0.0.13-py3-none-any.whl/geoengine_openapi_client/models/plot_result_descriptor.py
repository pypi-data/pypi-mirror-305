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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from geoengine_openapi_client.models.bounding_box2_d import BoundingBox2D
from geoengine_openapi_client.models.time_interval import TimeInterval

class PlotResultDescriptor(BaseModel):
    """
    A `ResultDescriptor` for plot queries  # noqa: E501
    """
    bbox: Optional[BoundingBox2D] = None
    spatial_reference: StrictStr = Field(..., alias="spatialReference")
    time: Optional[TimeInterval] = None
    __properties = ["bbox", "spatialReference", "time"]

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
    def from_json(cls, json_str: str) -> PlotResultDescriptor:
        """Create an instance of PlotResultDescriptor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of bbox
        if self.bbox:
            _dict['bbox'] = self.bbox.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time
        if self.time:
            _dict['time'] = self.time.to_dict()
        # set to None if bbox (nullable) is None
        # and __fields_set__ contains the field
        if self.bbox is None and "bbox" in self.__fields_set__:
            _dict['bbox'] = None

        # set to None if time (nullable) is None
        # and __fields_set__ contains the field
        if self.time is None and "time" in self.__fields_set__:
            _dict['time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlotResultDescriptor:
        """Create an instance of PlotResultDescriptor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlotResultDescriptor.parse_obj(obj)

        _obj = PlotResultDescriptor.parse_obj({
            "bbox": BoundingBox2D.from_dict(obj.get("bbox")) if obj.get("bbox") is not None else None,
            "spatial_reference": obj.get("spatialReference"),
            "time": TimeInterval.from_dict(obj.get("time")) if obj.get("time") is not None else None
        })
        return _obj


