# coding: utf-8

"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.8.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from geoengine_openapi_client.models.update_project import UpdateProject  # noqa: E501

class TestUpdateProject(unittest.TestCase):
    """UpdateProject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateProject:
        """Test UpdateProject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateProject`
        """
        model = UpdateProject()  # noqa: E501
        if include_optional:
            return UpdateProject(
                bounds = geoengine_openapi_client.models.st_rectangle.STRectangle(
                    bounding_box = geoengine_openapi_client.models.bounding_box2_d.BoundingBox2D(
                        lower_left_coordinate = geoengine_openapi_client.models.coordinate2_d.Coordinate2D(
                            x = 1.337, 
                            y = 1.337, ), 
                        upper_right_coordinate = geoengine_openapi_client.models.coordinate2_d.Coordinate2D(
                            x = 1.337, 
                            y = 1.337, ), ), 
                    spatial_reference = '', 
                    time_interval = geoengine_openapi_client.models.time_interval.TimeInterval(
                        end = 56, 
                        start = 56, ), ),
                description = '',
                id = '',
                layers = [
                    null
                    ],
                name = '',
                plots = [
                    null
                    ],
                time_step = geoengine_openapi_client.models.time_step.TimeStep(
                    granularity = 'millis', 
                    step = 0, )
            )
        else:
            return UpdateProject(
                id = '',
        )
        """

    def testUpdateProject(self):
        """Test UpdateProject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
