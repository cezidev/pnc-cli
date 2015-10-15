# coding: utf-8

"""
Copyright 2015 SmartBear Software

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

from datetime import datetime
from pprint import pformat
from six import iteritems


class BuildRecordSetRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuildRecordSetRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'performed_in_product_milestone_id': 'int',
            'distributed_in_product_milestone_id': 'int',
            'build_record_ids': 'list[int]'
        }

        self.attribute_map = {
            'id': 'id',
            'performed_in_product_milestone_id': 'performedInProductMilestoneId',
            'distributed_in_product_milestone_id': 'distributedInProductMilestoneId',
            'build_record_ids': 'buildRecordIds'
        }

        self._id = None
        self._performed_in_product_milestone_id = None
        self._distributed_in_product_milestone_id = None
        self._build_record_ids = None

    @property
    def id(self):
        """
        Gets the id of this BuildRecordSetRest.


        :return: The id of this BuildRecordSetRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildRecordSetRest.


        :param id: The id of this BuildRecordSetRest.
        :type: int
        """
        self._id = id

    @property
    def performed_in_product_milestone_id(self):
        """
        Gets the performed_in_product_milestone_id of this BuildRecordSetRest.


        :return: The performed_in_product_milestone_id of this BuildRecordSetRest.
        :rtype: int
        """
        return self._performed_in_product_milestone_id

    @performed_in_product_milestone_id.setter
    def performed_in_product_milestone_id(self, performed_in_product_milestone_id):
        """
        Sets the performed_in_product_milestone_id of this BuildRecordSetRest.


        :param performed_in_product_milestone_id: The performed_in_product_milestone_id of this BuildRecordSetRest.
        :type: int
        """
        self._performed_in_product_milestone_id = performed_in_product_milestone_id

    @property
    def distributed_in_product_milestone_id(self):
        """
        Gets the distributed_in_product_milestone_id of this BuildRecordSetRest.


        :return: The distributed_in_product_milestone_id of this BuildRecordSetRest.
        :rtype: int
        """
        return self._distributed_in_product_milestone_id

    @distributed_in_product_milestone_id.setter
    def distributed_in_product_milestone_id(self, distributed_in_product_milestone_id):
        """
        Sets the distributed_in_product_milestone_id of this BuildRecordSetRest.


        :param distributed_in_product_milestone_id: The distributed_in_product_milestone_id of this BuildRecordSetRest.
        :type: int
        """
        self._distributed_in_product_milestone_id = distributed_in_product_milestone_id

    @property
    def build_record_ids(self):
        """
        Gets the build_record_ids of this BuildRecordSetRest.


        :return: The build_record_ids of this BuildRecordSetRest.
        :rtype: list[int]
        """
        return self._build_record_ids

    @build_record_ids.setter
    def build_record_ids(self, build_record_ids):
        """
        Sets the build_record_ids of this BuildRecordSetRest.


        :param build_record_ids: The build_record_ids of this BuildRecordSetRest.
        :type: list[int]
        """
        self._build_record_ids = build_record_ids

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
	    elif isinstance(value, datetime):
		result[attr] = str(value)
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
