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

__all__ = [
    'GetRouteTableAssociationsResult',
    'AwaitableGetRouteTableAssociationsResult',
    'get_route_table_associations',
    'get_route_table_associations_output',
]

@pulumi.output_type
class GetRouteTableAssociationsResult:
    """
    A collection of values returned by getRouteTableAssociations.
    """
    def __init__(__self__, filters=None, id=None, ids=None, transit_gateway_route_table_id=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if transit_gateway_route_table_id and not isinstance(transit_gateway_route_table_id, str):
            raise TypeError("Expected argument 'transit_gateway_route_table_id' to be a str")
        pulumi.set(__self__, "transit_gateway_route_table_id", transit_gateway_route_table_id)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetRouteTableAssociationsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        Set of Transit Gateway Route Table Association identifiers.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> str:
        return pulumi.get(self, "transit_gateway_route_table_id")


class AwaitableGetRouteTableAssociationsResult(GetRouteTableAssociationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteTableAssociationsResult(
            filters=self.filters,
            id=self.id,
            ids=self.ids,
            transit_gateway_route_table_id=self.transit_gateway_route_table_id)


def get_route_table_associations(filters: Optional[Sequence[Union['GetRouteTableAssociationsFilterArgs', 'GetRouteTableAssociationsFilterArgsDict']]] = None,
                                 transit_gateway_route_table_id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouteTableAssociationsResult:
    """
    Provides information for multiple EC2 Transit Gateway Route Table Associations, such as their identifiers.

    ## Example Usage

    ### By Transit Gateway Identifier

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_route_table_associations(transit_gateway_route_table_id=example_aws_ec2_transit_gateway_route_table["id"])
    ```


    :param Sequence[Union['GetRouteTableAssociationsFilterArgs', 'GetRouteTableAssociationsFilterArgsDict']] filters: Custom filter block as described below.
           
           More complex filters can be expressed using one or more `filter` sub-blocks,
           which take the following arguments:
    :param str transit_gateway_route_table_id: Identifier of EC2 Transit Gateway Route Table.
           
           The following arguments are optional:
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['transitGatewayRouteTableId'] = transit_gateway_route_table_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ec2transitgateway/getRouteTableAssociations:getRouteTableAssociations', __args__, opts=opts, typ=GetRouteTableAssociationsResult).value

    return AwaitableGetRouteTableAssociationsResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        transit_gateway_route_table_id=pulumi.get(__ret__, 'transit_gateway_route_table_id'))
def get_route_table_associations_output(filters: Optional[pulumi.Input[Optional[Sequence[Union['GetRouteTableAssociationsFilterArgs', 'GetRouteTableAssociationsFilterArgsDict']]]]] = None,
                                        transit_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouteTableAssociationsResult]:
    """
    Provides information for multiple EC2 Transit Gateway Route Table Associations, such as their identifiers.

    ## Example Usage

    ### By Transit Gateway Identifier

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_route_table_associations(transit_gateway_route_table_id=example_aws_ec2_transit_gateway_route_table["id"])
    ```


    :param Sequence[Union['GetRouteTableAssociationsFilterArgs', 'GetRouteTableAssociationsFilterArgsDict']] filters: Custom filter block as described below.
           
           More complex filters can be expressed using one or more `filter` sub-blocks,
           which take the following arguments:
    :param str transit_gateway_route_table_id: Identifier of EC2 Transit Gateway Route Table.
           
           The following arguments are optional:
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['transitGatewayRouteTableId'] = transit_gateway_route_table_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:ec2transitgateway/getRouteTableAssociations:getRouteTableAssociations', __args__, opts=opts, typ=GetRouteTableAssociationsResult)
    return __ret__.apply(lambda __response__: GetRouteTableAssociationsResult(
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        ids=pulumi.get(__response__, 'ids'),
        transit_gateway_route_table_id=pulumi.get(__response__, 'transit_gateway_route_table_id')))
