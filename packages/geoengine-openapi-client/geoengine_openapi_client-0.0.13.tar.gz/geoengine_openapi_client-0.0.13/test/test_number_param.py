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

from geoengine_openapi_client.models.number_param import NumberParam  # noqa: E501

class TestNumberParam(unittest.TestCase):
    """NumberParam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NumberParam:
        """Test NumberParam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NumberParam`
        """
        model = NumberParam()  # noqa: E501
        if include_optional:
            return NumberParam(
                type = 'static',
                value = 0,
                attribute = '',
                default_value = 1.337,
                factor = 1.337
            )
        else:
            return NumberParam(
                type = 'static',
                value = 0,
                attribute = '',
                default_value = 1.337,
                factor = 1.337,
        )
        """

    def testNumberParam(self):
        """Test NumberParam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
