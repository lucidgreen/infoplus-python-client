# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import Infoplus
from Infoplus.api.bill_of_lading_api import BillOfLadingApi  # noqa: E501
from Infoplus.rest import ApiException


class TestBillOfLadingApi(unittest.TestCase):
    """BillOfLadingApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.bill_of_lading_api.BillOfLadingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_bill_of_lading(self):
        """Test case for add_bill_of_lading

        Create a billOfLading  # noqa: E501
        """
        pass

    def test_add_bill_of_lading_audit(self):
        """Test case for add_bill_of_lading_audit

        Add new audit for a billOfLading  # noqa: E501
        """
        pass

    def test_add_bill_of_lading_file(self):
        """Test case for add_bill_of_lading_file

        Attach a file to a billOfLading  # noqa: E501
        """
        pass

    def test_add_bill_of_lading_tag(self):
        """Test case for add_bill_of_lading_tag

        Add new tags for a billOfLading.  # noqa: E501
        """
        pass

    def test_delete_bill_of_lading(self):
        """Test case for delete_bill_of_lading

        Delete a billOfLading  # noqa: E501
        """
        pass

    def test_delete_bill_of_lading_tag(self):
        """Test case for delete_bill_of_lading_tag

        Delete a tag for a billOfLading.  # noqa: E501
        """
        pass

    def test_get_bill_of_lading_by_filter(self):
        """Test case for get_bill_of_lading_by_filter

        Search billOfLadings by filter  # noqa: E501
        """
        pass

    def test_get_bill_of_lading_by_id(self):
        """Test case for get_bill_of_lading_by_id

        Get a billOfLading by id  # noqa: E501
        """
        pass

    def test_get_bill_of_lading_tags(self):
        """Test case for get_bill_of_lading_tags

        Get the tags for a billOfLading.  # noqa: E501
        """
        pass

    def test_get_duplicate_bill_of_lading_by_id(self):
        """Test case for get_duplicate_bill_of_lading_by_id

        Get a duplicated a billOfLading by id  # noqa: E501
        """
        pass

    def test_update_bill_of_lading(self):
        """Test case for update_bill_of_lading

        Update a billOfLading  # noqa: E501
        """
        pass

    def test_update_bill_of_lading_custom_fields(self):
        """Test case for update_bill_of_lading_custom_fields

        Update a billOfLading custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()