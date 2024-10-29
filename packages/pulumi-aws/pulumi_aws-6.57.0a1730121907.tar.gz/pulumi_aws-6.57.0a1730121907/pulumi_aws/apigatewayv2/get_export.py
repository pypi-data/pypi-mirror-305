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

__all__ = [
    'GetExportResult',
    'AwaitableGetExportResult',
    'get_export',
    'get_export_output',
]

@pulumi.output_type
class GetExportResult:
    """
    A collection of values returned by getExport.
    """
    def __init__(__self__, api_id=None, body=None, export_version=None, id=None, include_extensions=None, output_type=None, specification=None, stage_name=None):
        if api_id and not isinstance(api_id, str):
            raise TypeError("Expected argument 'api_id' to be a str")
        pulumi.set(__self__, "api_id", api_id)
        if body and not isinstance(body, str):
            raise TypeError("Expected argument 'body' to be a str")
        pulumi.set(__self__, "body", body)
        if export_version and not isinstance(export_version, str):
            raise TypeError("Expected argument 'export_version' to be a str")
        pulumi.set(__self__, "export_version", export_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_extensions and not isinstance(include_extensions, bool):
            raise TypeError("Expected argument 'include_extensions' to be a bool")
        pulumi.set(__self__, "include_extensions", include_extensions)
        if output_type and not isinstance(output_type, str):
            raise TypeError("Expected argument 'output_type' to be a str")
        pulumi.set(__self__, "output_type", output_type)
        if specification and not isinstance(specification, str):
            raise TypeError("Expected argument 'specification' to be a str")
        pulumi.set(__self__, "specification", specification)
        if stage_name and not isinstance(stage_name, str):
            raise TypeError("Expected argument 'stage_name' to be a str")
        pulumi.set(__self__, "stage_name", stage_name)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> str:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter
    def body(self) -> str:
        """
        ID of the API.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter(name="exportVersion")
    def export_version(self) -> Optional[str]:
        return pulumi.get(self, "export_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includeExtensions")
    def include_extensions(self) -> Optional[bool]:
        return pulumi.get(self, "include_extensions")

    @property
    @pulumi.getter(name="outputType")
    def output_type(self) -> str:
        return pulumi.get(self, "output_type")

    @property
    @pulumi.getter
    def specification(self) -> str:
        return pulumi.get(self, "specification")

    @property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[str]:
        return pulumi.get(self, "stage_name")


class AwaitableGetExportResult(GetExportResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExportResult(
            api_id=self.api_id,
            body=self.body,
            export_version=self.export_version,
            id=self.id,
            include_extensions=self.include_extensions,
            output_type=self.output_type,
            specification=self.specification,
            stage_name=self.stage_name)


def get_export(api_id: Optional[str] = None,
               export_version: Optional[str] = None,
               include_extensions: Optional[bool] = None,
               output_type: Optional[str] = None,
               specification: Optional[str] = None,
               stage_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExportResult:
    """
    Exports a definition of an API in a particular output format and specification.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.apigatewayv2.get_export(api_id=test_aws_apigatewayv2_route["apiId"],
        specification="OAS30",
        output_type="JSON")
    ```


    :param str api_id: API identifier.
    :param str export_version: Version of the API Gateway export algorithm. API Gateway uses the latest version by default. Currently, the only supported version is `1.0`.
    :param bool include_extensions: Whether to include API Gateway extensions in the exported API definition. API Gateway extensions are included by default.
    :param str output_type: Output type of the exported definition file. Valid values are `JSON` and `YAML`.
    :param str specification: Version of the API specification to use. `OAS30`, for OpenAPI 3.0, is the only supported value.
    :param str stage_name: Name of the API stage to export. If you don't specify this property, a representation of the latest API configuration is exported.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['exportVersion'] = export_version
    __args__['includeExtensions'] = include_extensions
    __args__['outputType'] = output_type
    __args__['specification'] = specification
    __args__['stageName'] = stage_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:apigatewayv2/getExport:getExport', __args__, opts=opts, typ=GetExportResult).value

    return AwaitableGetExportResult(
        api_id=pulumi.get(__ret__, 'api_id'),
        body=pulumi.get(__ret__, 'body'),
        export_version=pulumi.get(__ret__, 'export_version'),
        id=pulumi.get(__ret__, 'id'),
        include_extensions=pulumi.get(__ret__, 'include_extensions'),
        output_type=pulumi.get(__ret__, 'output_type'),
        specification=pulumi.get(__ret__, 'specification'),
        stage_name=pulumi.get(__ret__, 'stage_name'))
def get_export_output(api_id: Optional[pulumi.Input[str]] = None,
                      export_version: Optional[pulumi.Input[Optional[str]]] = None,
                      include_extensions: Optional[pulumi.Input[Optional[bool]]] = None,
                      output_type: Optional[pulumi.Input[str]] = None,
                      specification: Optional[pulumi.Input[str]] = None,
                      stage_name: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExportResult]:
    """
    Exports a definition of an API in a particular output format and specification.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.apigatewayv2.get_export(api_id=test_aws_apigatewayv2_route["apiId"],
        specification="OAS30",
        output_type="JSON")
    ```


    :param str api_id: API identifier.
    :param str export_version: Version of the API Gateway export algorithm. API Gateway uses the latest version by default. Currently, the only supported version is `1.0`.
    :param bool include_extensions: Whether to include API Gateway extensions in the exported API definition. API Gateway extensions are included by default.
    :param str output_type: Output type of the exported definition file. Valid values are `JSON` and `YAML`.
    :param str specification: Version of the API specification to use. `OAS30`, for OpenAPI 3.0, is the only supported value.
    :param str stage_name: Name of the API stage to export. If you don't specify this property, a representation of the latest API configuration is exported.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['exportVersion'] = export_version
    __args__['includeExtensions'] = include_extensions
    __args__['outputType'] = output_type
    __args__['specification'] = specification
    __args__['stageName'] = stage_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:apigatewayv2/getExport:getExport', __args__, opts=opts, typ=GetExportResult)
    return __ret__.apply(lambda __response__: GetExportResult(
        api_id=pulumi.get(__response__, 'api_id'),
        body=pulumi.get(__response__, 'body'),
        export_version=pulumi.get(__response__, 'export_version'),
        id=pulumi.get(__response__, 'id'),
        include_extensions=pulumi.get(__response__, 'include_extensions'),
        output_type=pulumi.get(__response__, 'output_type'),
        specification=pulumi.get(__response__, 'specification'),
        stage_name=pulumi.get(__response__, 'stage_name')))
