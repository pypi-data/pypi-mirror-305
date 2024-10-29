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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from geoengine_openapi_client.models.gdal_meta_data_list import GdalMetaDataList
from geoengine_openapi_client.models.gdal_meta_data_regular import GdalMetaDataRegular
from geoengine_openapi_client.models.gdal_meta_data_static import GdalMetaDataStatic
from geoengine_openapi_client.models.gdal_metadata_net_cdf_cf import GdalMetadataNetCdfCf
from geoengine_openapi_client.models.mock_meta_data import MockMetaData
from geoengine_openapi_client.models.ogr_meta_data import OgrMetaData
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

METADATADEFINITION_ONE_OF_SCHEMAS = ["GdalMetaDataList", "GdalMetaDataRegular", "GdalMetaDataStatic", "GdalMetadataNetCdfCf", "MockMetaData", "OgrMetaData"]

class MetaDataDefinition(BaseModel):
    """
    MetaDataDefinition
    """
    # data type: MockMetaData
    oneof_schema_1_validator: Optional[MockMetaData] = None
    # data type: OgrMetaData
    oneof_schema_2_validator: Optional[OgrMetaData] = None
    # data type: GdalMetaDataRegular
    oneof_schema_3_validator: Optional[GdalMetaDataRegular] = None
    # data type: GdalMetaDataStatic
    oneof_schema_4_validator: Optional[GdalMetaDataStatic] = None
    # data type: GdalMetadataNetCdfCf
    oneof_schema_5_validator: Optional[GdalMetadataNetCdfCf] = None
    # data type: GdalMetaDataList
    oneof_schema_6_validator: Optional[GdalMetaDataList] = None
    if TYPE_CHECKING:
        actual_instance: Union[GdalMetaDataList, GdalMetaDataRegular, GdalMetaDataStatic, GdalMetadataNetCdfCf, MockMetaData, OgrMetaData]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(METADATADEFINITION_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = MetaDataDefinition.construct()
        error_messages = []
        match = 0
        # validate data type: MockMetaData
        if not isinstance(v, MockMetaData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MockMetaData`")
        else:
            match += 1
        # validate data type: OgrMetaData
        if not isinstance(v, OgrMetaData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OgrMetaData`")
        else:
            match += 1
        # validate data type: GdalMetaDataRegular
        if not isinstance(v, GdalMetaDataRegular):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GdalMetaDataRegular`")
        else:
            match += 1
        # validate data type: GdalMetaDataStatic
        if not isinstance(v, GdalMetaDataStatic):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GdalMetaDataStatic`")
        else:
            match += 1
        # validate data type: GdalMetadataNetCdfCf
        if not isinstance(v, GdalMetadataNetCdfCf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GdalMetadataNetCdfCf`")
        else:
            match += 1
        # validate data type: GdalMetaDataList
        if not isinstance(v, GdalMetaDataList):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GdalMetaDataList`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in MetaDataDefinition with oneOf schemas: GdalMetaDataList, GdalMetaDataRegular, GdalMetaDataStatic, GdalMetadataNetCdfCf, MockMetaData, OgrMetaData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in MetaDataDefinition with oneOf schemas: GdalMetaDataList, GdalMetaDataRegular, GdalMetaDataStatic, GdalMetadataNetCdfCf, MockMetaData, OgrMetaData. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> MetaDataDefinition:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> MetaDataDefinition:
        """Returns the object represented by the json string"""
        instance = MetaDataDefinition.construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `type` in the input.")

        # check if data type is `GdalMetaDataList`
        if _data_type == "GdalMetaDataList":
            instance.actual_instance = GdalMetaDataList.from_json(json_str)
            return instance

        # check if data type is `GdalMetaDataRegular`
        if _data_type == "GdalMetaDataRegular":
            instance.actual_instance = GdalMetaDataRegular.from_json(json_str)
            return instance

        # check if data type is `GdalMetaDataStatic`
        if _data_type == "GdalMetaDataStatic":
            instance.actual_instance = GdalMetaDataStatic.from_json(json_str)
            return instance

        # check if data type is `GdalMetadataNetCdfCf`
        if _data_type == "GdalMetadataNetCdfCf":
            instance.actual_instance = GdalMetadataNetCdfCf.from_json(json_str)
            return instance

        # check if data type is `GdalMetaDataStatic`
        if _data_type == "GdalStatic":
            instance.actual_instance = GdalMetaDataStatic.from_json(json_str)
            return instance

        # check if data type is `MockMetaData`
        if _data_type == "MockMetaData":
            instance.actual_instance = MockMetaData.from_json(json_str)
            return instance

        # check if data type is `OgrMetaData`
        if _data_type == "OgrMetaData":
            instance.actual_instance = OgrMetaData.from_json(json_str)
            return instance

        # deserialize data into MockMetaData
        try:
            instance.actual_instance = MockMetaData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OgrMetaData
        try:
            instance.actual_instance = OgrMetaData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GdalMetaDataRegular
        try:
            instance.actual_instance = GdalMetaDataRegular.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GdalMetaDataStatic
        try:
            instance.actual_instance = GdalMetaDataStatic.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GdalMetadataNetCdfCf
        try:
            instance.actual_instance = GdalMetadataNetCdfCf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GdalMetaDataList
        try:
            instance.actual_instance = GdalMetaDataList.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into MetaDataDefinition with oneOf schemas: GdalMetaDataList, GdalMetaDataRegular, GdalMetaDataStatic, GdalMetadataNetCdfCf, MockMetaData, OgrMetaData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into MetaDataDefinition with oneOf schemas: GdalMetaDataList, GdalMetaDataRegular, GdalMetaDataStatic, GdalMetadataNetCdfCf, MockMetaData, OgrMetaData. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


