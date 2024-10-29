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

__all__ = ['EnvironmentProfileArgs', 'EnvironmentProfile']

@pulumi.input_type
class EnvironmentProfileArgs:
    def __init__(__self__, *,
                 aws_account_region: pulumi.Input[str],
                 domain_identifier: pulumi.Input[str],
                 environment_blueprint_identifier: pulumi.Input[str],
                 project_identifier: pulumi.Input[str],
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 user_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentProfileUserParameterArgs']]]] = None):
        """
        The set of arguments for constructing a EnvironmentProfile resource.
        :param pulumi.Input[str] aws_account_region: Desired region for environment profile.
        :param pulumi.Input[str] domain_identifier: Domain Identifier for environment profile.
        :param pulumi.Input[str] environment_blueprint_identifier: ID of the blueprint which the environment will be created with.
        :param pulumi.Input[str] project_identifier: Project identifier for environment profile.
               
               The following arguments are optional:
        :param pulumi.Input[str] aws_account_id: Id of the AWS account being used.
        :param pulumi.Input[str] description: Description of environment profile.
        :param pulumi.Input[str] name: Name of the environment profile.
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentProfileUserParameterArgs']]] user_parameters: Array of user parameters of the environment profile with the following attributes:
        """
        pulumi.set(__self__, "aws_account_region", aws_account_region)
        pulumi.set(__self__, "domain_identifier", domain_identifier)
        pulumi.set(__self__, "environment_blueprint_identifier", environment_blueprint_identifier)
        pulumi.set(__self__, "project_identifier", project_identifier)
        if aws_account_id is not None:
            pulumi.set(__self__, "aws_account_id", aws_account_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if user_parameters is not None:
            pulumi.set(__self__, "user_parameters", user_parameters)

    @property
    @pulumi.getter(name="awsAccountRegion")
    def aws_account_region(self) -> pulumi.Input[str]:
        """
        Desired region for environment profile.
        """
        return pulumi.get(self, "aws_account_region")

    @aws_account_region.setter
    def aws_account_region(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_account_region", value)

    @property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Input[str]:
        """
        Domain Identifier for environment profile.
        """
        return pulumi.get(self, "domain_identifier")

    @domain_identifier.setter
    def domain_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_identifier", value)

    @property
    @pulumi.getter(name="environmentBlueprintIdentifier")
    def environment_blueprint_identifier(self) -> pulumi.Input[str]:
        """
        ID of the blueprint which the environment will be created with.
        """
        return pulumi.get(self, "environment_blueprint_identifier")

    @environment_blueprint_identifier.setter
    def environment_blueprint_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_blueprint_identifier", value)

    @property
    @pulumi.getter(name="projectIdentifier")
    def project_identifier(self) -> pulumi.Input[str]:
        """
        Project identifier for environment profile.

        The following arguments are optional:
        """
        return pulumi.get(self, "project_identifier")

    @project_identifier.setter
    def project_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_identifier", value)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the AWS account being used.
        """
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of environment profile.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the environment profile.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="userParameters")
    def user_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentProfileUserParameterArgs']]]]:
        """
        Array of user parameters of the environment profile with the following attributes:
        """
        return pulumi.get(self, "user_parameters")

    @user_parameters.setter
    def user_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentProfileUserParameterArgs']]]]):
        pulumi.set(self, "user_parameters", value)


@pulumi.input_type
class _EnvironmentProfileState:
    def __init__(__self__, *,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 aws_account_region: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_identifier: Optional[pulumi.Input[str]] = None,
                 environment_blueprint_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_identifier: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 user_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentProfileUserParameterArgs']]]] = None):
        """
        Input properties used for looking up and filtering EnvironmentProfile resources.
        :param pulumi.Input[str] aws_account_id: Id of the AWS account being used.
        :param pulumi.Input[str] aws_account_region: Desired region for environment profile.
        :param pulumi.Input[str] created_at: Creation time of environment profile.
        :param pulumi.Input[str] created_by: Creator of environment profile.
        :param pulumi.Input[str] description: Description of environment profile.
        :param pulumi.Input[str] domain_identifier: Domain Identifier for environment profile.
        :param pulumi.Input[str] environment_blueprint_identifier: ID of the blueprint which the environment will be created with.
        :param pulumi.Input[str] name: Name of the environment profile.
        :param pulumi.Input[str] project_identifier: Project identifier for environment profile.
               
               The following arguments are optional:
        :param pulumi.Input[str] updated_at: Time of last update to environment profile.
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentProfileUserParameterArgs']]] user_parameters: Array of user parameters of the environment profile with the following attributes:
        """
        if aws_account_id is not None:
            pulumi.set(__self__, "aws_account_id", aws_account_id)
        if aws_account_region is not None:
            pulumi.set(__self__, "aws_account_region", aws_account_region)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if domain_identifier is not None:
            pulumi.set(__self__, "domain_identifier", domain_identifier)
        if environment_blueprint_identifier is not None:
            pulumi.set(__self__, "environment_blueprint_identifier", environment_blueprint_identifier)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project_identifier is not None:
            pulumi.set(__self__, "project_identifier", project_identifier)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if user_parameters is not None:
            pulumi.set(__self__, "user_parameters", user_parameters)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the AWS account being used.
        """
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter(name="awsAccountRegion")
    def aws_account_region(self) -> Optional[pulumi.Input[str]]:
        """
        Desired region for environment profile.
        """
        return pulumi.get(self, "aws_account_region")

    @aws_account_region.setter
    def aws_account_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_account_region", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Creation time of environment profile.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        Creator of environment profile.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of environment profile.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Domain Identifier for environment profile.
        """
        return pulumi.get(self, "domain_identifier")

    @domain_identifier.setter
    def domain_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_identifier", value)

    @property
    @pulumi.getter(name="environmentBlueprintIdentifier")
    def environment_blueprint_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the blueprint which the environment will be created with.
        """
        return pulumi.get(self, "environment_blueprint_identifier")

    @environment_blueprint_identifier.setter
    def environment_blueprint_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_blueprint_identifier", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the environment profile.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="projectIdentifier")
    def project_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Project identifier for environment profile.

        The following arguments are optional:
        """
        return pulumi.get(self, "project_identifier")

    @project_identifier.setter
    def project_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_identifier", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        Time of last update to environment profile.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)

    @property
    @pulumi.getter(name="userParameters")
    def user_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentProfileUserParameterArgs']]]]:
        """
        Array of user parameters of the environment profile with the following attributes:
        """
        return pulumi.get(self, "user_parameters")

    @user_parameters.setter
    def user_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentProfileUserParameterArgs']]]]):
        pulumi.set(self, "user_parameters", value)


class EnvironmentProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 aws_account_region: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_identifier: Optional[pulumi.Input[str]] = None,
                 environment_blueprint_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_identifier: Optional[pulumi.Input[str]] = None,
                 user_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['EnvironmentProfileUserParameterArgs', 'EnvironmentProfileUserParameterArgsDict']]]]] = None,
                 __props__=None):
        """
        Resource for managing an AWS DataZone Environment Profile.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        domain_execution_role = aws.iam.Role("domain_execution_role",
            name="example-name",
            assume_role_policy=json.dumps({
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": [
                            "sts:AssumeRole",
                            "sts:TagSession",
                        ],
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "datazone.amazonaws.com",
                        },
                    },
                    {
                        "Action": [
                            "sts:AssumeRole",
                            "sts:TagSession",
                        ],
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "cloudformation.amazonaws.com",
                        },
                    },
                ],
            }),
            inline_policies=[{
                "name": "example-name",
                "policy": json.dumps({
                    "version": "2012-10-17",
                    "statement": [{
                        "action": [
                            "datazone:*",
                            "ram:*",
                            "sso:*",
                            "kms:*",
                        ],
                        "effect": "Allow",
                        "resource": "*",
                    }],
                }),
            }])
        test_domain = aws.datazone.Domain("test",
            name="example-name",
            domain_execution_role=domain_execution_role.arn)
        test_security_group = aws.ec2.SecurityGroup("test", name="example-name")
        test_project = aws.datazone.Project("test",
            domain_identifier=test_domain.id,
            glossary_terms=["2N8w6XJCwZf"],
            name="example-name",
            description="desc",
            skip_deletion_check=True)
        test = aws.get_caller_identity()
        test_get_region = aws.get_region()
        test_get_environment_blueprint = aws.datazone.get_environment_blueprint_output(domain_id=test_domain.id,
            name="DefaultDataLake",
            managed=True)
        test_environment_blueprint_configuration = aws.datazone.EnvironmentBlueprintConfiguration("test",
            domain_id=test_domain.id,
            environment_blueprint_id=test_get_environment_blueprint.id,
            provisioning_role_arn=domain_execution_role.arn,
            enabled_regions=[test_get_region.name])
        test_environment_profile = aws.datazone.EnvironmentProfile("test",
            aws_account_id=test.account_id,
            aws_account_region=test_get_region.name,
            description="description",
            environment_blueprint_identifier=test_get_environment_blueprint.id,
            name="example-name",
            project_identifier=test_project.id,
            domain_identifier=test_domain.id,
            user_parameters=[{
                "name": "consumerGlueDbName",
                "value": "value",
            }])
        ```

        ## Import

        Using `pulumi import`, import DataZone Environment Profile using a comma-delimited string combining `id` and `domain_identifier`. For example:

        ```sh
        $ pulumi import aws:datazone/environmentProfile:EnvironmentProfile example environment_profile-id-12345678,domain-id-12345678
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_account_id: Id of the AWS account being used.
        :param pulumi.Input[str] aws_account_region: Desired region for environment profile.
        :param pulumi.Input[str] description: Description of environment profile.
        :param pulumi.Input[str] domain_identifier: Domain Identifier for environment profile.
        :param pulumi.Input[str] environment_blueprint_identifier: ID of the blueprint which the environment will be created with.
        :param pulumi.Input[str] name: Name of the environment profile.
        :param pulumi.Input[str] project_identifier: Project identifier for environment profile.
               
               The following arguments are optional:
        :param pulumi.Input[Sequence[pulumi.Input[Union['EnvironmentProfileUserParameterArgs', 'EnvironmentProfileUserParameterArgsDict']]]] user_parameters: Array of user parameters of the environment profile with the following attributes:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS DataZone Environment Profile.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        domain_execution_role = aws.iam.Role("domain_execution_role",
            name="example-name",
            assume_role_policy=json.dumps({
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": [
                            "sts:AssumeRole",
                            "sts:TagSession",
                        ],
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "datazone.amazonaws.com",
                        },
                    },
                    {
                        "Action": [
                            "sts:AssumeRole",
                            "sts:TagSession",
                        ],
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "cloudformation.amazonaws.com",
                        },
                    },
                ],
            }),
            inline_policies=[{
                "name": "example-name",
                "policy": json.dumps({
                    "version": "2012-10-17",
                    "statement": [{
                        "action": [
                            "datazone:*",
                            "ram:*",
                            "sso:*",
                            "kms:*",
                        ],
                        "effect": "Allow",
                        "resource": "*",
                    }],
                }),
            }])
        test_domain = aws.datazone.Domain("test",
            name="example-name",
            domain_execution_role=domain_execution_role.arn)
        test_security_group = aws.ec2.SecurityGroup("test", name="example-name")
        test_project = aws.datazone.Project("test",
            domain_identifier=test_domain.id,
            glossary_terms=["2N8w6XJCwZf"],
            name="example-name",
            description="desc",
            skip_deletion_check=True)
        test = aws.get_caller_identity()
        test_get_region = aws.get_region()
        test_get_environment_blueprint = aws.datazone.get_environment_blueprint_output(domain_id=test_domain.id,
            name="DefaultDataLake",
            managed=True)
        test_environment_blueprint_configuration = aws.datazone.EnvironmentBlueprintConfiguration("test",
            domain_id=test_domain.id,
            environment_blueprint_id=test_get_environment_blueprint.id,
            provisioning_role_arn=domain_execution_role.arn,
            enabled_regions=[test_get_region.name])
        test_environment_profile = aws.datazone.EnvironmentProfile("test",
            aws_account_id=test.account_id,
            aws_account_region=test_get_region.name,
            description="description",
            environment_blueprint_identifier=test_get_environment_blueprint.id,
            name="example-name",
            project_identifier=test_project.id,
            domain_identifier=test_domain.id,
            user_parameters=[{
                "name": "consumerGlueDbName",
                "value": "value",
            }])
        ```

        ## Import

        Using `pulumi import`, import DataZone Environment Profile using a comma-delimited string combining `id` and `domain_identifier`. For example:

        ```sh
        $ pulumi import aws:datazone/environmentProfile:EnvironmentProfile example environment_profile-id-12345678,domain-id-12345678
        ```

        :param str resource_name: The name of the resource.
        :param EnvironmentProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 aws_account_region: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_identifier: Optional[pulumi.Input[str]] = None,
                 environment_blueprint_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_identifier: Optional[pulumi.Input[str]] = None,
                 user_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['EnvironmentProfileUserParameterArgs', 'EnvironmentProfileUserParameterArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentProfileArgs.__new__(EnvironmentProfileArgs)

            __props__.__dict__["aws_account_id"] = aws_account_id
            if aws_account_region is None and not opts.urn:
                raise TypeError("Missing required property 'aws_account_region'")
            __props__.__dict__["aws_account_region"] = aws_account_region
            __props__.__dict__["description"] = description
            if domain_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'domain_identifier'")
            __props__.__dict__["domain_identifier"] = domain_identifier
            if environment_blueprint_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'environment_blueprint_identifier'")
            __props__.__dict__["environment_blueprint_identifier"] = environment_blueprint_identifier
            __props__.__dict__["name"] = name
            if project_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'project_identifier'")
            __props__.__dict__["project_identifier"] = project_identifier
            __props__.__dict__["user_parameters"] = user_parameters
            __props__.__dict__["created_at"] = None
            __props__.__dict__["created_by"] = None
            __props__.__dict__["updated_at"] = None
        super(EnvironmentProfile, __self__).__init__(
            'aws:datazone/environmentProfile:EnvironmentProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            aws_account_id: Optional[pulumi.Input[str]] = None,
            aws_account_region: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            domain_identifier: Optional[pulumi.Input[str]] = None,
            environment_blueprint_identifier: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project_identifier: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            user_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['EnvironmentProfileUserParameterArgs', 'EnvironmentProfileUserParameterArgsDict']]]]] = None) -> 'EnvironmentProfile':
        """
        Get an existing EnvironmentProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_account_id: Id of the AWS account being used.
        :param pulumi.Input[str] aws_account_region: Desired region for environment profile.
        :param pulumi.Input[str] created_at: Creation time of environment profile.
        :param pulumi.Input[str] created_by: Creator of environment profile.
        :param pulumi.Input[str] description: Description of environment profile.
        :param pulumi.Input[str] domain_identifier: Domain Identifier for environment profile.
        :param pulumi.Input[str] environment_blueprint_identifier: ID of the blueprint which the environment will be created with.
        :param pulumi.Input[str] name: Name of the environment profile.
        :param pulumi.Input[str] project_identifier: Project identifier for environment profile.
               
               The following arguments are optional:
        :param pulumi.Input[str] updated_at: Time of last update to environment profile.
        :param pulumi.Input[Sequence[pulumi.Input[Union['EnvironmentProfileUserParameterArgs', 'EnvironmentProfileUserParameterArgsDict']]]] user_parameters: Array of user parameters of the environment profile with the following attributes:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EnvironmentProfileState.__new__(_EnvironmentProfileState)

        __props__.__dict__["aws_account_id"] = aws_account_id
        __props__.__dict__["aws_account_region"] = aws_account_region
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["description"] = description
        __props__.__dict__["domain_identifier"] = domain_identifier
        __props__.__dict__["environment_blueprint_identifier"] = environment_blueprint_identifier
        __props__.__dict__["name"] = name
        __props__.__dict__["project_identifier"] = project_identifier
        __props__.__dict__["updated_at"] = updated_at
        __props__.__dict__["user_parameters"] = user_parameters
        return EnvironmentProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[str]:
        """
        Id of the AWS account being used.
        """
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="awsAccountRegion")
    def aws_account_region(self) -> pulumi.Output[str]:
        """
        Desired region for environment profile.
        """
        return pulumi.get(self, "aws_account_region")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Creation time of environment profile.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        Creator of environment profile.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of environment profile.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Output[str]:
        """
        Domain Identifier for environment profile.
        """
        return pulumi.get(self, "domain_identifier")

    @property
    @pulumi.getter(name="environmentBlueprintIdentifier")
    def environment_blueprint_identifier(self) -> pulumi.Output[str]:
        """
        ID of the blueprint which the environment will be created with.
        """
        return pulumi.get(self, "environment_blueprint_identifier")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the environment profile.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectIdentifier")
    def project_identifier(self) -> pulumi.Output[str]:
        """
        Project identifier for environment profile.

        The following arguments are optional:
        """
        return pulumi.get(self, "project_identifier")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Time of last update to environment profile.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="userParameters")
    def user_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.EnvironmentProfileUserParameter']]]:
        """
        Array of user parameters of the environment profile with the following attributes:
        """
        return pulumi.get(self, "user_parameters")

