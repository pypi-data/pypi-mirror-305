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
    'GetApiResult',
    'AwaitableGetApiResult',
    'get_api',
    'get_api_output',
]

@pulumi.output_type
class GetApiResult:
    """
    A collection of values returned by getApi.
    """
    def __init__(__self__, api_endpoint=None, api_id=None, api_key_selection_expression=None, arn=None, cors_configurations=None, description=None, disable_execute_api_endpoint=None, execution_arn=None, id=None, name=None, protocol_type=None, route_selection_expression=None, tags=None, version=None):
        if api_endpoint and not isinstance(api_endpoint, str):
            raise TypeError("Expected argument 'api_endpoint' to be a str")
        pulumi.set(__self__, "api_endpoint", api_endpoint)
        if api_id and not isinstance(api_id, str):
            raise TypeError("Expected argument 'api_id' to be a str")
        pulumi.set(__self__, "api_id", api_id)
        if api_key_selection_expression and not isinstance(api_key_selection_expression, str):
            raise TypeError("Expected argument 'api_key_selection_expression' to be a str")
        pulumi.set(__self__, "api_key_selection_expression", api_key_selection_expression)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if cors_configurations and not isinstance(cors_configurations, list):
            raise TypeError("Expected argument 'cors_configurations' to be a list")
        pulumi.set(__self__, "cors_configurations", cors_configurations)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disable_execute_api_endpoint and not isinstance(disable_execute_api_endpoint, bool):
            raise TypeError("Expected argument 'disable_execute_api_endpoint' to be a bool")
        pulumi.set(__self__, "disable_execute_api_endpoint", disable_execute_api_endpoint)
        if execution_arn and not isinstance(execution_arn, str):
            raise TypeError("Expected argument 'execution_arn' to be a str")
        pulumi.set(__self__, "execution_arn", execution_arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if protocol_type and not isinstance(protocol_type, str):
            raise TypeError("Expected argument 'protocol_type' to be a str")
        pulumi.set(__self__, "protocol_type", protocol_type)
        if route_selection_expression and not isinstance(route_selection_expression, str):
            raise TypeError("Expected argument 'route_selection_expression' to be a str")
        pulumi.set(__self__, "route_selection_expression", route_selection_expression)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> str:
        """
        URI of the API, of the form `https://{api-id}.execute-api.{region}.amazonaws.com` for HTTP APIs and `wss://{api-id}.execute-api.{region}.amazonaws.com` for WebSocket APIs.
        """
        return pulumi.get(self, "api_endpoint")

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> str:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="apiKeySelectionExpression")
    def api_key_selection_expression(self) -> str:
        """
        An [API key selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions).
        Applicable for WebSocket APIs.
        """
        return pulumi.get(self, "api_key_selection_expression")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the API.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="corsConfigurations")
    def cors_configurations(self) -> Sequence['outputs.GetApiCorsConfigurationResult']:
        """
        Cross-origin resource sharing (CORS) [configuration](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html).
        Applicable for HTTP APIs.
        """
        return pulumi.get(self, "cors_configurations")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the API.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(self) -> bool:
        """
        Whether clients can invoke the API by using the default `execute-api` endpoint.
        """
        return pulumi.get(self, "disable_execute_api_endpoint")

    @property
    @pulumi.getter(name="executionArn")
    def execution_arn(self) -> str:
        """
        ARN prefix to be used in an `lambda.Permission`'s `source_arn` attribute
        or in an `iam.Policy` to authorize access to the [`@connections` API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html).
        See the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html) for details.
        """
        return pulumi.get(self, "execution_arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the API.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> str:
        """
        API protocol.
        """
        return pulumi.get(self, "protocol_type")

    @property
    @pulumi.getter(name="routeSelectionExpression")
    def route_selection_expression(self) -> str:
        """
        The [route selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-expressions) for the API.
        """
        return pulumi.get(self, "route_selection_expression")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Map of resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version identifier for the API.
        """
        return pulumi.get(self, "version")


class AwaitableGetApiResult(GetApiResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiResult(
            api_endpoint=self.api_endpoint,
            api_id=self.api_id,
            api_key_selection_expression=self.api_key_selection_expression,
            arn=self.arn,
            cors_configurations=self.cors_configurations,
            description=self.description,
            disable_execute_api_endpoint=self.disable_execute_api_endpoint,
            execution_arn=self.execution_arn,
            id=self.id,
            name=self.name,
            protocol_type=self.protocol_type,
            route_selection_expression=self.route_selection_expression,
            tags=self.tags,
            version=self.version)


def get_api(api_id: Optional[str] = None,
            tags: Optional[Mapping[str, str]] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiResult:
    """
    Provides details about a specific Amazon API Gateway Version 2 API.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.apigatewayv2.get_api(api_id="aabbccddee")
    ```


    :param str api_id: API identifier.
    :param Mapping[str, str] tags: Map of resource tags.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:apigatewayv2/getApi:getApi', __args__, opts=opts, typ=GetApiResult).value

    return AwaitableGetApiResult(
        api_endpoint=pulumi.get(__ret__, 'api_endpoint'),
        api_id=pulumi.get(__ret__, 'api_id'),
        api_key_selection_expression=pulumi.get(__ret__, 'api_key_selection_expression'),
        arn=pulumi.get(__ret__, 'arn'),
        cors_configurations=pulumi.get(__ret__, 'cors_configurations'),
        description=pulumi.get(__ret__, 'description'),
        disable_execute_api_endpoint=pulumi.get(__ret__, 'disable_execute_api_endpoint'),
        execution_arn=pulumi.get(__ret__, 'execution_arn'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        protocol_type=pulumi.get(__ret__, 'protocol_type'),
        route_selection_expression=pulumi.get(__ret__, 'route_selection_expression'),
        tags=pulumi.get(__ret__, 'tags'),
        version=pulumi.get(__ret__, 'version'))
def get_api_output(api_id: Optional[pulumi.Input[str]] = None,
                   tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiResult]:
    """
    Provides details about a specific Amazon API Gateway Version 2 API.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.apigatewayv2.get_api(api_id="aabbccddee")
    ```


    :param str api_id: API identifier.
    :param Mapping[str, str] tags: Map of resource tags.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:apigatewayv2/getApi:getApi', __args__, opts=opts, typ=GetApiResult)
    return __ret__.apply(lambda __response__: GetApiResult(
        api_endpoint=pulumi.get(__response__, 'api_endpoint'),
        api_id=pulumi.get(__response__, 'api_id'),
        api_key_selection_expression=pulumi.get(__response__, 'api_key_selection_expression'),
        arn=pulumi.get(__response__, 'arn'),
        cors_configurations=pulumi.get(__response__, 'cors_configurations'),
        description=pulumi.get(__response__, 'description'),
        disable_execute_api_endpoint=pulumi.get(__response__, 'disable_execute_api_endpoint'),
        execution_arn=pulumi.get(__response__, 'execution_arn'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        protocol_type=pulumi.get(__response__, 'protocol_type'),
        route_selection_expression=pulumi.get(__response__, 'route_selection_expression'),
        tags=pulumi.get(__response__, 'tags'),
        version=pulumi.get(__response__, 'version')))
