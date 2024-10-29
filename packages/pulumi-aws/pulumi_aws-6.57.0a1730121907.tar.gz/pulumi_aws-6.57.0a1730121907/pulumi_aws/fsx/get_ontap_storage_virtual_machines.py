# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetOntapStorageVirtualMachinesResult',
    'AwaitableGetOntapStorageVirtualMachinesResult',
    'get_ontap_storage_virtual_machines',
    'get_ontap_storage_virtual_machines_output',
]

@pulumi.output_type
class GetOntapStorageVirtualMachinesResult:
    """
    A collection of values returned by getOntapStorageVirtualMachines.
    """
    def __init__(__self__, filters=None, id=None, ids=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetOntapStorageVirtualMachinesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        List of all SVM IDs found.
        """
        return pulumi.get(self, "ids")


class AwaitableGetOntapStorageVirtualMachinesResult(GetOntapStorageVirtualMachinesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOntapStorageVirtualMachinesResult(
            filters=self.filters,
            id=self.id,
            ids=self.ids)


def get_ontap_storage_virtual_machines(filters: Optional[Sequence[Union['GetOntapStorageVirtualMachinesFilterArgs', 'GetOntapStorageVirtualMachinesFilterArgsDict']]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOntapStorageVirtualMachinesResult:
    """
    This resource can be useful for getting back a set of FSx ONTAP Storage Virtual Machine (SVM) IDs.

    ## Example Usage

    The following shows outputting all SVM IDs for a given FSx ONTAP File System.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.fsx.get_ontap_storage_virtual_machines(filters=[{
        "name": "file-system-id",
        "values": ["fs-12345678"],
    }])
    ```


    :param Sequence[Union['GetOntapStorageVirtualMachinesFilterArgs', 'GetOntapStorageVirtualMachinesFilterArgsDict']] filters: Configuration block. Detailed below.
    """
    __args__ = dict()
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:fsx/getOntapStorageVirtualMachines:getOntapStorageVirtualMachines', __args__, opts=opts, typ=GetOntapStorageVirtualMachinesResult).value

    return AwaitableGetOntapStorageVirtualMachinesResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'))
def get_ontap_storage_virtual_machines_output(filters: Optional[pulumi.Input[Optional[Sequence[Union['GetOntapStorageVirtualMachinesFilterArgs', 'GetOntapStorageVirtualMachinesFilterArgsDict']]]]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOntapStorageVirtualMachinesResult]:
    """
    This resource can be useful for getting back a set of FSx ONTAP Storage Virtual Machine (SVM) IDs.

    ## Example Usage

    The following shows outputting all SVM IDs for a given FSx ONTAP File System.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.fsx.get_ontap_storage_virtual_machines(filters=[{
        "name": "file-system-id",
        "values": ["fs-12345678"],
    }])
    ```


    :param Sequence[Union['GetOntapStorageVirtualMachinesFilterArgs', 'GetOntapStorageVirtualMachinesFilterArgsDict']] filters: Configuration block. Detailed below.
    """
    __args__ = dict()
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:fsx/getOntapStorageVirtualMachines:getOntapStorageVirtualMachines', __args__, opts=opts, typ=GetOntapStorageVirtualMachinesResult)
    return __ret__.apply(lambda __response__: GetOntapStorageVirtualMachinesResult(
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        ids=pulumi.get(__response__, 'ids')))
