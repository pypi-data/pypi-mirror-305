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
from geoengine_openapi_client.models.resource_id_dataset_id import ResourceIdDatasetId
from geoengine_openapi_client.models.resource_id_layer import ResourceIdLayer
from geoengine_openapi_client.models.resource_id_layer_collection import ResourceIdLayerCollection
from geoengine_openapi_client.models.resource_id_ml_model import ResourceIdMlModel
from geoengine_openapi_client.models.resource_id_project import ResourceIdProject
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

RESOURCEID_ONE_OF_SCHEMAS = ["ResourceIdDatasetId", "ResourceIdLayer", "ResourceIdLayerCollection", "ResourceIdMlModel", "ResourceIdProject"]

class ResourceId(BaseModel):
    """
    ResourceId
    """
    # data type: ResourceIdLayer
    oneof_schema_1_validator: Optional[ResourceIdLayer] = None
    # data type: ResourceIdLayerCollection
    oneof_schema_2_validator: Optional[ResourceIdLayerCollection] = None
    # data type: ResourceIdProject
    oneof_schema_3_validator: Optional[ResourceIdProject] = None
    # data type: ResourceIdDatasetId
    oneof_schema_4_validator: Optional[ResourceIdDatasetId] = None
    # data type: ResourceIdMlModel
    oneof_schema_5_validator: Optional[ResourceIdMlModel] = None
    if TYPE_CHECKING:
        actual_instance: Union[ResourceIdDatasetId, ResourceIdLayer, ResourceIdLayerCollection, ResourceIdMlModel, ResourceIdProject]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(RESOURCEID_ONE_OF_SCHEMAS, const=True)

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
        instance = ResourceId.construct()
        error_messages = []
        match = 0
        # validate data type: ResourceIdLayer
        if not isinstance(v, ResourceIdLayer):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResourceIdLayer`")
        else:
            match += 1
        # validate data type: ResourceIdLayerCollection
        if not isinstance(v, ResourceIdLayerCollection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResourceIdLayerCollection`")
        else:
            match += 1
        # validate data type: ResourceIdProject
        if not isinstance(v, ResourceIdProject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResourceIdProject`")
        else:
            match += 1
        # validate data type: ResourceIdDatasetId
        if not isinstance(v, ResourceIdDatasetId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResourceIdDatasetId`")
        else:
            match += 1
        # validate data type: ResourceIdMlModel
        if not isinstance(v, ResourceIdMlModel):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResourceIdMlModel`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ResourceId with oneOf schemas: ResourceIdDatasetId, ResourceIdLayer, ResourceIdLayerCollection, ResourceIdMlModel, ResourceIdProject. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ResourceId with oneOf schemas: ResourceIdDatasetId, ResourceIdLayer, ResourceIdLayerCollection, ResourceIdMlModel, ResourceIdProject. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ResourceId:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ResourceId:
        """Returns the object represented by the json string"""
        instance = ResourceId.construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `type` in the input.")

        # check if data type is `ResourceIdDatasetId`
        if _data_type == "DatasetId":
            instance.actual_instance = ResourceIdDatasetId.from_json(json_str)
            return instance

        # check if data type is `ResourceIdLayer`
        if _data_type == "Layer":
            instance.actual_instance = ResourceIdLayer.from_json(json_str)
            return instance

        # check if data type is `ResourceIdLayerCollection`
        if _data_type == "LayerCollection":
            instance.actual_instance = ResourceIdLayerCollection.from_json(json_str)
            return instance

        # check if data type is `ResourceIdMlModel`
        if _data_type == "MlModel":
            instance.actual_instance = ResourceIdMlModel.from_json(json_str)
            return instance

        # check if data type is `ResourceIdProject`
        if _data_type == "Project":
            instance.actual_instance = ResourceIdProject.from_json(json_str)
            return instance

        # check if data type is `ResourceIdDatasetId`
        if _data_type == "ResourceIdDatasetId":
            instance.actual_instance = ResourceIdDatasetId.from_json(json_str)
            return instance

        # check if data type is `ResourceIdLayer`
        if _data_type == "ResourceIdLayer":
            instance.actual_instance = ResourceIdLayer.from_json(json_str)
            return instance

        # check if data type is `ResourceIdLayerCollection`
        if _data_type == "ResourceIdLayerCollection":
            instance.actual_instance = ResourceIdLayerCollection.from_json(json_str)
            return instance

        # check if data type is `ResourceIdMlModel`
        if _data_type == "ResourceIdMlModel":
            instance.actual_instance = ResourceIdMlModel.from_json(json_str)
            return instance

        # check if data type is `ResourceIdProject`
        if _data_type == "ResourceIdProject":
            instance.actual_instance = ResourceIdProject.from_json(json_str)
            return instance

        # deserialize data into ResourceIdLayer
        try:
            instance.actual_instance = ResourceIdLayer.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResourceIdLayerCollection
        try:
            instance.actual_instance = ResourceIdLayerCollection.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResourceIdProject
        try:
            instance.actual_instance = ResourceIdProject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResourceIdDatasetId
        try:
            instance.actual_instance = ResourceIdDatasetId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResourceIdMlModel
        try:
            instance.actual_instance = ResourceIdMlModel.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ResourceId with oneOf schemas: ResourceIdDatasetId, ResourceIdLayer, ResourceIdLayerCollection, ResourceIdMlModel, ResourceIdProject. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ResourceId with oneOf schemas: ResourceIdDatasetId, ResourceIdLayer, ResourceIdLayerCollection, ResourceIdMlModel, ResourceIdProject. Details: " + ", ".join(error_messages))
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


