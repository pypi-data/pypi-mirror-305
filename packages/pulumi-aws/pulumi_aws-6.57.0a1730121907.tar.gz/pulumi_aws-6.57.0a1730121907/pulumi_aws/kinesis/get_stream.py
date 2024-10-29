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
    'GetStreamResult',
    'AwaitableGetStreamResult',
    'get_stream',
    'get_stream_output',
]

@pulumi.output_type
class GetStreamResult:
    """
    A collection of values returned by getStream.
    """
    def __init__(__self__, arn=None, closed_shards=None, creation_timestamp=None, encryption_type=None, id=None, kms_key_id=None, name=None, open_shards=None, retention_period=None, shard_level_metrics=None, status=None, stream_mode_details=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if closed_shards and not isinstance(closed_shards, list):
            raise TypeError("Expected argument 'closed_shards' to be a list")
        pulumi.set(__self__, "closed_shards", closed_shards)
        if creation_timestamp and not isinstance(creation_timestamp, int):
            raise TypeError("Expected argument 'creation_timestamp' to be a int")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if encryption_type and not isinstance(encryption_type, str):
            raise TypeError("Expected argument 'encryption_type' to be a str")
        pulumi.set(__self__, "encryption_type", encryption_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if open_shards and not isinstance(open_shards, list):
            raise TypeError("Expected argument 'open_shards' to be a list")
        pulumi.set(__self__, "open_shards", open_shards)
        if retention_period and not isinstance(retention_period, int):
            raise TypeError("Expected argument 'retention_period' to be a int")
        pulumi.set(__self__, "retention_period", retention_period)
        if shard_level_metrics and not isinstance(shard_level_metrics, list):
            raise TypeError("Expected argument 'shard_level_metrics' to be a list")
        pulumi.set(__self__, "shard_level_metrics", shard_level_metrics)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if stream_mode_details and not isinstance(stream_mode_details, list):
            raise TypeError("Expected argument 'stream_mode_details' to be a list")
        pulumi.set(__self__, "stream_mode_details", stream_mode_details)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the Kinesis Stream (same as id).
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="closedShards")
    def closed_shards(self) -> Sequence[str]:
        """
        List of shard ids in the CLOSED state. See [Shard State](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-after-resharding.html#kinesis-using-sdk-java-resharding-data-routing) for more.
        """
        return pulumi.get(self, "closed_shards")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> int:
        """
        Approximate UNIX timestamp that the stream was created.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> str:
        """
        Encryption type used.
        """
        return pulumi.get(self, "encryption_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> str:
        """
        GUID for the customer-managed AWS KMS key to use for encryption.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the Kinesis Stream.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="openShards")
    def open_shards(self) -> Sequence[str]:
        """
        List of shard ids in the OPEN state. See [Shard State](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-after-resharding.html#kinesis-using-sdk-java-resharding-data-routing) for more.
        """
        return pulumi.get(self, "open_shards")

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> int:
        """
        Length of time (in hours) data records are accessible after they are added to the stream.
        """
        return pulumi.get(self, "retention_period")

    @property
    @pulumi.getter(name="shardLevelMetrics")
    def shard_level_metrics(self) -> Sequence[str]:
        """
        List of shard-level CloudWatch metrics which are enabled for the stream. See [Monitoring with CloudWatch](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html) for more.
        """
        return pulumi.get(self, "shard_level_metrics")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Current status of the stream. The stream status is one of CREATING, DELETING, ACTIVE, or UPDATING.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="streamModeDetails")
    def stream_mode_details(self) -> Sequence['outputs.GetStreamStreamModeDetailResult']:
        """
        [Capacity mode](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html) of the data stream. Detailed below.
        """
        return pulumi.get(self, "stream_mode_details")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Map of tags to assigned to the stream.
        """
        return pulumi.get(self, "tags")


class AwaitableGetStreamResult(GetStreamResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStreamResult(
            arn=self.arn,
            closed_shards=self.closed_shards,
            creation_timestamp=self.creation_timestamp,
            encryption_type=self.encryption_type,
            id=self.id,
            kms_key_id=self.kms_key_id,
            name=self.name,
            open_shards=self.open_shards,
            retention_period=self.retention_period,
            shard_level_metrics=self.shard_level_metrics,
            status=self.status,
            stream_mode_details=self.stream_mode_details,
            tags=self.tags)


def get_stream(name: Optional[str] = None,
               tags: Optional[Mapping[str, str]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStreamResult:
    """
    Use this data source to get information about a Kinesis Stream for use in other
    resources.

    For more details, see the [Amazon Kinesis Documentation](https://aws.amazon.com/documentation/kinesis/).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    stream = aws.kinesis.get_stream(name="stream-name")
    ```


    :param str name: Name of the Kinesis Stream.
    :param Mapping[str, str] tags: Map of tags to assigned to the stream.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:kinesis/getStream:getStream', __args__, opts=opts, typ=GetStreamResult).value

    return AwaitableGetStreamResult(
        arn=pulumi.get(__ret__, 'arn'),
        closed_shards=pulumi.get(__ret__, 'closed_shards'),
        creation_timestamp=pulumi.get(__ret__, 'creation_timestamp'),
        encryption_type=pulumi.get(__ret__, 'encryption_type'),
        id=pulumi.get(__ret__, 'id'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        name=pulumi.get(__ret__, 'name'),
        open_shards=pulumi.get(__ret__, 'open_shards'),
        retention_period=pulumi.get(__ret__, 'retention_period'),
        shard_level_metrics=pulumi.get(__ret__, 'shard_level_metrics'),
        status=pulumi.get(__ret__, 'status'),
        stream_mode_details=pulumi.get(__ret__, 'stream_mode_details'),
        tags=pulumi.get(__ret__, 'tags'))
def get_stream_output(name: Optional[pulumi.Input[str]] = None,
                      tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStreamResult]:
    """
    Use this data source to get information about a Kinesis Stream for use in other
    resources.

    For more details, see the [Amazon Kinesis Documentation](https://aws.amazon.com/documentation/kinesis/).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    stream = aws.kinesis.get_stream(name="stream-name")
    ```


    :param str name: Name of the Kinesis Stream.
    :param Mapping[str, str] tags: Map of tags to assigned to the stream.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:kinesis/getStream:getStream', __args__, opts=opts, typ=GetStreamResult)
    return __ret__.apply(lambda __response__: GetStreamResult(
        arn=pulumi.get(__response__, 'arn'),
        closed_shards=pulumi.get(__response__, 'closed_shards'),
        creation_timestamp=pulumi.get(__response__, 'creation_timestamp'),
        encryption_type=pulumi.get(__response__, 'encryption_type'),
        id=pulumi.get(__response__, 'id'),
        kms_key_id=pulumi.get(__response__, 'kms_key_id'),
        name=pulumi.get(__response__, 'name'),
        open_shards=pulumi.get(__response__, 'open_shards'),
        retention_period=pulumi.get(__response__, 'retention_period'),
        shard_level_metrics=pulumi.get(__response__, 'shard_level_metrics'),
        status=pulumi.get(__response__, 'status'),
        stream_mode_details=pulumi.get(__response__, 'stream_mode_details'),
        tags=pulumi.get(__response__, 'tags')))
