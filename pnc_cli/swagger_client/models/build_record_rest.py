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


class BuildRecordRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuildRecordRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'submit_time': 'datetime',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'status': 'str',
            'build_configuration_id': 'int',
            'build_configuration_rev': 'int',
            'user_id': 'int',
            'scm_repo_url': 'str',
            'scm_revision': 'str',
            'build_driver_id': 'str',
            'system_image_id': 'int',
            'external_archive_id': 'int',
            'live_logs_uri': 'str',
            'build_config_set_record_id': 'int',
            'build_content_id': 'str',
            'build_record_set_ids': 'list[int]',
            'performed_milestone_build_record_set_ids': 'list[int]',
            'distributed_milestone_build_record_set_ids': 'list[int]'
        }

        self.attribute_map = {
            'id': 'id',
            'submit_time': 'submitTime',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'status': 'status',
            'build_configuration_id': 'buildConfigurationId',
            'build_configuration_rev': 'buildConfigurationRev',
            'user_id': 'userId',
            'scm_repo_url': 'scmRepoURL',
            'scm_revision': 'scmRevision',
            'build_driver_id': 'buildDriverId',
            'system_image_id': 'systemImageId',
            'external_archive_id': 'externalArchiveId',
            'live_logs_uri': 'liveLogsUri',
            'build_config_set_record_id': 'buildConfigSetRecordId',
            'build_content_id': 'buildContentId',
            'build_record_set_ids': 'buildRecordSetIds',
            'performed_milestone_build_record_set_ids': 'performedMilestoneBuildRecordSetIds',
            'distributed_milestone_build_record_set_ids': 'distributedMilestoneBuildRecordSetIds'
        }

        self._id = None
        self._submit_time = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._build_configuration_id = None
        self._build_configuration_rev = None
        self._user_id = None
        self._scm_repo_url = None
        self._scm_revision = None
        self._build_driver_id = None
        self._system_image_id = None
        self._external_archive_id = None
        self._live_logs_uri = None
        self._build_config_set_record_id = None
        self._build_content_id = None
        self._build_record_set_ids = None
        self._performed_milestone_build_record_set_ids = None
        self._distributed_milestone_build_record_set_ids = None

    @property
    def id(self):
        """
        Gets the id of this BuildRecordRest.


        :return: The id of this BuildRecordRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildRecordRest.


        :param id: The id of this BuildRecordRest.
        :type: int
        """
        self._id = id

    @property
    def submit_time(self):
        """
        Gets the submit_time of this BuildRecordRest.


        :return: The submit_time of this BuildRecordRest.
        :rtype: datetime
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """
        Sets the submit_time of this BuildRecordRest.


        :param submit_time: The submit_time of this BuildRecordRest.
        :type: datetime
        """
        self._submit_time = submit_time

    @property
    def start_time(self):
        """
        Gets the start_time of this BuildRecordRest.


        :return: The start_time of this BuildRecordRest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this BuildRecordRest.


        :param start_time: The start_time of this BuildRecordRest.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this BuildRecordRest.


        :return: The end_time of this BuildRecordRest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this BuildRecordRest.


        :param end_time: The end_time of this BuildRecordRest.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def status(self):
        """
        Gets the status of this BuildRecordRest.


        :return: The status of this BuildRecordRest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BuildRecordRest.


        :param status: The status of this BuildRecordRest.
        :type: str
        """
        self._status = status

    @property
    def build_configuration_id(self):
        """
        Gets the build_configuration_id of this BuildRecordRest.


        :return: The build_configuration_id of this BuildRecordRest.
        :rtype: int
        """
        return self._build_configuration_id

    @build_configuration_id.setter
    def build_configuration_id(self, build_configuration_id):
        """
        Sets the build_configuration_id of this BuildRecordRest.


        :param build_configuration_id: The build_configuration_id of this BuildRecordRest.
        :type: int
        """
        self._build_configuration_id = build_configuration_id

    @property
    def build_configuration_rev(self):
        """
        Gets the build_configuration_rev of this BuildRecordRest.


        :return: The build_configuration_rev of this BuildRecordRest.
        :rtype: int
        """
        return self._build_configuration_rev

    @build_configuration_rev.setter
    def build_configuration_rev(self, build_configuration_rev):
        """
        Sets the build_configuration_rev of this BuildRecordRest.


        :param build_configuration_rev: The build_configuration_rev of this BuildRecordRest.
        :type: int
        """
        self._build_configuration_rev = build_configuration_rev

    @property
    def user_id(self):
        """
        Gets the user_id of this BuildRecordRest.


        :return: The user_id of this BuildRecordRest.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this BuildRecordRest.


        :param user_id: The user_id of this BuildRecordRest.
        :type: int
        """
        self._user_id = user_id

    @property
    def scm_repo_url(self):
        """
        Gets the scm_repo_url of this BuildRecordRest.


        :return: The scm_repo_url of this BuildRecordRest.
        :rtype: str
        """
        return self._scm_repo_url

    @scm_repo_url.setter
    def scm_repo_url(self, scm_repo_url):
        """
        Sets the scm_repo_url of this BuildRecordRest.


        :param scm_repo_url: The scm_repo_url of this BuildRecordRest.
        :type: str
        """
        self._scm_repo_url = scm_repo_url

    @property
    def scm_revision(self):
        """
        Gets the scm_revision of this BuildRecordRest.


        :return: The scm_revision of this BuildRecordRest.
        :rtype: str
        """
        return self._scm_revision

    @scm_revision.setter
    def scm_revision(self, scm_revision):
        """
        Sets the scm_revision of this BuildRecordRest.


        :param scm_revision: The scm_revision of this BuildRecordRest.
        :type: str
        """
        self._scm_revision = scm_revision

    @property
    def build_driver_id(self):
        """
        Gets the build_driver_id of this BuildRecordRest.


        :return: The build_driver_id of this BuildRecordRest.
        :rtype: str
        """
        return self._build_driver_id

    @build_driver_id.setter
    def build_driver_id(self, build_driver_id):
        """
        Sets the build_driver_id of this BuildRecordRest.


        :param build_driver_id: The build_driver_id of this BuildRecordRest.
        :type: str
        """
        self._build_driver_id = build_driver_id

    @property
    def system_image_id(self):
        """
        Gets the system_image_id of this BuildRecordRest.


        :return: The system_image_id of this BuildRecordRest.
        :rtype: int
        """
        return self._system_image_id

    @system_image_id.setter
    def system_image_id(self, system_image_id):
        """
        Sets the system_image_id of this BuildRecordRest.


        :param system_image_id: The system_image_id of this BuildRecordRest.
        :type: int
        """
        self._system_image_id = system_image_id

    @property
    def external_archive_id(self):
        """
        Gets the external_archive_id of this BuildRecordRest.


        :return: The external_archive_id of this BuildRecordRest.
        :rtype: int
        """
        return self._external_archive_id

    @external_archive_id.setter
    def external_archive_id(self, external_archive_id):
        """
        Sets the external_archive_id of this BuildRecordRest.


        :param external_archive_id: The external_archive_id of this BuildRecordRest.
        :type: int
        """
        self._external_archive_id = external_archive_id

    @property
    def live_logs_uri(self):
        """
        Gets the live_logs_uri of this BuildRecordRest.


        :return: The live_logs_uri of this BuildRecordRest.
        :rtype: str
        """
        return self._live_logs_uri

    @live_logs_uri.setter
    def live_logs_uri(self, live_logs_uri):
        """
        Sets the live_logs_uri of this BuildRecordRest.


        :param live_logs_uri: The live_logs_uri of this BuildRecordRest.
        :type: str
        """
        self._live_logs_uri = live_logs_uri

    @property
    def build_config_set_record_id(self):
        """
        Gets the build_config_set_record_id of this BuildRecordRest.


        :return: The build_config_set_record_id of this BuildRecordRest.
        :rtype: int
        """
        return self._build_config_set_record_id

    @build_config_set_record_id.setter
    def build_config_set_record_id(self, build_config_set_record_id):
        """
        Sets the build_config_set_record_id of this BuildRecordRest.


        :param build_config_set_record_id: The build_config_set_record_id of this BuildRecordRest.
        :type: int
        """
        self._build_config_set_record_id = build_config_set_record_id

    @property
    def build_content_id(self):
        """
        Gets the build_content_id of this BuildRecordRest.


        :return: The build_content_id of this BuildRecordRest.
        :rtype: str
        """
        return self._build_content_id

    @build_content_id.setter
    def build_content_id(self, build_content_id):
        """
        Sets the build_content_id of this BuildRecordRest.


        :param build_content_id: The build_content_id of this BuildRecordRest.
        :type: str
        """
        self._build_content_id = build_content_id

    @property
    def build_record_set_ids(self):
        """
        Gets the build_record_set_ids of this BuildRecordRest.


        :return: The build_record_set_ids of this BuildRecordRest.
        :rtype: list[int]
        """
        return self._build_record_set_ids

    @build_record_set_ids.setter
    def build_record_set_ids(self, build_record_set_ids):
        """
        Sets the build_record_set_ids of this BuildRecordRest.


        :param build_record_set_ids: The build_record_set_ids of this BuildRecordRest.
        :type: list[int]
        """
        self._build_record_set_ids = build_record_set_ids

    @property
    def performed_milestone_build_record_set_ids(self):
        """
        Gets the performed_milestone_build_record_set_ids of this BuildRecordRest.


        :return: The performed_milestone_build_record_set_ids of this BuildRecordRest.
        :rtype: list[int]
        """
        return self._performed_milestone_build_record_set_ids

    @performed_milestone_build_record_set_ids.setter
    def performed_milestone_build_record_set_ids(self, performed_milestone_build_record_set_ids):
        """
        Sets the performed_milestone_build_record_set_ids of this BuildRecordRest.


        :param performed_milestone_build_record_set_ids: The performed_milestone_build_record_set_ids of this BuildRecordRest.
        :type: list[int]
        """
        self._performed_milestone_build_record_set_ids = performed_milestone_build_record_set_ids

    @property
    def distributed_milestone_build_record_set_ids(self):
        """
        Gets the distributed_milestone_build_record_set_ids of this BuildRecordRest.


        :return: The distributed_milestone_build_record_set_ids of this BuildRecordRest.
        :rtype: list[int]
        """
        return self._distributed_milestone_build_record_set_ids

    @distributed_milestone_build_record_set_ids.setter
    def distributed_milestone_build_record_set_ids(self, distributed_milestone_build_record_set_ids):
        """
        Sets the distributed_milestone_build_record_set_ids of this BuildRecordRest.


        :param distributed_milestone_build_record_set_ids: The distributed_milestone_build_record_set_ids of this BuildRecordRest.
        :type: list[int]
        """
        self._distributed_milestone_build_record_set_ids = distributed_milestone_build_record_set_ids

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
