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

try:
    from ._models_py3 import AaaaRecord
    from ._models_py3 import ARecord
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import CnameRecord
    from ._models_py3 import MxRecord
    from ._models_py3 import NsRecord
    from ._models_py3 import ProxyResource
    from ._models_py3 import PtrRecord
    from ._models_py3 import RecordSet
    from ._models_py3 import RecordSetUpdateParameters
    from ._models_py3 import Resource
    from ._models_py3 import SoaRecord
    from ._models_py3 import SrvRecord
    from ._models_py3 import TrackedResource
    from ._models_py3 import TxtRecord
    from ._models_py3 import Zone
    from ._models_py3 import ZoneDeleteResult
except (SyntaxError, ImportError):
    from ._models import AaaaRecord
    from ._models import ARecord
    from ._models import AzureEntityResource
    from ._models import CnameRecord
    from ._models import MxRecord
    from ._models import NsRecord
    from ._models import ProxyResource
    from ._models import PtrRecord
    from ._models import RecordSet
    from ._models import RecordSetUpdateParameters
    from ._models import Resource
    from ._models import SoaRecord
    from ._models import SrvRecord
    from ._models import TrackedResource
    from ._models import TxtRecord
    from ._models import Zone
    from ._models import ZoneDeleteResult
from ._paged_models import RecordSetPaged
from ._paged_models import ZonePaged
from ._dns_management_client_enums import (
    OperationStatus,
    HttpStatusCode,
    RecordType,
)

__all__ = [
    'AaaaRecord',
    'ARecord',
    'AzureEntityResource',
    'CnameRecord',
    'MxRecord',
    'NsRecord',
    'ProxyResource',
    'PtrRecord',
    'RecordSet',
    'RecordSetUpdateParameters',
    'Resource',
    'SoaRecord',
    'SrvRecord',
    'TrackedResource',
    'TxtRecord',
    'Zone',
    'ZoneDeleteResult',
    'RecordSetPaged',
    'ZonePaged',
    'OperationStatus',
    'HttpStatusCode',
    'RecordType',
]
