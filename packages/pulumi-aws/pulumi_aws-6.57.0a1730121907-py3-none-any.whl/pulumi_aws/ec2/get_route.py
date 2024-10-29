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
    'GetRouteResult',
    'AwaitableGetRouteResult',
    'get_route',
    'get_route_output',
]

@pulumi.output_type
class GetRouteResult:
    """
    A collection of values returned by getRoute.
    """
    def __init__(__self__, carrier_gateway_id=None, core_network_arn=None, destination_cidr_block=None, destination_ipv6_cidr_block=None, destination_prefix_list_id=None, egress_only_gateway_id=None, gateway_id=None, id=None, instance_id=None, local_gateway_id=None, nat_gateway_id=None, network_interface_id=None, route_table_id=None, transit_gateway_id=None, vpc_peering_connection_id=None):
        if carrier_gateway_id and not isinstance(carrier_gateway_id, str):
            raise TypeError("Expected argument 'carrier_gateway_id' to be a str")
        pulumi.set(__self__, "carrier_gateway_id", carrier_gateway_id)
        if core_network_arn and not isinstance(core_network_arn, str):
            raise TypeError("Expected argument 'core_network_arn' to be a str")
        pulumi.set(__self__, "core_network_arn", core_network_arn)
        if destination_cidr_block and not isinstance(destination_cidr_block, str):
            raise TypeError("Expected argument 'destination_cidr_block' to be a str")
        pulumi.set(__self__, "destination_cidr_block", destination_cidr_block)
        if destination_ipv6_cidr_block and not isinstance(destination_ipv6_cidr_block, str):
            raise TypeError("Expected argument 'destination_ipv6_cidr_block' to be a str")
        pulumi.set(__self__, "destination_ipv6_cidr_block", destination_ipv6_cidr_block)
        if destination_prefix_list_id and not isinstance(destination_prefix_list_id, str):
            raise TypeError("Expected argument 'destination_prefix_list_id' to be a str")
        pulumi.set(__self__, "destination_prefix_list_id", destination_prefix_list_id)
        if egress_only_gateway_id and not isinstance(egress_only_gateway_id, str):
            raise TypeError("Expected argument 'egress_only_gateway_id' to be a str")
        pulumi.set(__self__, "egress_only_gateway_id", egress_only_gateway_id)
        if gateway_id and not isinstance(gateway_id, str):
            raise TypeError("Expected argument 'gateway_id' to be a str")
        pulumi.set(__self__, "gateway_id", gateway_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if local_gateway_id and not isinstance(local_gateway_id, str):
            raise TypeError("Expected argument 'local_gateway_id' to be a str")
        pulumi.set(__self__, "local_gateway_id", local_gateway_id)
        if nat_gateway_id and not isinstance(nat_gateway_id, str):
            raise TypeError("Expected argument 'nat_gateway_id' to be a str")
        pulumi.set(__self__, "nat_gateway_id", nat_gateway_id)
        if network_interface_id and not isinstance(network_interface_id, str):
            raise TypeError("Expected argument 'network_interface_id' to be a str")
        pulumi.set(__self__, "network_interface_id", network_interface_id)
        if route_table_id and not isinstance(route_table_id, str):
            raise TypeError("Expected argument 'route_table_id' to be a str")
        pulumi.set(__self__, "route_table_id", route_table_id)
        if transit_gateway_id and not isinstance(transit_gateway_id, str):
            raise TypeError("Expected argument 'transit_gateway_id' to be a str")
        pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)
        if vpc_peering_connection_id and not isinstance(vpc_peering_connection_id, str):
            raise TypeError("Expected argument 'vpc_peering_connection_id' to be a str")
        pulumi.set(__self__, "vpc_peering_connection_id", vpc_peering_connection_id)

    @property
    @pulumi.getter(name="carrierGatewayId")
    def carrier_gateway_id(self) -> str:
        return pulumi.get(self, "carrier_gateway_id")

    @property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> str:
        return pulumi.get(self, "core_network_arn")

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> str:
        return pulumi.get(self, "destination_cidr_block")

    @property
    @pulumi.getter(name="destinationIpv6CidrBlock")
    def destination_ipv6_cidr_block(self) -> str:
        return pulumi.get(self, "destination_ipv6_cidr_block")

    @property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> str:
        return pulumi.get(self, "destination_prefix_list_id")

    @property
    @pulumi.getter(name="egressOnlyGatewayId")
    def egress_only_gateway_id(self) -> str:
        return pulumi.get(self, "egress_only_gateway_id")

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> str:
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> str:
        return pulumi.get(self, "local_gateway_id")

    @property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> str:
        return pulumi.get(self, "nat_gateway_id")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> str:
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> str:
        return pulumi.get(self, "route_table_id")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> str:
        return pulumi.get(self, "transit_gateway_id")

    @property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> str:
        return pulumi.get(self, "vpc_peering_connection_id")


class AwaitableGetRouteResult(GetRouteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteResult(
            carrier_gateway_id=self.carrier_gateway_id,
            core_network_arn=self.core_network_arn,
            destination_cidr_block=self.destination_cidr_block,
            destination_ipv6_cidr_block=self.destination_ipv6_cidr_block,
            destination_prefix_list_id=self.destination_prefix_list_id,
            egress_only_gateway_id=self.egress_only_gateway_id,
            gateway_id=self.gateway_id,
            id=self.id,
            instance_id=self.instance_id,
            local_gateway_id=self.local_gateway_id,
            nat_gateway_id=self.nat_gateway_id,
            network_interface_id=self.network_interface_id,
            route_table_id=self.route_table_id,
            transit_gateway_id=self.transit_gateway_id,
            vpc_peering_connection_id=self.vpc_peering_connection_id)


def get_route(carrier_gateway_id: Optional[str] = None,
              core_network_arn: Optional[str] = None,
              destination_cidr_block: Optional[str] = None,
              destination_ipv6_cidr_block: Optional[str] = None,
              destination_prefix_list_id: Optional[str] = None,
              egress_only_gateway_id: Optional[str] = None,
              gateway_id: Optional[str] = None,
              instance_id: Optional[str] = None,
              local_gateway_id: Optional[str] = None,
              nat_gateway_id: Optional[str] = None,
              network_interface_id: Optional[str] = None,
              route_table_id: Optional[str] = None,
              transit_gateway_id: Optional[str] = None,
              vpc_peering_connection_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouteResult:
    """
    `ec2.Route` provides details about a specific Route.

    This resource can prove useful when finding the resource associated with a CIDR. For example, finding the peering connection associated with a CIDR value.

    ## Example Usage

    The following example shows how one might use a CIDR value to find a network interface id and use this to create a data source of that network interface.

    ```python
    import pulumi
    import pulumi_aws as aws

    config = pulumi.Config()
    subnet_id = config.require_object("subnetId")
    selected = aws.ec2.get_route_table(subnet_id=subnet_id)
    route = aws.ec2.get_route(route_table_id=selected_aws_route_table["id"],
        destination_cidr_block="10.0.1.0/24")
    interface = aws.ec2.get_network_interface(id=route.network_interface_id)
    ```


    :param str carrier_gateway_id: EC2 Carrier Gateway ID of the Route belonging to the Route Table.
    :param str core_network_arn: Core network ARN of the Route belonging to the Route Table.
    :param str destination_cidr_block: CIDR block of the Route belonging to the Route Table.
    :param str destination_ipv6_cidr_block: IPv6 CIDR block of the Route belonging to the Route Table.
    :param str destination_prefix_list_id: ID of a managed prefix list destination of the Route belonging to the Route Table.
    :param str egress_only_gateway_id: Egress Only Gateway ID of the Route belonging to the Route Table.
    :param str gateway_id: Gateway ID of the Route belonging to the Route Table.
    :param str instance_id: Instance ID of the Route belonging to the Route Table.
    :param str local_gateway_id: Local Gateway ID of the Route belonging to the Route Table.
    :param str nat_gateway_id: NAT Gateway ID of the Route belonging to the Route Table.
    :param str network_interface_id: Network Interface ID of the Route belonging to the Route Table.
    :param str route_table_id: ID of the specific Route Table containing the Route entry.
           
           The following arguments are optional:
    :param str transit_gateway_id: EC2 Transit Gateway ID of the Route belonging to the Route Table.
    :param str vpc_peering_connection_id: VPC Peering Connection ID of the Route belonging to the Route Table.
    """
    __args__ = dict()
    __args__['carrierGatewayId'] = carrier_gateway_id
    __args__['coreNetworkArn'] = core_network_arn
    __args__['destinationCidrBlock'] = destination_cidr_block
    __args__['destinationIpv6CidrBlock'] = destination_ipv6_cidr_block
    __args__['destinationPrefixListId'] = destination_prefix_list_id
    __args__['egressOnlyGatewayId'] = egress_only_gateway_id
    __args__['gatewayId'] = gateway_id
    __args__['instanceId'] = instance_id
    __args__['localGatewayId'] = local_gateway_id
    __args__['natGatewayId'] = nat_gateway_id
    __args__['networkInterfaceId'] = network_interface_id
    __args__['routeTableId'] = route_table_id
    __args__['transitGatewayId'] = transit_gateway_id
    __args__['vpcPeeringConnectionId'] = vpc_peering_connection_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ec2/getRoute:getRoute', __args__, opts=opts, typ=GetRouteResult).value

    return AwaitableGetRouteResult(
        carrier_gateway_id=pulumi.get(__ret__, 'carrier_gateway_id'),
        core_network_arn=pulumi.get(__ret__, 'core_network_arn'),
        destination_cidr_block=pulumi.get(__ret__, 'destination_cidr_block'),
        destination_ipv6_cidr_block=pulumi.get(__ret__, 'destination_ipv6_cidr_block'),
        destination_prefix_list_id=pulumi.get(__ret__, 'destination_prefix_list_id'),
        egress_only_gateway_id=pulumi.get(__ret__, 'egress_only_gateway_id'),
        gateway_id=pulumi.get(__ret__, 'gateway_id'),
        id=pulumi.get(__ret__, 'id'),
        instance_id=pulumi.get(__ret__, 'instance_id'),
        local_gateway_id=pulumi.get(__ret__, 'local_gateway_id'),
        nat_gateway_id=pulumi.get(__ret__, 'nat_gateway_id'),
        network_interface_id=pulumi.get(__ret__, 'network_interface_id'),
        route_table_id=pulumi.get(__ret__, 'route_table_id'),
        transit_gateway_id=pulumi.get(__ret__, 'transit_gateway_id'),
        vpc_peering_connection_id=pulumi.get(__ret__, 'vpc_peering_connection_id'))
def get_route_output(carrier_gateway_id: Optional[pulumi.Input[Optional[str]]] = None,
                     core_network_arn: Optional[pulumi.Input[Optional[str]]] = None,
                     destination_cidr_block: Optional[pulumi.Input[Optional[str]]] = None,
                     destination_ipv6_cidr_block: Optional[pulumi.Input[Optional[str]]] = None,
                     destination_prefix_list_id: Optional[pulumi.Input[Optional[str]]] = None,
                     egress_only_gateway_id: Optional[pulumi.Input[Optional[str]]] = None,
                     gateway_id: Optional[pulumi.Input[Optional[str]]] = None,
                     instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                     local_gateway_id: Optional[pulumi.Input[Optional[str]]] = None,
                     nat_gateway_id: Optional[pulumi.Input[Optional[str]]] = None,
                     network_interface_id: Optional[pulumi.Input[Optional[str]]] = None,
                     route_table_id: Optional[pulumi.Input[str]] = None,
                     transit_gateway_id: Optional[pulumi.Input[Optional[str]]] = None,
                     vpc_peering_connection_id: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouteResult]:
    """
    `ec2.Route` provides details about a specific Route.

    This resource can prove useful when finding the resource associated with a CIDR. For example, finding the peering connection associated with a CIDR value.

    ## Example Usage

    The following example shows how one might use a CIDR value to find a network interface id and use this to create a data source of that network interface.

    ```python
    import pulumi
    import pulumi_aws as aws

    config = pulumi.Config()
    subnet_id = config.require_object("subnetId")
    selected = aws.ec2.get_route_table(subnet_id=subnet_id)
    route = aws.ec2.get_route(route_table_id=selected_aws_route_table["id"],
        destination_cidr_block="10.0.1.0/24")
    interface = aws.ec2.get_network_interface(id=route.network_interface_id)
    ```


    :param str carrier_gateway_id: EC2 Carrier Gateway ID of the Route belonging to the Route Table.
    :param str core_network_arn: Core network ARN of the Route belonging to the Route Table.
    :param str destination_cidr_block: CIDR block of the Route belonging to the Route Table.
    :param str destination_ipv6_cidr_block: IPv6 CIDR block of the Route belonging to the Route Table.
    :param str destination_prefix_list_id: ID of a managed prefix list destination of the Route belonging to the Route Table.
    :param str egress_only_gateway_id: Egress Only Gateway ID of the Route belonging to the Route Table.
    :param str gateway_id: Gateway ID of the Route belonging to the Route Table.
    :param str instance_id: Instance ID of the Route belonging to the Route Table.
    :param str local_gateway_id: Local Gateway ID of the Route belonging to the Route Table.
    :param str nat_gateway_id: NAT Gateway ID of the Route belonging to the Route Table.
    :param str network_interface_id: Network Interface ID of the Route belonging to the Route Table.
    :param str route_table_id: ID of the specific Route Table containing the Route entry.
           
           The following arguments are optional:
    :param str transit_gateway_id: EC2 Transit Gateway ID of the Route belonging to the Route Table.
    :param str vpc_peering_connection_id: VPC Peering Connection ID of the Route belonging to the Route Table.
    """
    __args__ = dict()
    __args__['carrierGatewayId'] = carrier_gateway_id
    __args__['coreNetworkArn'] = core_network_arn
    __args__['destinationCidrBlock'] = destination_cidr_block
    __args__['destinationIpv6CidrBlock'] = destination_ipv6_cidr_block
    __args__['destinationPrefixListId'] = destination_prefix_list_id
    __args__['egressOnlyGatewayId'] = egress_only_gateway_id
    __args__['gatewayId'] = gateway_id
    __args__['instanceId'] = instance_id
    __args__['localGatewayId'] = local_gateway_id
    __args__['natGatewayId'] = nat_gateway_id
    __args__['networkInterfaceId'] = network_interface_id
    __args__['routeTableId'] = route_table_id
    __args__['transitGatewayId'] = transit_gateway_id
    __args__['vpcPeeringConnectionId'] = vpc_peering_connection_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:ec2/getRoute:getRoute', __args__, opts=opts, typ=GetRouteResult)
    return __ret__.apply(lambda __response__: GetRouteResult(
        carrier_gateway_id=pulumi.get(__response__, 'carrier_gateway_id'),
        core_network_arn=pulumi.get(__response__, 'core_network_arn'),
        destination_cidr_block=pulumi.get(__response__, 'destination_cidr_block'),
        destination_ipv6_cidr_block=pulumi.get(__response__, 'destination_ipv6_cidr_block'),
        destination_prefix_list_id=pulumi.get(__response__, 'destination_prefix_list_id'),
        egress_only_gateway_id=pulumi.get(__response__, 'egress_only_gateway_id'),
        gateway_id=pulumi.get(__response__, 'gateway_id'),
        id=pulumi.get(__response__, 'id'),
        instance_id=pulumi.get(__response__, 'instance_id'),
        local_gateway_id=pulumi.get(__response__, 'local_gateway_id'),
        nat_gateway_id=pulumi.get(__response__, 'nat_gateway_id'),
        network_interface_id=pulumi.get(__response__, 'network_interface_id'),
        route_table_id=pulumi.get(__response__, 'route_table_id'),
        transit_gateway_id=pulumi.get(__response__, 'transit_gateway_id'),
        vpc_peering_connection_id=pulumi.get(__response__, 'vpc_peering_connection_id')))
