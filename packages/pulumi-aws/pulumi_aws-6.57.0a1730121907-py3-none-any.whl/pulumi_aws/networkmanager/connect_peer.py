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

__all__ = ['ConnectPeerArgs', 'ConnectPeer']

@pulumi.input_type
class ConnectPeerArgs:
    def __init__(__self__, *,
                 connect_attachment_id: pulumi.Input[str],
                 peer_address: pulumi.Input[str],
                 bgp_options: Optional[pulumi.Input['ConnectPeerBgpOptionsArgs']] = None,
                 core_network_address: Optional[pulumi.Input[str]] = None,
                 inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ConnectPeer resource.
        :param pulumi.Input[str] connect_attachment_id: The ID of the connection attachment.
        :param pulumi.Input[str] peer_address: The Connect peer address.
               
               The following arguments are optional:
        :param pulumi.Input['ConnectPeerBgpOptionsArgs'] bgp_options: The Connect peer BGP options.
        :param pulumi.Input[str] core_network_address: A Connect peer core network address.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inside_cidr_blocks: The inside IP addresses used for BGP peering. Required when the Connect attachment protocol is `GRE`. See `networkmanager.ConnectAttachment` for details.
        :param pulumi.Input[str] subnet_arn: The subnet ARN for the Connect peer. Required when the Connect attachment protocol is `NO_ENCAP`. See `networkmanager.ConnectAttachment` for details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value tags for the attachment. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "connect_attachment_id", connect_attachment_id)
        pulumi.set(__self__, "peer_address", peer_address)
        if bgp_options is not None:
            pulumi.set(__self__, "bgp_options", bgp_options)
        if core_network_address is not None:
            pulumi.set(__self__, "core_network_address", core_network_address)
        if inside_cidr_blocks is not None:
            pulumi.set(__self__, "inside_cidr_blocks", inside_cidr_blocks)
        if subnet_arn is not None:
            pulumi.set(__self__, "subnet_arn", subnet_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="connectAttachmentId")
    def connect_attachment_id(self) -> pulumi.Input[str]:
        """
        The ID of the connection attachment.
        """
        return pulumi.get(self, "connect_attachment_id")

    @connect_attachment_id.setter
    def connect_attachment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "connect_attachment_id", value)

    @property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> pulumi.Input[str]:
        """
        The Connect peer address.

        The following arguments are optional:
        """
        return pulumi.get(self, "peer_address")

    @peer_address.setter
    def peer_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_address", value)

    @property
    @pulumi.getter(name="bgpOptions")
    def bgp_options(self) -> Optional[pulumi.Input['ConnectPeerBgpOptionsArgs']]:
        """
        The Connect peer BGP options.
        """
        return pulumi.get(self, "bgp_options")

    @bgp_options.setter
    def bgp_options(self, value: Optional[pulumi.Input['ConnectPeerBgpOptionsArgs']]):
        pulumi.set(self, "bgp_options", value)

    @property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[pulumi.Input[str]]:
        """
        A Connect peer core network address.
        """
        return pulumi.get(self, "core_network_address")

    @core_network_address.setter
    def core_network_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "core_network_address", value)

    @property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The inside IP addresses used for BGP peering. Required when the Connect attachment protocol is `GRE`. See `networkmanager.ConnectAttachment` for details.
        """
        return pulumi.get(self, "inside_cidr_blocks")

    @inside_cidr_blocks.setter
    def inside_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "inside_cidr_blocks", value)

    @property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The subnet ARN for the Connect peer. Required when the Connect attachment protocol is `NO_ENCAP`. See `networkmanager.ConnectAttachment` for details.
        """
        return pulumi.get(self, "subnet_arn")

    @subnet_arn.setter
    def subnet_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value tags for the attachment. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ConnectPeerState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 bgp_options: Optional[pulumi.Input['ConnectPeerBgpOptionsArgs']] = None,
                 configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectPeerConfigurationArgs']]]] = None,
                 connect_attachment_id: Optional[pulumi.Input[str]] = None,
                 connect_peer_id: Optional[pulumi.Input[str]] = None,
                 core_network_address: Optional[pulumi.Input[str]] = None,
                 core_network_id: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 edge_location: Optional[pulumi.Input[str]] = None,
                 inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 peer_address: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 subnet_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ConnectPeer resources.
        :param pulumi.Input[str] arn: The ARN of the attachment.
        :param pulumi.Input['ConnectPeerBgpOptionsArgs'] bgp_options: The Connect peer BGP options.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectPeerConfigurationArgs']]] configurations: The configuration of the Connect peer.
        :param pulumi.Input[str] connect_attachment_id: The ID of the connection attachment.
        :param pulumi.Input[str] core_network_address: A Connect peer core network address.
        :param pulumi.Input[str] core_network_id: The ID of a core network.
        :param pulumi.Input[str] edge_location: The Region where the peer is located.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inside_cidr_blocks: The inside IP addresses used for BGP peering. Required when the Connect attachment protocol is `GRE`. See `networkmanager.ConnectAttachment` for details.
        :param pulumi.Input[str] peer_address: The Connect peer address.
               
               The following arguments are optional:
        :param pulumi.Input[str] state: The state of the Connect peer.
        :param pulumi.Input[str] subnet_arn: The subnet ARN for the Connect peer. Required when the Connect attachment protocol is `NO_ENCAP`. See `networkmanager.ConnectAttachment` for details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value tags for the attachment. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if bgp_options is not None:
            pulumi.set(__self__, "bgp_options", bgp_options)
        if configurations is not None:
            pulumi.set(__self__, "configurations", configurations)
        if connect_attachment_id is not None:
            pulumi.set(__self__, "connect_attachment_id", connect_attachment_id)
        if connect_peer_id is not None:
            pulumi.set(__self__, "connect_peer_id", connect_peer_id)
        if core_network_address is not None:
            pulumi.set(__self__, "core_network_address", core_network_address)
        if core_network_id is not None:
            pulumi.set(__self__, "core_network_id", core_network_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if edge_location is not None:
            pulumi.set(__self__, "edge_location", edge_location)
        if inside_cidr_blocks is not None:
            pulumi.set(__self__, "inside_cidr_blocks", inside_cidr_blocks)
        if peer_address is not None:
            pulumi.set(__self__, "peer_address", peer_address)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if subnet_arn is not None:
            pulumi.set(__self__, "subnet_arn", subnet_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the attachment.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="bgpOptions")
    def bgp_options(self) -> Optional[pulumi.Input['ConnectPeerBgpOptionsArgs']]:
        """
        The Connect peer BGP options.
        """
        return pulumi.get(self, "bgp_options")

    @bgp_options.setter
    def bgp_options(self, value: Optional[pulumi.Input['ConnectPeerBgpOptionsArgs']]):
        pulumi.set(self, "bgp_options", value)

    @property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectPeerConfigurationArgs']]]]:
        """
        The configuration of the Connect peer.
        """
        return pulumi.get(self, "configurations")

    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectPeerConfigurationArgs']]]]):
        pulumi.set(self, "configurations", value)

    @property
    @pulumi.getter(name="connectAttachmentId")
    def connect_attachment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the connection attachment.
        """
        return pulumi.get(self, "connect_attachment_id")

    @connect_attachment_id.setter
    def connect_attachment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connect_attachment_id", value)

    @property
    @pulumi.getter(name="connectPeerId")
    def connect_peer_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "connect_peer_id")

    @connect_peer_id.setter
    def connect_peer_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connect_peer_id", value)

    @property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[pulumi.Input[str]]:
        """
        A Connect peer core network address.
        """
        return pulumi.get(self, "core_network_address")

    @core_network_address.setter
    def core_network_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "core_network_address", value)

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a core network.
        """
        return pulumi.get(self, "core_network_id")

    @core_network_id.setter
    def core_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "core_network_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> Optional[pulumi.Input[str]]:
        """
        The Region where the peer is located.
        """
        return pulumi.get(self, "edge_location")

    @edge_location.setter
    def edge_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "edge_location", value)

    @property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The inside IP addresses used for BGP peering. Required when the Connect attachment protocol is `GRE`. See `networkmanager.ConnectAttachment` for details.
        """
        return pulumi.get(self, "inside_cidr_blocks")

    @inside_cidr_blocks.setter
    def inside_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "inside_cidr_blocks", value)

    @property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> Optional[pulumi.Input[str]]:
        """
        The Connect peer address.

        The following arguments are optional:
        """
        return pulumi.get(self, "peer_address")

    @peer_address.setter
    def peer_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_address", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the Connect peer.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The subnet ARN for the Connect peer. Required when the Connect attachment protocol is `NO_ENCAP`. See `networkmanager.ConnectAttachment` for details.
        """
        return pulumi.get(self, "subnet_arn")

    @subnet_arn.setter
    def subnet_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value tags for the attachment. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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


class ConnectPeer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_options: Optional[pulumi.Input[Union['ConnectPeerBgpOptionsArgs', 'ConnectPeerBgpOptionsArgsDict']]] = None,
                 connect_attachment_id: Optional[pulumi.Input[str]] = None,
                 core_network_address: Optional[pulumi.Input[str]] = None,
                 inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 peer_address: Optional[pulumi.Input[str]] = None,
                 subnet_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource for managing an AWS Network Manager Connect Peer.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.networkmanager.VpcAttachment("example",
            subnet_arns=[__item["arn"] for __item in example_aws_subnet],
            core_network_id=example_awscc_networkmanager_core_network["id"],
            vpc_arn=example_aws_vpc["arn"])
        example_connect_attachment = aws.networkmanager.ConnectAttachment("example",
            core_network_id=example_awscc_networkmanager_core_network["id"],
            transport_attachment_id=example.id,
            edge_location=example.edge_location,
            options={
                "protocol": "GRE",
            })
        example_connect_peer = aws.networkmanager.ConnectPeer("example",
            connect_attachment_id=example_connect_attachment.id,
            peer_address="127.0.0.1",
            bgp_options={
                "peer_asn": 65000,
            },
            inside_cidr_blocks=["172.16.0.0/16"])
        ```

        ### Usage with attachment accepter

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.networkmanager.VpcAttachment("example",
            subnet_arns=[__item["arn"] for __item in example_aws_subnet],
            core_network_id=example_awscc_networkmanager_core_network["id"],
            vpc_arn=example_aws_vpc["arn"])
        example_attachment_accepter = aws.networkmanager.AttachmentAccepter("example",
            attachment_id=example.id,
            attachment_type=example.attachment_type)
        example_connect_attachment = aws.networkmanager.ConnectAttachment("example",
            core_network_id=example_awscc_networkmanager_core_network["id"],
            transport_attachment_id=example.id,
            edge_location=example.edge_location,
            options={
                "protocol": "GRE",
            },
            opts = pulumi.ResourceOptions(depends_on=[test]))
        example2 = aws.networkmanager.AttachmentAccepter("example2",
            attachment_id=example_connect_attachment.id,
            attachment_type=example_connect_attachment.attachment_type)
        example_connect_peer = aws.networkmanager.ConnectPeer("example",
            connect_attachment_id=example_connect_attachment.id,
            peer_address="127.0.0.1",
            bgp_options={
                "peer_asn": 65500,
            },
            inside_cidr_blocks=["172.16.0.0/16"],
            opts = pulumi.ResourceOptions(depends_on=[example2]))
        ```

        ### Usage with a Tunnel-less Connect attachment

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.networkmanager.VpcAttachment("example",
            subnet_arns=[__item["arn"] for __item in example_aws_subnet],
            core_network_id=example_awscc_networkmanager_core_network["id"],
            vpc_arn=example_aws_vpc["arn"])
        example_connect_attachment = aws.networkmanager.ConnectAttachment("example",
            core_network_id=example_awscc_networkmanager_core_network["id"],
            transport_attachment_id=example.id,
            edge_location=example.edge_location,
            options={
                "protocol": "NO_ENCAP",
            })
        example_connect_peer = aws.networkmanager.ConnectPeer("example",
            connect_attachment_id=example_connect_attachment.id,
            peer_address="127.0.0.1",
            bgp_options={
                "peer_asn": 65000,
            },
            subnet_arn=test2["arn"])
        ```

        ## Import

        Using `pulumi import`, import `aws_networkmanager_connect_peer` using the connect peer ID. For example:

        ```sh
        $ pulumi import aws:networkmanager/connectPeer:ConnectPeer example connect-peer-061f3e96275db1acc
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ConnectPeerBgpOptionsArgs', 'ConnectPeerBgpOptionsArgsDict']] bgp_options: The Connect peer BGP options.
        :param pulumi.Input[str] connect_attachment_id: The ID of the connection attachment.
        :param pulumi.Input[str] core_network_address: A Connect peer core network address.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inside_cidr_blocks: The inside IP addresses used for BGP peering. Required when the Connect attachment protocol is `GRE`. See `networkmanager.ConnectAttachment` for details.
        :param pulumi.Input[str] peer_address: The Connect peer address.
               
               The following arguments are optional:
        :param pulumi.Input[str] subnet_arn: The subnet ARN for the Connect peer. Required when the Connect attachment protocol is `NO_ENCAP`. See `networkmanager.ConnectAttachment` for details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value tags for the attachment. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectPeerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS Network Manager Connect Peer.

        ## Example Usage

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.networkmanager.VpcAttachment("example",
            subnet_arns=[__item["arn"] for __item in example_aws_subnet],
            core_network_id=example_awscc_networkmanager_core_network["id"],
            vpc_arn=example_aws_vpc["arn"])
        example_connect_attachment = aws.networkmanager.ConnectAttachment("example",
            core_network_id=example_awscc_networkmanager_core_network["id"],
            transport_attachment_id=example.id,
            edge_location=example.edge_location,
            options={
                "protocol": "GRE",
            })
        example_connect_peer = aws.networkmanager.ConnectPeer("example",
            connect_attachment_id=example_connect_attachment.id,
            peer_address="127.0.0.1",
            bgp_options={
                "peer_asn": 65000,
            },
            inside_cidr_blocks=["172.16.0.0/16"])
        ```

        ### Usage with attachment accepter

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.networkmanager.VpcAttachment("example",
            subnet_arns=[__item["arn"] for __item in example_aws_subnet],
            core_network_id=example_awscc_networkmanager_core_network["id"],
            vpc_arn=example_aws_vpc["arn"])
        example_attachment_accepter = aws.networkmanager.AttachmentAccepter("example",
            attachment_id=example.id,
            attachment_type=example.attachment_type)
        example_connect_attachment = aws.networkmanager.ConnectAttachment("example",
            core_network_id=example_awscc_networkmanager_core_network["id"],
            transport_attachment_id=example.id,
            edge_location=example.edge_location,
            options={
                "protocol": "GRE",
            },
            opts = pulumi.ResourceOptions(depends_on=[test]))
        example2 = aws.networkmanager.AttachmentAccepter("example2",
            attachment_id=example_connect_attachment.id,
            attachment_type=example_connect_attachment.attachment_type)
        example_connect_peer = aws.networkmanager.ConnectPeer("example",
            connect_attachment_id=example_connect_attachment.id,
            peer_address="127.0.0.1",
            bgp_options={
                "peer_asn": 65500,
            },
            inside_cidr_blocks=["172.16.0.0/16"],
            opts = pulumi.ResourceOptions(depends_on=[example2]))
        ```

        ### Usage with a Tunnel-less Connect attachment

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.networkmanager.VpcAttachment("example",
            subnet_arns=[__item["arn"] for __item in example_aws_subnet],
            core_network_id=example_awscc_networkmanager_core_network["id"],
            vpc_arn=example_aws_vpc["arn"])
        example_connect_attachment = aws.networkmanager.ConnectAttachment("example",
            core_network_id=example_awscc_networkmanager_core_network["id"],
            transport_attachment_id=example.id,
            edge_location=example.edge_location,
            options={
                "protocol": "NO_ENCAP",
            })
        example_connect_peer = aws.networkmanager.ConnectPeer("example",
            connect_attachment_id=example_connect_attachment.id,
            peer_address="127.0.0.1",
            bgp_options={
                "peer_asn": 65000,
            },
            subnet_arn=test2["arn"])
        ```

        ## Import

        Using `pulumi import`, import `aws_networkmanager_connect_peer` using the connect peer ID. For example:

        ```sh
        $ pulumi import aws:networkmanager/connectPeer:ConnectPeer example connect-peer-061f3e96275db1acc
        ```

        :param str resource_name: The name of the resource.
        :param ConnectPeerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectPeerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_options: Optional[pulumi.Input[Union['ConnectPeerBgpOptionsArgs', 'ConnectPeerBgpOptionsArgsDict']]] = None,
                 connect_attachment_id: Optional[pulumi.Input[str]] = None,
                 core_network_address: Optional[pulumi.Input[str]] = None,
                 inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 peer_address: Optional[pulumi.Input[str]] = None,
                 subnet_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectPeerArgs.__new__(ConnectPeerArgs)

            __props__.__dict__["bgp_options"] = bgp_options
            if connect_attachment_id is None and not opts.urn:
                raise TypeError("Missing required property 'connect_attachment_id'")
            __props__.__dict__["connect_attachment_id"] = connect_attachment_id
            __props__.__dict__["core_network_address"] = core_network_address
            __props__.__dict__["inside_cidr_blocks"] = inside_cidr_blocks
            if peer_address is None and not opts.urn:
                raise TypeError("Missing required property 'peer_address'")
            __props__.__dict__["peer_address"] = peer_address
            __props__.__dict__["subnet_arn"] = subnet_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["configurations"] = None
            __props__.__dict__["connect_peer_id"] = None
            __props__.__dict__["core_network_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["edge_location"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["tags_all"] = None
        super(ConnectPeer, __self__).__init__(
            'aws:networkmanager/connectPeer:ConnectPeer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            bgp_options: Optional[pulumi.Input[Union['ConnectPeerBgpOptionsArgs', 'ConnectPeerBgpOptionsArgsDict']]] = None,
            configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ConnectPeerConfigurationArgs', 'ConnectPeerConfigurationArgsDict']]]]] = None,
            connect_attachment_id: Optional[pulumi.Input[str]] = None,
            connect_peer_id: Optional[pulumi.Input[str]] = None,
            core_network_address: Optional[pulumi.Input[str]] = None,
            core_network_id: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            edge_location: Optional[pulumi.Input[str]] = None,
            inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            peer_address: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            subnet_arn: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'ConnectPeer':
        """
        Get an existing ConnectPeer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the attachment.
        :param pulumi.Input[Union['ConnectPeerBgpOptionsArgs', 'ConnectPeerBgpOptionsArgsDict']] bgp_options: The Connect peer BGP options.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ConnectPeerConfigurationArgs', 'ConnectPeerConfigurationArgsDict']]]] configurations: The configuration of the Connect peer.
        :param pulumi.Input[str] connect_attachment_id: The ID of the connection attachment.
        :param pulumi.Input[str] core_network_address: A Connect peer core network address.
        :param pulumi.Input[str] core_network_id: The ID of a core network.
        :param pulumi.Input[str] edge_location: The Region where the peer is located.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inside_cidr_blocks: The inside IP addresses used for BGP peering. Required when the Connect attachment protocol is `GRE`. See `networkmanager.ConnectAttachment` for details.
        :param pulumi.Input[str] peer_address: The Connect peer address.
               
               The following arguments are optional:
        :param pulumi.Input[str] state: The state of the Connect peer.
        :param pulumi.Input[str] subnet_arn: The subnet ARN for the Connect peer. Required when the Connect attachment protocol is `NO_ENCAP`. See `networkmanager.ConnectAttachment` for details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value tags for the attachment. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectPeerState.__new__(_ConnectPeerState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["bgp_options"] = bgp_options
        __props__.__dict__["configurations"] = configurations
        __props__.__dict__["connect_attachment_id"] = connect_attachment_id
        __props__.__dict__["connect_peer_id"] = connect_peer_id
        __props__.__dict__["core_network_address"] = core_network_address
        __props__.__dict__["core_network_id"] = core_network_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["edge_location"] = edge_location
        __props__.__dict__["inside_cidr_blocks"] = inside_cidr_blocks
        __props__.__dict__["peer_address"] = peer_address
        __props__.__dict__["state"] = state
        __props__.__dict__["subnet_arn"] = subnet_arn
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return ConnectPeer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the attachment.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="bgpOptions")
    def bgp_options(self) -> pulumi.Output[Optional['outputs.ConnectPeerBgpOptions']]:
        """
        The Connect peer BGP options.
        """
        return pulumi.get(self, "bgp_options")

    @property
    @pulumi.getter
    def configurations(self) -> pulumi.Output[Sequence['outputs.ConnectPeerConfiguration']]:
        """
        The configuration of the Connect peer.
        """
        return pulumi.get(self, "configurations")

    @property
    @pulumi.getter(name="connectAttachmentId")
    def connect_attachment_id(self) -> pulumi.Output[str]:
        """
        The ID of the connection attachment.
        """
        return pulumi.get(self, "connect_attachment_id")

    @property
    @pulumi.getter(name="connectPeerId")
    def connect_peer_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "connect_peer_id")

    @property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> pulumi.Output[Optional[str]]:
        """
        A Connect peer core network address.
        """
        return pulumi.get(self, "core_network_address")

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Output[str]:
        """
        The ID of a core network.
        """
        return pulumi.get(self, "core_network_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> pulumi.Output[str]:
        """
        The Region where the peer is located.
        """
        return pulumi.get(self, "edge_location")

    @property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The inside IP addresses used for BGP peering. Required when the Connect attachment protocol is `GRE`. See `networkmanager.ConnectAttachment` for details.
        """
        return pulumi.get(self, "inside_cidr_blocks")

    @property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> pulumi.Output[str]:
        """
        The Connect peer address.

        The following arguments are optional:
        """
        return pulumi.get(self, "peer_address")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the Connect peer.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The subnet ARN for the Connect peer. Required when the Connect attachment protocol is `NO_ENCAP`. See `networkmanager.ConnectAttachment` for details.
        """
        return pulumi.get(self, "subnet_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value tags for the attachment. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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

