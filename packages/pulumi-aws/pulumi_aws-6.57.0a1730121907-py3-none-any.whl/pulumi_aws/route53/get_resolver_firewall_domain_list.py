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
    'GetResolverFirewallDomainListResult',
    'AwaitableGetResolverFirewallDomainListResult',
    'get_resolver_firewall_domain_list',
    'get_resolver_firewall_domain_list_output',
]

@pulumi.output_type
class GetResolverFirewallDomainListResult:
    """
    A collection of values returned by getResolverFirewallDomainList.
    """
    def __init__(__self__, arn=None, creation_time=None, creator_request_id=None, domain_count=None, firewall_domain_list_id=None, id=None, managed_owner_name=None, modification_time=None, name=None, status=None, status_message=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if creator_request_id and not isinstance(creator_request_id, str):
            raise TypeError("Expected argument 'creator_request_id' to be a str")
        pulumi.set(__self__, "creator_request_id", creator_request_id)
        if domain_count and not isinstance(domain_count, int):
            raise TypeError("Expected argument 'domain_count' to be a int")
        pulumi.set(__self__, "domain_count", domain_count)
        if firewall_domain_list_id and not isinstance(firewall_domain_list_id, str):
            raise TypeError("Expected argument 'firewall_domain_list_id' to be a str")
        pulumi.set(__self__, "firewall_domain_list_id", firewall_domain_list_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_owner_name and not isinstance(managed_owner_name, str):
            raise TypeError("Expected argument 'managed_owner_name' to be a str")
        pulumi.set(__self__, "managed_owner_name", managed_owner_name)
        if modification_time and not isinstance(modification_time, str):
            raise TypeError("Expected argument 'modification_time' to be a str")
        pulumi.set(__self__, "modification_time", modification_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_message and not isinstance(status_message, str):
            raise TypeError("Expected argument 'status_message' to be a str")
        pulumi.set(__self__, "status_message", status_message)

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="creatorRequestId")
    def creator_request_id(self) -> str:
        return pulumi.get(self, "creator_request_id")

    @property
    @pulumi.getter(name="domainCount")
    def domain_count(self) -> int:
        return pulumi.get(self, "domain_count")

    @property
    @pulumi.getter(name="firewallDomainListId")
    def firewall_domain_list_id(self) -> str:
        return pulumi.get(self, "firewall_domain_list_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedOwnerName")
    def managed_owner_name(self) -> str:
        return pulumi.get(self, "managed_owner_name")

    @property
    @pulumi.getter(name="modificationTime")
    def modification_time(self) -> str:
        return pulumi.get(self, "modification_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> str:
        return pulumi.get(self, "status_message")


class AwaitableGetResolverFirewallDomainListResult(GetResolverFirewallDomainListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResolverFirewallDomainListResult(
            arn=self.arn,
            creation_time=self.creation_time,
            creator_request_id=self.creator_request_id,
            domain_count=self.domain_count,
            firewall_domain_list_id=self.firewall_domain_list_id,
            id=self.id,
            managed_owner_name=self.managed_owner_name,
            modification_time=self.modification_time,
            name=self.name,
            status=self.status,
            status_message=self.status_message)


def get_resolver_firewall_domain_list(firewall_domain_list_id: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResolverFirewallDomainListResult:
    """
    `route53.ResolverFirewallDomainList` Retrieves the specified firewall domain list.

    This data source allows to retrieve details about a specific a Route 53 Resolver DNS Firewall domain list.

    ## Example Usage

    The following example shows how to get a firewall domain list from its ID.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.route53.get_resolver_firewall_domain_list(firewall_domain_list_id="rslvr-fdl-example")
    ```


    :param str firewall_domain_list_id: The ID of the domain list.
           
           The following attribute is additionally exported:
    """
    __args__ = dict()
    __args__['firewallDomainListId'] = firewall_domain_list_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:route53/getResolverFirewallDomainList:getResolverFirewallDomainList', __args__, opts=opts, typ=GetResolverFirewallDomainListResult).value

    return AwaitableGetResolverFirewallDomainListResult(
        arn=pulumi.get(__ret__, 'arn'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        creator_request_id=pulumi.get(__ret__, 'creator_request_id'),
        domain_count=pulumi.get(__ret__, 'domain_count'),
        firewall_domain_list_id=pulumi.get(__ret__, 'firewall_domain_list_id'),
        id=pulumi.get(__ret__, 'id'),
        managed_owner_name=pulumi.get(__ret__, 'managed_owner_name'),
        modification_time=pulumi.get(__ret__, 'modification_time'),
        name=pulumi.get(__ret__, 'name'),
        status=pulumi.get(__ret__, 'status'),
        status_message=pulumi.get(__ret__, 'status_message'))
def get_resolver_firewall_domain_list_output(firewall_domain_list_id: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResolverFirewallDomainListResult]:
    """
    `route53.ResolverFirewallDomainList` Retrieves the specified firewall domain list.

    This data source allows to retrieve details about a specific a Route 53 Resolver DNS Firewall domain list.

    ## Example Usage

    The following example shows how to get a firewall domain list from its ID.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.route53.get_resolver_firewall_domain_list(firewall_domain_list_id="rslvr-fdl-example")
    ```


    :param str firewall_domain_list_id: The ID of the domain list.
           
           The following attribute is additionally exported:
    """
    __args__ = dict()
    __args__['firewallDomainListId'] = firewall_domain_list_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:route53/getResolverFirewallDomainList:getResolverFirewallDomainList', __args__, opts=opts, typ=GetResolverFirewallDomainListResult)
    return __ret__.apply(lambda __response__: GetResolverFirewallDomainListResult(
        arn=pulumi.get(__response__, 'arn'),
        creation_time=pulumi.get(__response__, 'creation_time'),
        creator_request_id=pulumi.get(__response__, 'creator_request_id'),
        domain_count=pulumi.get(__response__, 'domain_count'),
        firewall_domain_list_id=pulumi.get(__response__, 'firewall_domain_list_id'),
        id=pulumi.get(__response__, 'id'),
        managed_owner_name=pulumi.get(__response__, 'managed_owner_name'),
        modification_time=pulumi.get(__response__, 'modification_time'),
        name=pulumi.get(__response__, 'name'),
        status=pulumi.get(__response__, 'status'),
        status_message=pulumi.get(__response__, 'status_message')))
