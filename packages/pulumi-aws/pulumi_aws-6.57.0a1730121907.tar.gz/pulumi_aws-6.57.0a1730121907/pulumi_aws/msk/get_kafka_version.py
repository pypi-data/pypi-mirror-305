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
    'GetKafkaVersionResult',
    'AwaitableGetKafkaVersionResult',
    'get_kafka_version',
    'get_kafka_version_output',
]

@pulumi.output_type
class GetKafkaVersionResult:
    """
    A collection of values returned by getKafkaVersion.
    """
    def __init__(__self__, id=None, preferred_versions=None, status=None, version=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if preferred_versions and not isinstance(preferred_versions, list):
            raise TypeError("Expected argument 'preferred_versions' to be a list")
        pulumi.set(__self__, "preferred_versions", preferred_versions)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="preferredVersions")
    def preferred_versions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "preferred_versions")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the MSK Kafka version eg. `ACTIVE` or `DEPRECATED`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def version(self) -> str:
        return pulumi.get(self, "version")


class AwaitableGetKafkaVersionResult(GetKafkaVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKafkaVersionResult(
            id=self.id,
            preferred_versions=self.preferred_versions,
            status=self.status,
            version=self.version)


def get_kafka_version(preferred_versions: Optional[Sequence[str]] = None,
                      version: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKafkaVersionResult:
    """
    Get information on a Amazon MSK Kafka Version

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    preferred = aws.msk.get_kafka_version(preferred_versions=[
        "2.4.1.1",
        "2.4.1",
        "2.2.1",
    ])
    example = aws.msk.get_kafka_version(version="2.8.0")
    ```


    :param Sequence[str] preferred_versions: Ordered list of preferred Kafka versions. The first match in this list will be returned. Either `preferred_versions` or `version` must be set.
    :param str version: Version of MSK Kafka. For example 2.4.1.1 or "2.2.1" etc. Either `preferred_versions` or `version` must be set.
    """
    __args__ = dict()
    __args__['preferredVersions'] = preferred_versions
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:msk/getKafkaVersion:getKafkaVersion', __args__, opts=opts, typ=GetKafkaVersionResult).value

    return AwaitableGetKafkaVersionResult(
        id=pulumi.get(__ret__, 'id'),
        preferred_versions=pulumi.get(__ret__, 'preferred_versions'),
        status=pulumi.get(__ret__, 'status'),
        version=pulumi.get(__ret__, 'version'))
def get_kafka_version_output(preferred_versions: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                             version: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKafkaVersionResult]:
    """
    Get information on a Amazon MSK Kafka Version

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    preferred = aws.msk.get_kafka_version(preferred_versions=[
        "2.4.1.1",
        "2.4.1",
        "2.2.1",
    ])
    example = aws.msk.get_kafka_version(version="2.8.0")
    ```


    :param Sequence[str] preferred_versions: Ordered list of preferred Kafka versions. The first match in this list will be returned. Either `preferred_versions` or `version` must be set.
    :param str version: Version of MSK Kafka. For example 2.4.1.1 or "2.2.1" etc. Either `preferred_versions` or `version` must be set.
    """
    __args__ = dict()
    __args__['preferredVersions'] = preferred_versions
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:msk/getKafkaVersion:getKafkaVersion', __args__, opts=opts, typ=GetKafkaVersionResult)
    return __ret__.apply(lambda __response__: GetKafkaVersionResult(
        id=pulumi.get(__response__, 'id'),
        preferred_versions=pulumi.get(__response__, 'preferred_versions'),
        status=pulumi.get(__response__, 'status'),
        version=pulumi.get(__response__, 'version')))
