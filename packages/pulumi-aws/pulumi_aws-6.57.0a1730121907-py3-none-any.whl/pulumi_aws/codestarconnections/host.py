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

__all__ = ['HostArgs', 'Host']

@pulumi.input_type
class HostArgs:
    def __init__(__self__, *,
                 provider_endpoint: pulumi.Input[str],
                 provider_type: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 vpc_configuration: Optional[pulumi.Input['HostVpcConfigurationArgs']] = None):
        """
        The set of arguments for constructing a Host resource.
        :param pulumi.Input[str] provider_endpoint: The endpoint of the infrastructure to be represented by the host after it is created.
        :param pulumi.Input[str] provider_type: The name of the external provider where your third-party code repository is configured.
        :param pulumi.Input[str] name: The name of the host to be created. The name must be unique in the calling AWS account.
        :param pulumi.Input['HostVpcConfigurationArgs'] vpc_configuration: The VPC configuration to be provisioned for the host. A VPC must be configured, and the infrastructure to be represented by the host must already be connected to the VPC.
        """
        pulumi.set(__self__, "provider_endpoint", provider_endpoint)
        pulumi.set(__self__, "provider_type", provider_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if vpc_configuration is not None:
            pulumi.set(__self__, "vpc_configuration", vpc_configuration)

    @property
    @pulumi.getter(name="providerEndpoint")
    def provider_endpoint(self) -> pulumi.Input[str]:
        """
        The endpoint of the infrastructure to be represented by the host after it is created.
        """
        return pulumi.get(self, "provider_endpoint")

    @provider_endpoint.setter
    def provider_endpoint(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_endpoint", value)

    @property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> pulumi.Input[str]:
        """
        The name of the external provider where your third-party code repository is configured.
        """
        return pulumi.get(self, "provider_type")

    @provider_type.setter
    def provider_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the host to be created. The name must be unique in the calling AWS account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> Optional[pulumi.Input['HostVpcConfigurationArgs']]:
        """
        The VPC configuration to be provisioned for the host. A VPC must be configured, and the infrastructure to be represented by the host must already be connected to the VPC.
        """
        return pulumi.get(self, "vpc_configuration")

    @vpc_configuration.setter
    def vpc_configuration(self, value: Optional[pulumi.Input['HostVpcConfigurationArgs']]):
        pulumi.set(self, "vpc_configuration", value)


@pulumi.input_type
class _HostState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_endpoint: Optional[pulumi.Input[str]] = None,
                 provider_type: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 vpc_configuration: Optional[pulumi.Input['HostVpcConfigurationArgs']] = None):
        """
        Input properties used for looking up and filtering Host resources.
        :param pulumi.Input[str] arn: The CodeStar Host ARN.
        :param pulumi.Input[str] name: The name of the host to be created. The name must be unique in the calling AWS account.
        :param pulumi.Input[str] provider_endpoint: The endpoint of the infrastructure to be represented by the host after it is created.
        :param pulumi.Input[str] provider_type: The name of the external provider where your third-party code repository is configured.
        :param pulumi.Input[str] status: The CodeStar Host status. Possible values are `PENDING`, `AVAILABLE`, `VPC_CONFIG_DELETING`, `VPC_CONFIG_INITIALIZING`, and `VPC_CONFIG_FAILED_INITIALIZATION`.
        :param pulumi.Input['HostVpcConfigurationArgs'] vpc_configuration: The VPC configuration to be provisioned for the host. A VPC must be configured, and the infrastructure to be represented by the host must already be connected to the VPC.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provider_endpoint is not None:
            pulumi.set(__self__, "provider_endpoint", provider_endpoint)
        if provider_type is not None:
            pulumi.set(__self__, "provider_type", provider_type)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if vpc_configuration is not None:
            pulumi.set(__self__, "vpc_configuration", vpc_configuration)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The CodeStar Host ARN.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the host to be created. The name must be unique in the calling AWS account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="providerEndpoint")
    def provider_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The endpoint of the infrastructure to be represented by the host after it is created.
        """
        return pulumi.get(self, "provider_endpoint")

    @provider_endpoint.setter
    def provider_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_endpoint", value)

    @property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the external provider where your third-party code repository is configured.
        """
        return pulumi.get(self, "provider_type")

    @provider_type.setter
    def provider_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_type", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The CodeStar Host status. Possible values are `PENDING`, `AVAILABLE`, `VPC_CONFIG_DELETING`, `VPC_CONFIG_INITIALIZING`, and `VPC_CONFIG_FAILED_INITIALIZATION`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> Optional[pulumi.Input['HostVpcConfigurationArgs']]:
        """
        The VPC configuration to be provisioned for the host. A VPC must be configured, and the infrastructure to be represented by the host must already be connected to the VPC.
        """
        return pulumi.get(self, "vpc_configuration")

    @vpc_configuration.setter
    def vpc_configuration(self, value: Optional[pulumi.Input['HostVpcConfigurationArgs']]):
        pulumi.set(self, "vpc_configuration", value)


class Host(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_endpoint: Optional[pulumi.Input[str]] = None,
                 provider_type: Optional[pulumi.Input[str]] = None,
                 vpc_configuration: Optional[pulumi.Input[Union['HostVpcConfigurationArgs', 'HostVpcConfigurationArgsDict']]] = None,
                 __props__=None):
        """
        Provides a CodeStar Host.

        > **NOTE:** The `codestarconnections.Host` resource is created in the state `PENDING`. Authentication with the host provider must be completed in the AWS Console. For more information visit [Set up a pending host](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-setup.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.codestarconnections.Host("example",
            name="example-host",
            provider_endpoint="https://example.com",
            provider_type="GitHubEnterpriseServer")
        ```

        ## Import

        Using `pulumi import`, import CodeStar Host using the ARN. For example:

        ```sh
        $ pulumi import aws:codestarconnections/host:Host example-host arn:aws:codestar-connections:us-west-1:0123456789:host/79d4d357-a2ee-41e4-b350-2fe39ae59448
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the host to be created. The name must be unique in the calling AWS account.
        :param pulumi.Input[str] provider_endpoint: The endpoint of the infrastructure to be represented by the host after it is created.
        :param pulumi.Input[str] provider_type: The name of the external provider where your third-party code repository is configured.
        :param pulumi.Input[Union['HostVpcConfigurationArgs', 'HostVpcConfigurationArgsDict']] vpc_configuration: The VPC configuration to be provisioned for the host. A VPC must be configured, and the infrastructure to be represented by the host must already be connected to the VPC.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HostArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a CodeStar Host.

        > **NOTE:** The `codestarconnections.Host` resource is created in the state `PENDING`. Authentication with the host provider must be completed in the AWS Console. For more information visit [Set up a pending host](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-setup.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.codestarconnections.Host("example",
            name="example-host",
            provider_endpoint="https://example.com",
            provider_type="GitHubEnterpriseServer")
        ```

        ## Import

        Using `pulumi import`, import CodeStar Host using the ARN. For example:

        ```sh
        $ pulumi import aws:codestarconnections/host:Host example-host arn:aws:codestar-connections:us-west-1:0123456789:host/79d4d357-a2ee-41e4-b350-2fe39ae59448
        ```

        :param str resource_name: The name of the resource.
        :param HostArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HostArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_endpoint: Optional[pulumi.Input[str]] = None,
                 provider_type: Optional[pulumi.Input[str]] = None,
                 vpc_configuration: Optional[pulumi.Input[Union['HostVpcConfigurationArgs', 'HostVpcConfigurationArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HostArgs.__new__(HostArgs)

            __props__.__dict__["name"] = name
            if provider_endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'provider_endpoint'")
            __props__.__dict__["provider_endpoint"] = provider_endpoint
            if provider_type is None and not opts.urn:
                raise TypeError("Missing required property 'provider_type'")
            __props__.__dict__["provider_type"] = provider_type
            __props__.__dict__["vpc_configuration"] = vpc_configuration
            __props__.__dict__["arn"] = None
            __props__.__dict__["status"] = None
        super(Host, __self__).__init__(
            'aws:codestarconnections/host:Host',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            provider_endpoint: Optional[pulumi.Input[str]] = None,
            provider_type: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            vpc_configuration: Optional[pulumi.Input[Union['HostVpcConfigurationArgs', 'HostVpcConfigurationArgsDict']]] = None) -> 'Host':
        """
        Get an existing Host resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The CodeStar Host ARN.
        :param pulumi.Input[str] name: The name of the host to be created. The name must be unique in the calling AWS account.
        :param pulumi.Input[str] provider_endpoint: The endpoint of the infrastructure to be represented by the host after it is created.
        :param pulumi.Input[str] provider_type: The name of the external provider where your third-party code repository is configured.
        :param pulumi.Input[str] status: The CodeStar Host status. Possible values are `PENDING`, `AVAILABLE`, `VPC_CONFIG_DELETING`, `VPC_CONFIG_INITIALIZING`, and `VPC_CONFIG_FAILED_INITIALIZATION`.
        :param pulumi.Input[Union['HostVpcConfigurationArgs', 'HostVpcConfigurationArgsDict']] vpc_configuration: The VPC configuration to be provisioned for the host. A VPC must be configured, and the infrastructure to be represented by the host must already be connected to the VPC.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HostState.__new__(_HostState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["name"] = name
        __props__.__dict__["provider_endpoint"] = provider_endpoint
        __props__.__dict__["provider_type"] = provider_type
        __props__.__dict__["status"] = status
        __props__.__dict__["vpc_configuration"] = vpc_configuration
        return Host(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The CodeStar Host ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the host to be created. The name must be unique in the calling AWS account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="providerEndpoint")
    def provider_endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint of the infrastructure to be represented by the host after it is created.
        """
        return pulumi.get(self, "provider_endpoint")

    @property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> pulumi.Output[str]:
        """
        The name of the external provider where your third-party code repository is configured.
        """
        return pulumi.get(self, "provider_type")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The CodeStar Host status. Possible values are `PENDING`, `AVAILABLE`, `VPC_CONFIG_DELETING`, `VPC_CONFIG_INITIALIZING`, and `VPC_CONFIG_FAILED_INITIALIZATION`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> pulumi.Output[Optional['outputs.HostVpcConfiguration']]:
        """
        The VPC configuration to be provisioned for the host. A VPC must be configured, and the infrastructure to be represented by the host must already be connected to the VPC.
        """
        return pulumi.get(self, "vpc_configuration")

