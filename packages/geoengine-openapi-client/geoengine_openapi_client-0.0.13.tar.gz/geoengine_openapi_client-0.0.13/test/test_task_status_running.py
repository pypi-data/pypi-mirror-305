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

from geoengine_openapi_client.models.task_status_running import TaskStatusRunning  # noqa: E501

class TestTaskStatusRunning(unittest.TestCase):
    """TaskStatusRunning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskStatusRunning:
        """Test TaskStatusRunning
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskStatusRunning`
        """
        model = TaskStatusRunning()  # noqa: E501
        if include_optional:
            return TaskStatusRunning(
                description = '',
                estimated_time_remaining = '',
                info = None,
                pct_complete = '',
                status = 'running',
                task_type = '',
                time_started = ''
            )
        else:
            return TaskStatusRunning(
                estimated_time_remaining = '',
                pct_complete = '',
                status = 'running',
                task_type = '',
                time_started = '',
        )
        """

    def testTaskStatusRunning(self):
        """Test TaskStatusRunning"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
