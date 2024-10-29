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
    'ResourceSetResourceArgs',
    'ResourceSetResourceArgsDict',
    'ResourceSetResourceDnsTargetResourceArgs',
    'ResourceSetResourceDnsTargetResourceArgsDict',
    'ResourceSetResourceDnsTargetResourceTargetResourceArgs',
    'ResourceSetResourceDnsTargetResourceTargetResourceArgsDict',
    'ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgs',
    'ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgsDict',
    'ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgs',
    'ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgsDict',
]

MYPY = False

if not MYPY:
    class ResourceSetResourceArgsDict(TypedDict):
        component_id: NotRequired[pulumi.Input[str]]
        dns_target_resource: NotRequired[pulumi.Input['ResourceSetResourceDnsTargetResourceArgsDict']]
        """
        Component for DNS/Routing Control Readiness Checks.
        """
        readiness_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        Recovery group ARN or cell ARN that contains this resource set.
        """
        resource_arn: NotRequired[pulumi.Input[str]]
        """
        ARN of the resource.
        """
elif False:
    ResourceSetResourceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ResourceSetResourceArgs:
    def __init__(__self__, *,
                 component_id: Optional[pulumi.Input[str]] = None,
                 dns_target_resource: Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceArgs']] = None,
                 readiness_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['ResourceSetResourceDnsTargetResourceArgs'] dns_target_resource: Component for DNS/Routing Control Readiness Checks.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] readiness_scopes: Recovery group ARN or cell ARN that contains this resource set.
        :param pulumi.Input[str] resource_arn: ARN of the resource.
        """
        if component_id is not None:
            pulumi.set(__self__, "component_id", component_id)
        if dns_target_resource is not None:
            pulumi.set(__self__, "dns_target_resource", dns_target_resource)
        if readiness_scopes is not None:
            pulumi.set(__self__, "readiness_scopes", readiness_scopes)
        if resource_arn is not None:
            pulumi.set(__self__, "resource_arn", resource_arn)

    @property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "component_id")

    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "component_id", value)

    @property
    @pulumi.getter(name="dnsTargetResource")
    def dns_target_resource(self) -> Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceArgs']]:
        """
        Component for DNS/Routing Control Readiness Checks.
        """
        return pulumi.get(self, "dns_target_resource")

    @dns_target_resource.setter
    def dns_target_resource(self, value: Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceArgs']]):
        pulumi.set(self, "dns_target_resource", value)

    @property
    @pulumi.getter(name="readinessScopes")
    def readiness_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Recovery group ARN or cell ARN that contains this resource set.
        """
        return pulumi.get(self, "readiness_scopes")

    @readiness_scopes.setter
    def readiness_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "readiness_scopes", value)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the resource.
        """
        return pulumi.get(self, "resource_arn")

    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_arn", value)


if not MYPY:
    class ResourceSetResourceDnsTargetResourceArgsDict(TypedDict):
        domain_name: pulumi.Input[str]
        """
        DNS Name that acts as the ingress point to a portion of application.
        """
        hosted_zone_arn: NotRequired[pulumi.Input[str]]
        """
        Hosted Zone ARN that contains the DNS record with the provided name of target resource.
        """
        record_set_id: NotRequired[pulumi.Input[str]]
        """
        Route53 record set id to uniquely identify a record given a `domain_name` and a `record_type`.
        """
        record_type: NotRequired[pulumi.Input[str]]
        """
        Type of DNS Record of target resource.
        """
        target_resource: NotRequired[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceArgsDict']]
        """
        Target resource the R53 record specified with the above params points to.
        """
elif False:
    ResourceSetResourceDnsTargetResourceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ResourceSetResourceDnsTargetResourceArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 hosted_zone_arn: Optional[pulumi.Input[str]] = None,
                 record_set_id: Optional[pulumi.Input[str]] = None,
                 record_type: Optional[pulumi.Input[str]] = None,
                 target_resource: Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceArgs']] = None):
        """
        :param pulumi.Input[str] domain_name: DNS Name that acts as the ingress point to a portion of application.
        :param pulumi.Input[str] hosted_zone_arn: Hosted Zone ARN that contains the DNS record with the provided name of target resource.
        :param pulumi.Input[str] record_set_id: Route53 record set id to uniquely identify a record given a `domain_name` and a `record_type`.
        :param pulumi.Input[str] record_type: Type of DNS Record of target resource.
        :param pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceArgs'] target_resource: Target resource the R53 record specified with the above params points to.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        if hosted_zone_arn is not None:
            pulumi.set(__self__, "hosted_zone_arn", hosted_zone_arn)
        if record_set_id is not None:
            pulumi.set(__self__, "record_set_id", record_set_id)
        if record_type is not None:
            pulumi.set(__self__, "record_type", record_type)
        if target_resource is not None:
            pulumi.set(__self__, "target_resource", target_resource)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        DNS Name that acts as the ingress point to a portion of application.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="hostedZoneArn")
    def hosted_zone_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Hosted Zone ARN that contains the DNS record with the provided name of target resource.
        """
        return pulumi.get(self, "hosted_zone_arn")

    @hosted_zone_arn.setter
    def hosted_zone_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hosted_zone_arn", value)

    @property
    @pulumi.getter(name="recordSetId")
    def record_set_id(self) -> Optional[pulumi.Input[str]]:
        """
        Route53 record set id to uniquely identify a record given a `domain_name` and a `record_type`.
        """
        return pulumi.get(self, "record_set_id")

    @record_set_id.setter
    def record_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "record_set_id", value)

    @property
    @pulumi.getter(name="recordType")
    def record_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of DNS Record of target resource.
        """
        return pulumi.get(self, "record_type")

    @record_type.setter
    def record_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "record_type", value)

    @property
    @pulumi.getter(name="targetResource")
    def target_resource(self) -> Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceArgs']]:
        """
        Target resource the R53 record specified with the above params points to.
        """
        return pulumi.get(self, "target_resource")

    @target_resource.setter
    def target_resource(self, value: Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceArgs']]):
        pulumi.set(self, "target_resource", value)


if not MYPY:
    class ResourceSetResourceDnsTargetResourceTargetResourceArgsDict(TypedDict):
        nlb_resource: NotRequired[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgsDict']]
        """
        NLB resource a DNS Target Resource points to. Required if `r53_resource` is not set.
        """
        r53_resource: NotRequired[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgsDict']]
        """
        Route53 resource a DNS Target Resource record points to.
        """
elif False:
    ResourceSetResourceDnsTargetResourceTargetResourceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ResourceSetResourceDnsTargetResourceTargetResourceArgs:
    def __init__(__self__, *,
                 nlb_resource: Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgs']] = None,
                 r53_resource: Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgs']] = None):
        """
        :param pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgs'] nlb_resource: NLB resource a DNS Target Resource points to. Required if `r53_resource` is not set.
        :param pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgs'] r53_resource: Route53 resource a DNS Target Resource record points to.
        """
        if nlb_resource is not None:
            pulumi.set(__self__, "nlb_resource", nlb_resource)
        if r53_resource is not None:
            pulumi.set(__self__, "r53_resource", r53_resource)

    @property
    @pulumi.getter(name="nlbResource")
    def nlb_resource(self) -> Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgs']]:
        """
        NLB resource a DNS Target Resource points to. Required if `r53_resource` is not set.
        """
        return pulumi.get(self, "nlb_resource")

    @nlb_resource.setter
    def nlb_resource(self, value: Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgs']]):
        pulumi.set(self, "nlb_resource", value)

    @property
    @pulumi.getter(name="r53Resource")
    def r53_resource(self) -> Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgs']]:
        """
        Route53 resource a DNS Target Resource record points to.
        """
        return pulumi.get(self, "r53_resource")

    @r53_resource.setter
    def r53_resource(self, value: Optional[pulumi.Input['ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgs']]):
        pulumi.set(self, "r53_resource", value)


if not MYPY:
    class ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgsDict(TypedDict):
        arn: NotRequired[pulumi.Input[str]]
        """
        NLB resource ARN.
        """
elif False:
    ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgs:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] arn: NLB resource ARN.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        NLB resource ARN.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)


if not MYPY:
    class ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgsDict(TypedDict):
        domain_name: NotRequired[pulumi.Input[str]]
        """
        Domain name that is targeted.
        """
        record_set_id: NotRequired[pulumi.Input[str]]
        """
        Resource record set ID that is targeted.
        """
elif False:
    ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgs:
    def __init__(__self__, *,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 record_set_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] domain_name: Domain name that is targeted.
        :param pulumi.Input[str] record_set_id: Resource record set ID that is targeted.
        """
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if record_set_id is not None:
            pulumi.set(__self__, "record_set_id", record_set_id)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Domain name that is targeted.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="recordSetId")
    def record_set_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource record set ID that is targeted.
        """
        return pulumi.get(self, "record_set_id")

    @record_set_id.setter
    def record_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "record_set_id", value)


