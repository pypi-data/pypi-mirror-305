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

__all__ = [
    'GetQuerySuggestionsBlockListResult',
    'AwaitableGetQuerySuggestionsBlockListResult',
    'get_query_suggestions_block_list',
    'get_query_suggestions_block_list_output',
]

@pulumi.output_type
class GetQuerySuggestionsBlockListResult:
    """
    A collection of values returned by getQuerySuggestionsBlockList.
    """
    def __init__(__self__, arn=None, created_at=None, description=None, error_message=None, file_size_bytes=None, id=None, index_id=None, item_count=None, name=None, query_suggestions_block_list_id=None, role_arn=None, source_s3_paths=None, status=None, tags=None, updated_at=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        pulumi.set(__self__, "error_message", error_message)
        if file_size_bytes and not isinstance(file_size_bytes, int):
            raise TypeError("Expected argument 'file_size_bytes' to be a int")
        pulumi.set(__self__, "file_size_bytes", file_size_bytes)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if index_id and not isinstance(index_id, str):
            raise TypeError("Expected argument 'index_id' to be a str")
        pulumi.set(__self__, "index_id", index_id)
        if item_count and not isinstance(item_count, int):
            raise TypeError("Expected argument 'item_count' to be a int")
        pulumi.set(__self__, "item_count", item_count)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if query_suggestions_block_list_id and not isinstance(query_suggestions_block_list_id, str):
            raise TypeError("Expected argument 'query_suggestions_block_list_id' to be a str")
        pulumi.set(__self__, "query_suggestions_block_list_id", query_suggestions_block_list_id)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if source_s3_paths and not isinstance(source_s3_paths, list):
            raise TypeError("Expected argument 'source_s3_paths' to be a list")
        pulumi.set(__self__, "source_s3_paths", source_s3_paths)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the block list.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Date-time a block list was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description for the block list.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        """
        Error message containing details if there are issues processing the block list.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="fileSizeBytes")
    def file_size_bytes(self) -> int:
        """
        Current size of the block list text file in S3.
        """
        return pulumi.get(self, "file_size_bytes")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="indexId")
    def index_id(self) -> str:
        return pulumi.get(self, "index_id")

    @property
    @pulumi.getter(name="itemCount")
    def item_count(self) -> int:
        """
        Current number of valid, non-empty words or phrases in the block list text file.
        """
        return pulumi.get(self, "item_count")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the block list.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="querySuggestionsBlockListId")
    def query_suggestions_block_list_id(self) -> str:
        return pulumi.get(self, "query_suggestions_block_list_id")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> str:
        """
        ARN of a role with permission to access the S3 bucket that contains the block list. For more information, see [IAM Roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html).
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="sourceS3Paths")
    def source_s3_paths(self) -> Sequence['outputs.GetQuerySuggestionsBlockListSourceS3PathResult']:
        """
        S3 location of the block list input data. Detailed below.
        """
        return pulumi.get(self, "source_s3_paths")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Current status of the block list. When the value is `ACTIVE`, the block list is ready for use.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Metadata that helps organize the block list you create.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        Date and time that the block list was last updated.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetQuerySuggestionsBlockListResult(GetQuerySuggestionsBlockListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQuerySuggestionsBlockListResult(
            arn=self.arn,
            created_at=self.created_at,
            description=self.description,
            error_message=self.error_message,
            file_size_bytes=self.file_size_bytes,
            id=self.id,
            index_id=self.index_id,
            item_count=self.item_count,
            name=self.name,
            query_suggestions_block_list_id=self.query_suggestions_block_list_id,
            role_arn=self.role_arn,
            source_s3_paths=self.source_s3_paths,
            status=self.status,
            tags=self.tags,
            updated_at=self.updated_at)


def get_query_suggestions_block_list(index_id: Optional[str] = None,
                                     query_suggestions_block_list_id: Optional[str] = None,
                                     tags: Optional[Mapping[str, str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQuerySuggestionsBlockListResult:
    """
    Provides details about a specific Amazon Kendra block list used for query suggestions for an index.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.kendra.get_query_suggestions_block_list(index_id="12345678-1234-1234-1234-123456789123",
        query_suggestions_block_list_id="87654321-1234-4321-4321-321987654321")
    ```


    :param str index_id: Identifier of the index that contains the block list.
    :param str query_suggestions_block_list_id: Identifier of the block list.
    :param Mapping[str, str] tags: Metadata that helps organize the block list you create.
    """
    __args__ = dict()
    __args__['indexId'] = index_id
    __args__['querySuggestionsBlockListId'] = query_suggestions_block_list_id
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:kendra/getQuerySuggestionsBlockList:getQuerySuggestionsBlockList', __args__, opts=opts, typ=GetQuerySuggestionsBlockListResult).value

    return AwaitableGetQuerySuggestionsBlockListResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_at=pulumi.get(__ret__, 'created_at'),
        description=pulumi.get(__ret__, 'description'),
        error_message=pulumi.get(__ret__, 'error_message'),
        file_size_bytes=pulumi.get(__ret__, 'file_size_bytes'),
        id=pulumi.get(__ret__, 'id'),
        index_id=pulumi.get(__ret__, 'index_id'),
        item_count=pulumi.get(__ret__, 'item_count'),
        name=pulumi.get(__ret__, 'name'),
        query_suggestions_block_list_id=pulumi.get(__ret__, 'query_suggestions_block_list_id'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        source_s3_paths=pulumi.get(__ret__, 'source_s3_paths'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        updated_at=pulumi.get(__ret__, 'updated_at'))
def get_query_suggestions_block_list_output(index_id: Optional[pulumi.Input[str]] = None,
                                            query_suggestions_block_list_id: Optional[pulumi.Input[str]] = None,
                                            tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQuerySuggestionsBlockListResult]:
    """
    Provides details about a specific Amazon Kendra block list used for query suggestions for an index.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.kendra.get_query_suggestions_block_list(index_id="12345678-1234-1234-1234-123456789123",
        query_suggestions_block_list_id="87654321-1234-4321-4321-321987654321")
    ```


    :param str index_id: Identifier of the index that contains the block list.
    :param str query_suggestions_block_list_id: Identifier of the block list.
    :param Mapping[str, str] tags: Metadata that helps organize the block list you create.
    """
    __args__ = dict()
    __args__['indexId'] = index_id
    __args__['querySuggestionsBlockListId'] = query_suggestions_block_list_id
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:kendra/getQuerySuggestionsBlockList:getQuerySuggestionsBlockList', __args__, opts=opts, typ=GetQuerySuggestionsBlockListResult)
    return __ret__.apply(lambda __response__: GetQuerySuggestionsBlockListResult(
        arn=pulumi.get(__response__, 'arn'),
        created_at=pulumi.get(__response__, 'created_at'),
        description=pulumi.get(__response__, 'description'),
        error_message=pulumi.get(__response__, 'error_message'),
        file_size_bytes=pulumi.get(__response__, 'file_size_bytes'),
        id=pulumi.get(__response__, 'id'),
        index_id=pulumi.get(__response__, 'index_id'),
        item_count=pulumi.get(__response__, 'item_count'),
        name=pulumi.get(__response__, 'name'),
        query_suggestions_block_list_id=pulumi.get(__response__, 'query_suggestions_block_list_id'),
        role_arn=pulumi.get(__response__, 'role_arn'),
        source_s3_paths=pulumi.get(__response__, 'source_s3_paths'),
        status=pulumi.get(__response__, 'status'),
        tags=pulumi.get(__response__, 'tags'),
        updated_at=pulumi.get(__response__, 'updated_at')))
