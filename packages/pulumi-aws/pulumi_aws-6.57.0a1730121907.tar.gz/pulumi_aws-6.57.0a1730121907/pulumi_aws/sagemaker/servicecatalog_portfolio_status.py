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

__all__ = ['ServicecatalogPortfolioStatusArgs', 'ServicecatalogPortfolioStatus']

@pulumi.input_type
class ServicecatalogPortfolioStatusArgs:
    def __init__(__self__, *,
                 status: pulumi.Input[str]):
        """
        The set of arguments for constructing a ServicecatalogPortfolioStatus resource.
        :param pulumi.Input[str] status: Whether Service Catalog is enabled or disabled in SageMaker. Valid values are `Enabled` and `Disabled`.
        """
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[str]:
        """
        Whether Service Catalog is enabled or disabled in SageMaker. Valid values are `Enabled` and `Disabled`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[str]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _ServicecatalogPortfolioStatusState:
    def __init__(__self__, *,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServicecatalogPortfolioStatus resources.
        :param pulumi.Input[str] status: Whether Service Catalog is enabled or disabled in SageMaker. Valid values are `Enabled` and `Disabled`.
        """
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Whether Service Catalog is enabled or disabled in SageMaker. Valid values are `Enabled` and `Disabled`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class ServicecatalogPortfolioStatus(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages status of Service Catalog in SageMaker. Service Catalog is used to create SageMaker projects.

        ## Example Usage

        Usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.sagemaker.ServicecatalogPortfolioStatus("example", status="Enabled")
        ```

        ## Import

        Using `pulumi import`, import models using the `id`. For example:

        ```sh
        $ pulumi import aws:sagemaker/servicecatalogPortfolioStatus:ServicecatalogPortfolioStatus example us-east-1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] status: Whether Service Catalog is enabled or disabled in SageMaker. Valid values are `Enabled` and `Disabled`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServicecatalogPortfolioStatusArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages status of Service Catalog in SageMaker. Service Catalog is used to create SageMaker projects.

        ## Example Usage

        Usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.sagemaker.ServicecatalogPortfolioStatus("example", status="Enabled")
        ```

        ## Import

        Using `pulumi import`, import models using the `id`. For example:

        ```sh
        $ pulumi import aws:sagemaker/servicecatalogPortfolioStatus:ServicecatalogPortfolioStatus example us-east-1
        ```

        :param str resource_name: The name of the resource.
        :param ServicecatalogPortfolioStatusArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServicecatalogPortfolioStatusArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServicecatalogPortfolioStatusArgs.__new__(ServicecatalogPortfolioStatusArgs)

            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
        super(ServicecatalogPortfolioStatus, __self__).__init__(
            'aws:sagemaker/servicecatalogPortfolioStatus:ServicecatalogPortfolioStatus',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'ServicecatalogPortfolioStatus':
        """
        Get an existing ServicecatalogPortfolioStatus resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] status: Whether Service Catalog is enabled or disabled in SageMaker. Valid values are `Enabled` and `Disabled`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServicecatalogPortfolioStatusState.__new__(_ServicecatalogPortfolioStatusState)

        __props__.__dict__["status"] = status
        return ServicecatalogPortfolioStatus(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Whether Service Catalog is enabled or disabled in SageMaker. Valid values are `Enabled` and `Disabled`.
        """
        return pulumi.get(self, "status")

