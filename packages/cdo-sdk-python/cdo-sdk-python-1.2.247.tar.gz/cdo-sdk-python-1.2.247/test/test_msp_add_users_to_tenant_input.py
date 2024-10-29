# coding: utf-8

"""
    CDO API

    Use the documentation to explore the endpoints CDO has to offer

    The version of the OpenAPI document: 1.1.0
    Contact: cdo.tac@cisco.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cdo_sdk_python.models.msp_add_users_to_tenant_input import MspAddUsersToTenantInput

class TestMspAddUsersToTenantInput(unittest.TestCase):
    """MspAddUsersToTenantInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MspAddUsersToTenantInput:
        """Test MspAddUsersToTenantInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MspAddUsersToTenantInput`
        """
        model = MspAddUsersToTenantInput()
        if include_optional:
            return MspAddUsersToTenantInput(
                users = [username: burak@cisco.com, role: ROLE_ADMIN]
            )
        else:
            return MspAddUsersToTenantInput(
                users = [username: burak@cisco.com, role: ROLE_ADMIN],
        )
        """

    def testMspAddUsersToTenantInput(self):
        """Test MspAddUsersToTenantInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
