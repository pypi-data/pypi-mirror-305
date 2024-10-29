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

__all__ = ['ControlArgs', 'Control']

@pulumi.input_type
class ControlArgs:
    def __init__(__self__, *,
                 action_plan_instructions: Optional[pulumi.Input[str]] = None,
                 action_plan_title: Optional[pulumi.Input[str]] = None,
                 control_mapping_sources: Optional[pulumi.Input[Sequence[pulumi.Input['ControlControlMappingSourceArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 testing_information: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Control resource.
        :param pulumi.Input[str] action_plan_instructions: Recommended actions to carry out if the control isn't fulfilled.
        :param pulumi.Input[str] action_plan_title: Title of the action plan for remediating the control.
        :param pulumi.Input[Sequence[pulumi.Input['ControlControlMappingSourceArgs']]] control_mapping_sources: Data mapping sources. See `control_mapping_sources` below.
               
               The following arguments are optional:
        :param pulumi.Input[str] description: Description of the control.
        :param pulumi.Input[str] name: Name of the control.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the control. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] testing_information: Steps to follow to determine if the control is satisfied.
        """
        if action_plan_instructions is not None:
            pulumi.set(__self__, "action_plan_instructions", action_plan_instructions)
        if action_plan_title is not None:
            pulumi.set(__self__, "action_plan_title", action_plan_title)
        if control_mapping_sources is not None:
            pulumi.set(__self__, "control_mapping_sources", control_mapping_sources)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if testing_information is not None:
            pulumi.set(__self__, "testing_information", testing_information)

    @property
    @pulumi.getter(name="actionPlanInstructions")
    def action_plan_instructions(self) -> Optional[pulumi.Input[str]]:
        """
        Recommended actions to carry out if the control isn't fulfilled.
        """
        return pulumi.get(self, "action_plan_instructions")

    @action_plan_instructions.setter
    def action_plan_instructions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_plan_instructions", value)

    @property
    @pulumi.getter(name="actionPlanTitle")
    def action_plan_title(self) -> Optional[pulumi.Input[str]]:
        """
        Title of the action plan for remediating the control.
        """
        return pulumi.get(self, "action_plan_title")

    @action_plan_title.setter
    def action_plan_title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_plan_title", value)

    @property
    @pulumi.getter(name="controlMappingSources")
    def control_mapping_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ControlControlMappingSourceArgs']]]]:
        """
        Data mapping sources. See `control_mapping_sources` below.

        The following arguments are optional:
        """
        return pulumi.get(self, "control_mapping_sources")

    @control_mapping_sources.setter
    def control_mapping_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ControlControlMappingSourceArgs']]]]):
        pulumi.set(self, "control_mapping_sources", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the control.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the control.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the control. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="testingInformation")
    def testing_information(self) -> Optional[pulumi.Input[str]]:
        """
        Steps to follow to determine if the control is satisfied.
        """
        return pulumi.get(self, "testing_information")

    @testing_information.setter
    def testing_information(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "testing_information", value)


@pulumi.input_type
class _ControlState:
    def __init__(__self__, *,
                 action_plan_instructions: Optional[pulumi.Input[str]] = None,
                 action_plan_title: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 control_mapping_sources: Optional[pulumi.Input[Sequence[pulumi.Input['ControlControlMappingSourceArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 testing_information: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Control resources.
        :param pulumi.Input[str] action_plan_instructions: Recommended actions to carry out if the control isn't fulfilled.
        :param pulumi.Input[str] action_plan_title: Title of the action plan for remediating the control.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the control.
               * `control_mapping_sources.*.source_id` - Unique identifier for the source.
        :param pulumi.Input[Sequence[pulumi.Input['ControlControlMappingSourceArgs']]] control_mapping_sources: Data mapping sources. See `control_mapping_sources` below.
               
               The following arguments are optional:
        :param pulumi.Input[str] description: Description of the control.
        :param pulumi.Input[str] name: Name of the control.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the control. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] testing_information: Steps to follow to determine if the control is satisfied.
        :param pulumi.Input[str] type: Type of control, such as a custom control or a standard control.
        """
        if action_plan_instructions is not None:
            pulumi.set(__self__, "action_plan_instructions", action_plan_instructions)
        if action_plan_title is not None:
            pulumi.set(__self__, "action_plan_title", action_plan_title)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if control_mapping_sources is not None:
            pulumi.set(__self__, "control_mapping_sources", control_mapping_sources)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if testing_information is not None:
            pulumi.set(__self__, "testing_information", testing_information)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="actionPlanInstructions")
    def action_plan_instructions(self) -> Optional[pulumi.Input[str]]:
        """
        Recommended actions to carry out if the control isn't fulfilled.
        """
        return pulumi.get(self, "action_plan_instructions")

    @action_plan_instructions.setter
    def action_plan_instructions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_plan_instructions", value)

    @property
    @pulumi.getter(name="actionPlanTitle")
    def action_plan_title(self) -> Optional[pulumi.Input[str]]:
        """
        Title of the action plan for remediating the control.
        """
        return pulumi.get(self, "action_plan_title")

    @action_plan_title.setter
    def action_plan_title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_plan_title", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the control.
        * `control_mapping_sources.*.source_id` - Unique identifier for the source.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="controlMappingSources")
    def control_mapping_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ControlControlMappingSourceArgs']]]]:
        """
        Data mapping sources. See `control_mapping_sources` below.

        The following arguments are optional:
        """
        return pulumi.get(self, "control_mapping_sources")

    @control_mapping_sources.setter
    def control_mapping_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ControlControlMappingSourceArgs']]]]):
        pulumi.set(self, "control_mapping_sources", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the control.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the control.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the control. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter(name="testingInformation")
    def testing_information(self) -> Optional[pulumi.Input[str]]:
        """
        Steps to follow to determine if the control is satisfied.
        """
        return pulumi.get(self, "testing_information")

    @testing_information.setter
    def testing_information(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "testing_information", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of control, such as a custom control or a standard control.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Control(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_plan_instructions: Optional[pulumi.Input[str]] = None,
                 action_plan_title: Optional[pulumi.Input[str]] = None,
                 control_mapping_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ControlControlMappingSourceArgs', 'ControlControlMappingSourceArgsDict']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 testing_information: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for managing an AWS Audit Manager Control.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.auditmanager.Control("example",
            name="example",
            control_mapping_sources=[{
                "source_name": "example",
                "source_set_up_option": "Procedural_Controls_Mapping",
                "source_type": "MANUAL",
            }])
        ```

        ## Import

        Using `pulumi import`, import an Audit Manager Control using the `id`. For example:

        ```sh
        $ pulumi import aws:auditmanager/control:Control example abc123-de45
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_plan_instructions: Recommended actions to carry out if the control isn't fulfilled.
        :param pulumi.Input[str] action_plan_title: Title of the action plan for remediating the control.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ControlControlMappingSourceArgs', 'ControlControlMappingSourceArgsDict']]]] control_mapping_sources: Data mapping sources. See `control_mapping_sources` below.
               
               The following arguments are optional:
        :param pulumi.Input[str] description: Description of the control.
        :param pulumi.Input[str] name: Name of the control.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the control. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] testing_information: Steps to follow to determine if the control is satisfied.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ControlArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS Audit Manager Control.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.auditmanager.Control("example",
            name="example",
            control_mapping_sources=[{
                "source_name": "example",
                "source_set_up_option": "Procedural_Controls_Mapping",
                "source_type": "MANUAL",
            }])
        ```

        ## Import

        Using `pulumi import`, import an Audit Manager Control using the `id`. For example:

        ```sh
        $ pulumi import aws:auditmanager/control:Control example abc123-de45
        ```

        :param str resource_name: The name of the resource.
        :param ControlArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ControlArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_plan_instructions: Optional[pulumi.Input[str]] = None,
                 action_plan_title: Optional[pulumi.Input[str]] = None,
                 control_mapping_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ControlControlMappingSourceArgs', 'ControlControlMappingSourceArgsDict']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 testing_information: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ControlArgs.__new__(ControlArgs)

            __props__.__dict__["action_plan_instructions"] = action_plan_instructions
            __props__.__dict__["action_plan_title"] = action_plan_title
            __props__.__dict__["control_mapping_sources"] = control_mapping_sources
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["testing_information"] = testing_information
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
            __props__.__dict__["type"] = None
        super(Control, __self__).__init__(
            'aws:auditmanager/control:Control',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action_plan_instructions: Optional[pulumi.Input[str]] = None,
            action_plan_title: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            control_mapping_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ControlControlMappingSourceArgs', 'ControlControlMappingSourceArgsDict']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            testing_information: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Control':
        """
        Get an existing Control resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_plan_instructions: Recommended actions to carry out if the control isn't fulfilled.
        :param pulumi.Input[str] action_plan_title: Title of the action plan for remediating the control.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the control.
               * `control_mapping_sources.*.source_id` - Unique identifier for the source.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ControlControlMappingSourceArgs', 'ControlControlMappingSourceArgsDict']]]] control_mapping_sources: Data mapping sources. See `control_mapping_sources` below.
               
               The following arguments are optional:
        :param pulumi.Input[str] description: Description of the control.
        :param pulumi.Input[str] name: Name of the control.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the control. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] testing_information: Steps to follow to determine if the control is satisfied.
        :param pulumi.Input[str] type: Type of control, such as a custom control or a standard control.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ControlState.__new__(_ControlState)

        __props__.__dict__["action_plan_instructions"] = action_plan_instructions
        __props__.__dict__["action_plan_title"] = action_plan_title
        __props__.__dict__["arn"] = arn
        __props__.__dict__["control_mapping_sources"] = control_mapping_sources
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["testing_information"] = testing_information
        __props__.__dict__["type"] = type
        return Control(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionPlanInstructions")
    def action_plan_instructions(self) -> pulumi.Output[Optional[str]]:
        """
        Recommended actions to carry out if the control isn't fulfilled.
        """
        return pulumi.get(self, "action_plan_instructions")

    @property
    @pulumi.getter(name="actionPlanTitle")
    def action_plan_title(self) -> pulumi.Output[Optional[str]]:
        """
        Title of the action plan for remediating the control.
        """
        return pulumi.get(self, "action_plan_title")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the control.
        * `control_mapping_sources.*.source_id` - Unique identifier for the source.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="controlMappingSources")
    def control_mapping_sources(self) -> pulumi.Output[Optional[Sequence['outputs.ControlControlMappingSource']]]:
        """
        Data mapping sources. See `control_mapping_sources` below.

        The following arguments are optional:
        """
        return pulumi.get(self, "control_mapping_sources")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the control.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the control.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the control. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="testingInformation")
    def testing_information(self) -> pulumi.Output[Optional[str]]:
        """
        Steps to follow to determine if the control is satisfied.
        """
        return pulumi.get(self, "testing_information")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of control, such as a custom control or a standard control.
        """
        return pulumi.get(self, "type")

