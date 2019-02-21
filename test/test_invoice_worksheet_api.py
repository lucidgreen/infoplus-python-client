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
from Infoplus.api.invoice_worksheet_api import InvoiceWorksheetApi  # noqa: E501
from Infoplus.rest import ApiException


class TestInvoiceWorksheetApi(unittest.TestCase):
    """InvoiceWorksheetApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.invoice_worksheet_api.InvoiceWorksheetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_invoice_worksheet(self):
        """Test case for add_invoice_worksheet

        Create an invoiceWorksheet  # noqa: E501
        """
        pass

    def test_add_invoice_worksheet_audit(self):
        """Test case for add_invoice_worksheet_audit

        Add new audit for an invoiceWorksheet  # noqa: E501
        """
        pass

    def test_add_invoice_worksheet_tag(self):
        """Test case for add_invoice_worksheet_tag

        Add new tags for an invoiceWorksheet.  # noqa: E501
        """
        pass

    def test_delete_invoice_worksheet(self):
        """Test case for delete_invoice_worksheet

        Delete an invoiceWorksheet  # noqa: E501
        """
        pass

    def test_delete_invoice_worksheet_tag(self):
        """Test case for delete_invoice_worksheet_tag

        Delete a tag for an invoiceWorksheet.  # noqa: E501
        """
        pass

    def test_get_duplicate_invoice_worksheet_by_id(self):
        """Test case for get_duplicate_invoice_worksheet_by_id

        Get a duplicated an invoiceWorksheet by id  # noqa: E501
        """
        pass

    def test_get_invoice_worksheet_by_filter(self):
        """Test case for get_invoice_worksheet_by_filter

        Search invoiceWorksheets by filter  # noqa: E501
        """
        pass

    def test_get_invoice_worksheet_by_id(self):
        """Test case for get_invoice_worksheet_by_id

        Get an invoiceWorksheet by id  # noqa: E501
        """
        pass

    def test_get_invoice_worksheet_tags(self):
        """Test case for get_invoice_worksheet_tags

        Get the tags for an invoiceWorksheet.  # noqa: E501
        """
        pass

    def test_update_invoice_worksheet(self):
        """Test case for update_invoice_worksheet

        Update an invoiceWorksheet  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()