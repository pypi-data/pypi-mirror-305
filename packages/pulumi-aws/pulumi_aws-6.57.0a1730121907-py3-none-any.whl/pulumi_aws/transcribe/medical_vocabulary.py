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

__all__ = ['MedicalVocabularyArgs', 'MedicalVocabulary']

@pulumi.input_type
class MedicalVocabularyArgs:
    def __init__(__self__, *,
                 language_code: pulumi.Input[str],
                 vocabulary_file_uri: pulumi.Input[str],
                 vocabulary_name: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MedicalVocabulary resource.
        :param pulumi.Input[str] language_code: The language code you selected for your medical vocabulary. US English (en-US) is the only language supported with Amazon Transcribe Medical.
        :param pulumi.Input[str] vocabulary_file_uri: The Amazon S3 location (URI) of the text file that contains your custom medical vocabulary.
        :param pulumi.Input[str] vocabulary_name: The name of the Medical Vocabulary.
               
               The following arguments are optional:
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the MedicalVocabulary. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "language_code", language_code)
        pulumi.set(__self__, "vocabulary_file_uri", vocabulary_file_uri)
        pulumi.set(__self__, "vocabulary_name", vocabulary_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[str]:
        """
        The language code you selected for your medical vocabulary. US English (en-US) is the only language supported with Amazon Transcribe Medical.
        """
        return pulumi.get(self, "language_code")

    @language_code.setter
    def language_code(self, value: pulumi.Input[str]):
        pulumi.set(self, "language_code", value)

    @property
    @pulumi.getter(name="vocabularyFileUri")
    def vocabulary_file_uri(self) -> pulumi.Input[str]:
        """
        The Amazon S3 location (URI) of the text file that contains your custom medical vocabulary.
        """
        return pulumi.get(self, "vocabulary_file_uri")

    @vocabulary_file_uri.setter
    def vocabulary_file_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "vocabulary_file_uri", value)

    @property
    @pulumi.getter(name="vocabularyName")
    def vocabulary_name(self) -> pulumi.Input[str]:
        """
        The name of the Medical Vocabulary.

        The following arguments are optional:
        """
        return pulumi.get(self, "vocabulary_name")

    @vocabulary_name.setter
    def vocabulary_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vocabulary_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the MedicalVocabulary. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _MedicalVocabularyState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 download_uri: Optional[pulumi.Input[str]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vocabulary_file_uri: Optional[pulumi.Input[str]] = None,
                 vocabulary_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MedicalVocabulary resources.
        :param pulumi.Input[str] arn: ARN of the MedicalVocabulary.
        :param pulumi.Input[str] download_uri: Generated download URI.
        :param pulumi.Input[str] language_code: The language code you selected for your medical vocabulary. US English (en-US) is the only language supported with Amazon Transcribe Medical.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the MedicalVocabulary. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] vocabulary_file_uri: The Amazon S3 location (URI) of the text file that contains your custom medical vocabulary.
        :param pulumi.Input[str] vocabulary_name: The name of the Medical Vocabulary.
               
               The following arguments are optional:
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if download_uri is not None:
            pulumi.set(__self__, "download_uri", download_uri)
        if language_code is not None:
            pulumi.set(__self__, "language_code", language_code)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if vocabulary_file_uri is not None:
            pulumi.set(__self__, "vocabulary_file_uri", vocabulary_file_uri)
        if vocabulary_name is not None:
            pulumi.set(__self__, "vocabulary_name", vocabulary_name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the MedicalVocabulary.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="downloadUri")
    def download_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Generated download URI.
        """
        return pulumi.get(self, "download_uri")

    @download_uri.setter
    def download_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "download_uri", value)

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[str]]:
        """
        The language code you selected for your medical vocabulary. US English (en-US) is the only language supported with Amazon Transcribe Medical.
        """
        return pulumi.get(self, "language_code")

    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "language_code", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the MedicalVocabulary. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
    @pulumi.getter(name="vocabularyFileUri")
    def vocabulary_file_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon S3 location (URI) of the text file that contains your custom medical vocabulary.
        """
        return pulumi.get(self, "vocabulary_file_uri")

    @vocabulary_file_uri.setter
    def vocabulary_file_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vocabulary_file_uri", value)

    @property
    @pulumi.getter(name="vocabularyName")
    def vocabulary_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Medical Vocabulary.

        The following arguments are optional:
        """
        return pulumi.get(self, "vocabulary_name")

    @vocabulary_name.setter
    def vocabulary_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vocabulary_name", value)


class MedicalVocabulary(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vocabulary_file_uri: Optional[pulumi.Input[str]] = None,
                 vocabulary_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for managing an AWS Transcribe MedicalVocabulary.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketV2("example",
            bucket="example-medical-vocab-123",
            force_destroy=True)
        object = aws.s3.BucketObjectv2("object",
            bucket=example.id,
            key="transcribe/test1.txt",
            source=pulumi.FileAsset("test.txt"))
        example_medical_vocabulary = aws.transcribe.MedicalVocabulary("example",
            vocabulary_name="example",
            language_code="en-US",
            vocabulary_file_uri=pulumi.Output.all(
                id=example.id,
                key=object.key
        ).apply(lambda resolved_outputs: f"s3://{resolved_outputs['id']}/{resolved_outputs['key']}")
        ,
            tags={
                "tag1": "value1",
                "tag2": "value3",
            },
            opts = pulumi.ResourceOptions(depends_on=[object]))
        ```

        ## Import

        Using `pulumi import`, import Transcribe MedicalVocabulary using the `vocabulary_name`. For example:

        ```sh
        $ pulumi import aws:transcribe/medicalVocabulary:MedicalVocabulary example example-name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] language_code: The language code you selected for your medical vocabulary. US English (en-US) is the only language supported with Amazon Transcribe Medical.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the MedicalVocabulary. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] vocabulary_file_uri: The Amazon S3 location (URI) of the text file that contains your custom medical vocabulary.
        :param pulumi.Input[str] vocabulary_name: The name of the Medical Vocabulary.
               
               The following arguments are optional:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MedicalVocabularyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS Transcribe MedicalVocabulary.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketV2("example",
            bucket="example-medical-vocab-123",
            force_destroy=True)
        object = aws.s3.BucketObjectv2("object",
            bucket=example.id,
            key="transcribe/test1.txt",
            source=pulumi.FileAsset("test.txt"))
        example_medical_vocabulary = aws.transcribe.MedicalVocabulary("example",
            vocabulary_name="example",
            language_code="en-US",
            vocabulary_file_uri=pulumi.Output.all(
                id=example.id,
                key=object.key
        ).apply(lambda resolved_outputs: f"s3://{resolved_outputs['id']}/{resolved_outputs['key']}")
        ,
            tags={
                "tag1": "value1",
                "tag2": "value3",
            },
            opts = pulumi.ResourceOptions(depends_on=[object]))
        ```

        ## Import

        Using `pulumi import`, import Transcribe MedicalVocabulary using the `vocabulary_name`. For example:

        ```sh
        $ pulumi import aws:transcribe/medicalVocabulary:MedicalVocabulary example example-name
        ```

        :param str resource_name: The name of the resource.
        :param MedicalVocabularyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MedicalVocabularyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vocabulary_file_uri: Optional[pulumi.Input[str]] = None,
                 vocabulary_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MedicalVocabularyArgs.__new__(MedicalVocabularyArgs)

            if language_code is None and not opts.urn:
                raise TypeError("Missing required property 'language_code'")
            __props__.__dict__["language_code"] = language_code
            __props__.__dict__["tags"] = tags
            if vocabulary_file_uri is None and not opts.urn:
                raise TypeError("Missing required property 'vocabulary_file_uri'")
            __props__.__dict__["vocabulary_file_uri"] = vocabulary_file_uri
            if vocabulary_name is None and not opts.urn:
                raise TypeError("Missing required property 'vocabulary_name'")
            __props__.__dict__["vocabulary_name"] = vocabulary_name
            __props__.__dict__["arn"] = None
            __props__.__dict__["download_uri"] = None
            __props__.__dict__["tags_all"] = None
        super(MedicalVocabulary, __self__).__init__(
            'aws:transcribe/medicalVocabulary:MedicalVocabulary',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            download_uri: Optional[pulumi.Input[str]] = None,
            language_code: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vocabulary_file_uri: Optional[pulumi.Input[str]] = None,
            vocabulary_name: Optional[pulumi.Input[str]] = None) -> 'MedicalVocabulary':
        """
        Get an existing MedicalVocabulary resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the MedicalVocabulary.
        :param pulumi.Input[str] download_uri: Generated download URI.
        :param pulumi.Input[str] language_code: The language code you selected for your medical vocabulary. US English (en-US) is the only language supported with Amazon Transcribe Medical.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the MedicalVocabulary. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] vocabulary_file_uri: The Amazon S3 location (URI) of the text file that contains your custom medical vocabulary.
        :param pulumi.Input[str] vocabulary_name: The name of the Medical Vocabulary.
               
               The following arguments are optional:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MedicalVocabularyState.__new__(_MedicalVocabularyState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["download_uri"] = download_uri
        __props__.__dict__["language_code"] = language_code
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["vocabulary_file_uri"] = vocabulary_file_uri
        __props__.__dict__["vocabulary_name"] = vocabulary_name
        return MedicalVocabulary(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the MedicalVocabulary.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="downloadUri")
    def download_uri(self) -> pulumi.Output[str]:
        """
        Generated download URI.
        """
        return pulumi.get(self, "download_uri")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[str]:
        """
        The language code you selected for your medical vocabulary. US English (en-US) is the only language supported with Amazon Transcribe Medical.
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the MedicalVocabulary. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    @_utilities.deprecated("""Please use `tags` instead.""")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="vocabularyFileUri")
    def vocabulary_file_uri(self) -> pulumi.Output[str]:
        """
        The Amazon S3 location (URI) of the text file that contains your custom medical vocabulary.
        """
        return pulumi.get(self, "vocabulary_file_uri")

    @property
    @pulumi.getter(name="vocabularyName")
    def vocabulary_name(self) -> pulumi.Output[str]:
        """
        The name of the Medical Vocabulary.

        The following arguments are optional:
        """
        return pulumi.get(self, "vocabulary_name")

