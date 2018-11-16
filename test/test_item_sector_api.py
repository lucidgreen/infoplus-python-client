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
from Infoplus.api.item_sector_api import ItemSectorApi  # noqa: E501
from Infoplus.rest import ApiException


class TestItemSectorApi(unittest.TestCase):
    """ItemSectorApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.item_sector_api.ItemSectorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_item_sector(self):
        """Test case for add_item_sector

        Create an itemSector  # noqa: E501
        """
        pass

    def test_add_item_sector_audit(self):
        """Test case for add_item_sector_audit

        Add new audit for an itemSector  # noqa: E501
        """
        pass

    def test_add_item_sector_tag(self):
        """Test case for add_item_sector_tag

        Add new tags for an itemSector.  # noqa: E501
        """
        pass

    def test_delete_item_sector(self):
        """Test case for delete_item_sector

        Delete an itemSector  # noqa: E501
        """
        pass

    def test_delete_item_sector_tag(self):
        """Test case for delete_item_sector_tag

        Delete a tag for an itemSector.  # noqa: E501
        """
        pass

    def test_get_duplicate_item_sector_by_id(self):
        """Test case for get_duplicate_item_sector_by_id

        Get a duplicated an itemSector by id  # noqa: E501
        """
        pass

    def test_get_item_sector_by_filter(self):
        """Test case for get_item_sector_by_filter

        Search itemSectors by filter  # noqa: E501
        """
        pass

    def test_get_item_sector_by_id(self):
        """Test case for get_item_sector_by_id

        Get an itemSector by id  # noqa: E501
        """
        pass

    def test_get_item_sector_tags(self):
        """Test case for get_item_sector_tags

        Get the tags for an itemSector.  # noqa: E501
        """
        pass

    def test_update_item_sector(self):
        """Test case for update_item_sector

        Update an itemSector  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
