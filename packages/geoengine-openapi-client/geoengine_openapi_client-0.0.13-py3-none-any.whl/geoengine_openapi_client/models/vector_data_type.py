# coding: utf-8

"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.8.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class VectorDataType(str, Enum):
    """
    An enum that contains all possible vector data types
    """

    """
    allowed enum values
    """
    DATA = 'Data'
    MULTIPOINT = 'MultiPoint'
    MULTILINESTRING = 'MultiLineString'
    MULTIPOLYGON = 'MultiPolygon'

    @classmethod
    def from_json(cls, json_str: str) -> VectorDataType:
        """Create an instance of VectorDataType from a JSON string"""
        return VectorDataType(json.loads(json_str))


