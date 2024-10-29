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

__all__ = ['ContributorInsightsArgs', 'ContributorInsights']

@pulumi.input_type
class ContributorInsightsArgs:
    def __init__(__self__, *,
                 table_name: pulumi.Input[str],
                 index_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ContributorInsights resource.
        :param pulumi.Input[str] table_name: The name of the table to enable contributor insights
        :param pulumi.Input[str] index_name: The global secondary index name
        """
        pulumi.set(__self__, "table_name", table_name)
        if index_name is not None:
            pulumi.set(__self__, "index_name", index_name)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[str]:
        """
        The name of the table to enable contributor insights
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "table_name", value)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> Optional[pulumi.Input[str]]:
        """
        The global secondary index name
        """
        return pulumi.get(self, "index_name")

    @index_name.setter
    def index_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "index_name", value)


@pulumi.input_type
class _ContributorInsightsState:
    def __init__(__self__, *,
                 index_name: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ContributorInsights resources.
        :param pulumi.Input[str] index_name: The global secondary index name
        :param pulumi.Input[str] table_name: The name of the table to enable contributor insights
        """
        if index_name is not None:
            pulumi.set(__self__, "index_name", index_name)
        if table_name is not None:
            pulumi.set(__self__, "table_name", table_name)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> Optional[pulumi.Input[str]]:
        """
        The global secondary index name
        """
        return pulumi.get(self, "index_name")

    @index_name.setter
    def index_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "index_name", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the table to enable contributor insights
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_name", value)


class ContributorInsights(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 index_name: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a DynamoDB contributor insights resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.dynamodb.ContributorInsights("test", table_name="ExampleTableName")
        ```

        ## Import

        Using `pulumi import`, import `aws_dynamodb_contributor_insights` using the format `name:table_name/index:index_name`, followed by the account number. For example:

        ```sh
        $ pulumi import aws:dynamodb/contributorInsights:ContributorInsights test name:ExampleTableName/index:ExampleIndexName/123456789012
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] index_name: The global secondary index name
        :param pulumi.Input[str] table_name: The name of the table to enable contributor insights
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContributorInsightsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DynamoDB contributor insights resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.dynamodb.ContributorInsights("test", table_name="ExampleTableName")
        ```

        ## Import

        Using `pulumi import`, import `aws_dynamodb_contributor_insights` using the format `name:table_name/index:index_name`, followed by the account number. For example:

        ```sh
        $ pulumi import aws:dynamodb/contributorInsights:ContributorInsights test name:ExampleTableName/index:ExampleIndexName/123456789012
        ```

        :param str resource_name: The name of the resource.
        :param ContributorInsightsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContributorInsightsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 index_name: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContributorInsightsArgs.__new__(ContributorInsightsArgs)

            __props__.__dict__["index_name"] = index_name
            if table_name is None and not opts.urn:
                raise TypeError("Missing required property 'table_name'")
            __props__.__dict__["table_name"] = table_name
        super(ContributorInsights, __self__).__init__(
            'aws:dynamodb/contributorInsights:ContributorInsights',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            index_name: Optional[pulumi.Input[str]] = None,
            table_name: Optional[pulumi.Input[str]] = None) -> 'ContributorInsights':
        """
        Get an existing ContributorInsights resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] index_name: The global secondary index name
        :param pulumi.Input[str] table_name: The name of the table to enable contributor insights
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ContributorInsightsState.__new__(_ContributorInsightsState)

        __props__.__dict__["index_name"] = index_name
        __props__.__dict__["table_name"] = table_name
        return ContributorInsights(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Output[Optional[str]]:
        """
        The global secondary index name
        """
        return pulumi.get(self, "index_name")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[str]:
        """
        The name of the table to enable contributor insights
        """
        return pulumi.get(self, "table_name")

