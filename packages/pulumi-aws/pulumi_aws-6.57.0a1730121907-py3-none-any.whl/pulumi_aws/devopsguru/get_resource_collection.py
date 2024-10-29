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
    'GetResourceCollectionResult',
    'AwaitableGetResourceCollectionResult',
    'get_resource_collection',
    'get_resource_collection_output',
]

@pulumi.output_type
class GetResourceCollectionResult:
    """
    A collection of values returned by getResourceCollection.
    """
    def __init__(__self__, cloudformations=None, id=None, tags=None, type=None):
        if cloudformations and not isinstance(cloudformations, list):
            raise TypeError("Expected argument 'cloudformations' to be a list")
        pulumi.set(__self__, "cloudformations", cloudformations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def cloudformations(self) -> Optional[Sequence['outputs.GetResourceCollectionCloudformationResult']]:
        """
        A collection of AWS CloudFormation stacks. See `cloudformation` below for additional details.
        """
        return pulumi.get(self, "cloudformations")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Type of AWS resource collection to create (same value as `type`).
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.GetResourceCollectionTagResult']]:
        """
        AWS tags used to filter the resources in the resource collection. See `tags` below for additional details.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


class AwaitableGetResourceCollectionResult(GetResourceCollectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceCollectionResult(
            cloudformations=self.cloudformations,
            id=self.id,
            tags=self.tags,
            type=self.type)


def get_resource_collection(cloudformations: Optional[Sequence[Union['GetResourceCollectionCloudformationArgs', 'GetResourceCollectionCloudformationArgsDict']]] = None,
                            tags: Optional[Sequence[Union['GetResourceCollectionTagArgs', 'GetResourceCollectionTagArgsDict']]] = None,
                            type: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceCollectionResult:
    """
    Data source for managing an AWS DevOps Guru Resource Collection.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.devopsguru.get_resource_collection(type="AWS_SERVICE")
    ```


    :param Sequence[Union['GetResourceCollectionCloudformationArgs', 'GetResourceCollectionCloudformationArgsDict']] cloudformations: A collection of AWS CloudFormation stacks. See `cloudformation` below for additional details.
    :param Sequence[Union['GetResourceCollectionTagArgs', 'GetResourceCollectionTagArgsDict']] tags: AWS tags used to filter the resources in the resource collection. See `tags` below for additional details.
    :param str type: Type of AWS resource collection to create. Valid values are `AWS_CLOUD_FORMATION`, `AWS_SERVICE`, and `AWS_TAGS`.
    """
    __args__ = dict()
    __args__['cloudformations'] = cloudformations
    __args__['tags'] = tags
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:devopsguru/getResourceCollection:getResourceCollection', __args__, opts=opts, typ=GetResourceCollectionResult).value

    return AwaitableGetResourceCollectionResult(
        cloudformations=pulumi.get(__ret__, 'cloudformations'),
        id=pulumi.get(__ret__, 'id'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))
def get_resource_collection_output(cloudformations: Optional[pulumi.Input[Optional[Sequence[Union['GetResourceCollectionCloudformationArgs', 'GetResourceCollectionCloudformationArgsDict']]]]] = None,
                                   tags: Optional[pulumi.Input[Optional[Sequence[Union['GetResourceCollectionTagArgs', 'GetResourceCollectionTagArgsDict']]]]] = None,
                                   type: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceCollectionResult]:
    """
    Data source for managing an AWS DevOps Guru Resource Collection.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.devopsguru.get_resource_collection(type="AWS_SERVICE")
    ```


    :param Sequence[Union['GetResourceCollectionCloudformationArgs', 'GetResourceCollectionCloudformationArgsDict']] cloudformations: A collection of AWS CloudFormation stacks. See `cloudformation` below for additional details.
    :param Sequence[Union['GetResourceCollectionTagArgs', 'GetResourceCollectionTagArgsDict']] tags: AWS tags used to filter the resources in the resource collection. See `tags` below for additional details.
    :param str type: Type of AWS resource collection to create. Valid values are `AWS_CLOUD_FORMATION`, `AWS_SERVICE`, and `AWS_TAGS`.
    """
    __args__ = dict()
    __args__['cloudformations'] = cloudformations
    __args__['tags'] = tags
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:devopsguru/getResourceCollection:getResourceCollection', __args__, opts=opts, typ=GetResourceCollectionResult)
    return __ret__.apply(lambda __response__: GetResourceCollectionResult(
        cloudformations=pulumi.get(__response__, 'cloudformations'),
        id=pulumi.get(__response__, 'id'),
        tags=pulumi.get(__response__, 'tags'),
        type=pulumi.get(__response__, 'type')))
