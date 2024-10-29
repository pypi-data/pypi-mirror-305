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
    'GetExperienceResult',
    'AwaitableGetExperienceResult',
    'get_experience',
    'get_experience_output',
]

@pulumi.output_type
class GetExperienceResult:
    """
    A collection of values returned by getExperience.
    """
    def __init__(__self__, arn=None, configurations=None, created_at=None, description=None, endpoints=None, error_message=None, experience_id=None, id=None, index_id=None, name=None, role_arn=None, status=None, updated_at=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if configurations and not isinstance(configurations, list):
            raise TypeError("Expected argument 'configurations' to be a list")
        pulumi.set(__self__, "configurations", configurations)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if endpoints and not isinstance(endpoints, list):
            raise TypeError("Expected argument 'endpoints' to be a list")
        pulumi.set(__self__, "endpoints", endpoints)
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        pulumi.set(__self__, "error_message", error_message)
        if experience_id and not isinstance(experience_id, str):
            raise TypeError("Expected argument 'experience_id' to be a str")
        pulumi.set(__self__, "experience_id", experience_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if index_id and not isinstance(index_id, str):
            raise TypeError("Expected argument 'index_id' to be a str")
        pulumi.set(__self__, "index_id", index_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the Experience.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def configurations(self) -> Sequence['outputs.GetExperienceConfigurationResult']:
        """
        Block that specifies the configuration information for your Amazon Kendra Experience. This includes `content_source_configuration`, which specifies the data source IDs and/or FAQ IDs, and `user_identity_configuration`, which specifies the user or group information to grant access to your Amazon Kendra Experience. Documented below.
        """
        return pulumi.get(self, "configurations")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Unix datetime that the Experience was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the Experience.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def endpoints(self) -> Sequence['outputs.GetExperienceEndpointResult']:
        """
        Shows the endpoint URLs for your Amazon Kendra Experiences. The URLs are unique and fully hosted by AWS. Documented below.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        """
        Reason your Amazon Kendra Experience could not properly process.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="experienceId")
    def experience_id(self) -> str:
        return pulumi.get(self, "experience_id")

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
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the Experience.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> str:
        """
        Shows the ARN of a role with permission to access `Query` API, `QuerySuggestions` API, `SubmitFeedback` API, and AWS SSO that stores your user and group information.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Current processing status of your Amazon Kendra Experience. When the status is `ACTIVE`, your Amazon Kendra Experience is ready to use. When the status is `FAILED`, the `error_message` field contains the reason that this failed.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        Date and time that the Experience was last updated.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetExperienceResult(GetExperienceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExperienceResult(
            arn=self.arn,
            configurations=self.configurations,
            created_at=self.created_at,
            description=self.description,
            endpoints=self.endpoints,
            error_message=self.error_message,
            experience_id=self.experience_id,
            id=self.id,
            index_id=self.index_id,
            name=self.name,
            role_arn=self.role_arn,
            status=self.status,
            updated_at=self.updated_at)


def get_experience(experience_id: Optional[str] = None,
                   index_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExperienceResult:
    """
    Provides details about a specific Amazon Kendra Experience.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.kendra.get_experience(experience_id="87654321-1234-4321-4321-321987654321",
        index_id="12345678-1234-1234-1234-123456789123")
    ```


    :param str experience_id: Identifier of the Experience.
    :param str index_id: Identifier of the index that contains the Experience.
    """
    __args__ = dict()
    __args__['experienceId'] = experience_id
    __args__['indexId'] = index_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:kendra/getExperience:getExperience', __args__, opts=opts, typ=GetExperienceResult).value

    return AwaitableGetExperienceResult(
        arn=pulumi.get(__ret__, 'arn'),
        configurations=pulumi.get(__ret__, 'configurations'),
        created_at=pulumi.get(__ret__, 'created_at'),
        description=pulumi.get(__ret__, 'description'),
        endpoints=pulumi.get(__ret__, 'endpoints'),
        error_message=pulumi.get(__ret__, 'error_message'),
        experience_id=pulumi.get(__ret__, 'experience_id'),
        id=pulumi.get(__ret__, 'id'),
        index_id=pulumi.get(__ret__, 'index_id'),
        name=pulumi.get(__ret__, 'name'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        status=pulumi.get(__ret__, 'status'),
        updated_at=pulumi.get(__ret__, 'updated_at'))
def get_experience_output(experience_id: Optional[pulumi.Input[str]] = None,
                          index_id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExperienceResult]:
    """
    Provides details about a specific Amazon Kendra Experience.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.kendra.get_experience(experience_id="87654321-1234-4321-4321-321987654321",
        index_id="12345678-1234-1234-1234-123456789123")
    ```


    :param str experience_id: Identifier of the Experience.
    :param str index_id: Identifier of the index that contains the Experience.
    """
    __args__ = dict()
    __args__['experienceId'] = experience_id
    __args__['indexId'] = index_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:kendra/getExperience:getExperience', __args__, opts=opts, typ=GetExperienceResult)
    return __ret__.apply(lambda __response__: GetExperienceResult(
        arn=pulumi.get(__response__, 'arn'),
        configurations=pulumi.get(__response__, 'configurations'),
        created_at=pulumi.get(__response__, 'created_at'),
        description=pulumi.get(__response__, 'description'),
        endpoints=pulumi.get(__response__, 'endpoints'),
        error_message=pulumi.get(__response__, 'error_message'),
        experience_id=pulumi.get(__response__, 'experience_id'),
        id=pulumi.get(__response__, 'id'),
        index_id=pulumi.get(__response__, 'index_id'),
        name=pulumi.get(__response__, 'name'),
        role_arn=pulumi.get(__response__, 'role_arn'),
        status=pulumi.get(__response__, 'status'),
        updated_at=pulumi.get(__response__, 'updated_at')))
