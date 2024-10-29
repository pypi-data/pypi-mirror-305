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

__all__ = ['TemplateArgs', 'Template']

@pulumi.input_type
class TemplateArgs:
    def __init__(__self__, *,
                 html: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 text: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Template resource.
        :param pulumi.Input[str] html: The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        :param pulumi.Input[str] name: The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        :param pulumi.Input[str] subject: The subject line of the email.
        :param pulumi.Input[str] text: The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
        """
        if html is not None:
            pulumi.set(__self__, "html", html)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if subject is not None:
            pulumi.set(__self__, "subject", subject)
        if text is not None:
            pulumi.set(__self__, "text", text)

    @property
    @pulumi.getter
    def html(self) -> Optional[pulumi.Input[str]]:
        """
        The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        """
        return pulumi.get(self, "html")

    @html.setter
    def html(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "html", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[str]]:
        """
        The subject line of the email.
        """
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[str]]:
        """
        The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
        """
        return pulumi.get(self, "text")

    @text.setter
    def text(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "text", value)


@pulumi.input_type
class _TemplateState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 html: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 text: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Template resources.
        :param pulumi.Input[str] arn: The ARN of the SES template
        :param pulumi.Input[str] html: The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        :param pulumi.Input[str] name: The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        :param pulumi.Input[str] subject: The subject line of the email.
        :param pulumi.Input[str] text: The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if html is not None:
            pulumi.set(__self__, "html", html)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if subject is not None:
            pulumi.set(__self__, "subject", subject)
        if text is not None:
            pulumi.set(__self__, "text", text)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the SES template
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def html(self) -> Optional[pulumi.Input[str]]:
        """
        The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        """
        return pulumi.get(self, "html")

    @html.setter
    def html(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "html", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[str]]:
        """
        The subject line of the email.
        """
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[str]]:
        """
        The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
        """
        return pulumi.get(self, "text")

    @text.setter
    def text(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "text", value)


class Template(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 html: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 text: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to create a SES template.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        my_template = aws.ses.Template("MyTemplate",
            name="MyTemplate",
            subject="Greetings, {{name}}!",
            html="<h1>Hello {{name}},</h1><p>Your favorite animal is {{favoriteanimal}}.</p>",
            text=\"\"\"Hello {{name}},\\x0d
        Your favorite animal is {{favoriteanimal}}.\"\"\")
        ```

        ## Import

        Using `pulumi import`, import SES templates using the template name. For example:

        ```sh
        $ pulumi import aws:ses/template:Template MyTemplate MyTemplate
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] html: The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        :param pulumi.Input[str] name: The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        :param pulumi.Input[str] subject: The subject line of the email.
        :param pulumi.Input[str] text: The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TemplateArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to create a SES template.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        my_template = aws.ses.Template("MyTemplate",
            name="MyTemplate",
            subject="Greetings, {{name}}!",
            html="<h1>Hello {{name}},</h1><p>Your favorite animal is {{favoriteanimal}}.</p>",
            text=\"\"\"Hello {{name}},\\x0d
        Your favorite animal is {{favoriteanimal}}.\"\"\")
        ```

        ## Import

        Using `pulumi import`, import SES templates using the template name. For example:

        ```sh
        $ pulumi import aws:ses/template:Template MyTemplate MyTemplate
        ```

        :param str resource_name: The name of the resource.
        :param TemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 html: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 text: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TemplateArgs.__new__(TemplateArgs)

            __props__.__dict__["html"] = html
            __props__.__dict__["name"] = name
            __props__.__dict__["subject"] = subject
            __props__.__dict__["text"] = text
            __props__.__dict__["arn"] = None
        super(Template, __self__).__init__(
            'aws:ses/template:Template',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            html: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            subject: Optional[pulumi.Input[str]] = None,
            text: Optional[pulumi.Input[str]] = None) -> 'Template':
        """
        Get an existing Template resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the SES template
        :param pulumi.Input[str] html: The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        :param pulumi.Input[str] name: The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        :param pulumi.Input[str] subject: The subject line of the email.
        :param pulumi.Input[str] text: The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TemplateState.__new__(_TemplateState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["html"] = html
        __props__.__dict__["name"] = name
        __props__.__dict__["subject"] = subject
        __props__.__dict__["text"] = text
        return Template(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the SES template
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def html(self) -> pulumi.Output[Optional[str]]:
        """
        The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        """
        return pulumi.get(self, "html")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Output[Optional[str]]:
        """
        The subject line of the email.
        """
        return pulumi.get(self, "subject")

    @property
    @pulumi.getter
    def text(self) -> pulumi.Output[Optional[str]]:
        """
        The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
        """
        return pulumi.get(self, "text")

