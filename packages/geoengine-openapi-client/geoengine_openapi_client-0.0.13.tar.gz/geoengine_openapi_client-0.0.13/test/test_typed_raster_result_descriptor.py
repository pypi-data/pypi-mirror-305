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

from geoengine_openapi_client.models.typed_raster_result_descriptor import TypedRasterResultDescriptor  # noqa: E501

class TestTypedRasterResultDescriptor(unittest.TestCase):
    """TypedRasterResultDescriptor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TypedRasterResultDescriptor:
        """Test TypedRasterResultDescriptor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TypedRasterResultDescriptor`
        """
        model = TypedRasterResultDescriptor()  # noqa: E501
        if include_optional:
            return TypedRasterResultDescriptor(
                bands = [
                    geoengine_openapi_client.models.raster_band_descriptor.RasterBandDescriptor(
                        measurement = null, 
                        name = '', )
                    ],
                bbox = geoengine_openapi_client.models.spatial_partition2_d.SpatialPartition2D(
                    lower_right_coordinate = geoengine_openapi_client.models.coordinate2_d.Coordinate2D(
                        x = 1.337, 
                        y = 1.337, ), 
                    upper_left_coordinate = geoengine_openapi_client.models.coordinate2_d.Coordinate2D(
                        x = 1.337, 
                        y = 1.337, ), ),
                data_type = 'U8',
                resolution = geoengine_openapi_client.models.spatial_resolution.SpatialResolution(
                    x = 1.337, 
                    y = 1.337, ),
                spatial_reference = '',
                time = geoengine_openapi_client.models.time_interval.TimeInterval(
                    end = 56, 
                    start = 56, ),
                type = 'raster'
            )
        else:
            return TypedRasterResultDescriptor(
                bands = [
                    geoengine_openapi_client.models.raster_band_descriptor.RasterBandDescriptor(
                        measurement = null, 
                        name = '', )
                    ],
                data_type = 'U8',
                spatial_reference = '',
                type = 'raster',
        )
        """

    def testTypedRasterResultDescriptor(self):
        """Test TypedRasterResultDescriptor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
