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

__all__ = [
    'GetGroupsResult',
    'AwaitableGetGroupsResult',
    'get_groups',
    'get_groups_output',
]

@pulumi.output_type
class GetGroupsResult:
    """
    A collection of values returned by getGroups.
    """
    def __init__(__self__, groups=None, id=None, identity_store_id=None):
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_store_id and not isinstance(identity_store_id, str):
            raise TypeError("Expected argument 'identity_store_id' to be a str")
        pulumi.set(__self__, "identity_store_id", identity_store_id)

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.GetGroupsGroupResult']:
        """
        List of Identity Store Groups
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> str:
        return pulumi.get(self, "identity_store_id")


class AwaitableGetGroupsResult(GetGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupsResult(
            groups=self.groups,
            id=self.id,
            identity_store_id=self.identity_store_id)


def get_groups(identity_store_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupsResult:
    """
    Data source for managing an AWS SSO Identity Store Groups.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ssoadmin.get_instances()
    example_get_groups = aws.identitystore.get_groups(identity_store_id=example.identity_store_ids[0])
    ```


    :param str identity_store_id: Identity Store ID associated with the Single Sign-On (SSO) Instance.
    """
    __args__ = dict()
    __args__['identityStoreId'] = identity_store_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:identitystore/getGroups:getGroups', __args__, opts=opts, typ=GetGroupsResult).value

    return AwaitableGetGroupsResult(
        groups=pulumi.get(__ret__, 'groups'),
        id=pulumi.get(__ret__, 'id'),
        identity_store_id=pulumi.get(__ret__, 'identity_store_id'))
def get_groups_output(identity_store_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupsResult]:
    """
    Data source for managing an AWS SSO Identity Store Groups.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ssoadmin.get_instances()
    example_get_groups = aws.identitystore.get_groups(identity_store_id=example.identity_store_ids[0])
    ```


    :param str identity_store_id: Identity Store ID associated with the Single Sign-On (SSO) Instance.
    """
    __args__ = dict()
    __args__['identityStoreId'] = identity_store_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:identitystore/getGroups:getGroups', __args__, opts=opts, typ=GetGroupsResult)
    return __ret__.apply(lambda __response__: GetGroupsResult(
        groups=pulumi.get(__response__, 'groups'),
        id=pulumi.get(__response__, 'id'),
        identity_store_id=pulumi.get(__response__, 'identity_store_id')))
