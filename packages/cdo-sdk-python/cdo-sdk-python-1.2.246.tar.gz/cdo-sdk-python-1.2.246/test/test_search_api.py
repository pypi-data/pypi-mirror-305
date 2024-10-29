# coding: utf-8

"""
    Cisco Defense Orchestrator API

    Use the interactive documentation to explore the endpoints CDO has to offer

    The version of the OpenAPI document: 0.0.1
    Contact: cdo.tac@cisco.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cdo_sdk_python.api.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SearchApi()

    def tearDown(self) -> None:
        pass

    def test_initiate_full_indexing(self) -> None:
        """Test case for initiate_full_indexing

        Rebuild search index
        """
        pass

    def test_search(self) -> None:
        """Test case for search

        Search
        """
        pass


if __name__ == '__main__':
    unittest.main()
