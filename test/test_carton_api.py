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
from Infoplus.api.carton_api import CartonApi  # noqa: E501
from Infoplus.rest import ApiException


class TestCartonApi(unittest.TestCase):
    """CartonApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.carton_api.CartonApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_carton(self):
        """Test case for add_carton

        Create a carton  # noqa: E501
        """
        pass

    def test_add_carton_audit(self):
        """Test case for add_carton_audit

        Add new audit for a carton  # noqa: E501
        """
        pass

    def test_add_carton_file(self):
        """Test case for add_carton_file

        Attach a file to a carton  # noqa: E501
        """
        pass

    def test_add_carton_tag(self):
        """Test case for add_carton_tag

        Add new tags for a carton.  # noqa: E501
        """
        pass

    def test_delete_carton(self):
        """Test case for delete_carton

        Delete a carton  # noqa: E501
        """
        pass

    def test_delete_carton_tag(self):
        """Test case for delete_carton_tag

        Delete a tag for a carton.  # noqa: E501
        """
        pass

    def test_get_carton_by_filter(self):
        """Test case for get_carton_by_filter

        Search cartons by filter  # noqa: E501
        """
        pass

    def test_get_carton_by_id(self):
        """Test case for get_carton_by_id

        Get a carton by id  # noqa: E501
        """
        pass

    def test_get_carton_tags(self):
        """Test case for get_carton_tags

        Get the tags for a carton.  # noqa: E501
        """
        pass

    def test_get_duplicate_carton_by_id(self):
        """Test case for get_duplicate_carton_by_id

        Get a duplicated a carton by id  # noqa: E501
        """
        pass

    def test_update_carton(self):
        """Test case for update_carton

        Update a carton  # noqa: E501
        """
        pass

    def test_update_carton_custom_fields(self):
        """Test case for update_carton_custom_fields

        Update a carton custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
