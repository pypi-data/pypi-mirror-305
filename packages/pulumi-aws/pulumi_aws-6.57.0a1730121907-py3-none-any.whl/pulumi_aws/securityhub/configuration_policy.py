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

__all__ = ['ConfigurationPolicyArgs', 'ConfigurationPolicy']

@pulumi.input_type
class ConfigurationPolicyArgs:
    def __init__(__self__, *,
                 configuration_policy: pulumi.Input['ConfigurationPolicyConfigurationPolicyArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConfigurationPolicy resource.
        :param pulumi.Input['ConfigurationPolicyConfigurationPolicyArgs'] configuration_policy: Defines how Security Hub is configured. See below.
        :param pulumi.Input[str] description: The description of the configuration policy.
        :param pulumi.Input[str] name: The name of the configuration policy.
        """
        pulumi.set(__self__, "configuration_policy", configuration_policy)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="configurationPolicy")
    def configuration_policy(self) -> pulumi.Input['ConfigurationPolicyConfigurationPolicyArgs']:
        """
        Defines how Security Hub is configured. See below.
        """
        return pulumi.get(self, "configuration_policy")

    @configuration_policy.setter
    def configuration_policy(self, value: pulumi.Input['ConfigurationPolicyConfigurationPolicyArgs']):
        pulumi.set(self, "configuration_policy", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the configuration policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the configuration policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ConfigurationPolicyState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 configuration_policy: Optional[pulumi.Input['ConfigurationPolicyConfigurationPolicyArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConfigurationPolicy resources.
        :param pulumi.Input['ConfigurationPolicyConfigurationPolicyArgs'] configuration_policy: Defines how Security Hub is configured. See below.
        :param pulumi.Input[str] description: The description of the configuration policy.
        :param pulumi.Input[str] name: The name of the configuration policy.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if configuration_policy is not None:
            pulumi.set(__self__, "configuration_policy", configuration_policy)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="configurationPolicy")
    def configuration_policy(self) -> Optional[pulumi.Input['ConfigurationPolicyConfigurationPolicyArgs']]:
        """
        Defines how Security Hub is configured. See below.
        """
        return pulumi.get(self, "configuration_policy")

    @configuration_policy.setter
    def configuration_policy(self, value: Optional[pulumi.Input['ConfigurationPolicyConfigurationPolicyArgs']]):
        pulumi.set(self, "configuration_policy", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the configuration policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the configuration policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ConfigurationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_policy: Optional[pulumi.Input[Union['ConfigurationPolicyConfigurationPolicyArgs', 'ConfigurationPolicyConfigurationPolicyArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages Security Hub configuration policy

        > **NOTE:** This resource requires `securityhub.OrganizationConfiguration` to be configured of type `CENTRAL`. More information about Security Hub central configuration and configuration policies can be found in the [How Security Hub configuration policies work](https://docs.aws.amazon.com/securityhub/latest/userguide/configuration-policies-overview.html) documentation.

        ## Example Usage

        ### Default standards enabled

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.securityhub.FindingAggregator("example", linking_mode="ALL_REGIONS")
        example_organization_configuration = aws.securityhub.OrganizationConfiguration("example",
            auto_enable=False,
            auto_enable_standards="NONE",
            organization_configuration={
                "configuration_type": "CENTRAL",
            },
            opts = pulumi.ResourceOptions(depends_on=[example]))
        example_configuration_policy = aws.securityhub.ConfigurationPolicy("example",
            name="Example",
            description="This is an example configuration policy",
            configuration_policy={
                "service_enabled": True,
                "enabled_standard_arns": [
                    "arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0",
                    "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
                ],
                "security_controls_configuration": {
                    "disabled_control_identifiers": [],
                },
            },
            opts = pulumi.ResourceOptions(depends_on=[example_organization_configuration]))
        ```

        ### Disabled Policy

        ```python
        import pulumi
        import pulumi_aws as aws

        disabled = aws.securityhub.ConfigurationPolicy("disabled",
            name="Disabled",
            description="This is an example of disabled configuration policy",
            configuration_policy={
                "service_enabled": False,
            },
            opts = pulumi.ResourceOptions(depends_on=[example]))
        ```

        ### Custom Control Configuration

        ```python
        import pulumi
        import pulumi_aws as aws

        disabled = aws.securityhub.ConfigurationPolicy("disabled",
            name="Custom Controls",
            description="This is an example of configuration policy with custom control settings",
            configuration_policy={
                "service_enabled": True,
                "enabled_standard_arns": [
                    "arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0",
                    "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
                ],
                "security_controls_configuration": {
                    "enabled_control_identifiers": [
                        "APIGateway.1",
                        "IAM.7",
                    ],
                    "security_control_custom_parameters": [
                        {
                            "security_control_id": "APIGateway.1",
                            "parameters": [{
                                "name": "loggingLevel",
                                "value_type": "CUSTOM",
                                "enum": {
                                    "value": "INFO",
                                },
                            }],
                        },
                        {
                            "security_control_id": "IAM.7",
                            "parameters": [
                                {
                                    "name": "RequireLowercaseCharacters",
                                    "value_type": "CUSTOM",
                                    "bool": {
                                        "value": False,
                                    },
                                },
                                {
                                    "name": "MaxPasswordAge",
                                    "value_type": "CUSTOM",
                                    "int": {
                                        "value": 60,
                                    },
                                },
                            ],
                        },
                    ],
                },
            },
            opts = pulumi.ResourceOptions(depends_on=[example]))
        ```

        ## Import

        Using `pulumi import`, import an existing Security Hub enabled account using the universally unique identifier (UUID) of the policy. For example:

        ```sh
        $ pulumi import aws:securityhub/configurationPolicy:ConfigurationPolicy example "00000000-1111-2222-3333-444444444444"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ConfigurationPolicyConfigurationPolicyArgs', 'ConfigurationPolicyConfigurationPolicyArgsDict']] configuration_policy: Defines how Security Hub is configured. See below.
        :param pulumi.Input[str] description: The description of the configuration policy.
        :param pulumi.Input[str] name: The name of the configuration policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages Security Hub configuration policy

        > **NOTE:** This resource requires `securityhub.OrganizationConfiguration` to be configured of type `CENTRAL`. More information about Security Hub central configuration and configuration policies can be found in the [How Security Hub configuration policies work](https://docs.aws.amazon.com/securityhub/latest/userguide/configuration-policies-overview.html) documentation.

        ## Example Usage

        ### Default standards enabled

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.securityhub.FindingAggregator("example", linking_mode="ALL_REGIONS")
        example_organization_configuration = aws.securityhub.OrganizationConfiguration("example",
            auto_enable=False,
            auto_enable_standards="NONE",
            organization_configuration={
                "configuration_type": "CENTRAL",
            },
            opts = pulumi.ResourceOptions(depends_on=[example]))
        example_configuration_policy = aws.securityhub.ConfigurationPolicy("example",
            name="Example",
            description="This is an example configuration policy",
            configuration_policy={
                "service_enabled": True,
                "enabled_standard_arns": [
                    "arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0",
                    "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
                ],
                "security_controls_configuration": {
                    "disabled_control_identifiers": [],
                },
            },
            opts = pulumi.ResourceOptions(depends_on=[example_organization_configuration]))
        ```

        ### Disabled Policy

        ```python
        import pulumi
        import pulumi_aws as aws

        disabled = aws.securityhub.ConfigurationPolicy("disabled",
            name="Disabled",
            description="This is an example of disabled configuration policy",
            configuration_policy={
                "service_enabled": False,
            },
            opts = pulumi.ResourceOptions(depends_on=[example]))
        ```

        ### Custom Control Configuration

        ```python
        import pulumi
        import pulumi_aws as aws

        disabled = aws.securityhub.ConfigurationPolicy("disabled",
            name="Custom Controls",
            description="This is an example of configuration policy with custom control settings",
            configuration_policy={
                "service_enabled": True,
                "enabled_standard_arns": [
                    "arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0",
                    "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
                ],
                "security_controls_configuration": {
                    "enabled_control_identifiers": [
                        "APIGateway.1",
                        "IAM.7",
                    ],
                    "security_control_custom_parameters": [
                        {
                            "security_control_id": "APIGateway.1",
                            "parameters": [{
                                "name": "loggingLevel",
                                "value_type": "CUSTOM",
                                "enum": {
                                    "value": "INFO",
                                },
                            }],
                        },
                        {
                            "security_control_id": "IAM.7",
                            "parameters": [
                                {
                                    "name": "RequireLowercaseCharacters",
                                    "value_type": "CUSTOM",
                                    "bool": {
                                        "value": False,
                                    },
                                },
                                {
                                    "name": "MaxPasswordAge",
                                    "value_type": "CUSTOM",
                                    "int": {
                                        "value": 60,
                                    },
                                },
                            ],
                        },
                    ],
                },
            },
            opts = pulumi.ResourceOptions(depends_on=[example]))
        ```

        ## Import

        Using `pulumi import`, import an existing Security Hub enabled account using the universally unique identifier (UUID) of the policy. For example:

        ```sh
        $ pulumi import aws:securityhub/configurationPolicy:ConfigurationPolicy example "00000000-1111-2222-3333-444444444444"
        ```

        :param str resource_name: The name of the resource.
        :param ConfigurationPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_policy: Optional[pulumi.Input[Union['ConfigurationPolicyConfigurationPolicyArgs', 'ConfigurationPolicyConfigurationPolicyArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigurationPolicyArgs.__new__(ConfigurationPolicyArgs)

            if configuration_policy is None and not opts.urn:
                raise TypeError("Missing required property 'configuration_policy'")
            __props__.__dict__["configuration_policy"] = configuration_policy
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["arn"] = None
        super(ConfigurationPolicy, __self__).__init__(
            'aws:securityhub/configurationPolicy:ConfigurationPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            configuration_policy: Optional[pulumi.Input[Union['ConfigurationPolicyConfigurationPolicyArgs', 'ConfigurationPolicyConfigurationPolicyArgsDict']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'ConfigurationPolicy':
        """
        Get an existing ConfigurationPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ConfigurationPolicyConfigurationPolicyArgs', 'ConfigurationPolicyConfigurationPolicyArgsDict']] configuration_policy: Defines how Security Hub is configured. See below.
        :param pulumi.Input[str] description: The description of the configuration policy.
        :param pulumi.Input[str] name: The name of the configuration policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConfigurationPolicyState.__new__(_ConfigurationPolicyState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["configuration_policy"] = configuration_policy
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        return ConfigurationPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="configurationPolicy")
    def configuration_policy(self) -> pulumi.Output['outputs.ConfigurationPolicyConfigurationPolicy']:
        """
        Defines how Security Hub is configured. See below.
        """
        return pulumi.get(self, "configuration_policy")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the configuration policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the configuration policy.
        """
        return pulumi.get(self, "name")

