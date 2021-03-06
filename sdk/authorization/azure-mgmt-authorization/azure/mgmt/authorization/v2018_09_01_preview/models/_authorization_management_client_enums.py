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

from enum import Enum


class PrincipalType(str, Enum):

    user = "User"
    group = "Group"
    service_principal = "ServicePrincipal"
    unknown = "Unknown"
    directory_role_template = "DirectoryRoleTemplate"
    foreign_group = "ForeignGroup"
    application = "Application"
    msi = "MSI"
    directory_object_or_group = "DirectoryObjectOrGroup"
    everyone = "Everyone"
