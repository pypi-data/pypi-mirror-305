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

__all__ = ['GatewayAssociationProposalArgs', 'GatewayAssociationProposal']

@pulumi.input_type
class GatewayAssociationProposalArgs:
    def __init__(__self__, *,
                 associated_gateway_id: pulumi.Input[str],
                 dx_gateway_id: pulumi.Input[str],
                 dx_gateway_owner_account_id: pulumi.Input[str],
                 allowed_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a GatewayAssociationProposal resource.
        :param pulumi.Input[str] associated_gateway_id: The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
        :param pulumi.Input[str] dx_gateway_id: Direct Connect Gateway identifier.
        :param pulumi.Input[str] dx_gateway_owner_account_id: AWS Account identifier of the Direct Connect Gateway's owner.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_prefixes: VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
        """
        pulumi.set(__self__, "associated_gateway_id", associated_gateway_id)
        pulumi.set(__self__, "dx_gateway_id", dx_gateway_id)
        pulumi.set(__self__, "dx_gateway_owner_account_id", dx_gateway_owner_account_id)
        if allowed_prefixes is not None:
            pulumi.set(__self__, "allowed_prefixes", allowed_prefixes)

    @property
    @pulumi.getter(name="associatedGatewayId")
    def associated_gateway_id(self) -> pulumi.Input[str]:
        """
        The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
        """
        return pulumi.get(self, "associated_gateway_id")

    @associated_gateway_id.setter
    def associated_gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "associated_gateway_id", value)

    @property
    @pulumi.getter(name="dxGatewayId")
    def dx_gateway_id(self) -> pulumi.Input[str]:
        """
        Direct Connect Gateway identifier.
        """
        return pulumi.get(self, "dx_gateway_id")

    @dx_gateway_id.setter
    def dx_gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dx_gateway_id", value)

    @property
    @pulumi.getter(name="dxGatewayOwnerAccountId")
    def dx_gateway_owner_account_id(self) -> pulumi.Input[str]:
        """
        AWS Account identifier of the Direct Connect Gateway's owner.
        """
        return pulumi.get(self, "dx_gateway_owner_account_id")

    @dx_gateway_owner_account_id.setter
    def dx_gateway_owner_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dx_gateway_owner_account_id", value)

    @property
    @pulumi.getter(name="allowedPrefixes")
    def allowed_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
        """
        return pulumi.get(self, "allowed_prefixes")

    @allowed_prefixes.setter
    def allowed_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_prefixes", value)


@pulumi.input_type
class _GatewayAssociationProposalState:
    def __init__(__self__, *,
                 allowed_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 associated_gateway_id: Optional[pulumi.Input[str]] = None,
                 associated_gateway_owner_account_id: Optional[pulumi.Input[str]] = None,
                 associated_gateway_type: Optional[pulumi.Input[str]] = None,
                 dx_gateway_id: Optional[pulumi.Input[str]] = None,
                 dx_gateway_owner_account_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GatewayAssociationProposal resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_prefixes: VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
        :param pulumi.Input[str] associated_gateway_id: The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
        :param pulumi.Input[str] associated_gateway_owner_account_id: The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
        :param pulumi.Input[str] associated_gateway_type: The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
        :param pulumi.Input[str] dx_gateway_id: Direct Connect Gateway identifier.
        :param pulumi.Input[str] dx_gateway_owner_account_id: AWS Account identifier of the Direct Connect Gateway's owner.
        """
        if allowed_prefixes is not None:
            pulumi.set(__self__, "allowed_prefixes", allowed_prefixes)
        if associated_gateway_id is not None:
            pulumi.set(__self__, "associated_gateway_id", associated_gateway_id)
        if associated_gateway_owner_account_id is not None:
            pulumi.set(__self__, "associated_gateway_owner_account_id", associated_gateway_owner_account_id)
        if associated_gateway_type is not None:
            pulumi.set(__self__, "associated_gateway_type", associated_gateway_type)
        if dx_gateway_id is not None:
            pulumi.set(__self__, "dx_gateway_id", dx_gateway_id)
        if dx_gateway_owner_account_id is not None:
            pulumi.set(__self__, "dx_gateway_owner_account_id", dx_gateway_owner_account_id)

    @property
    @pulumi.getter(name="allowedPrefixes")
    def allowed_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
        """
        return pulumi.get(self, "allowed_prefixes")

    @allowed_prefixes.setter
    def allowed_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_prefixes", value)

    @property
    @pulumi.getter(name="associatedGatewayId")
    def associated_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
        """
        return pulumi.get(self, "associated_gateway_id")

    @associated_gateway_id.setter
    def associated_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "associated_gateway_id", value)

    @property
    @pulumi.getter(name="associatedGatewayOwnerAccountId")
    def associated_gateway_owner_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
        """
        return pulumi.get(self, "associated_gateway_owner_account_id")

    @associated_gateway_owner_account_id.setter
    def associated_gateway_owner_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "associated_gateway_owner_account_id", value)

    @property
    @pulumi.getter(name="associatedGatewayType")
    def associated_gateway_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
        """
        return pulumi.get(self, "associated_gateway_type")

    @associated_gateway_type.setter
    def associated_gateway_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "associated_gateway_type", value)

    @property
    @pulumi.getter(name="dxGatewayId")
    def dx_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        Direct Connect Gateway identifier.
        """
        return pulumi.get(self, "dx_gateway_id")

    @dx_gateway_id.setter
    def dx_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dx_gateway_id", value)

    @property
    @pulumi.getter(name="dxGatewayOwnerAccountId")
    def dx_gateway_owner_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS Account identifier of the Direct Connect Gateway's owner.
        """
        return pulumi.get(self, "dx_gateway_owner_account_id")

    @dx_gateway_owner_account_id.setter
    def dx_gateway_owner_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dx_gateway_owner_account_id", value)


class GatewayAssociationProposal(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 associated_gateway_id: Optional[pulumi.Input[str]] = None,
                 dx_gateway_id: Optional[pulumi.Input[str]] = None,
                 dx_gateway_owner_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Direct Connect Gateway Association Proposal, typically for enabling cross-account associations. For single account associations, see the `directconnect.GatewayAssociation` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.directconnect.GatewayAssociationProposal("example",
            dx_gateway_id=example_aws_dx_gateway["id"],
            dx_gateway_owner_account_id=example_aws_dx_gateway["ownerAccountId"],
            associated_gateway_id=example_aws_vpn_gateway["id"])
        ```

        ## Import

        Using a proposal ID, Direct Connect Gateway ID and associated gateway ID separated by `/`:

        __With `pulumi import`__, import Direct Connect Gateway Association Proposals using either a proposal ID or proposal ID, Direct Connect Gateway ID and associated gateway ID separated by `/`. For example:

        Using a proposal ID:

        ```sh
        $ pulumi import aws:directconnect/gatewayAssociationProposal:GatewayAssociationProposal example ac90e981-b718-4364-872d-65478c84fafe
        ```
        Using a proposal ID, Direct Connect Gateway ID and associated gateway ID separated by `/`:

        ```sh
        $ pulumi import aws:directconnect/gatewayAssociationProposal:GatewayAssociationProposal example ac90e981-b718-4364-872d-65478c84fafe/abcd1234-dcba-5678-be23-cdef9876ab45/vgw-12345678
        ```
        The latter case is useful when a previous proposal has been accepted and deleted by AWS.
        The `aws_dx_gateway_association_proposal` resource will then represent a pseudo-proposal for the same Direct Connect Gateway and associated gateway. If no previous proposal is available, use a tool like [`uuidgen`](http://manpages.ubuntu.com/manpages/bionic/man1/uuidgen.1.html) to generate a new random pseudo-proposal ID.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_prefixes: VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
        :param pulumi.Input[str] associated_gateway_id: The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
        :param pulumi.Input[str] dx_gateway_id: Direct Connect Gateway identifier.
        :param pulumi.Input[str] dx_gateway_owner_account_id: AWS Account identifier of the Direct Connect Gateway's owner.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GatewayAssociationProposalArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Direct Connect Gateway Association Proposal, typically for enabling cross-account associations. For single account associations, see the `directconnect.GatewayAssociation` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.directconnect.GatewayAssociationProposal("example",
            dx_gateway_id=example_aws_dx_gateway["id"],
            dx_gateway_owner_account_id=example_aws_dx_gateway["ownerAccountId"],
            associated_gateway_id=example_aws_vpn_gateway["id"])
        ```

        ## Import

        Using a proposal ID, Direct Connect Gateway ID and associated gateway ID separated by `/`:

        __With `pulumi import`__, import Direct Connect Gateway Association Proposals using either a proposal ID or proposal ID, Direct Connect Gateway ID and associated gateway ID separated by `/`. For example:

        Using a proposal ID:

        ```sh
        $ pulumi import aws:directconnect/gatewayAssociationProposal:GatewayAssociationProposal example ac90e981-b718-4364-872d-65478c84fafe
        ```
        Using a proposal ID, Direct Connect Gateway ID and associated gateway ID separated by `/`:

        ```sh
        $ pulumi import aws:directconnect/gatewayAssociationProposal:GatewayAssociationProposal example ac90e981-b718-4364-872d-65478c84fafe/abcd1234-dcba-5678-be23-cdef9876ab45/vgw-12345678
        ```
        The latter case is useful when a previous proposal has been accepted and deleted by AWS.
        The `aws_dx_gateway_association_proposal` resource will then represent a pseudo-proposal for the same Direct Connect Gateway and associated gateway. If no previous proposal is available, use a tool like [`uuidgen`](http://manpages.ubuntu.com/manpages/bionic/man1/uuidgen.1.html) to generate a new random pseudo-proposal ID.

        :param str resource_name: The name of the resource.
        :param GatewayAssociationProposalArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GatewayAssociationProposalArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 associated_gateway_id: Optional[pulumi.Input[str]] = None,
                 dx_gateway_id: Optional[pulumi.Input[str]] = None,
                 dx_gateway_owner_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GatewayAssociationProposalArgs.__new__(GatewayAssociationProposalArgs)

            __props__.__dict__["allowed_prefixes"] = allowed_prefixes
            if associated_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'associated_gateway_id'")
            __props__.__dict__["associated_gateway_id"] = associated_gateway_id
            if dx_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'dx_gateway_id'")
            __props__.__dict__["dx_gateway_id"] = dx_gateway_id
            if dx_gateway_owner_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'dx_gateway_owner_account_id'")
            __props__.__dict__["dx_gateway_owner_account_id"] = dx_gateway_owner_account_id
            __props__.__dict__["associated_gateway_owner_account_id"] = None
            __props__.__dict__["associated_gateway_type"] = None
        super(GatewayAssociationProposal, __self__).__init__(
            'aws:directconnect/gatewayAssociationProposal:GatewayAssociationProposal',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allowed_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            associated_gateway_id: Optional[pulumi.Input[str]] = None,
            associated_gateway_owner_account_id: Optional[pulumi.Input[str]] = None,
            associated_gateway_type: Optional[pulumi.Input[str]] = None,
            dx_gateway_id: Optional[pulumi.Input[str]] = None,
            dx_gateway_owner_account_id: Optional[pulumi.Input[str]] = None) -> 'GatewayAssociationProposal':
        """
        Get an existing GatewayAssociationProposal resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_prefixes: VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
        :param pulumi.Input[str] associated_gateway_id: The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
        :param pulumi.Input[str] associated_gateway_owner_account_id: The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
        :param pulumi.Input[str] associated_gateway_type: The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
        :param pulumi.Input[str] dx_gateway_id: Direct Connect Gateway identifier.
        :param pulumi.Input[str] dx_gateway_owner_account_id: AWS Account identifier of the Direct Connect Gateway's owner.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GatewayAssociationProposalState.__new__(_GatewayAssociationProposalState)

        __props__.__dict__["allowed_prefixes"] = allowed_prefixes
        __props__.__dict__["associated_gateway_id"] = associated_gateway_id
        __props__.__dict__["associated_gateway_owner_account_id"] = associated_gateway_owner_account_id
        __props__.__dict__["associated_gateway_type"] = associated_gateway_type
        __props__.__dict__["dx_gateway_id"] = dx_gateway_id
        __props__.__dict__["dx_gateway_owner_account_id"] = dx_gateway_owner_account_id
        return GatewayAssociationProposal(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedPrefixes")
    def allowed_prefixes(self) -> pulumi.Output[Sequence[str]]:
        """
        VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
        """
        return pulumi.get(self, "allowed_prefixes")

    @property
    @pulumi.getter(name="associatedGatewayId")
    def associated_gateway_id(self) -> pulumi.Output[str]:
        """
        The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
        """
        return pulumi.get(self, "associated_gateway_id")

    @property
    @pulumi.getter(name="associatedGatewayOwnerAccountId")
    def associated_gateway_owner_account_id(self) -> pulumi.Output[str]:
        """
        The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
        """
        return pulumi.get(self, "associated_gateway_owner_account_id")

    @property
    @pulumi.getter(name="associatedGatewayType")
    def associated_gateway_type(self) -> pulumi.Output[str]:
        """
        The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
        """
        return pulumi.get(self, "associated_gateway_type")

    @property
    @pulumi.getter(name="dxGatewayId")
    def dx_gateway_id(self) -> pulumi.Output[str]:
        """
        Direct Connect Gateway identifier.
        """
        return pulumi.get(self, "dx_gateway_id")

    @property
    @pulumi.getter(name="dxGatewayOwnerAccountId")
    def dx_gateway_owner_account_id(self) -> pulumi.Output[str]:
        """
        AWS Account identifier of the Direct Connect Gateway's owner.
        """
        return pulumi.get(self, "dx_gateway_owner_account_id")

