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
    'GetInferenceProfileResult',
    'AwaitableGetInferenceProfileResult',
    'get_inference_profile',
    'get_inference_profile_output',
]

@pulumi.output_type
class GetInferenceProfileResult:
    """
    A collection of values returned by getInferenceProfile.
    """
    def __init__(__self__, created_at=None, description=None, id=None, inference_profile_arn=None, inference_profile_id=None, inference_profile_name=None, models=None, status=None, type=None, updated_at=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inference_profile_arn and not isinstance(inference_profile_arn, str):
            raise TypeError("Expected argument 'inference_profile_arn' to be a str")
        pulumi.set(__self__, "inference_profile_arn", inference_profile_arn)
        if inference_profile_id and not isinstance(inference_profile_id, str):
            raise TypeError("Expected argument 'inference_profile_id' to be a str")
        pulumi.set(__self__, "inference_profile_id", inference_profile_id)
        if inference_profile_name and not isinstance(inference_profile_name, str):
            raise TypeError("Expected argument 'inference_profile_name' to be a str")
        pulumi.set(__self__, "inference_profile_name", inference_profile_name)
        if models and not isinstance(models, list):
            raise TypeError("Expected argument 'models' to be a list")
        pulumi.set(__self__, "models", models)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time at which the inference profile was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the inference profile.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inferenceProfileArn")
    def inference_profile_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the inference profile.
        """
        return pulumi.get(self, "inference_profile_arn")

    @property
    @pulumi.getter(name="inferenceProfileId")
    def inference_profile_id(self) -> str:
        return pulumi.get(self, "inference_profile_id")

    @property
    @pulumi.getter(name="inferenceProfileName")
    def inference_profile_name(self) -> str:
        """
        The unique identifier of the inference profile.
        """
        return pulumi.get(self, "inference_profile_name")

    @property
    @pulumi.getter
    def models(self) -> Sequence['outputs.GetInferenceProfileModelResult']:
        """
        A list of information about each model in the inference profile. See `models`.
        """
        return pulumi.get(self, "models")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the inference profile. `ACTIVE` means that the inference profile is available to use.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the inference profile. `SYSTEM_DEFINED` means that the inference profile is defined by Amazon Bedrock.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The time at which the inference profile was last updated.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetInferenceProfileResult(GetInferenceProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInferenceProfileResult(
            created_at=self.created_at,
            description=self.description,
            id=self.id,
            inference_profile_arn=self.inference_profile_arn,
            inference_profile_id=self.inference_profile_id,
            inference_profile_name=self.inference_profile_name,
            models=self.models,
            status=self.status,
            type=self.type,
            updated_at=self.updated_at)


def get_inference_profile(inference_profile_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInferenceProfileResult:
    """
    Data source for managing an AWS Bedrock Inference Profile.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.bedrock.get_inference_profiles()
    test_get_inference_profile = aws.bedrock.get_inference_profile(inference_profile_id=test.inference_profile_summaries[0].inference_profile_id)
    ```


    :param str inference_profile_id: Inference Profile identifier.
    """
    __args__ = dict()
    __args__['inferenceProfileId'] = inference_profile_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:bedrock/getInferenceProfile:getInferenceProfile', __args__, opts=opts, typ=GetInferenceProfileResult).value

    return AwaitableGetInferenceProfileResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        inference_profile_arn=pulumi.get(__ret__, 'inference_profile_arn'),
        inference_profile_id=pulumi.get(__ret__, 'inference_profile_id'),
        inference_profile_name=pulumi.get(__ret__, 'inference_profile_name'),
        models=pulumi.get(__ret__, 'models'),
        status=pulumi.get(__ret__, 'status'),
        type=pulumi.get(__ret__, 'type'),
        updated_at=pulumi.get(__ret__, 'updated_at'))
def get_inference_profile_output(inference_profile_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInferenceProfileResult]:
    """
    Data source for managing an AWS Bedrock Inference Profile.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.bedrock.get_inference_profiles()
    test_get_inference_profile = aws.bedrock.get_inference_profile(inference_profile_id=test.inference_profile_summaries[0].inference_profile_id)
    ```


    :param str inference_profile_id: Inference Profile identifier.
    """
    __args__ = dict()
    __args__['inferenceProfileId'] = inference_profile_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:bedrock/getInferenceProfile:getInferenceProfile', __args__, opts=opts, typ=GetInferenceProfileResult)
    return __ret__.apply(lambda __response__: GetInferenceProfileResult(
        created_at=pulumi.get(__response__, 'created_at'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        inference_profile_arn=pulumi.get(__response__, 'inference_profile_arn'),
        inference_profile_id=pulumi.get(__response__, 'inference_profile_id'),
        inference_profile_name=pulumi.get(__response__, 'inference_profile_name'),
        models=pulumi.get(__response__, 'models'),
        status=pulumi.get(__response__, 'status'),
        type=pulumi.get(__response__, 'type'),
        updated_at=pulumi.get(__response__, 'updated_at')))
