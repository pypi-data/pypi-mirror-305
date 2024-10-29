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
    'GetAnalysisResult',
    'AwaitableGetAnalysisResult',
    'get_analysis',
    'get_analysis_output',
]

warnings.warn("""aws.quicksight/getanalysis.getAnalysis has been deprecated in favor of aws.quicksight/getquicksightanalysis.getQuicksightAnalysis""", DeprecationWarning)

@pulumi.output_type
class GetAnalysisResult:
    """
    A collection of values returned by getAnalysis.
    """
    def __init__(__self__, analysis_id=None, arn=None, aws_account_id=None, created_time=None, id=None, last_published_time=None, last_updated_time=None, name=None, permissions=None, status=None, tags=None, theme_arn=None):
        if analysis_id and not isinstance(analysis_id, str):
            raise TypeError("Expected argument 'analysis_id' to be a str")
        pulumi.set(__self__, "analysis_id", analysis_id)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if aws_account_id and not isinstance(aws_account_id, str):
            raise TypeError("Expected argument 'aws_account_id' to be a str")
        pulumi.set(__self__, "aws_account_id", aws_account_id)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_published_time and not isinstance(last_published_time, str):
            raise TypeError("Expected argument 'last_published_time' to be a str")
        pulumi.set(__self__, "last_published_time", last_published_time)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if theme_arn and not isinstance(theme_arn, str):
            raise TypeError("Expected argument 'theme_arn' to be a str")
        pulumi.set(__self__, "theme_arn", theme_arn)

    @property
    @pulumi.getter(name="analysisId")
    def analysis_id(self) -> str:
        return pulumi.get(self, "analysis_id")

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> str:
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastPublishedTime")
    def last_published_time(self) -> str:
        return pulumi.get(self, "last_published_time")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> str:
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> Sequence['outputs.GetAnalysisPermissionResult']:
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="themeArn")
    def theme_arn(self) -> str:
        return pulumi.get(self, "theme_arn")


class AwaitableGetAnalysisResult(GetAnalysisResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAnalysisResult(
            analysis_id=self.analysis_id,
            arn=self.arn,
            aws_account_id=self.aws_account_id,
            created_time=self.created_time,
            id=self.id,
            last_published_time=self.last_published_time,
            last_updated_time=self.last_updated_time,
            name=self.name,
            permissions=self.permissions,
            status=self.status,
            tags=self.tags,
            theme_arn=self.theme_arn)


def get_analysis(analysis_id: Optional[str] = None,
                 aws_account_id: Optional[str] = None,
                 tags: Optional[Mapping[str, str]] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAnalysisResult:
    """
    Data source for managing an AWS QuickSight Analysis.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.quicksight.get_quicksight_analysis(analysis_id="example-id")
    ```


    :param str analysis_id: Identifier for the analysis.
           
           The following arguments are optional:
    :param str aws_account_id: AWS account ID.
    """
    pulumi.log.warn("""get_analysis is deprecated: aws.quicksight/getanalysis.getAnalysis has been deprecated in favor of aws.quicksight/getquicksightanalysis.getQuicksightAnalysis""")
    __args__ = dict()
    __args__['analysisId'] = analysis_id
    __args__['awsAccountId'] = aws_account_id
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:quicksight/getAnalysis:getAnalysis', __args__, opts=opts, typ=GetAnalysisResult).value

    return AwaitableGetAnalysisResult(
        analysis_id=pulumi.get(__ret__, 'analysis_id'),
        arn=pulumi.get(__ret__, 'arn'),
        aws_account_id=pulumi.get(__ret__, 'aws_account_id'),
        created_time=pulumi.get(__ret__, 'created_time'),
        id=pulumi.get(__ret__, 'id'),
        last_published_time=pulumi.get(__ret__, 'last_published_time'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        name=pulumi.get(__ret__, 'name'),
        permissions=pulumi.get(__ret__, 'permissions'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        theme_arn=pulumi.get(__ret__, 'theme_arn'))
def get_analysis_output(analysis_id: Optional[pulumi.Input[str]] = None,
                        aws_account_id: Optional[pulumi.Input[Optional[str]]] = None,
                        tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAnalysisResult]:
    """
    Data source for managing an AWS QuickSight Analysis.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.quicksight.get_quicksight_analysis(analysis_id="example-id")
    ```


    :param str analysis_id: Identifier for the analysis.
           
           The following arguments are optional:
    :param str aws_account_id: AWS account ID.
    """
    pulumi.log.warn("""get_analysis is deprecated: aws.quicksight/getanalysis.getAnalysis has been deprecated in favor of aws.quicksight/getquicksightanalysis.getQuicksightAnalysis""")
    __args__ = dict()
    __args__['analysisId'] = analysis_id
    __args__['awsAccountId'] = aws_account_id
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:quicksight/getAnalysis:getAnalysis', __args__, opts=opts, typ=GetAnalysisResult)
    return __ret__.apply(lambda __response__: GetAnalysisResult(
        analysis_id=pulumi.get(__response__, 'analysis_id'),
        arn=pulumi.get(__response__, 'arn'),
        aws_account_id=pulumi.get(__response__, 'aws_account_id'),
        created_time=pulumi.get(__response__, 'created_time'),
        id=pulumi.get(__response__, 'id'),
        last_published_time=pulumi.get(__response__, 'last_published_time'),
        last_updated_time=pulumi.get(__response__, 'last_updated_time'),
        name=pulumi.get(__response__, 'name'),
        permissions=pulumi.get(__response__, 'permissions'),
        status=pulumi.get(__response__, 'status'),
        tags=pulumi.get(__response__, 'tags'),
        theme_arn=pulumi.get(__response__, 'theme_arn')))
