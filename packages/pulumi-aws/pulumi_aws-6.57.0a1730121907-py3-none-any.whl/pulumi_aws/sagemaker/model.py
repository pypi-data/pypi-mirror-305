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

__all__ = ['ModelArgs', 'Model']

@pulumi.input_type
class ModelArgs:
    def __init__(__self__, *,
                 execution_role_arn: pulumi.Input[str],
                 containers: Optional[pulumi.Input[Sequence[pulumi.Input['ModelContainerArgs']]]] = None,
                 enable_network_isolation: Optional[pulumi.Input[bool]] = None,
                 inference_execution_config: Optional[pulumi.Input['ModelInferenceExecutionConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary_container: Optional[pulumi.Input['ModelPrimaryContainerArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_config: Optional[pulumi.Input['ModelVpcConfigArgs']] = None):
        """
        The set of arguments for constructing a Model resource.
        :param pulumi.Input[str] execution_role_arn: A role that SageMaker can assume to access model artifacts and docker images for deployment.
        :param pulumi.Input[Sequence[pulumi.Input['ModelContainerArgs']]] containers: Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
        :param pulumi.Input[bool] enable_network_isolation: Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
        :param pulumi.Input['ModelInferenceExecutionConfigArgs'] inference_execution_config: Specifies details of how containers in a multi-container endpoint are called. see Inference Execution Config.
        :param pulumi.Input[str] name: The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
        :param pulumi.Input['ModelPrimaryContainerArgs'] primary_container: The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input['ModelVpcConfigArgs'] vpc_config: Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
        """
        pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        if containers is not None:
            pulumi.set(__self__, "containers", containers)
        if enable_network_isolation is not None:
            pulumi.set(__self__, "enable_network_isolation", enable_network_isolation)
        if inference_execution_config is not None:
            pulumi.set(__self__, "inference_execution_config", inference_execution_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if primary_container is not None:
            pulumi.set(__self__, "primary_container", primary_container)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_config is not None:
            pulumi.set(__self__, "vpc_config", vpc_config)

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Input[str]:
        """
        A role that SageMaker can assume to access model artifacts and docker images for deployment.
        """
        return pulumi.get(self, "execution_role_arn")

    @execution_role_arn.setter
    def execution_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "execution_role_arn", value)

    @property
    @pulumi.getter
    def containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ModelContainerArgs']]]]:
        """
        Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
        """
        return pulumi.get(self, "containers")

    @containers.setter
    def containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ModelContainerArgs']]]]):
        pulumi.set(self, "containers", value)

    @property
    @pulumi.getter(name="enableNetworkIsolation")
    def enable_network_isolation(self) -> Optional[pulumi.Input[bool]]:
        """
        Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
        """
        return pulumi.get(self, "enable_network_isolation")

    @enable_network_isolation.setter
    def enable_network_isolation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_network_isolation", value)

    @property
    @pulumi.getter(name="inferenceExecutionConfig")
    def inference_execution_config(self) -> Optional[pulumi.Input['ModelInferenceExecutionConfigArgs']]:
        """
        Specifies details of how containers in a multi-container endpoint are called. see Inference Execution Config.
        """
        return pulumi.get(self, "inference_execution_config")

    @inference_execution_config.setter
    def inference_execution_config(self, value: Optional[pulumi.Input['ModelInferenceExecutionConfigArgs']]):
        pulumi.set(self, "inference_execution_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="primaryContainer")
    def primary_container(self) -> Optional[pulumi.Input['ModelPrimaryContainerArgs']]:
        """
        The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
        """
        return pulumi.get(self, "primary_container")

    @primary_container.setter
    def primary_container(self, value: Optional[pulumi.Input['ModelPrimaryContainerArgs']]):
        pulumi.set(self, "primary_container", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input['ModelVpcConfigArgs']]:
        """
        Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
        """
        return pulumi.get(self, "vpc_config")

    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input['ModelVpcConfigArgs']]):
        pulumi.set(self, "vpc_config", value)


@pulumi.input_type
class _ModelState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 containers: Optional[pulumi.Input[Sequence[pulumi.Input['ModelContainerArgs']]]] = None,
                 enable_network_isolation: Optional[pulumi.Input[bool]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 inference_execution_config: Optional[pulumi.Input['ModelInferenceExecutionConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary_container: Optional[pulumi.Input['ModelPrimaryContainerArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_config: Optional[pulumi.Input['ModelVpcConfigArgs']] = None):
        """
        Input properties used for looking up and filtering Model resources.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this model.
        :param pulumi.Input[Sequence[pulumi.Input['ModelContainerArgs']]] containers: Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
        :param pulumi.Input[bool] enable_network_isolation: Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
        :param pulumi.Input[str] execution_role_arn: A role that SageMaker can assume to access model artifacts and docker images for deployment.
        :param pulumi.Input['ModelInferenceExecutionConfigArgs'] inference_execution_config: Specifies details of how containers in a multi-container endpoint are called. see Inference Execution Config.
        :param pulumi.Input[str] name: The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
        :param pulumi.Input['ModelPrimaryContainerArgs'] primary_container: The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input['ModelVpcConfigArgs'] vpc_config: Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if containers is not None:
            pulumi.set(__self__, "containers", containers)
        if enable_network_isolation is not None:
            pulumi.set(__self__, "enable_network_isolation", enable_network_isolation)
        if execution_role_arn is not None:
            pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        if inference_execution_config is not None:
            pulumi.set(__self__, "inference_execution_config", inference_execution_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if primary_container is not None:
            pulumi.set(__self__, "primary_container", primary_container)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if vpc_config is not None:
            pulumi.set(__self__, "vpc_config", vpc_config)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) assigned by AWS to this model.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ModelContainerArgs']]]]:
        """
        Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
        """
        return pulumi.get(self, "containers")

    @containers.setter
    def containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ModelContainerArgs']]]]):
        pulumi.set(self, "containers", value)

    @property
    @pulumi.getter(name="enableNetworkIsolation")
    def enable_network_isolation(self) -> Optional[pulumi.Input[bool]]:
        """
        Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
        """
        return pulumi.get(self, "enable_network_isolation")

    @enable_network_isolation.setter
    def enable_network_isolation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_network_isolation", value)

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        A role that SageMaker can assume to access model artifacts and docker images for deployment.
        """
        return pulumi.get(self, "execution_role_arn")

    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "execution_role_arn", value)

    @property
    @pulumi.getter(name="inferenceExecutionConfig")
    def inference_execution_config(self) -> Optional[pulumi.Input['ModelInferenceExecutionConfigArgs']]:
        """
        Specifies details of how containers in a multi-container endpoint are called. see Inference Execution Config.
        """
        return pulumi.get(self, "inference_execution_config")

    @inference_execution_config.setter
    def inference_execution_config(self, value: Optional[pulumi.Input['ModelInferenceExecutionConfigArgs']]):
        pulumi.set(self, "inference_execution_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="primaryContainer")
    def primary_container(self) -> Optional[pulumi.Input['ModelPrimaryContainerArgs']]:
        """
        The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
        """
        return pulumi.get(self, "primary_container")

    @primary_container.setter
    def primary_container(self, value: Optional[pulumi.Input['ModelPrimaryContainerArgs']]):
        pulumi.set(self, "primary_container", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input['ModelVpcConfigArgs']]:
        """
        Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
        """
        return pulumi.get(self, "vpc_config")

    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input['ModelVpcConfigArgs']]):
        pulumi.set(self, "vpc_config", value)


class Model(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 containers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ModelContainerArgs', 'ModelContainerArgsDict']]]]] = None,
                 enable_network_isolation: Optional[pulumi.Input[bool]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 inference_execution_config: Optional[pulumi.Input[Union['ModelInferenceExecutionConfigArgs', 'ModelInferenceExecutionConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary_container: Optional[pulumi.Input[Union['ModelPrimaryContainerArgs', 'ModelPrimaryContainerArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_config: Optional[pulumi.Input[Union['ModelVpcConfigArgs', 'ModelVpcConfigArgsDict']]] = None,
                 __props__=None):
        """
        Provides a SageMaker model resource.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        assume_role = aws.iam.get_policy_document(statements=[{
            "actions": ["sts:AssumeRole"],
            "principals": [{
                "type": "Service",
                "identifiers": ["sagemaker.amazonaws.com"],
            }],
        }])
        example_role = aws.iam.Role("example", assume_role_policy=assume_role.json)
        test = aws.sagemaker.get_prebuilt_ecr_image(repository_name="kmeans")
        example = aws.sagemaker.Model("example",
            name="my-model",
            execution_role_arn=example_role.arn,
            primary_container={
                "image": test.registry_path,
            })
        ```

        ## Inference Execution Config

        * `mode` - (Required) How containers in a multi-container are run. The following values are valid `Serial` and `Direct`.

        ## Import

        Using `pulumi import`, import models using the `name`. For example:

        ```sh
        $ pulumi import aws:sagemaker/model:Model test_model model-foo
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ModelContainerArgs', 'ModelContainerArgsDict']]]] containers: Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
        :param pulumi.Input[bool] enable_network_isolation: Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
        :param pulumi.Input[str] execution_role_arn: A role that SageMaker can assume to access model artifacts and docker images for deployment.
        :param pulumi.Input[Union['ModelInferenceExecutionConfigArgs', 'ModelInferenceExecutionConfigArgsDict']] inference_execution_config: Specifies details of how containers in a multi-container endpoint are called. see Inference Execution Config.
        :param pulumi.Input[str] name: The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[Union['ModelPrimaryContainerArgs', 'ModelPrimaryContainerArgsDict']] primary_container: The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Union['ModelVpcConfigArgs', 'ModelVpcConfigArgsDict']] vpc_config: Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ModelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a SageMaker model resource.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        assume_role = aws.iam.get_policy_document(statements=[{
            "actions": ["sts:AssumeRole"],
            "principals": [{
                "type": "Service",
                "identifiers": ["sagemaker.amazonaws.com"],
            }],
        }])
        example_role = aws.iam.Role("example", assume_role_policy=assume_role.json)
        test = aws.sagemaker.get_prebuilt_ecr_image(repository_name="kmeans")
        example = aws.sagemaker.Model("example",
            name="my-model",
            execution_role_arn=example_role.arn,
            primary_container={
                "image": test.registry_path,
            })
        ```

        ## Inference Execution Config

        * `mode` - (Required) How containers in a multi-container are run. The following values are valid `Serial` and `Direct`.

        ## Import

        Using `pulumi import`, import models using the `name`. For example:

        ```sh
        $ pulumi import aws:sagemaker/model:Model test_model model-foo
        ```

        :param str resource_name: The name of the resource.
        :param ModelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ModelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 containers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ModelContainerArgs', 'ModelContainerArgsDict']]]]] = None,
                 enable_network_isolation: Optional[pulumi.Input[bool]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 inference_execution_config: Optional[pulumi.Input[Union['ModelInferenceExecutionConfigArgs', 'ModelInferenceExecutionConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary_container: Optional[pulumi.Input[Union['ModelPrimaryContainerArgs', 'ModelPrimaryContainerArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_config: Optional[pulumi.Input[Union['ModelVpcConfigArgs', 'ModelVpcConfigArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ModelArgs.__new__(ModelArgs)

            __props__.__dict__["containers"] = containers
            __props__.__dict__["enable_network_isolation"] = enable_network_isolation
            if execution_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'execution_role_arn'")
            __props__.__dict__["execution_role_arn"] = execution_role_arn
            __props__.__dict__["inference_execution_config"] = inference_execution_config
            __props__.__dict__["name"] = name
            __props__.__dict__["primary_container"] = primary_container
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpc_config"] = vpc_config
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
        super(Model, __self__).__init__(
            'aws:sagemaker/model:Model',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            containers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ModelContainerArgs', 'ModelContainerArgsDict']]]]] = None,
            enable_network_isolation: Optional[pulumi.Input[bool]] = None,
            execution_role_arn: Optional[pulumi.Input[str]] = None,
            inference_execution_config: Optional[pulumi.Input[Union['ModelInferenceExecutionConfigArgs', 'ModelInferenceExecutionConfigArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            primary_container: Optional[pulumi.Input[Union['ModelPrimaryContainerArgs', 'ModelPrimaryContainerArgsDict']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_config: Optional[pulumi.Input[Union['ModelVpcConfigArgs', 'ModelVpcConfigArgsDict']]] = None) -> 'Model':
        """
        Get an existing Model resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this model.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ModelContainerArgs', 'ModelContainerArgsDict']]]] containers: Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
        :param pulumi.Input[bool] enable_network_isolation: Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
        :param pulumi.Input[str] execution_role_arn: A role that SageMaker can assume to access model artifacts and docker images for deployment.
        :param pulumi.Input[Union['ModelInferenceExecutionConfigArgs', 'ModelInferenceExecutionConfigArgsDict']] inference_execution_config: Specifies details of how containers in a multi-container endpoint are called. see Inference Execution Config.
        :param pulumi.Input[str] name: The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[Union['ModelPrimaryContainerArgs', 'ModelPrimaryContainerArgsDict']] primary_container: The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[Union['ModelVpcConfigArgs', 'ModelVpcConfigArgsDict']] vpc_config: Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ModelState.__new__(_ModelState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["containers"] = containers
        __props__.__dict__["enable_network_isolation"] = enable_network_isolation
        __props__.__dict__["execution_role_arn"] = execution_role_arn
        __props__.__dict__["inference_execution_config"] = inference_execution_config
        __props__.__dict__["name"] = name
        __props__.__dict__["primary_container"] = primary_container
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["vpc_config"] = vpc_config
        return Model(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) assigned by AWS to this model.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def containers(self) -> pulumi.Output[Optional[Sequence['outputs.ModelContainer']]]:
        """
        Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
        """
        return pulumi.get(self, "containers")

    @property
    @pulumi.getter(name="enableNetworkIsolation")
    def enable_network_isolation(self) -> pulumi.Output[Optional[bool]]:
        """
        Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
        """
        return pulumi.get(self, "enable_network_isolation")

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[str]:
        """
        A role that SageMaker can assume to access model artifacts and docker images for deployment.
        """
        return pulumi.get(self, "execution_role_arn")

    @property
    @pulumi.getter(name="inferenceExecutionConfig")
    def inference_execution_config(self) -> pulumi.Output['outputs.ModelInferenceExecutionConfig']:
        """
        Specifies details of how containers in a multi-container endpoint are called. see Inference Execution Config.
        """
        return pulumi.get(self, "inference_execution_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryContainer")
    def primary_container(self) -> pulumi.Output[Optional['outputs.ModelPrimaryContainer']]:
        """
        The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
        """
        return pulumi.get(self, "primary_container")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[Optional['outputs.ModelVpcConfig']]:
        """
        Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
        """
        return pulumi.get(self, "vpc_config")

