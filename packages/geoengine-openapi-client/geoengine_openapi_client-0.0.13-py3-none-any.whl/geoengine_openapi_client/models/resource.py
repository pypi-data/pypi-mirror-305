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
from geoengine_openapi_client.models.dataset_resource import DatasetResource
from geoengine_openapi_client.models.layer_collection_resource import LayerCollectionResource
from geoengine_openapi_client.models.layer_resource import LayerResource
from geoengine_openapi_client.models.project_resource import ProjectResource
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

RESOURCE_ONE_OF_SCHEMAS = ["DatasetResource", "LayerCollectionResource", "LayerResource", "ProjectResource"]

class Resource(BaseModel):
    """
    Resource
    """
    # data type: LayerResource
    oneof_schema_1_validator: Optional[LayerResource] = None
    # data type: LayerCollectionResource
    oneof_schema_2_validator: Optional[LayerCollectionResource] = None
    # data type: ProjectResource
    oneof_schema_3_validator: Optional[ProjectResource] = None
    # data type: DatasetResource
    oneof_schema_4_validator: Optional[DatasetResource] = None
    if TYPE_CHECKING:
        actual_instance: Union[DatasetResource, LayerCollectionResource, LayerResource, ProjectResource]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(RESOURCE_ONE_OF_SCHEMAS, const=True)

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
        instance = Resource.construct()
        error_messages = []
        match = 0
        # validate data type: LayerResource
        if not isinstance(v, LayerResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LayerResource`")
        else:
            match += 1
        # validate data type: LayerCollectionResource
        if not isinstance(v, LayerCollectionResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LayerCollectionResource`")
        else:
            match += 1
        # validate data type: ProjectResource
        if not isinstance(v, ProjectResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ProjectResource`")
        else:
            match += 1
        # validate data type: DatasetResource
        if not isinstance(v, DatasetResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DatasetResource`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in Resource with oneOf schemas: DatasetResource, LayerCollectionResource, LayerResource, ProjectResource. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in Resource with oneOf schemas: DatasetResource, LayerCollectionResource, LayerResource, ProjectResource. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Resource:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Resource:
        """Returns the object represented by the json string"""
        instance = Resource.construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `type` in the input.")

        # check if data type is `DatasetResource`
        if _data_type == "DatasetResource":
            instance.actual_instance = DatasetResource.from_json(json_str)
            return instance

        # check if data type is `LayerCollectionResource`
        if _data_type == "LayerCollectionResource":
            instance.actual_instance = LayerCollectionResource.from_json(json_str)
            return instance

        # check if data type is `LayerResource`
        if _data_type == "LayerResource":
            instance.actual_instance = LayerResource.from_json(json_str)
            return instance

        # check if data type is `ProjectResource`
        if _data_type == "ProjectResource":
            instance.actual_instance = ProjectResource.from_json(json_str)
            return instance

        # check if data type is `DatasetResource`
        if _data_type == "dataset":
            instance.actual_instance = DatasetResource.from_json(json_str)
            return instance

        # check if data type is `LayerResource`
        if _data_type == "layer":
            instance.actual_instance = LayerResource.from_json(json_str)
            return instance

        # check if data type is `LayerCollectionResource`
        if _data_type == "layerCollection":
            instance.actual_instance = LayerCollectionResource.from_json(json_str)
            return instance

        # check if data type is `ProjectResource`
        if _data_type == "project":
            instance.actual_instance = ProjectResource.from_json(json_str)
            return instance

        # deserialize data into LayerResource
        try:
            instance.actual_instance = LayerResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LayerCollectionResource
        try:
            instance.actual_instance = LayerCollectionResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ProjectResource
        try:
            instance.actual_instance = ProjectResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DatasetResource
        try:
            instance.actual_instance = DatasetResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Resource with oneOf schemas: DatasetResource, LayerCollectionResource, LayerResource, ProjectResource. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Resource with oneOf schemas: DatasetResource, LayerCollectionResource, LayerResource, ProjectResource. Details: " + ", ".join(error_messages))
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


