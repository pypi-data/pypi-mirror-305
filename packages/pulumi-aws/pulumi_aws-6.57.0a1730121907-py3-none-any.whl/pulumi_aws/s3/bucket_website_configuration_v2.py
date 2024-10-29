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

__all__ = ['BucketWebsiteConfigurationV2Args', 'BucketWebsiteConfigurationV2']

@pulumi.input_type
class BucketWebsiteConfigurationV2Args:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 error_document: Optional[pulumi.Input['BucketWebsiteConfigurationV2ErrorDocumentArgs']] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 index_document: Optional[pulumi.Input['BucketWebsiteConfigurationV2IndexDocumentArgs']] = None,
                 redirect_all_requests_to: Optional[pulumi.Input['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs']] = None,
                 routing_rule_details: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input['BucketWebsiteConfigurationV2RoutingRuleArgs']]]] = None):
        """
        The set of arguments for constructing a BucketWebsiteConfigurationV2 resource.
        :param pulumi.Input[str] bucket: Name of the bucket.
        :param pulumi.Input['BucketWebsiteConfigurationV2ErrorDocumentArgs'] error_document: Name of the error document for the website. See below.
        :param pulumi.Input[str] expected_bucket_owner: Account ID of the expected bucket owner.
        :param pulumi.Input['BucketWebsiteConfigurationV2IndexDocumentArgs'] index_document: Name of the index document for the website. See below.
        :param pulumi.Input['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs'] redirect_all_requests_to: Redirect behavior for every request to this bucket's website endpoint. See below. Conflicts with `error_document`, `index_document`, and `routing_rule`.
        :param pulumi.Input[str] routing_rule_details: JSON array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
               describing redirect behavior and when redirects are applied. Use this parameter when your routing rules contain empty String values (`""`) as seen in the example above.
        :param pulumi.Input[Sequence[pulumi.Input['BucketWebsiteConfigurationV2RoutingRuleArgs']]] routing_rules: List of rules that define when a redirect is applied and the redirect behavior. See below.
        """
        pulumi.set(__self__, "bucket", bucket)
        if error_document is not None:
            pulumi.set(__self__, "error_document", error_document)
        if expected_bucket_owner is not None:
            pulumi.set(__self__, "expected_bucket_owner", expected_bucket_owner)
        if index_document is not None:
            pulumi.set(__self__, "index_document", index_document)
        if redirect_all_requests_to is not None:
            pulumi.set(__self__, "redirect_all_requests_to", redirect_all_requests_to)
        if routing_rule_details is not None:
            pulumi.set(__self__, "routing_rule_details", routing_rule_details)
        if routing_rules is not None:
            pulumi.set(__self__, "routing_rules", routing_rules)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        Name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="errorDocument")
    def error_document(self) -> Optional[pulumi.Input['BucketWebsiteConfigurationV2ErrorDocumentArgs']]:
        """
        Name of the error document for the website. See below.
        """
        return pulumi.get(self, "error_document")

    @error_document.setter
    def error_document(self, value: Optional[pulumi.Input['BucketWebsiteConfigurationV2ErrorDocumentArgs']]):
        pulumi.set(self, "error_document", value)

    @property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[str]]:
        """
        Account ID of the expected bucket owner.
        """
        return pulumi.get(self, "expected_bucket_owner")

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expected_bucket_owner", value)

    @property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> Optional[pulumi.Input['BucketWebsiteConfigurationV2IndexDocumentArgs']]:
        """
        Name of the index document for the website. See below.
        """
        return pulumi.get(self, "index_document")

    @index_document.setter
    def index_document(self, value: Optional[pulumi.Input['BucketWebsiteConfigurationV2IndexDocumentArgs']]):
        pulumi.set(self, "index_document", value)

    @property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(self) -> Optional[pulumi.Input['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs']]:
        """
        Redirect behavior for every request to this bucket's website endpoint. See below. Conflicts with `error_document`, `index_document`, and `routing_rule`.
        """
        return pulumi.get(self, "redirect_all_requests_to")

    @redirect_all_requests_to.setter
    def redirect_all_requests_to(self, value: Optional[pulumi.Input['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs']]):
        pulumi.set(self, "redirect_all_requests_to", value)

    @property
    @pulumi.getter(name="routingRuleDetails")
    def routing_rule_details(self) -> Optional[pulumi.Input[str]]:
        """
        JSON array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
        describing redirect behavior and when redirects are applied. Use this parameter when your routing rules contain empty String values (`""`) as seen in the example above.
        """
        return pulumi.get(self, "routing_rule_details")

    @routing_rule_details.setter
    def routing_rule_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_rule_details", value)

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketWebsiteConfigurationV2RoutingRuleArgs']]]]:
        """
        List of rules that define when a redirect is applied and the redirect behavior. See below.
        """
        return pulumi.get(self, "routing_rules")

    @routing_rules.setter
    def routing_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketWebsiteConfigurationV2RoutingRuleArgs']]]]):
        pulumi.set(self, "routing_rules", value)


@pulumi.input_type
class _BucketWebsiteConfigurationV2State:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 error_document: Optional[pulumi.Input['BucketWebsiteConfigurationV2ErrorDocumentArgs']] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 index_document: Optional[pulumi.Input['BucketWebsiteConfigurationV2IndexDocumentArgs']] = None,
                 redirect_all_requests_to: Optional[pulumi.Input['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs']] = None,
                 routing_rule_details: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input['BucketWebsiteConfigurationV2RoutingRuleArgs']]]] = None,
                 website_domain: Optional[pulumi.Input[str]] = None,
                 website_endpoint: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BucketWebsiteConfigurationV2 resources.
        :param pulumi.Input[str] bucket: Name of the bucket.
        :param pulumi.Input['BucketWebsiteConfigurationV2ErrorDocumentArgs'] error_document: Name of the error document for the website. See below.
        :param pulumi.Input[str] expected_bucket_owner: Account ID of the expected bucket owner.
        :param pulumi.Input['BucketWebsiteConfigurationV2IndexDocumentArgs'] index_document: Name of the index document for the website. See below.
        :param pulumi.Input['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs'] redirect_all_requests_to: Redirect behavior for every request to this bucket's website endpoint. See below. Conflicts with `error_document`, `index_document`, and `routing_rule`.
        :param pulumi.Input[str] routing_rule_details: JSON array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
               describing redirect behavior and when redirects are applied. Use this parameter when your routing rules contain empty String values (`""`) as seen in the example above.
        :param pulumi.Input[Sequence[pulumi.Input['BucketWebsiteConfigurationV2RoutingRuleArgs']]] routing_rules: List of rules that define when a redirect is applied and the redirect behavior. See below.
        :param pulumi.Input[str] website_domain: Domain of the website endpoint. This is used to create Route 53 alias records.
        :param pulumi.Input[str] website_endpoint: Website endpoint.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if error_document is not None:
            pulumi.set(__self__, "error_document", error_document)
        if expected_bucket_owner is not None:
            pulumi.set(__self__, "expected_bucket_owner", expected_bucket_owner)
        if index_document is not None:
            pulumi.set(__self__, "index_document", index_document)
        if redirect_all_requests_to is not None:
            pulumi.set(__self__, "redirect_all_requests_to", redirect_all_requests_to)
        if routing_rule_details is not None:
            pulumi.set(__self__, "routing_rule_details", routing_rule_details)
        if routing_rules is not None:
            pulumi.set(__self__, "routing_rules", routing_rules)
        if website_domain is not None:
            pulumi.set(__self__, "website_domain", website_domain)
        if website_endpoint is not None:
            pulumi.set(__self__, "website_endpoint", website_endpoint)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="errorDocument")
    def error_document(self) -> Optional[pulumi.Input['BucketWebsiteConfigurationV2ErrorDocumentArgs']]:
        """
        Name of the error document for the website. See below.
        """
        return pulumi.get(self, "error_document")

    @error_document.setter
    def error_document(self, value: Optional[pulumi.Input['BucketWebsiteConfigurationV2ErrorDocumentArgs']]):
        pulumi.set(self, "error_document", value)

    @property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[str]]:
        """
        Account ID of the expected bucket owner.
        """
        return pulumi.get(self, "expected_bucket_owner")

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expected_bucket_owner", value)

    @property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> Optional[pulumi.Input['BucketWebsiteConfigurationV2IndexDocumentArgs']]:
        """
        Name of the index document for the website. See below.
        """
        return pulumi.get(self, "index_document")

    @index_document.setter
    def index_document(self, value: Optional[pulumi.Input['BucketWebsiteConfigurationV2IndexDocumentArgs']]):
        pulumi.set(self, "index_document", value)

    @property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(self) -> Optional[pulumi.Input['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs']]:
        """
        Redirect behavior for every request to this bucket's website endpoint. See below. Conflicts with `error_document`, `index_document`, and `routing_rule`.
        """
        return pulumi.get(self, "redirect_all_requests_to")

    @redirect_all_requests_to.setter
    def redirect_all_requests_to(self, value: Optional[pulumi.Input['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs']]):
        pulumi.set(self, "redirect_all_requests_to", value)

    @property
    @pulumi.getter(name="routingRuleDetails")
    def routing_rule_details(self) -> Optional[pulumi.Input[str]]:
        """
        JSON array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
        describing redirect behavior and when redirects are applied. Use this parameter when your routing rules contain empty String values (`""`) as seen in the example above.
        """
        return pulumi.get(self, "routing_rule_details")

    @routing_rule_details.setter
    def routing_rule_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_rule_details", value)

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketWebsiteConfigurationV2RoutingRuleArgs']]]]:
        """
        List of rules that define when a redirect is applied and the redirect behavior. See below.
        """
        return pulumi.get(self, "routing_rules")

    @routing_rules.setter
    def routing_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketWebsiteConfigurationV2RoutingRuleArgs']]]]):
        pulumi.set(self, "routing_rules", value)

    @property
    @pulumi.getter(name="websiteDomain")
    def website_domain(self) -> Optional[pulumi.Input[str]]:
        """
        Domain of the website endpoint. This is used to create Route 53 alias records.
        """
        return pulumi.get(self, "website_domain")

    @website_domain.setter
    def website_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "website_domain", value)

    @property
    @pulumi.getter(name="websiteEndpoint")
    def website_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Website endpoint.
        """
        return pulumi.get(self, "website_endpoint")

    @website_endpoint.setter
    def website_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "website_endpoint", value)


class BucketWebsiteConfigurationV2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 error_document: Optional[pulumi.Input[Union['BucketWebsiteConfigurationV2ErrorDocumentArgs', 'BucketWebsiteConfigurationV2ErrorDocumentArgsDict']]] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 index_document: Optional[pulumi.Input[Union['BucketWebsiteConfigurationV2IndexDocumentArgs', 'BucketWebsiteConfigurationV2IndexDocumentArgsDict']]] = None,
                 redirect_all_requests_to: Optional[pulumi.Input[Union['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs', 'BucketWebsiteConfigurationV2RedirectAllRequestsToArgsDict']]] = None,
                 routing_rule_details: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['BucketWebsiteConfigurationV2RoutingRuleArgs', 'BucketWebsiteConfigurationV2RoutingRuleArgsDict']]]]] = None,
                 __props__=None):
        """
        Provides an S3 bucket website configuration resource. For more information, see [Hosting Websites on S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).

        > This resource cannot be used with S3 directory buckets.

        ## Example Usage

        ### With `routing_rule` configured

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketWebsiteConfigurationV2("example",
            bucket=example_aws_s3_bucket["id"],
            index_document={
                "suffix": "index.html",
            },
            error_document={
                "key": "error.html",
            },
            routing_rules=[{
                "condition": {
                    "key_prefix_equals": "docs/",
                },
                "redirect": {
                    "replace_key_prefix_with": "documents/",
                },
            }])
        ```

        ### With `routing_rules` configured

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketWebsiteConfigurationV2("example",
            bucket=example_aws_s3_bucket["id"],
            index_document={
                "suffix": "index.html",
            },
            error_document={
                "key": "error.html",
            },
            routing_rule_details=\"\"\"[{
            "Condition": {
                "KeyPrefixEquals": "docs/"
            },
            "Redirect": {
                "ReplaceKeyPrefixWith": ""
            }
        }]
        \"\"\")
        ```

        ## Import

        If the owner (account ID) of the source bucket differs from the account used to configure the AWS Provider, import using the `bucket` and `expected_bucket_owner` separated by a comma (`,`):

        __Using `pulumi import` to import__ S3 bucket website configuration using the `bucket` or using the `bucket` and `expected_bucket_owner` separated by a comma (`,`). For example:

        If the owner (account ID) of the source bucket is the same account used to configure the AWS Provider, import using the `bucket`:

        ```sh
        $ pulumi import aws:s3/bucketWebsiteConfigurationV2:BucketWebsiteConfigurationV2 example bucket-name
        ```
        If the owner (account ID) of the source bucket differs from the account used to configure the AWS Provider, import using the `bucket` and `expected_bucket_owner` separated by a comma (`,`):

        ```sh
        $ pulumi import aws:s3/bucketWebsiteConfigurationV2:BucketWebsiteConfigurationV2 example bucket-name,123456789012
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: Name of the bucket.
        :param pulumi.Input[Union['BucketWebsiteConfigurationV2ErrorDocumentArgs', 'BucketWebsiteConfigurationV2ErrorDocumentArgsDict']] error_document: Name of the error document for the website. See below.
        :param pulumi.Input[str] expected_bucket_owner: Account ID of the expected bucket owner.
        :param pulumi.Input[Union['BucketWebsiteConfigurationV2IndexDocumentArgs', 'BucketWebsiteConfigurationV2IndexDocumentArgsDict']] index_document: Name of the index document for the website. See below.
        :param pulumi.Input[Union['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs', 'BucketWebsiteConfigurationV2RedirectAllRequestsToArgsDict']] redirect_all_requests_to: Redirect behavior for every request to this bucket's website endpoint. See below. Conflicts with `error_document`, `index_document`, and `routing_rule`.
        :param pulumi.Input[str] routing_rule_details: JSON array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
               describing redirect behavior and when redirects are applied. Use this parameter when your routing rules contain empty String values (`""`) as seen in the example above.
        :param pulumi.Input[Sequence[pulumi.Input[Union['BucketWebsiteConfigurationV2RoutingRuleArgs', 'BucketWebsiteConfigurationV2RoutingRuleArgsDict']]]] routing_rules: List of rules that define when a redirect is applied and the redirect behavior. See below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BucketWebsiteConfigurationV2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an S3 bucket website configuration resource. For more information, see [Hosting Websites on S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).

        > This resource cannot be used with S3 directory buckets.

        ## Example Usage

        ### With `routing_rule` configured

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketWebsiteConfigurationV2("example",
            bucket=example_aws_s3_bucket["id"],
            index_document={
                "suffix": "index.html",
            },
            error_document={
                "key": "error.html",
            },
            routing_rules=[{
                "condition": {
                    "key_prefix_equals": "docs/",
                },
                "redirect": {
                    "replace_key_prefix_with": "documents/",
                },
            }])
        ```

        ### With `routing_rules` configured

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketWebsiteConfigurationV2("example",
            bucket=example_aws_s3_bucket["id"],
            index_document={
                "suffix": "index.html",
            },
            error_document={
                "key": "error.html",
            },
            routing_rule_details=\"\"\"[{
            "Condition": {
                "KeyPrefixEquals": "docs/"
            },
            "Redirect": {
                "ReplaceKeyPrefixWith": ""
            }
        }]
        \"\"\")
        ```

        ## Import

        If the owner (account ID) of the source bucket differs from the account used to configure the AWS Provider, import using the `bucket` and `expected_bucket_owner` separated by a comma (`,`):

        __Using `pulumi import` to import__ S3 bucket website configuration using the `bucket` or using the `bucket` and `expected_bucket_owner` separated by a comma (`,`). For example:

        If the owner (account ID) of the source bucket is the same account used to configure the AWS Provider, import using the `bucket`:

        ```sh
        $ pulumi import aws:s3/bucketWebsiteConfigurationV2:BucketWebsiteConfigurationV2 example bucket-name
        ```
        If the owner (account ID) of the source bucket differs from the account used to configure the AWS Provider, import using the `bucket` and `expected_bucket_owner` separated by a comma (`,`):

        ```sh
        $ pulumi import aws:s3/bucketWebsiteConfigurationV2:BucketWebsiteConfigurationV2 example bucket-name,123456789012
        ```

        :param str resource_name: The name of the resource.
        :param BucketWebsiteConfigurationV2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketWebsiteConfigurationV2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 error_document: Optional[pulumi.Input[Union['BucketWebsiteConfigurationV2ErrorDocumentArgs', 'BucketWebsiteConfigurationV2ErrorDocumentArgsDict']]] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 index_document: Optional[pulumi.Input[Union['BucketWebsiteConfigurationV2IndexDocumentArgs', 'BucketWebsiteConfigurationV2IndexDocumentArgsDict']]] = None,
                 redirect_all_requests_to: Optional[pulumi.Input[Union['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs', 'BucketWebsiteConfigurationV2RedirectAllRequestsToArgsDict']]] = None,
                 routing_rule_details: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['BucketWebsiteConfigurationV2RoutingRuleArgs', 'BucketWebsiteConfigurationV2RoutingRuleArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BucketWebsiteConfigurationV2Args.__new__(BucketWebsiteConfigurationV2Args)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["error_document"] = error_document
            __props__.__dict__["expected_bucket_owner"] = expected_bucket_owner
            __props__.__dict__["index_document"] = index_document
            __props__.__dict__["redirect_all_requests_to"] = redirect_all_requests_to
            __props__.__dict__["routing_rule_details"] = routing_rule_details
            __props__.__dict__["routing_rules"] = routing_rules
            __props__.__dict__["website_domain"] = None
            __props__.__dict__["website_endpoint"] = None
        super(BucketWebsiteConfigurationV2, __self__).__init__(
            'aws:s3/bucketWebsiteConfigurationV2:BucketWebsiteConfigurationV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            error_document: Optional[pulumi.Input[Union['BucketWebsiteConfigurationV2ErrorDocumentArgs', 'BucketWebsiteConfigurationV2ErrorDocumentArgsDict']]] = None,
            expected_bucket_owner: Optional[pulumi.Input[str]] = None,
            index_document: Optional[pulumi.Input[Union['BucketWebsiteConfigurationV2IndexDocumentArgs', 'BucketWebsiteConfigurationV2IndexDocumentArgsDict']]] = None,
            redirect_all_requests_to: Optional[pulumi.Input[Union['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs', 'BucketWebsiteConfigurationV2RedirectAllRequestsToArgsDict']]] = None,
            routing_rule_details: Optional[pulumi.Input[str]] = None,
            routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['BucketWebsiteConfigurationV2RoutingRuleArgs', 'BucketWebsiteConfigurationV2RoutingRuleArgsDict']]]]] = None,
            website_domain: Optional[pulumi.Input[str]] = None,
            website_endpoint: Optional[pulumi.Input[str]] = None) -> 'BucketWebsiteConfigurationV2':
        """
        Get an existing BucketWebsiteConfigurationV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: Name of the bucket.
        :param pulumi.Input[Union['BucketWebsiteConfigurationV2ErrorDocumentArgs', 'BucketWebsiteConfigurationV2ErrorDocumentArgsDict']] error_document: Name of the error document for the website. See below.
        :param pulumi.Input[str] expected_bucket_owner: Account ID of the expected bucket owner.
        :param pulumi.Input[Union['BucketWebsiteConfigurationV2IndexDocumentArgs', 'BucketWebsiteConfigurationV2IndexDocumentArgsDict']] index_document: Name of the index document for the website. See below.
        :param pulumi.Input[Union['BucketWebsiteConfigurationV2RedirectAllRequestsToArgs', 'BucketWebsiteConfigurationV2RedirectAllRequestsToArgsDict']] redirect_all_requests_to: Redirect behavior for every request to this bucket's website endpoint. See below. Conflicts with `error_document`, `index_document`, and `routing_rule`.
        :param pulumi.Input[str] routing_rule_details: JSON array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
               describing redirect behavior and when redirects are applied. Use this parameter when your routing rules contain empty String values (`""`) as seen in the example above.
        :param pulumi.Input[Sequence[pulumi.Input[Union['BucketWebsiteConfigurationV2RoutingRuleArgs', 'BucketWebsiteConfigurationV2RoutingRuleArgsDict']]]] routing_rules: List of rules that define when a redirect is applied and the redirect behavior. See below.
        :param pulumi.Input[str] website_domain: Domain of the website endpoint. This is used to create Route 53 alias records.
        :param pulumi.Input[str] website_endpoint: Website endpoint.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BucketWebsiteConfigurationV2State.__new__(_BucketWebsiteConfigurationV2State)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["error_document"] = error_document
        __props__.__dict__["expected_bucket_owner"] = expected_bucket_owner
        __props__.__dict__["index_document"] = index_document
        __props__.__dict__["redirect_all_requests_to"] = redirect_all_requests_to
        __props__.__dict__["routing_rule_details"] = routing_rule_details
        __props__.__dict__["routing_rules"] = routing_rules
        __props__.__dict__["website_domain"] = website_domain
        __props__.__dict__["website_endpoint"] = website_endpoint
        return BucketWebsiteConfigurationV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        Name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="errorDocument")
    def error_document(self) -> pulumi.Output[Optional['outputs.BucketWebsiteConfigurationV2ErrorDocument']]:
        """
        Name of the error document for the website. See below.
        """
        return pulumi.get(self, "error_document")

    @property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> pulumi.Output[Optional[str]]:
        """
        Account ID of the expected bucket owner.
        """
        return pulumi.get(self, "expected_bucket_owner")

    @property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> pulumi.Output[Optional['outputs.BucketWebsiteConfigurationV2IndexDocument']]:
        """
        Name of the index document for the website. See below.
        """
        return pulumi.get(self, "index_document")

    @property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(self) -> pulumi.Output[Optional['outputs.BucketWebsiteConfigurationV2RedirectAllRequestsTo']]:
        """
        Redirect behavior for every request to this bucket's website endpoint. See below. Conflicts with `error_document`, `index_document`, and `routing_rule`.
        """
        return pulumi.get(self, "redirect_all_requests_to")

    @property
    @pulumi.getter(name="routingRuleDetails")
    def routing_rule_details(self) -> pulumi.Output[str]:
        """
        JSON array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
        describing redirect behavior and when redirects are applied. Use this parameter when your routing rules contain empty String values (`""`) as seen in the example above.
        """
        return pulumi.get(self, "routing_rule_details")

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> pulumi.Output[Sequence['outputs.BucketWebsiteConfigurationV2RoutingRule']]:
        """
        List of rules that define when a redirect is applied and the redirect behavior. See below.
        """
        return pulumi.get(self, "routing_rules")

    @property
    @pulumi.getter(name="websiteDomain")
    def website_domain(self) -> pulumi.Output[str]:
        """
        Domain of the website endpoint. This is used to create Route 53 alias records.
        """
        return pulumi.get(self, "website_domain")

    @property
    @pulumi.getter(name="websiteEndpoint")
    def website_endpoint(self) -> pulumi.Output[str]:
        """
        Website endpoint.
        """
        return pulumi.get(self, "website_endpoint")

