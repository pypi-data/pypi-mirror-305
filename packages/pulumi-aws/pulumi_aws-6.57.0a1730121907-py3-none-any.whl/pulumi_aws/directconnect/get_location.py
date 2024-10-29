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
    'GetLocationResult',
    'AwaitableGetLocationResult',
    'get_location',
    'get_location_output',
]

@pulumi.output_type
class GetLocationResult:
    """
    A collection of values returned by getLocation.
    """
    def __init__(__self__, available_macsec_port_speeds=None, available_port_speeds=None, available_providers=None, id=None, location_code=None, location_name=None):
        if available_macsec_port_speeds and not isinstance(available_macsec_port_speeds, list):
            raise TypeError("Expected argument 'available_macsec_port_speeds' to be a list")
        pulumi.set(__self__, "available_macsec_port_speeds", available_macsec_port_speeds)
        if available_port_speeds and not isinstance(available_port_speeds, list):
            raise TypeError("Expected argument 'available_port_speeds' to be a list")
        pulumi.set(__self__, "available_port_speeds", available_port_speeds)
        if available_providers and not isinstance(available_providers, list):
            raise TypeError("Expected argument 'available_providers' to be a list")
        pulumi.set(__self__, "available_providers", available_providers)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location_code and not isinstance(location_code, str):
            raise TypeError("Expected argument 'location_code' to be a str")
        pulumi.set(__self__, "location_code", location_code)
        if location_name and not isinstance(location_name, str):
            raise TypeError("Expected argument 'location_name' to be a str")
        pulumi.set(__self__, "location_name", location_name)

    @property
    @pulumi.getter(name="availableMacsecPortSpeeds")
    def available_macsec_port_speeds(self) -> Sequence[str]:
        """
        The available MAC Security (MACsec) port speeds for the location.
        """
        return pulumi.get(self, "available_macsec_port_speeds")

    @property
    @pulumi.getter(name="availablePortSpeeds")
    def available_port_speeds(self) -> Sequence[str]:
        """
        The available port speeds for the location.
        """
        return pulumi.get(self, "available_port_speeds")

    @property
    @pulumi.getter(name="availableProviders")
    def available_providers(self) -> Sequence[str]:
        """
        Names of the service providers for the location.
        """
        return pulumi.get(self, "available_providers")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="locationCode")
    def location_code(self) -> str:
        return pulumi.get(self, "location_code")

    @property
    @pulumi.getter(name="locationName")
    def location_name(self) -> str:
        """
        Name of the location. This includes the name of the colocation partner and the physical site of the building.
        """
        return pulumi.get(self, "location_name")


class AwaitableGetLocationResult(GetLocationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocationResult(
            available_macsec_port_speeds=self.available_macsec_port_speeds,
            available_port_speeds=self.available_port_speeds,
            available_providers=self.available_providers,
            id=self.id,
            location_code=self.location_code,
            location_name=self.location_name)


def get_location(location_code: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocationResult:
    """
    Retrieve information about a specific AWS Direct Connect location in the current AWS Region.
    These are the locations that can be specified when configuring `directconnect.Connection` or `directconnect.LinkAggregationGroup` resources.

    > **Note:** This data source is different from the `directconnect_get_locations` data source which retrieves information about all the AWS Direct Connect locations in the current AWS Region.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.directconnect.get_location(location_code="CS32A-24FL")
    ```


    :param str location_code: Code for the location to retrieve.
    """
    __args__ = dict()
    __args__['locationCode'] = location_code
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:directconnect/getLocation:getLocation', __args__, opts=opts, typ=GetLocationResult).value

    return AwaitableGetLocationResult(
        available_macsec_port_speeds=pulumi.get(__ret__, 'available_macsec_port_speeds'),
        available_port_speeds=pulumi.get(__ret__, 'available_port_speeds'),
        available_providers=pulumi.get(__ret__, 'available_providers'),
        id=pulumi.get(__ret__, 'id'),
        location_code=pulumi.get(__ret__, 'location_code'),
        location_name=pulumi.get(__ret__, 'location_name'))
def get_location_output(location_code: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocationResult]:
    """
    Retrieve information about a specific AWS Direct Connect location in the current AWS Region.
    These are the locations that can be specified when configuring `directconnect.Connection` or `directconnect.LinkAggregationGroup` resources.

    > **Note:** This data source is different from the `directconnect_get_locations` data source which retrieves information about all the AWS Direct Connect locations in the current AWS Region.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.directconnect.get_location(location_code="CS32A-24FL")
    ```


    :param str location_code: Code for the location to retrieve.
    """
    __args__ = dict()
    __args__['locationCode'] = location_code
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:directconnect/getLocation:getLocation', __args__, opts=opts, typ=GetLocationResult)
    return __ret__.apply(lambda __response__: GetLocationResult(
        available_macsec_port_speeds=pulumi.get(__response__, 'available_macsec_port_speeds'),
        available_port_speeds=pulumi.get(__response__, 'available_port_speeds'),
        available_providers=pulumi.get(__response__, 'available_providers'),
        id=pulumi.get(__response__, 'id'),
        location_code=pulumi.get(__response__, 'location_code'),
        location_name=pulumi.get(__response__, 'location_name')))
