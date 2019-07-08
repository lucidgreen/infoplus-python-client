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
from Infoplus.api.customer_invoice_template_api import CustomerInvoiceTemplateApi  # noqa: E501
from Infoplus.rest import ApiException


class TestCustomerInvoiceTemplateApi(unittest.TestCase):
    """CustomerInvoiceTemplateApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.customer_invoice_template_api.CustomerInvoiceTemplateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_customer_invoice_template(self):
        """Test case for add_customer_invoice_template

        Create a customerInvoiceTemplate  # noqa: E501
        """
        pass

    def test_add_customer_invoice_template_audit(self):
        """Test case for add_customer_invoice_template_audit

        Add new audit for a customerInvoiceTemplate  # noqa: E501
        """
        pass

    def test_add_customer_invoice_template_file(self):
        """Test case for add_customer_invoice_template_file

        Attach a file to a customerInvoiceTemplate  # noqa: E501
        """
        pass

    def test_add_customer_invoice_template_tag(self):
        """Test case for add_customer_invoice_template_tag

        Add new tags for a customerInvoiceTemplate.  # noqa: E501
        """
        pass

    def test_delete_customer_invoice_template(self):
        """Test case for delete_customer_invoice_template

        Delete a customerInvoiceTemplate  # noqa: E501
        """
        pass

    def test_delete_customer_invoice_template_tag(self):
        """Test case for delete_customer_invoice_template_tag

        Delete a tag for a customerInvoiceTemplate.  # noqa: E501
        """
        pass

    def test_get_customer_invoice_template_by_filter(self):
        """Test case for get_customer_invoice_template_by_filter

        Search customerInvoiceTemplates by filter  # noqa: E501
        """
        pass

    def test_get_customer_invoice_template_by_id(self):
        """Test case for get_customer_invoice_template_by_id

        Get a customerInvoiceTemplate by id  # noqa: E501
        """
        pass

    def test_get_customer_invoice_template_tags(self):
        """Test case for get_customer_invoice_template_tags

        Get the tags for a customerInvoiceTemplate.  # noqa: E501
        """
        pass

    def test_get_duplicate_customer_invoice_template_by_id(self):
        """Test case for get_duplicate_customer_invoice_template_by_id

        Get a duplicated a customerInvoiceTemplate by id  # noqa: E501
        """
        pass

    def test_update_customer_invoice_template(self):
        """Test case for update_customer_invoice_template

        Update a customerInvoiceTemplate  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
