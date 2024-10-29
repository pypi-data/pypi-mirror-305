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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from geoengine_openapi_client.models.raster_band_descriptor import RasterBandDescriptor
from geoengine_openapi_client.models.raster_data_type import RasterDataType
from geoengine_openapi_client.models.spatial_partition2_d import SpatialPartition2D
from geoengine_openapi_client.models.spatial_resolution import SpatialResolution
from geoengine_openapi_client.models.time_interval import TimeInterval

class TypedRasterResultDescriptor(BaseModel):
    """
    A `ResultDescriptor` for raster queries  # noqa: E501
    """
    bands: conlist(RasterBandDescriptor) = Field(...)
    bbox: Optional[SpatialPartition2D] = None
    data_type: RasterDataType = Field(..., alias="dataType")
    resolution: Optional[SpatialResolution] = None
    spatial_reference: StrictStr = Field(..., alias="spatialReference")
    time: Optional[TimeInterval] = None
    type: StrictStr = Field(...)
    __properties = ["bands", "bbox", "dataType", "resolution", "spatialReference", "time", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('raster'):
            raise ValueError("must be one of enum values ('raster')")
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
    def from_json(cls, json_str: str) -> TypedRasterResultDescriptor:
        """Create an instance of TypedRasterResultDescriptor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in bands (list)
        _items = []
        if self.bands:
            for _item in self.bands:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bands'] = _items
        # override the default output from pydantic by calling `to_dict()` of bbox
        if self.bbox:
            _dict['bbox'] = self.bbox.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resolution
        if self.resolution:
            _dict['resolution'] = self.resolution.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time
        if self.time:
            _dict['time'] = self.time.to_dict()
        # set to None if bbox (nullable) is None
        # and __fields_set__ contains the field
        if self.bbox is None and "bbox" in self.__fields_set__:
            _dict['bbox'] = None

        # set to None if resolution (nullable) is None
        # and __fields_set__ contains the field
        if self.resolution is None and "resolution" in self.__fields_set__:
            _dict['resolution'] = None

        # set to None if time (nullable) is None
        # and __fields_set__ contains the field
        if self.time is None and "time" in self.__fields_set__:
            _dict['time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TypedRasterResultDescriptor:
        """Create an instance of TypedRasterResultDescriptor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TypedRasterResultDescriptor.parse_obj(obj)

        _obj = TypedRasterResultDescriptor.parse_obj({
            "bands": [RasterBandDescriptor.from_dict(_item) for _item in obj.get("bands")] if obj.get("bands") is not None else None,
            "bbox": SpatialPartition2D.from_dict(obj.get("bbox")) if obj.get("bbox") is not None else None,
            "data_type": obj.get("dataType"),
            "resolution": SpatialResolution.from_dict(obj.get("resolution")) if obj.get("resolution") is not None else None,
            "spatial_reference": obj.get("spatialReference"),
            "time": TimeInterval.from_dict(obj.get("time")) if obj.get("time") is not None else None,
            "type": obj.get("type")
        })
        return _obj


