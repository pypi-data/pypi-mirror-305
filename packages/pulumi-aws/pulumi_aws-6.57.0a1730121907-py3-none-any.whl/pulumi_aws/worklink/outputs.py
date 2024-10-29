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
    'FleetIdentityProvider',
    'FleetNetwork',
]

@pulumi.output_type
class FleetIdentityProvider(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "samlMetadata":
            suggest = "saml_metadata"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FleetIdentityProvider. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FleetIdentityProvider.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FleetIdentityProvider.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 saml_metadata: str,
                 type: str):
        """
        :param str saml_metadata: The SAML metadata document provided by the customer’s identity provider.
        :param str type: The type of identity provider.
        """
        pulumi.set(__self__, "saml_metadata", saml_metadata)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="samlMetadata")
    def saml_metadata(self) -> str:
        """
        The SAML metadata document provided by the customer’s identity provider.
        """
        return pulumi.get(self, "saml_metadata")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of identity provider.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class FleetNetwork(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "securityGroupIds":
            suggest = "security_group_ids"
        elif key == "subnetIds":
            suggest = "subnet_ids"
        elif key == "vpcId":
            suggest = "vpc_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FleetNetwork. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FleetNetwork.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FleetNetwork.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 security_group_ids: Sequence[str],
                 subnet_ids: Sequence[str],
                 vpc_id: str):
        """
        :param Sequence[str] security_group_ids: A list of security group IDs associated with access to the provided subnets.
               
               **identity_provider** requires the following:
               
               > **NOTE:** `identity_provider` cannot be removed without force recreating.
        :param Sequence[str] subnet_ids: A list of subnet IDs used for X-ENI connections from Amazon WorkLink rendering containers.
        :param str vpc_id: The VPC ID with connectivity to associated websites.
        """
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[str]:
        """
        A list of security group IDs associated with access to the provided subnets.

        **identity_provider** requires the following:

        > **NOTE:** `identity_provider` cannot be removed without force recreating.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        A list of subnet IDs used for X-ENI connections from Amazon WorkLink rendering containers.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The VPC ID with connectivity to associated websites.
        """
        return pulumi.get(self, "vpc_id")


