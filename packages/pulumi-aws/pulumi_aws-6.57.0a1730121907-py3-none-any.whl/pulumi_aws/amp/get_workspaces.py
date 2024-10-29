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
    'GetWorkspacesResult',
    'AwaitableGetWorkspacesResult',
    'get_workspaces',
    'get_workspaces_output',
]

@pulumi.output_type
class GetWorkspacesResult:
    """
    A collection of values returned by getWorkspaces.
    """
    def __init__(__self__, alias_prefix=None, aliases=None, arns=None, id=None, workspace_ids=None):
        if alias_prefix and not isinstance(alias_prefix, str):
            raise TypeError("Expected argument 'alias_prefix' to be a str")
        pulumi.set(__self__, "alias_prefix", alias_prefix)
        if aliases and not isinstance(aliases, list):
            raise TypeError("Expected argument 'aliases' to be a list")
        pulumi.set(__self__, "aliases", aliases)
        if arns and not isinstance(arns, list):
            raise TypeError("Expected argument 'arns' to be a list")
        pulumi.set(__self__, "arns", arns)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if workspace_ids and not isinstance(workspace_ids, list):
            raise TypeError("Expected argument 'workspace_ids' to be a list")
        pulumi.set(__self__, "workspace_ids", workspace_ids)

    @property
    @pulumi.getter(name="aliasPrefix")
    def alias_prefix(self) -> Optional[str]:
        return pulumi.get(self, "alias_prefix")

    @property
    @pulumi.getter
    def aliases(self) -> Sequence[str]:
        """
        List of aliases of the matched Prometheus workspaces.
        """
        return pulumi.get(self, "aliases")

    @property
    @pulumi.getter
    def arns(self) -> Sequence[str]:
        """
        List of ARNs of the matched Prometheus workspaces.
        """
        return pulumi.get(self, "arns")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="workspaceIds")
    def workspace_ids(self) -> Sequence[str]:
        """
        List of workspace IDs of the matched Prometheus workspaces.
        """
        return pulumi.get(self, "workspace_ids")


class AwaitableGetWorkspacesResult(GetWorkspacesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspacesResult(
            alias_prefix=self.alias_prefix,
            aliases=self.aliases,
            arns=self.arns,
            id=self.id,
            workspace_ids=self.workspace_ids)


def get_workspaces(alias_prefix: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspacesResult:
    """
    Provides the aliases, ARNs, and workspace IDs of Amazon Prometheus workspaces.

    ## Example Usage

    The following example returns all of the workspaces in a region:

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.amp.get_workspaces()
    ```

    The following example filters the workspaces by alias. Only the workspaces with
    aliases that begin with the value of `alias_prefix` will be returned:

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.amp.get_workspaces(alias_prefix="example")
    ```


    :param str alias_prefix: Limits results to workspaces with aliases that begin with this value.
    """
    __args__ = dict()
    __args__['aliasPrefix'] = alias_prefix
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:amp/getWorkspaces:getWorkspaces', __args__, opts=opts, typ=GetWorkspacesResult).value

    return AwaitableGetWorkspacesResult(
        alias_prefix=pulumi.get(__ret__, 'alias_prefix'),
        aliases=pulumi.get(__ret__, 'aliases'),
        arns=pulumi.get(__ret__, 'arns'),
        id=pulumi.get(__ret__, 'id'),
        workspace_ids=pulumi.get(__ret__, 'workspace_ids'))
def get_workspaces_output(alias_prefix: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspacesResult]:
    """
    Provides the aliases, ARNs, and workspace IDs of Amazon Prometheus workspaces.

    ## Example Usage

    The following example returns all of the workspaces in a region:

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.amp.get_workspaces()
    ```

    The following example filters the workspaces by alias. Only the workspaces with
    aliases that begin with the value of `alias_prefix` will be returned:

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.amp.get_workspaces(alias_prefix="example")
    ```


    :param str alias_prefix: Limits results to workspaces with aliases that begin with this value.
    """
    __args__ = dict()
    __args__['aliasPrefix'] = alias_prefix
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:amp/getWorkspaces:getWorkspaces', __args__, opts=opts, typ=GetWorkspacesResult)
    return __ret__.apply(lambda __response__: GetWorkspacesResult(
        alias_prefix=pulumi.get(__response__, 'alias_prefix'),
        aliases=pulumi.get(__response__, 'aliases'),
        arns=pulumi.get(__response__, 'arns'),
        id=pulumi.get(__response__, 'id'),
        workspace_ids=pulumi.get(__response__, 'workspace_ids')))
