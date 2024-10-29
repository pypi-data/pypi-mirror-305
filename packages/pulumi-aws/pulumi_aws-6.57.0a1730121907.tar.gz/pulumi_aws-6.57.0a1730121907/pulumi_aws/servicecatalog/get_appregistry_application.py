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
    'GetAppregistryApplicationResult',
    'AwaitableGetAppregistryApplicationResult',
    'get_appregistry_application',
    'get_appregistry_application_output',
]

@pulumi.output_type
class GetAppregistryApplicationResult:
    """
    A collection of values returned by getAppregistryApplication.
    """
    def __init__(__self__, application_tag=None, arn=None, description=None, id=None, name=None):
        if application_tag and not isinstance(application_tag, dict):
            raise TypeError("Expected argument 'application_tag' to be a dict")
        pulumi.set(__self__, "application_tag", application_tag)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="applicationTag")
    def application_tag(self) -> Mapping[str, str]:
        """
        A map with a single tag key-value pair used to associate resources with the application.
        """
        return pulumi.get(self, "application_tag")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN (Amazon Resource Name) of the application.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the application.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the application.
        """
        return pulumi.get(self, "name")


class AwaitableGetAppregistryApplicationResult(GetAppregistryApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppregistryApplicationResult(
            application_tag=self.application_tag,
            arn=self.arn,
            description=self.description,
            id=self.id,
            name=self.name)


def get_appregistry_application(id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppregistryApplicationResult:
    """
    Data source for managing an AWS Service Catalog AppRegistry Application.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.servicecatalog.get_appregistry_application(id="application-1234")
    ```


    :param str id: Application identifier.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:servicecatalog/getAppregistryApplication:getAppregistryApplication', __args__, opts=opts, typ=GetAppregistryApplicationResult).value

    return AwaitableGetAppregistryApplicationResult(
        application_tag=pulumi.get(__ret__, 'application_tag'),
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))
def get_appregistry_application_output(id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppregistryApplicationResult]:
    """
    Data source for managing an AWS Service Catalog AppRegistry Application.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.servicecatalog.get_appregistry_application(id="application-1234")
    ```


    :param str id: Application identifier.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:servicecatalog/getAppregistryApplication:getAppregistryApplication', __args__, opts=opts, typ=GetAppregistryApplicationResult)
    return __ret__.apply(lambda __response__: GetAppregistryApplicationResult(
        application_tag=pulumi.get(__response__, 'application_tag'),
        arn=pulumi.get(__response__, 'arn'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name')))
