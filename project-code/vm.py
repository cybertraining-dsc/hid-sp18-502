# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.vm_hardware_profile import VMHardwareProfile  # noqa: F401,E501
from swagger_server.models.vm_network_profile import VMNetworkProfile  # noqa: F401,E501
from swagger_server.models.vm_os_profile import VMOsProfile  # noqa: F401,E501
from swagger_server.models.vm_storage_profile import VMStorageProfile  # noqa: F401,E501
from swagger_server import util


class VM(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, identity=None, os_profile=None, storage_profile=None, name=None, tags=None, vm_id=None, hardware_profile=None, provisioning_state=None, network_profile=None, type=None, id=None, location=None):  # noqa: E501
        """VM - a model defined in Swagger

        :param identity: The identity of this VM.  # noqa: E501
        :type identity: str
        :param os_profile: The os_profile of this VM.  # noqa: E501
        :type os_profile: VMOsProfile
        :param storage_profile: The storage_profile of this VM.  # noqa: E501
        :type storage_profile: VMStorageProfile
        :param name: The name of this VM.  # noqa: E501
        :type name: str
        :param tags: The tags of this VM.  # noqa: E501
        :type tags: str
        :param vm_id: The vm_id of this VM.  # noqa: E501
        :type vm_id: str
        :param hardware_profile: The hardware_profile of this VM.  # noqa: E501
        :type hardware_profile: VMHardwareProfile
        :param provisioning_state: The provisioning_state of this VM.  # noqa: E501
        :type provisioning_state: str
        :param network_profile: The network_profile of this VM.  # noqa: E501
        :type network_profile: VMNetworkProfile
        :param type: The type of this VM.  # noqa: E501
        :type type: str
        :param id: The id of this VM.  # noqa: E501
        :type id: str
        :param location: The location of this VM.  # noqa: E501
        :type location: str
        """
        self.swagger_types = {
            'identity': str,
            'os_profile': VMOsProfile,
            'storage_profile': VMStorageProfile,
            'name': str,
            'tags': str,
            'vm_id': str,
            'hardware_profile': VMHardwareProfile,
            'provisioning_state': str,
            'network_profile': VMNetworkProfile,
            'type': str,
            'id': str,
            'location': str
        }

        self.attribute_map = {
            'identity': 'identity',
            'os_profile': 'os_profile',
            'storage_profile': 'storage_profile',
            'name': 'name',
            'tags': 'tags',
            'vm_id': 'vm_id',
            'hardware_profile': 'hardware_profile',
            'provisioning_state': 'provisioning_state',
            'network_profile': 'network_profile',
            'type': 'type',
            'id': 'id',
            'location': 'location'
        }

        self._identity = identity
        self._os_profile = os_profile
        self._storage_profile = storage_profile
        self._name = name
        self._tags = tags
        self._vm_id = vm_id
        self._hardware_profile = hardware_profile
        self._provisioning_state = provisioning_state
        self._network_profile = network_profile
        self._type = type
        self._id = id
        self._location = location

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VM of this VM.  # noqa: E501
        :rtype: VM
        """
        return util.deserialize_model(dikt, cls)

    @property
    def identity(self):
        """Gets the identity of this VM.


        :return: The identity of this VM.
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this VM.


        :param identity: The identity of this VM.
        :type identity: str
        """

        self._identity = identity

    @property
    def os_profile(self):
        """Gets the os_profile of this VM.


        :return: The os_profile of this VM.
        :rtype: VMOsProfile
        """
        return self._os_profile

    @os_profile.setter
    def os_profile(self, os_profile):
        """Sets the os_profile of this VM.


        :param os_profile: The os_profile of this VM.
        :type os_profile: VMOsProfile
        """

        self._os_profile = os_profile

    @property
    def storage_profile(self):
        """Gets the storage_profile of this VM.


        :return: The storage_profile of this VM.
        :rtype: VMStorageProfile
        """
        return self._storage_profile

    @storage_profile.setter
    def storage_profile(self, storage_profile):
        """Sets the storage_profile of this VM.


        :param storage_profile: The storage_profile of this VM.
        :type storage_profile: VMStorageProfile
        """

        self._storage_profile = storage_profile

    @property
    def name(self):
        """Gets the name of this VM.


        :return: The name of this VM.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VM.


        :param name: The name of this VM.
        :type name: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this VM.


        :return: The tags of this VM.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VM.


        :param tags: The tags of this VM.
        :type tags: str
        """

        self._tags = tags

    @property
    def vm_id(self):
        """Gets the vm_id of this VM.


        :return: The vm_id of this VM.
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this VM.


        :param vm_id: The vm_id of this VM.
        :type vm_id: str
        """

        self._vm_id = vm_id

    @property
    def hardware_profile(self):
        """Gets the hardware_profile of this VM.


        :return: The hardware_profile of this VM.
        :rtype: VMHardwareProfile
        """
        return self._hardware_profile

    @hardware_profile.setter
    def hardware_profile(self, hardware_profile):
        """Sets the hardware_profile of this VM.


        :param hardware_profile: The hardware_profile of this VM.
        :type hardware_profile: VMHardwareProfile
        """

        self._hardware_profile = hardware_profile

    @property
    def provisioning_state(self):
        """Gets the provisioning_state of this VM.


        :return: The provisioning_state of this VM.
        :rtype: str
        """
        return self._provisioning_state

    @provisioning_state.setter
    def provisioning_state(self, provisioning_state):
        """Sets the provisioning_state of this VM.


        :param provisioning_state: The provisioning_state of this VM.
        :type provisioning_state: str
        """

        self._provisioning_state = provisioning_state

    @property
    def network_profile(self):
        """Gets the network_profile of this VM.


        :return: The network_profile of this VM.
        :rtype: VMNetworkProfile
        """
        return self._network_profile

    @network_profile.setter
    def network_profile(self, network_profile):
        """Sets the network_profile of this VM.


        :param network_profile: The network_profile of this VM.
        :type network_profile: VMNetworkProfile
        """

        self._network_profile = network_profile

    @property
    def type(self):
        """Gets the type of this VM.


        :return: The type of this VM.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VM.


        :param type: The type of this VM.
        :type type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this VM.


        :return: The id of this VM.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VM.


        :param id: The id of this VM.
        :type id: str
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this VM.


        :return: The location of this VM.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this VM.


        :param location: The location of this VM.
        :type location: str
        """

        self._location = location
