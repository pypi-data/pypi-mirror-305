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
    'GetDefaultKmsKeyResult',
    'AwaitableGetDefaultKmsKeyResult',
    'get_default_kms_key',
    'get_default_kms_key_output',
]

@pulumi.output_type
class GetDefaultKmsKeyResult:
    """
    A collection of values returned by getDefaultKmsKey.
    """
    def __init__(__self__, id=None, key_arn=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_arn and not isinstance(key_arn, str):
            raise TypeError("Expected argument 'key_arn' to be a str")
        pulumi.set(__self__, "key_arn", key_arn)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> str:
        """
        ARN of the default KMS key uses to encrypt an EBS volume in this region when no key is specified in an API call that creates the volume and encryption by default is enabled.
        """
        return pulumi.get(self, "key_arn")


class AwaitableGetDefaultKmsKeyResult(GetDefaultKmsKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDefaultKmsKeyResult(
            id=self.id,
            key_arn=self.key_arn)


def get_default_kms_key(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDefaultKmsKeyResult:
    """
    Use this data source to get the default EBS encryption KMS key in the current region.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    current = aws.ebs.get_default_kms_key()
    example = aws.ebs.Volume("example",
        availability_zone="us-west-2a",
        encrypted=True,
        kms_key_id=current.key_arn)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ebs/getDefaultKmsKey:getDefaultKmsKey', __args__, opts=opts, typ=GetDefaultKmsKeyResult).value

    return AwaitableGetDefaultKmsKeyResult(
        id=pulumi.get(__ret__, 'id'),
        key_arn=pulumi.get(__ret__, 'key_arn'))
def get_default_kms_key_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDefaultKmsKeyResult]:
    """
    Use this data source to get the default EBS encryption KMS key in the current region.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    current = aws.ebs.get_default_kms_key()
    example = aws.ebs.Volume("example",
        availability_zone="us-west-2a",
        encrypted=True,
        kms_key_id=current.key_arn)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:ebs/getDefaultKmsKey:getDefaultKmsKey', __args__, opts=opts, typ=GetDefaultKmsKeyResult)
    return __ret__.apply(lambda __response__: GetDefaultKmsKeyResult(
        id=pulumi.get(__response__, 'id'),
        key_arn=pulumi.get(__response__, 'key_arn')))
