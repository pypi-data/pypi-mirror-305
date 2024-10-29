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





class RasterDataType(str, Enum):
    """
    RasterDataType
    """

    """
    allowed enum values
    """
    U8 = 'U8'
    U16 = 'U16'
    U32 = 'U32'
    U64 = 'U64'
    I8 = 'I8'
    I16 = 'I16'
    I32 = 'I32'
    I64 = 'I64'
    F32 = 'F32'
    F64 = 'F64'

    @classmethod
    def from_json(cls, json_str: str) -> RasterDataType:
        """Create an instance of RasterDataType from a JSON string"""
        return RasterDataType(json.loads(json_str))


