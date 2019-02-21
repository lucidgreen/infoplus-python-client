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


class JobStep(object):
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
        'sequence_no': 'int',
        'name': 'str',
        'assembly_instructions': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'sequence_no': 'sequenceNo',
        'name': 'name',
        'assembly_instructions': 'assemblyInstructions',
        'custom_fields': 'customFields'
    }

    def __init__(self, sequence_no=None, name=None, assembly_instructions=None, custom_fields=None):  # noqa: E501
        """JobStep - a model defined in Swagger"""  # noqa: E501

        self._sequence_no = None
        self._name = None
        self._assembly_instructions = None
        self._custom_fields = None
        self.discriminator = None

        if sequence_no is not None:
            self.sequence_no = sequence_no
        self.name = name
        if assembly_instructions is not None:
            self.assembly_instructions = assembly_instructions
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def sequence_no(self):
        """Gets the sequence_no of this JobStep.  # noqa: E501


        :return: The sequence_no of this JobStep.  # noqa: E501
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        """Sets the sequence_no of this JobStep.


        :param sequence_no: The sequence_no of this JobStep.  # noqa: E501
        :type: int
        """

        self._sequence_no = sequence_no

    @property
    def name(self):
        """Gets the name of this JobStep.  # noqa: E501


        :return: The name of this JobStep.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobStep.


        :param name: The name of this JobStep.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def assembly_instructions(self):
        """Gets the assembly_instructions of this JobStep.  # noqa: E501


        :return: The assembly_instructions of this JobStep.  # noqa: E501
        :rtype: str
        """
        return self._assembly_instructions

    @assembly_instructions.setter
    def assembly_instructions(self, assembly_instructions):
        """Sets the assembly_instructions of this JobStep.


        :param assembly_instructions: The assembly_instructions of this JobStep.  # noqa: E501
        :type: str
        """

        self._assembly_instructions = assembly_instructions

    @property
    def custom_fields(self):
        """Gets the custom_fields of this JobStep.  # noqa: E501


        :return: The custom_fields of this JobStep.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this JobStep.


        :param custom_fields: The custom_fields of this JobStep.  # noqa: E501
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
        if not isinstance(other, JobStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other