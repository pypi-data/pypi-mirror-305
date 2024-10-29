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

__all__ = [
    'GetAclResult',
    'AwaitableGetAclResult',
    'get_acl',
    'get_acl_output',
]

@pulumi.output_type
class GetAclResult:
    """
    A collection of values returned by getAcl.
    """
    def __init__(__self__, arn=None, id=None, minimum_engine_version=None, name=None, tags=None, user_names=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if minimum_engine_version and not isinstance(minimum_engine_version, str):
            raise TypeError("Expected argument 'minimum_engine_version' to be a str")
        pulumi.set(__self__, "minimum_engine_version", minimum_engine_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if user_names and not isinstance(user_names, list):
            raise TypeError("Expected argument 'user_names' to be a list")
        pulumi.set(__self__, "user_names", user_names)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the ACL.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="minimumEngineVersion")
    def minimum_engine_version(self) -> str:
        """
        The minimum engine version supported by the ACL.
        """
        return pulumi.get(self, "minimum_engine_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Map of tags assigned to the ACL.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userNames")
    def user_names(self) -> Sequence[str]:
        """
        Set of MemoryDB user names included in this ACL.
        """
        return pulumi.get(self, "user_names")


class AwaitableGetAclResult(GetAclResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAclResult(
            arn=self.arn,
            id=self.id,
            minimum_engine_version=self.minimum_engine_version,
            name=self.name,
            tags=self.tags,
            user_names=self.user_names)


def get_acl(name: Optional[str] = None,
            tags: Optional[Mapping[str, str]] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAclResult:
    """
    Provides information about a MemoryDB ACL.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.memorydb.get_acl(name="my-acl")
    ```


    :param str name: Name of the ACL.
    :param Mapping[str, str] tags: Map of tags assigned to the ACL.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:memorydb/getAcl:getAcl', __args__, opts=opts, typ=GetAclResult).value

    return AwaitableGetAclResult(
        arn=pulumi.get(__ret__, 'arn'),
        id=pulumi.get(__ret__, 'id'),
        minimum_engine_version=pulumi.get(__ret__, 'minimum_engine_version'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'),
        user_names=pulumi.get(__ret__, 'user_names'))
def get_acl_output(name: Optional[pulumi.Input[str]] = None,
                   tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAclResult]:
    """
    Provides information about a MemoryDB ACL.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.memorydb.get_acl(name="my-acl")
    ```


    :param str name: Name of the ACL.
    :param Mapping[str, str] tags: Map of tags assigned to the ACL.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:memorydb/getAcl:getAcl', __args__, opts=opts, typ=GetAclResult)
    return __ret__.apply(lambda __response__: GetAclResult(
        arn=pulumi.get(__response__, 'arn'),
        id=pulumi.get(__response__, 'id'),
        minimum_engine_version=pulumi.get(__response__, 'minimum_engine_version'),
        name=pulumi.get(__response__, 'name'),
        tags=pulumi.get(__response__, 'tags'),
        user_names=pulumi.get(__response__, 'user_names')))
