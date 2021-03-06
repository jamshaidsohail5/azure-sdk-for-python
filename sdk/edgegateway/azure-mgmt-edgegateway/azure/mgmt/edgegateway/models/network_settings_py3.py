# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .arm_base_model_py3 import ARMBaseModel


class NetworkSettings(ARMBaseModel):
    """The network settings of a device.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The path ID that uniquely identifies the object.
    :vartype id: str
    :ivar name: The object name.
    :vartype name: str
    :ivar type: The hierarchical type of the object.
    :vartype type: str
    :ivar network_adapters: The network adapter list on the device.
    :vartype network_adapters:
     list[~azure.mgmt.edgegateway.models.NetworkAdapter]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'network_adapters': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'network_adapters': {'key': 'properties.networkAdapters', 'type': '[NetworkAdapter]'},
    }

    def __init__(self, **kwargs) -> None:
        super(NetworkSettings, self).__init__(**kwargs)
        self.network_adapters = None
