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

__all__ = ['RestoreTestingSelectionArgs', 'RestoreTestingSelection']

@pulumi.input_type
class RestoreTestingSelectionArgs:
    def __init__(__self__, *,
                 iam_role_arn: pulumi.Input[str],
                 protected_resource_type: pulumi.Input[str],
                 restore_testing_plan_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 protected_resource_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 protected_resource_conditions: Optional[pulumi.Input['RestoreTestingSelectionProtectedResourceConditionsArgs']] = None,
                 restore_metadata_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validation_window_hours: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a RestoreTestingSelection resource.
        :param pulumi.Input[str] iam_role_arn: The ARN of the IAM role.
        :param pulumi.Input[str] protected_resource_type: The type of the protected resource.
        :param pulumi.Input[str] restore_testing_plan_name: The name of the restore testing plan.
        :param pulumi.Input[str] name: The name of the backup restore testing selection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protected_resource_arns: The ARNs for the protected resources.
        :param pulumi.Input['RestoreTestingSelectionProtectedResourceConditionsArgs'] protected_resource_conditions: The conditions for the protected resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] restore_metadata_overrides: Override certain restore metadata keys. See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html) .
        """
        pulumi.set(__self__, "iam_role_arn", iam_role_arn)
        pulumi.set(__self__, "protected_resource_type", protected_resource_type)
        pulumi.set(__self__, "restore_testing_plan_name", restore_testing_plan_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if protected_resource_arns is not None:
            pulumi.set(__self__, "protected_resource_arns", protected_resource_arns)
        if protected_resource_conditions is not None:
            pulumi.set(__self__, "protected_resource_conditions", protected_resource_conditions)
        if restore_metadata_overrides is not None:
            pulumi.set(__self__, "restore_metadata_overrides", restore_metadata_overrides)
        if validation_window_hours is not None:
            pulumi.set(__self__, "validation_window_hours", validation_window_hours)

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the IAM role.
        """
        return pulumi.get(self, "iam_role_arn")

    @iam_role_arn.setter
    def iam_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "iam_role_arn", value)

    @property
    @pulumi.getter(name="protectedResourceType")
    def protected_resource_type(self) -> pulumi.Input[str]:
        """
        The type of the protected resource.
        """
        return pulumi.get(self, "protected_resource_type")

    @protected_resource_type.setter
    def protected_resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "protected_resource_type", value)

    @property
    @pulumi.getter(name="restoreTestingPlanName")
    def restore_testing_plan_name(self) -> pulumi.Input[str]:
        """
        The name of the restore testing plan.
        """
        return pulumi.get(self, "restore_testing_plan_name")

    @restore_testing_plan_name.setter
    def restore_testing_plan_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "restore_testing_plan_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the backup restore testing selection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="protectedResourceArns")
    def protected_resource_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ARNs for the protected resources.
        """
        return pulumi.get(self, "protected_resource_arns")

    @protected_resource_arns.setter
    def protected_resource_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "protected_resource_arns", value)

    @property
    @pulumi.getter(name="protectedResourceConditions")
    def protected_resource_conditions(self) -> Optional[pulumi.Input['RestoreTestingSelectionProtectedResourceConditionsArgs']]:
        """
        The conditions for the protected resource.
        """
        return pulumi.get(self, "protected_resource_conditions")

    @protected_resource_conditions.setter
    def protected_resource_conditions(self, value: Optional[pulumi.Input['RestoreTestingSelectionProtectedResourceConditionsArgs']]):
        pulumi.set(self, "protected_resource_conditions", value)

    @property
    @pulumi.getter(name="restoreMetadataOverrides")
    def restore_metadata_overrides(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Override certain restore metadata keys. See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html) .
        """
        return pulumi.get(self, "restore_metadata_overrides")

    @restore_metadata_overrides.setter
    def restore_metadata_overrides(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "restore_metadata_overrides", value)

    @property
    @pulumi.getter(name="validationWindowHours")
    def validation_window_hours(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "validation_window_hours")

    @validation_window_hours.setter
    def validation_window_hours(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "validation_window_hours", value)


@pulumi.input_type
class _RestoreTestingSelectionState:
    def __init__(__self__, *,
                 iam_role_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protected_resource_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 protected_resource_conditions: Optional[pulumi.Input['RestoreTestingSelectionProtectedResourceConditionsArgs']] = None,
                 protected_resource_type: Optional[pulumi.Input[str]] = None,
                 restore_metadata_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 restore_testing_plan_name: Optional[pulumi.Input[str]] = None,
                 validation_window_hours: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering RestoreTestingSelection resources.
        :param pulumi.Input[str] iam_role_arn: The ARN of the IAM role.
        :param pulumi.Input[str] name: The name of the backup restore testing selection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protected_resource_arns: The ARNs for the protected resources.
        :param pulumi.Input['RestoreTestingSelectionProtectedResourceConditionsArgs'] protected_resource_conditions: The conditions for the protected resource.
        :param pulumi.Input[str] protected_resource_type: The type of the protected resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] restore_metadata_overrides: Override certain restore metadata keys. See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html) .
        :param pulumi.Input[str] restore_testing_plan_name: The name of the restore testing plan.
        """
        if iam_role_arn is not None:
            pulumi.set(__self__, "iam_role_arn", iam_role_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if protected_resource_arns is not None:
            pulumi.set(__self__, "protected_resource_arns", protected_resource_arns)
        if protected_resource_conditions is not None:
            pulumi.set(__self__, "protected_resource_conditions", protected_resource_conditions)
        if protected_resource_type is not None:
            pulumi.set(__self__, "protected_resource_type", protected_resource_type)
        if restore_metadata_overrides is not None:
            pulumi.set(__self__, "restore_metadata_overrides", restore_metadata_overrides)
        if restore_testing_plan_name is not None:
            pulumi.set(__self__, "restore_testing_plan_name", restore_testing_plan_name)
        if validation_window_hours is not None:
            pulumi.set(__self__, "validation_window_hours", validation_window_hours)

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the IAM role.
        """
        return pulumi.get(self, "iam_role_arn")

    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iam_role_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the backup restore testing selection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="protectedResourceArns")
    def protected_resource_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ARNs for the protected resources.
        """
        return pulumi.get(self, "protected_resource_arns")

    @protected_resource_arns.setter
    def protected_resource_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "protected_resource_arns", value)

    @property
    @pulumi.getter(name="protectedResourceConditions")
    def protected_resource_conditions(self) -> Optional[pulumi.Input['RestoreTestingSelectionProtectedResourceConditionsArgs']]:
        """
        The conditions for the protected resource.
        """
        return pulumi.get(self, "protected_resource_conditions")

    @protected_resource_conditions.setter
    def protected_resource_conditions(self, value: Optional[pulumi.Input['RestoreTestingSelectionProtectedResourceConditionsArgs']]):
        pulumi.set(self, "protected_resource_conditions", value)

    @property
    @pulumi.getter(name="protectedResourceType")
    def protected_resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the protected resource.
        """
        return pulumi.get(self, "protected_resource_type")

    @protected_resource_type.setter
    def protected_resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protected_resource_type", value)

    @property
    @pulumi.getter(name="restoreMetadataOverrides")
    def restore_metadata_overrides(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Override certain restore metadata keys. See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html) .
        """
        return pulumi.get(self, "restore_metadata_overrides")

    @restore_metadata_overrides.setter
    def restore_metadata_overrides(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "restore_metadata_overrides", value)

    @property
    @pulumi.getter(name="restoreTestingPlanName")
    def restore_testing_plan_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the restore testing plan.
        """
        return pulumi.get(self, "restore_testing_plan_name")

    @restore_testing_plan_name.setter
    def restore_testing_plan_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_testing_plan_name", value)

    @property
    @pulumi.getter(name="validationWindowHours")
    def validation_window_hours(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "validation_window_hours")

    @validation_window_hours.setter
    def validation_window_hours(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "validation_window_hours", value)


class RestoreTestingSelection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 iam_role_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protected_resource_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 protected_resource_conditions: Optional[pulumi.Input[Union['RestoreTestingSelectionProtectedResourceConditionsArgs', 'RestoreTestingSelectionProtectedResourceConditionsArgsDict']]] = None,
                 protected_resource_type: Optional[pulumi.Input[str]] = None,
                 restore_metadata_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 restore_testing_plan_name: Optional[pulumi.Input[str]] = None,
                 validation_window_hours: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource for managing an AWS Backup Restore Testing Selection.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.backup.RestoreTestingSelection("example",
            name="ec2_selection",
            restore_testing_plan_name=example_aws_backup_restore_testing_plan["name"],
            protected_resource_type="EC2",
            iam_role_arn=example_aws_iam_role["arn"],
            protected_resource_arns=["*"])
        ```

        ### Advanced Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.backup.RestoreTestingSelection("example",
            name="ec2_selection",
            restore_testing_plan_name=example_aws_backup_restore_testing_plan["name"],
            protected_resource_type="EC2",
            iam_role_arn=example_aws_iam_role["arn"],
            protected_resource_conditions={
                "string_equals": [{
                    "key": "aws:ResourceTag/backup",
                    "value": "true",
                }],
            })
        ```

        ## Import

        Using `pulumi import`, import Backup Restore Testing Selection using `name:restore_testing_plan_name`. For example:

        ```sh
        $ pulumi import aws:backup/restoreTestingSelection:RestoreTestingSelection example restore_testing_selection_12345678:restore_testing_plan_12345678
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] iam_role_arn: The ARN of the IAM role.
        :param pulumi.Input[str] name: The name of the backup restore testing selection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protected_resource_arns: The ARNs for the protected resources.
        :param pulumi.Input[Union['RestoreTestingSelectionProtectedResourceConditionsArgs', 'RestoreTestingSelectionProtectedResourceConditionsArgsDict']] protected_resource_conditions: The conditions for the protected resource.
        :param pulumi.Input[str] protected_resource_type: The type of the protected resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] restore_metadata_overrides: Override certain restore metadata keys. See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html) .
        :param pulumi.Input[str] restore_testing_plan_name: The name of the restore testing plan.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RestoreTestingSelectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS Backup Restore Testing Selection.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.backup.RestoreTestingSelection("example",
            name="ec2_selection",
            restore_testing_plan_name=example_aws_backup_restore_testing_plan["name"],
            protected_resource_type="EC2",
            iam_role_arn=example_aws_iam_role["arn"],
            protected_resource_arns=["*"])
        ```

        ### Advanced Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.backup.RestoreTestingSelection("example",
            name="ec2_selection",
            restore_testing_plan_name=example_aws_backup_restore_testing_plan["name"],
            protected_resource_type="EC2",
            iam_role_arn=example_aws_iam_role["arn"],
            protected_resource_conditions={
                "string_equals": [{
                    "key": "aws:ResourceTag/backup",
                    "value": "true",
                }],
            })
        ```

        ## Import

        Using `pulumi import`, import Backup Restore Testing Selection using `name:restore_testing_plan_name`. For example:

        ```sh
        $ pulumi import aws:backup/restoreTestingSelection:RestoreTestingSelection example restore_testing_selection_12345678:restore_testing_plan_12345678
        ```

        :param str resource_name: The name of the resource.
        :param RestoreTestingSelectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RestoreTestingSelectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 iam_role_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 protected_resource_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 protected_resource_conditions: Optional[pulumi.Input[Union['RestoreTestingSelectionProtectedResourceConditionsArgs', 'RestoreTestingSelectionProtectedResourceConditionsArgsDict']]] = None,
                 protected_resource_type: Optional[pulumi.Input[str]] = None,
                 restore_metadata_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 restore_testing_plan_name: Optional[pulumi.Input[str]] = None,
                 validation_window_hours: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RestoreTestingSelectionArgs.__new__(RestoreTestingSelectionArgs)

            if iam_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'iam_role_arn'")
            __props__.__dict__["iam_role_arn"] = iam_role_arn
            __props__.__dict__["name"] = name
            __props__.__dict__["protected_resource_arns"] = protected_resource_arns
            __props__.__dict__["protected_resource_conditions"] = protected_resource_conditions
            if protected_resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'protected_resource_type'")
            __props__.__dict__["protected_resource_type"] = protected_resource_type
            __props__.__dict__["restore_metadata_overrides"] = restore_metadata_overrides
            if restore_testing_plan_name is None and not opts.urn:
                raise TypeError("Missing required property 'restore_testing_plan_name'")
            __props__.__dict__["restore_testing_plan_name"] = restore_testing_plan_name
            __props__.__dict__["validation_window_hours"] = validation_window_hours
        super(RestoreTestingSelection, __self__).__init__(
            'aws:backup/restoreTestingSelection:RestoreTestingSelection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            iam_role_arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            protected_resource_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            protected_resource_conditions: Optional[pulumi.Input[Union['RestoreTestingSelectionProtectedResourceConditionsArgs', 'RestoreTestingSelectionProtectedResourceConditionsArgsDict']]] = None,
            protected_resource_type: Optional[pulumi.Input[str]] = None,
            restore_metadata_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            restore_testing_plan_name: Optional[pulumi.Input[str]] = None,
            validation_window_hours: Optional[pulumi.Input[int]] = None) -> 'RestoreTestingSelection':
        """
        Get an existing RestoreTestingSelection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] iam_role_arn: The ARN of the IAM role.
        :param pulumi.Input[str] name: The name of the backup restore testing selection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protected_resource_arns: The ARNs for the protected resources.
        :param pulumi.Input[Union['RestoreTestingSelectionProtectedResourceConditionsArgs', 'RestoreTestingSelectionProtectedResourceConditionsArgsDict']] protected_resource_conditions: The conditions for the protected resource.
        :param pulumi.Input[str] protected_resource_type: The type of the protected resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] restore_metadata_overrides: Override certain restore metadata keys. See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html) .
        :param pulumi.Input[str] restore_testing_plan_name: The name of the restore testing plan.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RestoreTestingSelectionState.__new__(_RestoreTestingSelectionState)

        __props__.__dict__["iam_role_arn"] = iam_role_arn
        __props__.__dict__["name"] = name
        __props__.__dict__["protected_resource_arns"] = protected_resource_arns
        __props__.__dict__["protected_resource_conditions"] = protected_resource_conditions
        __props__.__dict__["protected_resource_type"] = protected_resource_type
        __props__.__dict__["restore_metadata_overrides"] = restore_metadata_overrides
        __props__.__dict__["restore_testing_plan_name"] = restore_testing_plan_name
        __props__.__dict__["validation_window_hours"] = validation_window_hours
        return RestoreTestingSelection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the IAM role.
        """
        return pulumi.get(self, "iam_role_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the backup restore testing selection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="protectedResourceArns")
    def protected_resource_arns(self) -> pulumi.Output[Sequence[str]]:
        """
        The ARNs for the protected resources.
        """
        return pulumi.get(self, "protected_resource_arns")

    @property
    @pulumi.getter(name="protectedResourceConditions")
    def protected_resource_conditions(self) -> pulumi.Output[Optional['outputs.RestoreTestingSelectionProtectedResourceConditions']]:
        """
        The conditions for the protected resource.
        """
        return pulumi.get(self, "protected_resource_conditions")

    @property
    @pulumi.getter(name="protectedResourceType")
    def protected_resource_type(self) -> pulumi.Output[str]:
        """
        The type of the protected resource.
        """
        return pulumi.get(self, "protected_resource_type")

    @property
    @pulumi.getter(name="restoreMetadataOverrides")
    def restore_metadata_overrides(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Override certain restore metadata keys. See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html) .
        """
        return pulumi.get(self, "restore_metadata_overrides")

    @property
    @pulumi.getter(name="restoreTestingPlanName")
    def restore_testing_plan_name(self) -> pulumi.Output[str]:
        """
        The name of the restore testing plan.
        """
        return pulumi.get(self, "restore_testing_plan_name")

    @property
    @pulumi.getter(name="validationWindowHours")
    def validation_window_hours(self) -> pulumi.Output[int]:
        return pulumi.get(self, "validation_window_hours")

