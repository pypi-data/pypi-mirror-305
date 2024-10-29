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

__all__ = ['PlanArgs', 'Plan']

@pulumi.input_type
class PlanArgs:
    def __init__(__self__, *,
                 rules: pulumi.Input[Sequence[pulumi.Input['PlanRuleArgs']]],
                 advanced_backup_settings: Optional[pulumi.Input[Sequence[pulumi.Input['PlanAdvancedBackupSettingArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Plan resource.
        :param pulumi.Input[Sequence[pulumi.Input['PlanRuleArgs']]] rules: A rule object that specifies a scheduled task that is used to back up a selection of resources.
        :param pulumi.Input[Sequence[pulumi.Input['PlanAdvancedBackupSettingArgs']]] advanced_backup_settings: An object that specifies backup options for each resource type.
        :param pulumi.Input[str] name: The display name of a backup plan.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Metadata that you can assign to help organize the plans you create. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "rules", rules)
        if advanced_backup_settings is not None:
            pulumi.set(__self__, "advanced_backup_settings", advanced_backup_settings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['PlanRuleArgs']]]:
        """
        A rule object that specifies a scheduled task that is used to back up a selection of resources.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['PlanRuleArgs']]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="advancedBackupSettings")
    def advanced_backup_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PlanAdvancedBackupSettingArgs']]]]:
        """
        An object that specifies backup options for each resource type.
        """
        return pulumi.get(self, "advanced_backup_settings")

    @advanced_backup_settings.setter
    def advanced_backup_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PlanAdvancedBackupSettingArgs']]]]):
        pulumi.set(self, "advanced_backup_settings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of a backup plan.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Metadata that you can assign to help organize the plans you create. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _PlanState:
    def __init__(__self__, *,
                 advanced_backup_settings: Optional[pulumi.Input[Sequence[pulumi.Input['PlanAdvancedBackupSettingArgs']]]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['PlanRuleArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Plan resources.
        :param pulumi.Input[Sequence[pulumi.Input['PlanAdvancedBackupSettingArgs']]] advanced_backup_settings: An object that specifies backup options for each resource type.
        :param pulumi.Input[str] arn: The ARN of the backup plan.
        :param pulumi.Input[str] name: The display name of a backup plan.
        :param pulumi.Input[Sequence[pulumi.Input['PlanRuleArgs']]] rules: A rule object that specifies a scheduled task that is used to back up a selection of resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Metadata that you can assign to help organize the plans you create. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] version: Unique, randomly generated, Unicode, UTF-8 encoded string that serves as the version ID of the backup plan.
        """
        if advanced_backup_settings is not None:
            pulumi.set(__self__, "advanced_backup_settings", advanced_backup_settings)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="advancedBackupSettings")
    def advanced_backup_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PlanAdvancedBackupSettingArgs']]]]:
        """
        An object that specifies backup options for each resource type.
        """
        return pulumi.get(self, "advanced_backup_settings")

    @advanced_backup_settings.setter
    def advanced_backup_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PlanAdvancedBackupSettingArgs']]]]):
        pulumi.set(self, "advanced_backup_settings", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the backup plan.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of a backup plan.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PlanRuleArgs']]]]:
        """
        A rule object that specifies a scheduled task that is used to back up a selection of resources.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PlanRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Metadata that you can assign to help organize the plans you create. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Unique, randomly generated, Unicode, UTF-8 encoded string that serves as the version ID of the backup plan.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Plan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advanced_backup_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PlanAdvancedBackupSettingArgs', 'PlanAdvancedBackupSettingArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PlanRuleArgs', 'PlanRuleArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides an AWS Backup plan resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.backup.Plan("example",
            name="my_example_backup_plan",
            rules=[{
                "rule_name": "my_example_backup_rule",
                "target_vault_name": test["name"],
                "schedule": "cron(0 12 * * ? *)",
                "lifecycle": {
                    "delete_after": 14,
                },
            }],
            advanced_backup_settings=[{
                "backup_options": {
                    "windows_vss": "enabled",
                },
                "resource_type": "EC2",
            }])
        ```

        ## Import

        Using `pulumi import`, import Backup Plan using the `id`. For example:

        ```sh
        $ pulumi import aws:backup/plan:Plan test <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['PlanAdvancedBackupSettingArgs', 'PlanAdvancedBackupSettingArgsDict']]]] advanced_backup_settings: An object that specifies backup options for each resource type.
        :param pulumi.Input[str] name: The display name of a backup plan.
        :param pulumi.Input[Sequence[pulumi.Input[Union['PlanRuleArgs', 'PlanRuleArgsDict']]]] rules: A rule object that specifies a scheduled task that is used to back up a selection of resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Metadata that you can assign to help organize the plans you create. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PlanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AWS Backup plan resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.backup.Plan("example",
            name="my_example_backup_plan",
            rules=[{
                "rule_name": "my_example_backup_rule",
                "target_vault_name": test["name"],
                "schedule": "cron(0 12 * * ? *)",
                "lifecycle": {
                    "delete_after": 14,
                },
            }],
            advanced_backup_settings=[{
                "backup_options": {
                    "windows_vss": "enabled",
                },
                "resource_type": "EC2",
            }])
        ```

        ## Import

        Using `pulumi import`, import Backup Plan using the `id`. For example:

        ```sh
        $ pulumi import aws:backup/plan:Plan test <id>
        ```

        :param str resource_name: The name of the resource.
        :param PlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advanced_backup_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PlanAdvancedBackupSettingArgs', 'PlanAdvancedBackupSettingArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PlanRuleArgs', 'PlanRuleArgsDict']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PlanArgs.__new__(PlanArgs)

            __props__.__dict__["advanced_backup_settings"] = advanced_backup_settings
            __props__.__dict__["name"] = name
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
            __props__.__dict__["version"] = None
        super(Plan, __self__).__init__(
            'aws:backup/plan:Plan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            advanced_backup_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PlanAdvancedBackupSettingArgs', 'PlanAdvancedBackupSettingArgsDict']]]]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PlanRuleArgs', 'PlanRuleArgsDict']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'Plan':
        """
        Get an existing Plan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['PlanAdvancedBackupSettingArgs', 'PlanAdvancedBackupSettingArgsDict']]]] advanced_backup_settings: An object that specifies backup options for each resource type.
        :param pulumi.Input[str] arn: The ARN of the backup plan.
        :param pulumi.Input[str] name: The display name of a backup plan.
        :param pulumi.Input[Sequence[pulumi.Input[Union['PlanRuleArgs', 'PlanRuleArgsDict']]]] rules: A rule object that specifies a scheduled task that is used to back up a selection of resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Metadata that you can assign to help organize the plans you create. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] version: Unique, randomly generated, Unicode, UTF-8 encoded string that serves as the version ID of the backup plan.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PlanState.__new__(_PlanState)

        __props__.__dict__["advanced_backup_settings"] = advanced_backup_settings
        __props__.__dict__["arn"] = arn
        __props__.__dict__["name"] = name
        __props__.__dict__["rules"] = rules
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["version"] = version
        return Plan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="advancedBackupSettings")
    def advanced_backup_settings(self) -> pulumi.Output[Optional[Sequence['outputs.PlanAdvancedBackupSetting']]]:
        """
        An object that specifies backup options for each resource type.
        """
        return pulumi.get(self, "advanced_backup_settings")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the backup plan.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The display name of a backup plan.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.PlanRule']]:
        """
        A rule object that specifies a scheduled task that is used to back up a selection of resources.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Metadata that you can assign to help organize the plans you create. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Unique, randomly generated, Unicode, UTF-8 encoded string that serves as the version ID of the backup plan.
        """
        return pulumi.get(self, "version")

