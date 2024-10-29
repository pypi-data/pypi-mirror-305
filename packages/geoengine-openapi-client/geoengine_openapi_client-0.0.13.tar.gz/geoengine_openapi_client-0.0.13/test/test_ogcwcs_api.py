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

from geoengine_openapi_client.api.ogcwcs_api import OGCWCSApi  # noqa: E501


class TestOGCWCSApi(unittest.TestCase):
    """OGCWCSApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OGCWCSApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_wcs_capabilities_handler(self) -> None:
        """Test case for wcs_capabilities_handler

        Get WCS Capabilities  # noqa: E501
        """
        pass

    def test_wcs_describe_coverage_handler(self) -> None:
        """Test case for wcs_describe_coverage_handler

        Get WCS Coverage Description  # noqa: E501
        """
        pass

    def test_wcs_get_coverage_handler(self) -> None:
        """Test case for wcs_get_coverage_handler

        Get WCS Coverage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
