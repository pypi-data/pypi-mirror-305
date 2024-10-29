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
    'GetLinkResult',
    'AwaitableGetLinkResult',
    'get_link',
    'get_link_output',
]

@pulumi.output_type
class GetLinkResult:
    """
    A collection of values returned by getLink.
    """
    def __init__(__self__, arn=None, id=None, label=None, label_template=None, link_configurations=None, link_id=None, link_identifier=None, resource_types=None, sink_arn=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if label_template and not isinstance(label_template, str):
            raise TypeError("Expected argument 'label_template' to be a str")
        pulumi.set(__self__, "label_template", label_template)
        if link_configurations and not isinstance(link_configurations, list):
            raise TypeError("Expected argument 'link_configurations' to be a list")
        pulumi.set(__self__, "link_configurations", link_configurations)
        if link_id and not isinstance(link_id, str):
            raise TypeError("Expected argument 'link_id' to be a str")
        pulumi.set(__self__, "link_id", link_id)
        if link_identifier and not isinstance(link_identifier, str):
            raise TypeError("Expected argument 'link_identifier' to be a str")
        pulumi.set(__self__, "link_identifier", link_identifier)
        if resource_types and not isinstance(resource_types, list):
            raise TypeError("Expected argument 'resource_types' to be a list")
        pulumi.set(__self__, "resource_types", resource_types)
        if sink_arn and not isinstance(sink_arn, str):
            raise TypeError("Expected argument 'sink_arn' to be a str")
        pulumi.set(__self__, "sink_arn", sink_arn)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the link.
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
    def label(self) -> str:
        """
        Label that is assigned to this link.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="labelTemplate")
    def label_template(self) -> str:
        """
        Human-readable name used to identify this source account when you are viewing data from it in the monitoring account.
        """
        return pulumi.get(self, "label_template")

    @property
    @pulumi.getter(name="linkConfigurations")
    def link_configurations(self) -> Sequence['outputs.GetLinkLinkConfigurationResult']:
        """
        Configuration for creating filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account. See `link_configuration` Block for details.
        """
        return pulumi.get(self, "link_configurations")

    @property
    @pulumi.getter(name="linkId")
    def link_id(self) -> str:
        """
        ID string that AWS generated as part of the link ARN.
        """
        return pulumi.get(self, "link_id")

    @property
    @pulumi.getter(name="linkIdentifier")
    def link_identifier(self) -> str:
        return pulumi.get(self, "link_identifier")

    @property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[str]:
        """
        Types of data that the source account shares with the monitoring account.
        """
        return pulumi.get(self, "resource_types")

    @property
    @pulumi.getter(name="sinkArn")
    def sink_arn(self) -> str:
        """
        ARN of the sink that is used for this link.
        """
        return pulumi.get(self, "sink_arn")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags")


class AwaitableGetLinkResult(GetLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLinkResult(
            arn=self.arn,
            id=self.id,
            label=self.label,
            label_template=self.label_template,
            link_configurations=self.link_configurations,
            link_id=self.link_id,
            link_identifier=self.link_identifier,
            resource_types=self.resource_types,
            sink_arn=self.sink_arn,
            tags=self.tags)


def get_link(link_identifier: Optional[str] = None,
             tags: Optional[Mapping[str, str]] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLinkResult:
    """
    Data source for managing an AWS CloudWatch Observability Access Manager Link.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.oam.get_link(link_identifier="arn:aws:oam:us-west-1:111111111111:link/abcd1234-a123-456a-a12b-a123b456c789")
    ```


    :param str link_identifier: ARN of the link.
    """
    __args__ = dict()
    __args__['linkIdentifier'] = link_identifier
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:oam/getLink:getLink', __args__, opts=opts, typ=GetLinkResult).value

    return AwaitableGetLinkResult(
        arn=pulumi.get(__ret__, 'arn'),
        id=pulumi.get(__ret__, 'id'),
        label=pulumi.get(__ret__, 'label'),
        label_template=pulumi.get(__ret__, 'label_template'),
        link_configurations=pulumi.get(__ret__, 'link_configurations'),
        link_id=pulumi.get(__ret__, 'link_id'),
        link_identifier=pulumi.get(__ret__, 'link_identifier'),
        resource_types=pulumi.get(__ret__, 'resource_types'),
        sink_arn=pulumi.get(__ret__, 'sink_arn'),
        tags=pulumi.get(__ret__, 'tags'))
def get_link_output(link_identifier: Optional[pulumi.Input[str]] = None,
                    tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLinkResult]:
    """
    Data source for managing an AWS CloudWatch Observability Access Manager Link.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.oam.get_link(link_identifier="arn:aws:oam:us-west-1:111111111111:link/abcd1234-a123-456a-a12b-a123b456c789")
    ```


    :param str link_identifier: ARN of the link.
    """
    __args__ = dict()
    __args__['linkIdentifier'] = link_identifier
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:oam/getLink:getLink', __args__, opts=opts, typ=GetLinkResult)
    return __ret__.apply(lambda __response__: GetLinkResult(
        arn=pulumi.get(__response__, 'arn'),
        id=pulumi.get(__response__, 'id'),
        label=pulumi.get(__response__, 'label'),
        label_template=pulumi.get(__response__, 'label_template'),
        link_configurations=pulumi.get(__response__, 'link_configurations'),
        link_id=pulumi.get(__response__, 'link_id'),
        link_identifier=pulumi.get(__response__, 'link_identifier'),
        resource_types=pulumi.get(__response__, 'resource_types'),
        sink_arn=pulumi.get(__response__, 'sink_arn'),
        tags=pulumi.get(__response__, 'tags')))
