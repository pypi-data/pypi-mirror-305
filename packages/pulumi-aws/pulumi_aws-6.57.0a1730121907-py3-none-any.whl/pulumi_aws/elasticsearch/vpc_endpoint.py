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

__all__ = ['VpcEndpointArgs', 'VpcEndpoint']

@pulumi.input_type
class VpcEndpointArgs:
    def __init__(__self__, *,
                 domain_arn: pulumi.Input[str],
                 vpc_options: pulumi.Input['VpcEndpointVpcOptionsArgs']):
        """
        The set of arguments for constructing a VpcEndpoint resource.
        :param pulumi.Input[str] domain_arn: Specifies the Amazon Resource Name (ARN) of the domain to create the endpoint for
        :param pulumi.Input['VpcEndpointVpcOptionsArgs'] vpc_options: Options to specify the subnets and security groups for the endpoint.
        """
        pulumi.set(__self__, "domain_arn", domain_arn)
        pulumi.set(__self__, "vpc_options", vpc_options)

    @property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> pulumi.Input[str]:
        """
        Specifies the Amazon Resource Name (ARN) of the domain to create the endpoint for
        """
        return pulumi.get(self, "domain_arn")

    @domain_arn.setter
    def domain_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_arn", value)

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> pulumi.Input['VpcEndpointVpcOptionsArgs']:
        """
        Options to specify the subnets and security groups for the endpoint.
        """
        return pulumi.get(self, "vpc_options")

    @vpc_options.setter
    def vpc_options(self, value: pulumi.Input['VpcEndpointVpcOptionsArgs']):
        pulumi.set(self, "vpc_options", value)


@pulumi.input_type
class _VpcEndpointState:
    def __init__(__self__, *,
                 domain_arn: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 vpc_options: Optional[pulumi.Input['VpcEndpointVpcOptionsArgs']] = None):
        """
        Input properties used for looking up and filtering VpcEndpoint resources.
        :param pulumi.Input[str] domain_arn: Specifies the Amazon Resource Name (ARN) of the domain to create the endpoint for
        :param pulumi.Input[str] endpoint: The connection endpoint ID for connecting to the domain.
        :param pulumi.Input['VpcEndpointVpcOptionsArgs'] vpc_options: Options to specify the subnets and security groups for the endpoint.
        """
        if domain_arn is not None:
            pulumi.set(__self__, "domain_arn", domain_arn)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if vpc_options is not None:
            pulumi.set(__self__, "vpc_options", vpc_options)

    @property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Amazon Resource Name (ARN) of the domain to create the endpoint for
        """
        return pulumi.get(self, "domain_arn")

    @domain_arn.setter
    def domain_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_arn", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The connection endpoint ID for connecting to the domain.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Optional[pulumi.Input['VpcEndpointVpcOptionsArgs']]:
        """
        Options to specify the subnets and security groups for the endpoint.
        """
        return pulumi.get(self, "vpc_options")

    @vpc_options.setter
    def vpc_options(self, value: Optional[pulumi.Input['VpcEndpointVpcOptionsArgs']]):
        pulumi.set(self, "vpc_options", value)


class VpcEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_arn: Optional[pulumi.Input[str]] = None,
                 vpc_options: Optional[pulumi.Input[Union['VpcEndpointVpcOptionsArgs', 'VpcEndpointVpcOptionsArgsDict']]] = None,
                 __props__=None):
        """
        Manages an [AWS Elasticsearch VPC Endpoint](https://docs.aws.amazon.com/elasticsearch-service/latest/APIReference/API_CreateVpcEndpoint.html). Creates an Amazon elasticsearch Service-managed VPC endpoint.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo = aws.elasticsearch.VpcEndpoint("foo",
            domain_arn=domain1["arn"],
            vpc_options={
                "security_group_ids": [
                    test["id"],
                    test2["id"],
                ],
                "subnet_ids": [
                    test_aws_subnet["id"],
                    test2_aws_subnet["id"],
                ],
            })
        ```

        ## Import

        Using `pulumi import`, import elasticsearch VPC endpoint connections using the `id`. For example:

        ```sh
        $ pulumi import aws:elasticsearch/vpcEndpoint:VpcEndpoint example endpoint-id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_arn: Specifies the Amazon Resource Name (ARN) of the domain to create the endpoint for
        :param pulumi.Input[Union['VpcEndpointVpcOptionsArgs', 'VpcEndpointVpcOptionsArgsDict']] vpc_options: Options to specify the subnets and security groups for the endpoint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an [AWS Elasticsearch VPC Endpoint](https://docs.aws.amazon.com/elasticsearch-service/latest/APIReference/API_CreateVpcEndpoint.html). Creates an Amazon elasticsearch Service-managed VPC endpoint.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo = aws.elasticsearch.VpcEndpoint("foo",
            domain_arn=domain1["arn"],
            vpc_options={
                "security_group_ids": [
                    test["id"],
                    test2["id"],
                ],
                "subnet_ids": [
                    test_aws_subnet["id"],
                    test2_aws_subnet["id"],
                ],
            })
        ```

        ## Import

        Using `pulumi import`, import elasticsearch VPC endpoint connections using the `id`. For example:

        ```sh
        $ pulumi import aws:elasticsearch/vpcEndpoint:VpcEndpoint example endpoint-id
        ```

        :param str resource_name: The name of the resource.
        :param VpcEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_arn: Optional[pulumi.Input[str]] = None,
                 vpc_options: Optional[pulumi.Input[Union['VpcEndpointVpcOptionsArgs', 'VpcEndpointVpcOptionsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcEndpointArgs.__new__(VpcEndpointArgs)

            if domain_arn is None and not opts.urn:
                raise TypeError("Missing required property 'domain_arn'")
            __props__.__dict__["domain_arn"] = domain_arn
            if vpc_options is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_options'")
            __props__.__dict__["vpc_options"] = vpc_options
            __props__.__dict__["endpoint"] = None
        super(VpcEndpoint, __self__).__init__(
            'aws:elasticsearch/vpcEndpoint:VpcEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_arn: Optional[pulumi.Input[str]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            vpc_options: Optional[pulumi.Input[Union['VpcEndpointVpcOptionsArgs', 'VpcEndpointVpcOptionsArgsDict']]] = None) -> 'VpcEndpoint':
        """
        Get an existing VpcEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_arn: Specifies the Amazon Resource Name (ARN) of the domain to create the endpoint for
        :param pulumi.Input[str] endpoint: The connection endpoint ID for connecting to the domain.
        :param pulumi.Input[Union['VpcEndpointVpcOptionsArgs', 'VpcEndpointVpcOptionsArgsDict']] vpc_options: Options to specify the subnets and security groups for the endpoint.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpcEndpointState.__new__(_VpcEndpointState)

        __props__.__dict__["domain_arn"] = domain_arn
        __props__.__dict__["endpoint"] = endpoint
        __props__.__dict__["vpc_options"] = vpc_options
        return VpcEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> pulumi.Output[str]:
        """
        Specifies the Amazon Resource Name (ARN) of the domain to create the endpoint for
        """
        return pulumi.get(self, "domain_arn")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        The connection endpoint ID for connecting to the domain.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> pulumi.Output['outputs.VpcEndpointVpcOptions']:
        """
        Options to specify the subnets and security groups for the endpoint.
        """
        return pulumi.get(self, "vpc_options")

