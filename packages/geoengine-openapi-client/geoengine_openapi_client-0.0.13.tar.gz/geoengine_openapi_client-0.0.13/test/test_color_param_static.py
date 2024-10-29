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

from geoengine_openapi_client.models.color_param_static import ColorParamStatic  # noqa: E501

class TestColorParamStatic(unittest.TestCase):
    """ColorParamStatic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ColorParamStatic:
        """Test ColorParamStatic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ColorParamStatic`
        """
        model = ColorParamStatic()  # noqa: E501
        if include_optional:
            return ColorParamStatic(
                color = [
                    56
                    ],
                type = 'static'
            )
        else:
            return ColorParamStatic(
                color = [
                    56
                    ],
                type = 'static',
        )
        """

    def testColorParamStatic(self):
        """Test ColorParamStatic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
