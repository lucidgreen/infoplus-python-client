# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class OrderLine(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OrderLine - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'order_no': 'float',
            'lob_id': 'int',
            'sku': 'str',
            'po_no_id': 'int',
            'ordered_qty': 'int',
            'allowed_qty': 'int',
            'shipped_qty': 'int',
            'backorder_qty': 'int',
            'rev_date': 'str',
            'charge_code': 'str',
            'distribution_code': 'str',
            'upc': 'str',
            'vendor_sku': 'str',
            'order_source_sku': 'str',
            'unit_cost': 'float',
            'unit_sell': 'float',
            'unit_discount': 'float',
            'extended_cost': 'float',
            'extended_sell': 'float',
            'extended_discount': 'float',
            'nc_extended_sell': 'float',
            'item_weight': 'float',
            'production_lot': 'str',
            'weight_per_wrap': 'float',
            'sector': 'str',
            'order_assembly_instructions': 'str',
            'item_account_code_id': 'int',
            'item_legacy_low_stock_contact_id': 'int',
            'item_major_group_id': 'int',
            'item_sub_group_id': 'int',
            'item_product_code_id': 'int',
            'item_summary_code_id': 'int',
            'custom_fields': 'dict(str, object)'
        }

        self.attribute_map = {
            'id': 'id',
            'order_no': 'orderNo',
            'lob_id': 'lobId',
            'sku': 'sku',
            'po_no_id': 'poNoId',
            'ordered_qty': 'orderedQty',
            'allowed_qty': 'allowedQty',
            'shipped_qty': 'shippedQty',
            'backorder_qty': 'backorderQty',
            'rev_date': 'revDate',
            'charge_code': 'chargeCode',
            'distribution_code': 'distributionCode',
            'upc': 'upc',
            'vendor_sku': 'vendorSKU',
            'order_source_sku': 'orderSourceSKU',
            'unit_cost': 'unitCost',
            'unit_sell': 'unitSell',
            'unit_discount': 'unitDiscount',
            'extended_cost': 'extendedCost',
            'extended_sell': 'extendedSell',
            'extended_discount': 'extendedDiscount',
            'nc_extended_sell': 'ncExtendedSell',
            'item_weight': 'itemWeight',
            'production_lot': 'productionLot',
            'weight_per_wrap': 'weightPerWrap',
            'sector': 'sector',
            'order_assembly_instructions': 'orderAssemblyInstructions',
            'item_account_code_id': 'itemAccountCodeId',
            'item_legacy_low_stock_contact_id': 'itemLegacyLowStockContactId',
            'item_major_group_id': 'itemMajorGroupId',
            'item_sub_group_id': 'itemSubGroupId',
            'item_product_code_id': 'itemProductCodeId',
            'item_summary_code_id': 'itemSummaryCodeId',
            'custom_fields': 'customFields'
        }

        self._id = None
        self._order_no = None
        self._lob_id = None
        self._sku = None
        self._po_no_id = None
        self._ordered_qty = None
        self._allowed_qty = None
        self._shipped_qty = None
        self._backorder_qty = None
        self._rev_date = None
        self._charge_code = None
        self._distribution_code = None
        self._upc = None
        self._vendor_sku = None
        self._order_source_sku = None
        self._unit_cost = None
        self._unit_sell = None
        self._unit_discount = None
        self._extended_cost = None
        self._extended_sell = None
        self._extended_discount = None
        self._nc_extended_sell = None
        self._item_weight = None
        self._production_lot = None
        self._weight_per_wrap = None
        self._sector = None
        self._order_assembly_instructions = None
        self._item_account_code_id = None
        self._item_legacy_low_stock_contact_id = None
        self._item_major_group_id = None
        self._item_sub_group_id = None
        self._item_product_code_id = None
        self._item_summary_code_id = None
        self._custom_fields = None

    @property
    def id(self):
        """
        Gets the id of this OrderLine.


        :return: The id of this OrderLine.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrderLine.


        :param id: The id of this OrderLine.
        :type: int
        """
        self._id = id

    @property
    def order_no(self):
        """
        Gets the order_no of this OrderLine.


        :return: The order_no of this OrderLine.
        :rtype: float
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """
        Sets the order_no of this OrderLine.


        :param order_no: The order_no of this OrderLine.
        :type: float
        """
        self._order_no = order_no

    @property
    def lob_id(self):
        """
        Gets the lob_id of this OrderLine.


        :return: The lob_id of this OrderLine.
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """
        Sets the lob_id of this OrderLine.


        :param lob_id: The lob_id of this OrderLine.
        :type: int
        """
        self._lob_id = lob_id

    @property
    def sku(self):
        """
        Gets the sku of this OrderLine.


        :return: The sku of this OrderLine.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this OrderLine.


        :param sku: The sku of this OrderLine.
        :type: str
        """
        self._sku = sku

    @property
    def po_no_id(self):
        """
        Gets the po_no_id of this OrderLine.


        :return: The po_no_id of this OrderLine.
        :rtype: int
        """
        return self._po_no_id

    @po_no_id.setter
    def po_no_id(self, po_no_id):
        """
        Sets the po_no_id of this OrderLine.


        :param po_no_id: The po_no_id of this OrderLine.
        :type: int
        """
        self._po_no_id = po_no_id

    @property
    def ordered_qty(self):
        """
        Gets the ordered_qty of this OrderLine.


        :return: The ordered_qty of this OrderLine.
        :rtype: int
        """
        return self._ordered_qty

    @ordered_qty.setter
    def ordered_qty(self, ordered_qty):
        """
        Sets the ordered_qty of this OrderLine.


        :param ordered_qty: The ordered_qty of this OrderLine.
        :type: int
        """
        self._ordered_qty = ordered_qty

    @property
    def allowed_qty(self):
        """
        Gets the allowed_qty of this OrderLine.


        :return: The allowed_qty of this OrderLine.
        :rtype: int
        """
        return self._allowed_qty

    @allowed_qty.setter
    def allowed_qty(self, allowed_qty):
        """
        Sets the allowed_qty of this OrderLine.


        :param allowed_qty: The allowed_qty of this OrderLine.
        :type: int
        """
        self._allowed_qty = allowed_qty

    @property
    def shipped_qty(self):
        """
        Gets the shipped_qty of this OrderLine.


        :return: The shipped_qty of this OrderLine.
        :rtype: int
        """
        return self._shipped_qty

    @shipped_qty.setter
    def shipped_qty(self, shipped_qty):
        """
        Sets the shipped_qty of this OrderLine.


        :param shipped_qty: The shipped_qty of this OrderLine.
        :type: int
        """
        self._shipped_qty = shipped_qty

    @property
    def backorder_qty(self):
        """
        Gets the backorder_qty of this OrderLine.


        :return: The backorder_qty of this OrderLine.
        :rtype: int
        """
        return self._backorder_qty

    @backorder_qty.setter
    def backorder_qty(self, backorder_qty):
        """
        Sets the backorder_qty of this OrderLine.


        :param backorder_qty: The backorder_qty of this OrderLine.
        :type: int
        """
        self._backorder_qty = backorder_qty

    @property
    def rev_date(self):
        """
        Gets the rev_date of this OrderLine.


        :return: The rev_date of this OrderLine.
        :rtype: str
        """
        return self._rev_date

    @rev_date.setter
    def rev_date(self, rev_date):
        """
        Sets the rev_date of this OrderLine.


        :param rev_date: The rev_date of this OrderLine.
        :type: str
        """
        self._rev_date = rev_date

    @property
    def charge_code(self):
        """
        Gets the charge_code of this OrderLine.


        :return: The charge_code of this OrderLine.
        :rtype: str
        """
        return self._charge_code

    @charge_code.setter
    def charge_code(self, charge_code):
        """
        Sets the charge_code of this OrderLine.


        :param charge_code: The charge_code of this OrderLine.
        :type: str
        """
        self._charge_code = charge_code

    @property
    def distribution_code(self):
        """
        Gets the distribution_code of this OrderLine.


        :return: The distribution_code of this OrderLine.
        :rtype: str
        """
        return self._distribution_code

    @distribution_code.setter
    def distribution_code(self, distribution_code):
        """
        Sets the distribution_code of this OrderLine.


        :param distribution_code: The distribution_code of this OrderLine.
        :type: str
        """
        self._distribution_code = distribution_code

    @property
    def upc(self):
        """
        Gets the upc of this OrderLine.


        :return: The upc of this OrderLine.
        :rtype: str
        """
        return self._upc

    @upc.setter
    def upc(self, upc):
        """
        Sets the upc of this OrderLine.


        :param upc: The upc of this OrderLine.
        :type: str
        """
        self._upc = upc

    @property
    def vendor_sku(self):
        """
        Gets the vendor_sku of this OrderLine.


        :return: The vendor_sku of this OrderLine.
        :rtype: str
        """
        return self._vendor_sku

    @vendor_sku.setter
    def vendor_sku(self, vendor_sku):
        """
        Sets the vendor_sku of this OrderLine.


        :param vendor_sku: The vendor_sku of this OrderLine.
        :type: str
        """
        self._vendor_sku = vendor_sku

    @property
    def order_source_sku(self):
        """
        Gets the order_source_sku of this OrderLine.


        :return: The order_source_sku of this OrderLine.
        :rtype: str
        """
        return self._order_source_sku

    @order_source_sku.setter
    def order_source_sku(self, order_source_sku):
        """
        Sets the order_source_sku of this OrderLine.


        :param order_source_sku: The order_source_sku of this OrderLine.
        :type: str
        """
        self._order_source_sku = order_source_sku

    @property
    def unit_cost(self):
        """
        Gets the unit_cost of this OrderLine.


        :return: The unit_cost of this OrderLine.
        :rtype: float
        """
        return self._unit_cost

    @unit_cost.setter
    def unit_cost(self, unit_cost):
        """
        Sets the unit_cost of this OrderLine.


        :param unit_cost: The unit_cost of this OrderLine.
        :type: float
        """
        self._unit_cost = unit_cost

    @property
    def unit_sell(self):
        """
        Gets the unit_sell of this OrderLine.


        :return: The unit_sell of this OrderLine.
        :rtype: float
        """
        return self._unit_sell

    @unit_sell.setter
    def unit_sell(self, unit_sell):
        """
        Sets the unit_sell of this OrderLine.


        :param unit_sell: The unit_sell of this OrderLine.
        :type: float
        """
        self._unit_sell = unit_sell

    @property
    def unit_discount(self):
        """
        Gets the unit_discount of this OrderLine.


        :return: The unit_discount of this OrderLine.
        :rtype: float
        """
        return self._unit_discount

    @unit_discount.setter
    def unit_discount(self, unit_discount):
        """
        Sets the unit_discount of this OrderLine.


        :param unit_discount: The unit_discount of this OrderLine.
        :type: float
        """
        self._unit_discount = unit_discount

    @property
    def extended_cost(self):
        """
        Gets the extended_cost of this OrderLine.


        :return: The extended_cost of this OrderLine.
        :rtype: float
        """
        return self._extended_cost

    @extended_cost.setter
    def extended_cost(self, extended_cost):
        """
        Sets the extended_cost of this OrderLine.


        :param extended_cost: The extended_cost of this OrderLine.
        :type: float
        """
        self._extended_cost = extended_cost

    @property
    def extended_sell(self):
        """
        Gets the extended_sell of this OrderLine.


        :return: The extended_sell of this OrderLine.
        :rtype: float
        """
        return self._extended_sell

    @extended_sell.setter
    def extended_sell(self, extended_sell):
        """
        Sets the extended_sell of this OrderLine.


        :param extended_sell: The extended_sell of this OrderLine.
        :type: float
        """
        self._extended_sell = extended_sell

    @property
    def extended_discount(self):
        """
        Gets the extended_discount of this OrderLine.


        :return: The extended_discount of this OrderLine.
        :rtype: float
        """
        return self._extended_discount

    @extended_discount.setter
    def extended_discount(self, extended_discount):
        """
        Sets the extended_discount of this OrderLine.


        :param extended_discount: The extended_discount of this OrderLine.
        :type: float
        """
        self._extended_discount = extended_discount

    @property
    def nc_extended_sell(self):
        """
        Gets the nc_extended_sell of this OrderLine.


        :return: The nc_extended_sell of this OrderLine.
        :rtype: float
        """
        return self._nc_extended_sell

    @nc_extended_sell.setter
    def nc_extended_sell(self, nc_extended_sell):
        """
        Sets the nc_extended_sell of this OrderLine.


        :param nc_extended_sell: The nc_extended_sell of this OrderLine.
        :type: float
        """
        self._nc_extended_sell = nc_extended_sell

    @property
    def item_weight(self):
        """
        Gets the item_weight of this OrderLine.


        :return: The item_weight of this OrderLine.
        :rtype: float
        """
        return self._item_weight

    @item_weight.setter
    def item_weight(self, item_weight):
        """
        Sets the item_weight of this OrderLine.


        :param item_weight: The item_weight of this OrderLine.
        :type: float
        """
        self._item_weight = item_weight

    @property
    def production_lot(self):
        """
        Gets the production_lot of this OrderLine.


        :return: The production_lot of this OrderLine.
        :rtype: str
        """
        return self._production_lot

    @production_lot.setter
    def production_lot(self, production_lot):
        """
        Sets the production_lot of this OrderLine.


        :param production_lot: The production_lot of this OrderLine.
        :type: str
        """
        self._production_lot = production_lot

    @property
    def weight_per_wrap(self):
        """
        Gets the weight_per_wrap of this OrderLine.


        :return: The weight_per_wrap of this OrderLine.
        :rtype: float
        """
        return self._weight_per_wrap

    @weight_per_wrap.setter
    def weight_per_wrap(self, weight_per_wrap):
        """
        Sets the weight_per_wrap of this OrderLine.


        :param weight_per_wrap: The weight_per_wrap of this OrderLine.
        :type: float
        """
        self._weight_per_wrap = weight_per_wrap

    @property
    def sector(self):
        """
        Gets the sector of this OrderLine.


        :return: The sector of this OrderLine.
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """
        Sets the sector of this OrderLine.


        :param sector: The sector of this OrderLine.
        :type: str
        """
        self._sector = sector

    @property
    def order_assembly_instructions(self):
        """
        Gets the order_assembly_instructions of this OrderLine.


        :return: The order_assembly_instructions of this OrderLine.
        :rtype: str
        """
        return self._order_assembly_instructions

    @order_assembly_instructions.setter
    def order_assembly_instructions(self, order_assembly_instructions):
        """
        Sets the order_assembly_instructions of this OrderLine.


        :param order_assembly_instructions: The order_assembly_instructions of this OrderLine.
        :type: str
        """
        self._order_assembly_instructions = order_assembly_instructions

    @property
    def item_account_code_id(self):
        """
        Gets the item_account_code_id of this OrderLine.


        :return: The item_account_code_id of this OrderLine.
        :rtype: int
        """
        return self._item_account_code_id

    @item_account_code_id.setter
    def item_account_code_id(self, item_account_code_id):
        """
        Sets the item_account_code_id of this OrderLine.


        :param item_account_code_id: The item_account_code_id of this OrderLine.
        :type: int
        """
        self._item_account_code_id = item_account_code_id

    @property
    def item_legacy_low_stock_contact_id(self):
        """
        Gets the item_legacy_low_stock_contact_id of this OrderLine.


        :return: The item_legacy_low_stock_contact_id of this OrderLine.
        :rtype: int
        """
        return self._item_legacy_low_stock_contact_id

    @item_legacy_low_stock_contact_id.setter
    def item_legacy_low_stock_contact_id(self, item_legacy_low_stock_contact_id):
        """
        Sets the item_legacy_low_stock_contact_id of this OrderLine.


        :param item_legacy_low_stock_contact_id: The item_legacy_low_stock_contact_id of this OrderLine.
        :type: int
        """
        self._item_legacy_low_stock_contact_id = item_legacy_low_stock_contact_id

    @property
    def item_major_group_id(self):
        """
        Gets the item_major_group_id of this OrderLine.


        :return: The item_major_group_id of this OrderLine.
        :rtype: int
        """
        return self._item_major_group_id

    @item_major_group_id.setter
    def item_major_group_id(self, item_major_group_id):
        """
        Sets the item_major_group_id of this OrderLine.


        :param item_major_group_id: The item_major_group_id of this OrderLine.
        :type: int
        """
        self._item_major_group_id = item_major_group_id

    @property
    def item_sub_group_id(self):
        """
        Gets the item_sub_group_id of this OrderLine.


        :return: The item_sub_group_id of this OrderLine.
        :rtype: int
        """
        return self._item_sub_group_id

    @item_sub_group_id.setter
    def item_sub_group_id(self, item_sub_group_id):
        """
        Sets the item_sub_group_id of this OrderLine.


        :param item_sub_group_id: The item_sub_group_id of this OrderLine.
        :type: int
        """
        self._item_sub_group_id = item_sub_group_id

    @property
    def item_product_code_id(self):
        """
        Gets the item_product_code_id of this OrderLine.


        :return: The item_product_code_id of this OrderLine.
        :rtype: int
        """
        return self._item_product_code_id

    @item_product_code_id.setter
    def item_product_code_id(self, item_product_code_id):
        """
        Sets the item_product_code_id of this OrderLine.


        :param item_product_code_id: The item_product_code_id of this OrderLine.
        :type: int
        """
        self._item_product_code_id = item_product_code_id

    @property
    def item_summary_code_id(self):
        """
        Gets the item_summary_code_id of this OrderLine.


        :return: The item_summary_code_id of this OrderLine.
        :rtype: int
        """
        return self._item_summary_code_id

    @item_summary_code_id.setter
    def item_summary_code_id(self, item_summary_code_id):
        """
        Sets the item_summary_code_id of this OrderLine.


        :param item_summary_code_id: The item_summary_code_id of this OrderLine.
        :type: int
        """
        self._item_summary_code_id = item_summary_code_id

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this OrderLine.


        :return: The custom_fields of this OrderLine.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this OrderLine.


        :param custom_fields: The custom_fields of this OrderLine.
        :type: dict(str, object)
        """
        self._custom_fields = custom_fields

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

