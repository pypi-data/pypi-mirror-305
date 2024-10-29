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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    """
    A collection of values returned by getCluster.
    """
    def __init__(__self__, arn=None, cluster_name=None, id=None, pending_tasks_count=None, registered_container_instances_count=None, running_tasks_count=None, service_connect_defaults=None, settings=None, status=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        pulumi.set(__self__, "cluster_name", cluster_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if pending_tasks_count and not isinstance(pending_tasks_count, int):
            raise TypeError("Expected argument 'pending_tasks_count' to be a int")
        pulumi.set(__self__, "pending_tasks_count", pending_tasks_count)
        if registered_container_instances_count and not isinstance(registered_container_instances_count, int):
            raise TypeError("Expected argument 'registered_container_instances_count' to be a int")
        pulumi.set(__self__, "registered_container_instances_count", registered_container_instances_count)
        if running_tasks_count and not isinstance(running_tasks_count, int):
            raise TypeError("Expected argument 'running_tasks_count' to be a int")
        pulumi.set(__self__, "running_tasks_count", running_tasks_count)
        if service_connect_defaults and not isinstance(service_connect_defaults, list):
            raise TypeError("Expected argument 'service_connect_defaults' to be a list")
        pulumi.set(__self__, "service_connect_defaults", service_connect_defaults)
        if settings and not isinstance(settings, list):
            raise TypeError("Expected argument 'settings' to be a list")
        pulumi.set(__self__, "settings", settings)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the ECS Cluster
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> str:
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="pendingTasksCount")
    def pending_tasks_count(self) -> int:
        """
        Number of pending tasks for the ECS Cluster
        """
        return pulumi.get(self, "pending_tasks_count")

    @property
    @pulumi.getter(name="registeredContainerInstancesCount")
    def registered_container_instances_count(self) -> int:
        """
        The number of registered container instances for the ECS Cluster
        """
        return pulumi.get(self, "registered_container_instances_count")

    @property
    @pulumi.getter(name="runningTasksCount")
    def running_tasks_count(self) -> int:
        """
        Number of running tasks for the ECS Cluster
        """
        return pulumi.get(self, "running_tasks_count")

    @property
    @pulumi.getter(name="serviceConnectDefaults")
    def service_connect_defaults(self) -> Sequence['outputs.GetClusterServiceConnectDefaultResult']:
        """
        The default Service Connect namespace
        """
        return pulumi.get(self, "service_connect_defaults")

    @property
    @pulumi.getter
    def settings(self) -> Sequence['outputs.GetClusterSettingResult']:
        """
        Settings associated with the ECS Cluster
        """
        return pulumi.get(self, "settings")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the ECS Cluster
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            arn=self.arn,
            cluster_name=self.cluster_name,
            id=self.id,
            pending_tasks_count=self.pending_tasks_count,
            registered_container_instances_count=self.registered_container_instances_count,
            running_tasks_count=self.running_tasks_count,
            service_connect_defaults=self.service_connect_defaults,
            settings=self.settings,
            status=self.status,
            tags=self.tags)


def get_cluster(cluster_name: Optional[str] = None,
                tags: Optional[Mapping[str, str]] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    The ECS Cluster data source allows access to details of a specific
    cluster within an AWS ECS service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    ecs_mongo = aws.ecs.get_cluster(cluster_name="ecs-mongo-production")
    ```


    :param str cluster_name: Name of the ECS Cluster
    :param Mapping[str, str] tags: Key-value map of resource tags
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ecs/getCluster:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        arn=pulumi.get(__ret__, 'arn'),
        cluster_name=pulumi.get(__ret__, 'cluster_name'),
        id=pulumi.get(__ret__, 'id'),
        pending_tasks_count=pulumi.get(__ret__, 'pending_tasks_count'),
        registered_container_instances_count=pulumi.get(__ret__, 'registered_container_instances_count'),
        running_tasks_count=pulumi.get(__ret__, 'running_tasks_count'),
        service_connect_defaults=pulumi.get(__ret__, 'service_connect_defaults'),
        settings=pulumi.get(__ret__, 'settings'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'))
def get_cluster_output(cluster_name: Optional[pulumi.Input[str]] = None,
                       tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    The ECS Cluster data source allows access to details of a specific
    cluster within an AWS ECS service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    ecs_mongo = aws.ecs.get_cluster(cluster_name="ecs-mongo-production")
    ```


    :param str cluster_name: Name of the ECS Cluster
    :param Mapping[str, str] tags: Key-value map of resource tags
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:ecs/getCluster:getCluster', __args__, opts=opts, typ=GetClusterResult)
    return __ret__.apply(lambda __response__: GetClusterResult(
        arn=pulumi.get(__response__, 'arn'),
        cluster_name=pulumi.get(__response__, 'cluster_name'),
        id=pulumi.get(__response__, 'id'),
        pending_tasks_count=pulumi.get(__response__, 'pending_tasks_count'),
        registered_container_instances_count=pulumi.get(__response__, 'registered_container_instances_count'),
        running_tasks_count=pulumi.get(__response__, 'running_tasks_count'),
        service_connect_defaults=pulumi.get(__response__, 'service_connect_defaults'),
        settings=pulumi.get(__response__, 'settings'),
        status=pulumi.get(__response__, 'status'),
        tags=pulumi.get(__response__, 'tags')))
