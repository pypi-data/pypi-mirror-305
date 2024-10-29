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
    'GetOriginAccessControlResult',
    'AwaitableGetOriginAccessControlResult',
    'get_origin_access_control',
    'get_origin_access_control_output',
]

@pulumi.output_type
class GetOriginAccessControlResult:
    """
    A collection of values returned by getOriginAccessControl.
    """
    def __init__(__self__, description=None, etag=None, id=None, name=None, origin_access_control_origin_type=None, signing_behavior=None, signing_protocol=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if origin_access_control_origin_type and not isinstance(origin_access_control_origin_type, str):
            raise TypeError("Expected argument 'origin_access_control_origin_type' to be a str")
        pulumi.set(__self__, "origin_access_control_origin_type", origin_access_control_origin_type)
        if signing_behavior and not isinstance(signing_behavior, str):
            raise TypeError("Expected argument 'signing_behavior' to be a str")
        pulumi.set(__self__, "signing_behavior", signing_behavior)
        if signing_protocol and not isinstance(signing_protocol, str):
            raise TypeError("Expected argument 'signing_protocol' to be a str")
        pulumi.set(__self__, "signing_protocol", signing_protocol)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of the origin access control.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Current version of the origin access control's information. For example: `E2QWRUHAPOMQZL`.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A name to identify the origin access control.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="originAccessControlOriginType")
    def origin_access_control_origin_type(self) -> str:
        """
        The type of origin that this origin access control is for.
        """
        return pulumi.get(self, "origin_access_control_origin_type")

    @property
    @pulumi.getter(name="signingBehavior")
    def signing_behavior(self) -> str:
        """
        Specifies which requests CloudFront signs.
        """
        return pulumi.get(self, "signing_behavior")

    @property
    @pulumi.getter(name="signingProtocol")
    def signing_protocol(self) -> str:
        """
        The signing protocol of the origin access control, which determines how CloudFront signs (authenticates) requests.
        """
        return pulumi.get(self, "signing_protocol")


class AwaitableGetOriginAccessControlResult(GetOriginAccessControlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOriginAccessControlResult(
            description=self.description,
            etag=self.etag,
            id=self.id,
            name=self.name,
            origin_access_control_origin_type=self.origin_access_control_origin_type,
            signing_behavior=self.signing_behavior,
            signing_protocol=self.signing_protocol)


def get_origin_access_control(id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOriginAccessControlResult:
    """
    Use this data source to retrieve information for an Amazon CloudFront origin access control config.

    ## Example Usage

    The below example retrieves a CloudFront origin access control config.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.cloudfront.get_origin_access_control(id="E2T5VTFBZJ3BJB")
    ```


    :param str id: The identifier for the origin access control settings. For example: `E2T5VTFBZJ3BJB`.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:cloudfront/getOriginAccessControl:getOriginAccessControl', __args__, opts=opts, typ=GetOriginAccessControlResult).value

    return AwaitableGetOriginAccessControlResult(
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        origin_access_control_origin_type=pulumi.get(__ret__, 'origin_access_control_origin_type'),
        signing_behavior=pulumi.get(__ret__, 'signing_behavior'),
        signing_protocol=pulumi.get(__ret__, 'signing_protocol'))
def get_origin_access_control_output(id: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOriginAccessControlResult]:
    """
    Use this data source to retrieve information for an Amazon CloudFront origin access control config.

    ## Example Usage

    The below example retrieves a CloudFront origin access control config.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.cloudfront.get_origin_access_control(id="E2T5VTFBZJ3BJB")
    ```


    :param str id: The identifier for the origin access control settings. For example: `E2T5VTFBZJ3BJB`.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:cloudfront/getOriginAccessControl:getOriginAccessControl', __args__, opts=opts, typ=GetOriginAccessControlResult)
    return __ret__.apply(lambda __response__: GetOriginAccessControlResult(
        description=pulumi.get(__response__, 'description'),
        etag=pulumi.get(__response__, 'etag'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        origin_access_control_origin_type=pulumi.get(__response__, 'origin_access_control_origin_type'),
        signing_behavior=pulumi.get(__response__, 'signing_behavior'),
        signing_protocol=pulumi.get(__response__, 'signing_protocol')))
