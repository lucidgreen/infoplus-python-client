# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BillingCodeActivity(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'imported_id': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'date': 'datetime',
        'quantity': 'float',
        'lob_id': 'int',
        'user_id': 'int',
        'email': 'str',
        'billing_code_type_id': 'int',
        'billing_code_type_name': 'str',
        'note': 'str',
        'record_type_name': 'str',
        'record_type_id': 'int',
        'record_id': 'str',
        'extended_charge': 'float',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'imported_id': 'importedId',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'date': 'date',
        'quantity': 'quantity',
        'lob_id': 'lobId',
        'user_id': 'userId',
        'email': 'email',
        'billing_code_type_id': 'billingCodeTypeId',
        'billing_code_type_name': 'billingCodeTypeName',
        'note': 'note',
        'record_type_name': 'recordTypeName',
        'record_type_id': 'recordTypeId',
        'record_id': 'recordId',
        'extended_charge': 'extendedCharge',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, imported_id=None, create_date=None, modify_date=None, date=None, quantity=None, lob_id=None, user_id=None, email=None, billing_code_type_id=None, billing_code_type_name=None, note=None, record_type_name=None, record_type_id=None, record_id=None, extended_charge=None, custom_fields=None):  # noqa: E501
        """BillingCodeActivity - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._imported_id = None
        self._create_date = None
        self._modify_date = None
        self._date = None
        self._quantity = None
        self._lob_id = None
        self._user_id = None
        self._email = None
        self._billing_code_type_id = None
        self._billing_code_type_name = None
        self._note = None
        self._record_type_name = None
        self._record_type_id = None
        self._record_id = None
        self._extended_charge = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if imported_id is not None:
            self.imported_id = imported_id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if date is not None:
            self.date = date
        self.quantity = quantity
        self.lob_id = lob_id
        self.user_id = user_id
        if email is not None:
            self.email = email
        self.billing_code_type_id = billing_code_type_id
        if billing_code_type_name is not None:
            self.billing_code_type_name = billing_code_type_name
        if note is not None:
            self.note = note
        if record_type_name is not None:
            self.record_type_name = record_type_name
        if record_type_id is not None:
            self.record_type_id = record_type_id
        if record_id is not None:
            self.record_id = record_id
        if extended_charge is not None:
            self.extended_charge = extended_charge
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this BillingCodeActivity.  # noqa: E501


        :return: The id of this BillingCodeActivity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BillingCodeActivity.


        :param id: The id of this BillingCodeActivity.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def imported_id(self):
        """Gets the imported_id of this BillingCodeActivity.  # noqa: E501


        :return: The imported_id of this BillingCodeActivity.  # noqa: E501
        :rtype: int
        """
        return self._imported_id

    @imported_id.setter
    def imported_id(self, imported_id):
        """Sets the imported_id of this BillingCodeActivity.


        :param imported_id: The imported_id of this BillingCodeActivity.  # noqa: E501
        :type: int
        """

        self._imported_id = imported_id

    @property
    def create_date(self):
        """Gets the create_date of this BillingCodeActivity.  # noqa: E501


        :return: The create_date of this BillingCodeActivity.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this BillingCodeActivity.


        :param create_date: The create_date of this BillingCodeActivity.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this BillingCodeActivity.  # noqa: E501


        :return: The modify_date of this BillingCodeActivity.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this BillingCodeActivity.


        :param modify_date: The modify_date of this BillingCodeActivity.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def date(self):
        """Gets the date of this BillingCodeActivity.  # noqa: E501


        :return: The date of this BillingCodeActivity.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this BillingCodeActivity.


        :param date: The date of this BillingCodeActivity.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def quantity(self):
        """Gets the quantity of this BillingCodeActivity.  # noqa: E501


        :return: The quantity of this BillingCodeActivity.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this BillingCodeActivity.


        :param quantity: The quantity of this BillingCodeActivity.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def lob_id(self):
        """Gets the lob_id of this BillingCodeActivity.  # noqa: E501


        :return: The lob_id of this BillingCodeActivity.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this BillingCodeActivity.


        :param lob_id: The lob_id of this BillingCodeActivity.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def user_id(self):
        """Gets the user_id of this BillingCodeActivity.  # noqa: E501


        :return: The user_id of this BillingCodeActivity.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BillingCodeActivity.


        :param user_id: The user_id of this BillingCodeActivity.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def email(self):
        """Gets the email of this BillingCodeActivity.  # noqa: E501


        :return: The email of this BillingCodeActivity.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BillingCodeActivity.


        :param email: The email of this BillingCodeActivity.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def billing_code_type_id(self):
        """Gets the billing_code_type_id of this BillingCodeActivity.  # noqa: E501


        :return: The billing_code_type_id of this BillingCodeActivity.  # noqa: E501
        :rtype: int
        """
        return self._billing_code_type_id

    @billing_code_type_id.setter
    def billing_code_type_id(self, billing_code_type_id):
        """Sets the billing_code_type_id of this BillingCodeActivity.


        :param billing_code_type_id: The billing_code_type_id of this BillingCodeActivity.  # noqa: E501
        :type: int
        """
        if billing_code_type_id is None:
            raise ValueError("Invalid value for `billing_code_type_id`, must not be `None`")  # noqa: E501

        self._billing_code_type_id = billing_code_type_id

    @property
    def billing_code_type_name(self):
        """Gets the billing_code_type_name of this BillingCodeActivity.  # noqa: E501


        :return: The billing_code_type_name of this BillingCodeActivity.  # noqa: E501
        :rtype: str
        """
        return self._billing_code_type_name

    @billing_code_type_name.setter
    def billing_code_type_name(self, billing_code_type_name):
        """Sets the billing_code_type_name of this BillingCodeActivity.


        :param billing_code_type_name: The billing_code_type_name of this BillingCodeActivity.  # noqa: E501
        :type: str
        """

        self._billing_code_type_name = billing_code_type_name

    @property
    def note(self):
        """Gets the note of this BillingCodeActivity.  # noqa: E501


        :return: The note of this BillingCodeActivity.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this BillingCodeActivity.


        :param note: The note of this BillingCodeActivity.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def record_type_name(self):
        """Gets the record_type_name of this BillingCodeActivity.  # noqa: E501


        :return: The record_type_name of this BillingCodeActivity.  # noqa: E501
        :rtype: str
        """
        return self._record_type_name

    @record_type_name.setter
    def record_type_name(self, record_type_name):
        """Sets the record_type_name of this BillingCodeActivity.


        :param record_type_name: The record_type_name of this BillingCodeActivity.  # noqa: E501
        :type: str
        """

        self._record_type_name = record_type_name

    @property
    def record_type_id(self):
        """Gets the record_type_id of this BillingCodeActivity.  # noqa: E501


        :return: The record_type_id of this BillingCodeActivity.  # noqa: E501
        :rtype: int
        """
        return self._record_type_id

    @record_type_id.setter
    def record_type_id(self, record_type_id):
        """Sets the record_type_id of this BillingCodeActivity.


        :param record_type_id: The record_type_id of this BillingCodeActivity.  # noqa: E501
        :type: int
        """

        self._record_type_id = record_type_id

    @property
    def record_id(self):
        """Gets the record_id of this BillingCodeActivity.  # noqa: E501


        :return: The record_id of this BillingCodeActivity.  # noqa: E501
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this BillingCodeActivity.


        :param record_id: The record_id of this BillingCodeActivity.  # noqa: E501
        :type: str
        """

        self._record_id = record_id

    @property
    def extended_charge(self):
        """Gets the extended_charge of this BillingCodeActivity.  # noqa: E501


        :return: The extended_charge of this BillingCodeActivity.  # noqa: E501
        :rtype: float
        """
        return self._extended_charge

    @extended_charge.setter
    def extended_charge(self, extended_charge):
        """Sets the extended_charge of this BillingCodeActivity.


        :param extended_charge: The extended_charge of this BillingCodeActivity.  # noqa: E501
        :type: float
        """

        self._extended_charge = extended_charge

    @property
    def custom_fields(self):
        """Gets the custom_fields of this BillingCodeActivity.  # noqa: E501


        :return: The custom_fields of this BillingCodeActivity.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this BillingCodeActivity.


        :param custom_fields: The custom_fields of this BillingCodeActivity.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BillingCodeActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
