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
    'GetSinkResult',
    'AwaitableGetSinkResult',
    'get_sink',
    'get_sink_output',
]

@pulumi.output_type
class GetSinkResult:
    """
    A collection of values returned by getSink.
    """
    def __init__(__self__, arn=None, id=None, name=None, sink_id=None, sink_identifier=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sink_id and not isinstance(sink_id, str):
            raise TypeError("Expected argument 'sink_id' to be a str")
        pulumi.set(__self__, "sink_id", sink_id)
        if sink_identifier and not isinstance(sink_identifier, str):
            raise TypeError("Expected argument 'sink_identifier' to be a str")
        pulumi.set(__self__, "sink_identifier", sink_identifier)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the sink.
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
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the sink.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sinkId")
    def sink_id(self) -> str:
        """
        Random ID string that AWS generated as part of the sink ARN.
        """
        return pulumi.get(self, "sink_id")

    @property
    @pulumi.getter(name="sinkIdentifier")
    def sink_identifier(self) -> str:
        return pulumi.get(self, "sink_identifier")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Tags assigned to the sink.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSinkResult(GetSinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSinkResult(
            arn=self.arn,
            id=self.id,
            name=self.name,
            sink_id=self.sink_id,
            sink_identifier=self.sink_identifier,
            tags=self.tags)


def get_sink(sink_identifier: Optional[str] = None,
             tags: Optional[Mapping[str, str]] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSinkResult:
    """
    Data source for managing an AWS CloudWatch Observability Access Manager Sink.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.oam.get_sink(sink_identifier="arn:aws:oam:us-west-1:111111111111:sink/abcd1234-a123-456a-a12b-a123b456c789")
    ```


    :param str sink_identifier: ARN of the sink.
    :param Mapping[str, str] tags: Tags assigned to the sink.
    """
    __args__ = dict()
    __args__['sinkIdentifier'] = sink_identifier
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:oam/getSink:getSink', __args__, opts=opts, typ=GetSinkResult).value

    return AwaitableGetSinkResult(
        arn=pulumi.get(__ret__, 'arn'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        sink_id=pulumi.get(__ret__, 'sink_id'),
        sink_identifier=pulumi.get(__ret__, 'sink_identifier'),
        tags=pulumi.get(__ret__, 'tags'))
def get_sink_output(sink_identifier: Optional[pulumi.Input[str]] = None,
                    tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSinkResult]:
    """
    Data source for managing an AWS CloudWatch Observability Access Manager Sink.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.oam.get_sink(sink_identifier="arn:aws:oam:us-west-1:111111111111:sink/abcd1234-a123-456a-a12b-a123b456c789")
    ```


    :param str sink_identifier: ARN of the sink.
    :param Mapping[str, str] tags: Tags assigned to the sink.
    """
    __args__ = dict()
    __args__['sinkIdentifier'] = sink_identifier
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:oam/getSink:getSink', __args__, opts=opts, typ=GetSinkResult)
    return __ret__.apply(lambda __response__: GetSinkResult(
        arn=pulumi.get(__response__, 'arn'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        sink_id=pulumi.get(__response__, 'sink_id'),
        sink_identifier=pulumi.get(__response__, 'sink_identifier'),
        tags=pulumi.get(__response__, 'tags')))
