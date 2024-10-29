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
    'GetDomainResult',
    'AwaitableGetDomainResult',
    'get_domain',
    'get_domain_output',
]

@pulumi.output_type
class GetDomainResult:
    """
    A collection of values returned by getDomain.
    """
    def __init__(__self__, access_policies=None, advanced_options=None, advanced_security_options=None, arn=None, auto_tune_options=None, cluster_configs=None, cognito_options=None, created=None, dashboard_endpoint=None, dashboard_endpoint_v2=None, deleted=None, domain_endpoint_v2_hosted_zone_id=None, domain_id=None, domain_name=None, ebs_options=None, encryption_at_rests=None, endpoint=None, endpoint_v2=None, engine_version=None, id=None, ip_address_type=None, kibana_endpoint=None, log_publishing_options=None, node_to_node_encryptions=None, off_peak_window_options=None, processing=None, snapshot_options=None, software_update_options=None, tags=None, vpc_options=None):
        if access_policies and not isinstance(access_policies, str):
            raise TypeError("Expected argument 'access_policies' to be a str")
        pulumi.set(__self__, "access_policies", access_policies)
        if advanced_options and not isinstance(advanced_options, dict):
            raise TypeError("Expected argument 'advanced_options' to be a dict")
        pulumi.set(__self__, "advanced_options", advanced_options)
        if advanced_security_options and not isinstance(advanced_security_options, list):
            raise TypeError("Expected argument 'advanced_security_options' to be a list")
        pulumi.set(__self__, "advanced_security_options", advanced_security_options)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if auto_tune_options and not isinstance(auto_tune_options, list):
            raise TypeError("Expected argument 'auto_tune_options' to be a list")
        pulumi.set(__self__, "auto_tune_options", auto_tune_options)
        if cluster_configs and not isinstance(cluster_configs, list):
            raise TypeError("Expected argument 'cluster_configs' to be a list")
        pulumi.set(__self__, "cluster_configs", cluster_configs)
        if cognito_options and not isinstance(cognito_options, list):
            raise TypeError("Expected argument 'cognito_options' to be a list")
        pulumi.set(__self__, "cognito_options", cognito_options)
        if created and not isinstance(created, bool):
            raise TypeError("Expected argument 'created' to be a bool")
        pulumi.set(__self__, "created", created)
        if dashboard_endpoint and not isinstance(dashboard_endpoint, str):
            raise TypeError("Expected argument 'dashboard_endpoint' to be a str")
        pulumi.set(__self__, "dashboard_endpoint", dashboard_endpoint)
        if dashboard_endpoint_v2 and not isinstance(dashboard_endpoint_v2, str):
            raise TypeError("Expected argument 'dashboard_endpoint_v2' to be a str")
        pulumi.set(__self__, "dashboard_endpoint_v2", dashboard_endpoint_v2)
        if deleted and not isinstance(deleted, bool):
            raise TypeError("Expected argument 'deleted' to be a bool")
        pulumi.set(__self__, "deleted", deleted)
        if domain_endpoint_v2_hosted_zone_id and not isinstance(domain_endpoint_v2_hosted_zone_id, str):
            raise TypeError("Expected argument 'domain_endpoint_v2_hosted_zone_id' to be a str")
        pulumi.set(__self__, "domain_endpoint_v2_hosted_zone_id", domain_endpoint_v2_hosted_zone_id)
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        pulumi.set(__self__, "domain_id", domain_id)
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if ebs_options and not isinstance(ebs_options, list):
            raise TypeError("Expected argument 'ebs_options' to be a list")
        pulumi.set(__self__, "ebs_options", ebs_options)
        if encryption_at_rests and not isinstance(encryption_at_rests, list):
            raise TypeError("Expected argument 'encryption_at_rests' to be a list")
        pulumi.set(__self__, "encryption_at_rests", encryption_at_rests)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if endpoint_v2 and not isinstance(endpoint_v2, str):
            raise TypeError("Expected argument 'endpoint_v2' to be a str")
        pulumi.set(__self__, "endpoint_v2", endpoint_v2)
        if engine_version and not isinstance(engine_version, str):
            raise TypeError("Expected argument 'engine_version' to be a str")
        pulumi.set(__self__, "engine_version", engine_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address_type and not isinstance(ip_address_type, str):
            raise TypeError("Expected argument 'ip_address_type' to be a str")
        pulumi.set(__self__, "ip_address_type", ip_address_type)
        if kibana_endpoint and not isinstance(kibana_endpoint, str):
            raise TypeError("Expected argument 'kibana_endpoint' to be a str")
        pulumi.set(__self__, "kibana_endpoint", kibana_endpoint)
        if log_publishing_options and not isinstance(log_publishing_options, list):
            raise TypeError("Expected argument 'log_publishing_options' to be a list")
        pulumi.set(__self__, "log_publishing_options", log_publishing_options)
        if node_to_node_encryptions and not isinstance(node_to_node_encryptions, list):
            raise TypeError("Expected argument 'node_to_node_encryptions' to be a list")
        pulumi.set(__self__, "node_to_node_encryptions", node_to_node_encryptions)
        if off_peak_window_options and not isinstance(off_peak_window_options, dict):
            raise TypeError("Expected argument 'off_peak_window_options' to be a dict")
        pulumi.set(__self__, "off_peak_window_options", off_peak_window_options)
        if processing and not isinstance(processing, bool):
            raise TypeError("Expected argument 'processing' to be a bool")
        pulumi.set(__self__, "processing", processing)
        if snapshot_options and not isinstance(snapshot_options, list):
            raise TypeError("Expected argument 'snapshot_options' to be a list")
        pulumi.set(__self__, "snapshot_options", snapshot_options)
        if software_update_options and not isinstance(software_update_options, list):
            raise TypeError("Expected argument 'software_update_options' to be a list")
        pulumi.set(__self__, "software_update_options", software_update_options)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if vpc_options and not isinstance(vpc_options, list):
            raise TypeError("Expected argument 'vpc_options' to be a list")
        pulumi.set(__self__, "vpc_options", vpc_options)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> str:
        """
        Policy document attached to the domain.
        """
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> Mapping[str, str]:
        """
        Key-value string pairs to specify advanced configuration options.
        """
        return pulumi.get(self, "advanced_options")

    @property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> Sequence['outputs.GetDomainAdvancedSecurityOptionResult']:
        """
        Status of the OpenSearch domain's advanced security options. The block consists of the following attributes:
        """
        return pulumi.get(self, "advanced_security_options")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the domain.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoTuneOptions")
    def auto_tune_options(self) -> Sequence['outputs.GetDomainAutoTuneOptionResult']:
        """
        Configuration of the Auto-Tune options of the domain.
        """
        return pulumi.get(self, "auto_tune_options")

    @property
    @pulumi.getter(name="clusterConfigs")
    def cluster_configs(self) -> Sequence['outputs.GetDomainClusterConfigResult']:
        """
        Cluster configuration of the domain.
        """
        return pulumi.get(self, "cluster_configs")

    @property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> Sequence['outputs.GetDomainCognitoOptionResult']:
        """
        Domain Amazon Cognito Authentication options for Dashboard.
        """
        return pulumi.get(self, "cognito_options")

    @property
    @pulumi.getter
    def created(self) -> bool:
        """
        Status of the creation of the domain.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="dashboardEndpoint")
    def dashboard_endpoint(self) -> str:
        """
        Domain-specific endpoint used to access the [Dashboard application](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html).
        """
        return pulumi.get(self, "dashboard_endpoint")

    @property
    @pulumi.getter(name="dashboardEndpointV2")
    def dashboard_endpoint_v2(self) -> str:
        """
        V2 domain-specific endpoint used to access the [Dashboard application](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html)
        """
        return pulumi.get(self, "dashboard_endpoint_v2")

    @property
    @pulumi.getter
    def deleted(self) -> bool:
        """
        Status of the deletion of the domain.
        """
        return pulumi.get(self, "deleted")

    @property
    @pulumi.getter(name="domainEndpointV2HostedZoneId")
    def domain_endpoint_v2_hosted_zone_id(self) -> str:
        """
        Dual stack hosted zone ID for the domain.
        """
        return pulumi.get(self, "domain_endpoint_v2_hosted_zone_id")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> str:
        """
        Unique identifier for the domain.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> str:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="ebsOptions")
    def ebs_options(self) -> Sequence['outputs.GetDomainEbsOptionResult']:
        """
        EBS Options for the instances in the domain.
        """
        return pulumi.get(self, "ebs_options")

    @property
    @pulumi.getter(name="encryptionAtRests")
    def encryption_at_rests(self) -> Sequence['outputs.GetDomainEncryptionAtRestResult']:
        """
        Domain encryption at rest related options.
        """
        return pulumi.get(self, "encryption_at_rests")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        Domain-specific endpoint used to submit index, search, and data upload requests.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="endpointV2")
    def endpoint_v2(self) -> str:
        """
        V2 domain-specific endpoint that works with both IPv4 and IPv6 addresses, used to submit index, search, and data upload requests.
        """
        return pulumi.get(self, "endpoint_v2")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        """
        OpenSearch version for the domain.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> str:
        """
        Type of IP addresses supported by the endpoint for the domain.
        """
        return pulumi.get(self, "ip_address_type")

    @property
    @pulumi.getter(name="kibanaEndpoint")
    @_utilities.deprecated("""use 'dashboard_endpoint' attribute instead""")
    def kibana_endpoint(self) -> str:
        """
        (**Deprecated**) Domain-specific endpoint for kibana without https scheme. Use the `dashboard_endpoint` attribute instead.
        """
        return pulumi.get(self, "kibana_endpoint")

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Sequence['outputs.GetDomainLogPublishingOptionResult']:
        """
        Domain log publishing related options.
        """
        return pulumi.get(self, "log_publishing_options")

    @property
    @pulumi.getter(name="nodeToNodeEncryptions")
    def node_to_node_encryptions(self) -> Sequence['outputs.GetDomainNodeToNodeEncryptionResult']:
        """
        Domain in transit encryption related options.
        """
        return pulumi.get(self, "node_to_node_encryptions")

    @property
    @pulumi.getter(name="offPeakWindowOptions")
    def off_peak_window_options(self) -> Optional['outputs.GetDomainOffPeakWindowOptionsResult']:
        """
        Off Peak update options
        """
        return pulumi.get(self, "off_peak_window_options")

    @property
    @pulumi.getter
    def processing(self) -> bool:
        """
        Status of a configuration change in the domain.
        """
        return pulumi.get(self, "processing")

    @property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> Sequence['outputs.GetDomainSnapshotOptionResult']:
        """
        Domain snapshot related options.
        """
        return pulumi.get(self, "snapshot_options")

    @property
    @pulumi.getter(name="softwareUpdateOptions")
    def software_update_options(self) -> Sequence['outputs.GetDomainSoftwareUpdateOptionResult']:
        """
        Software update options for the domain
        """
        return pulumi.get(self, "software_update_options")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Tags assigned to the domain.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Sequence['outputs.GetDomainVpcOptionResult']:
        """
        VPC Options for private OpenSearch domains.
        """
        return pulumi.get(self, "vpc_options")


class AwaitableGetDomainResult(GetDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainResult(
            access_policies=self.access_policies,
            advanced_options=self.advanced_options,
            advanced_security_options=self.advanced_security_options,
            arn=self.arn,
            auto_tune_options=self.auto_tune_options,
            cluster_configs=self.cluster_configs,
            cognito_options=self.cognito_options,
            created=self.created,
            dashboard_endpoint=self.dashboard_endpoint,
            dashboard_endpoint_v2=self.dashboard_endpoint_v2,
            deleted=self.deleted,
            domain_endpoint_v2_hosted_zone_id=self.domain_endpoint_v2_hosted_zone_id,
            domain_id=self.domain_id,
            domain_name=self.domain_name,
            ebs_options=self.ebs_options,
            encryption_at_rests=self.encryption_at_rests,
            endpoint=self.endpoint,
            endpoint_v2=self.endpoint_v2,
            engine_version=self.engine_version,
            id=self.id,
            ip_address_type=self.ip_address_type,
            kibana_endpoint=self.kibana_endpoint,
            log_publishing_options=self.log_publishing_options,
            node_to_node_encryptions=self.node_to_node_encryptions,
            off_peak_window_options=self.off_peak_window_options,
            processing=self.processing,
            snapshot_options=self.snapshot_options,
            software_update_options=self.software_update_options,
            tags=self.tags,
            vpc_options=self.vpc_options)


def get_domain(domain_name: Optional[str] = None,
               off_peak_window_options: Optional[Union['GetDomainOffPeakWindowOptionsArgs', 'GetDomainOffPeakWindowOptionsArgsDict']] = None,
               tags: Optional[Mapping[str, str]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainResult:
    """
    Use this data source to get information about an OpenSearch Domain

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    my_domain = aws.opensearch.get_domain(domain_name="my-domain-name")
    ```


    :param str domain_name: Name of the domain.
    :param Union['GetDomainOffPeakWindowOptionsArgs', 'GetDomainOffPeakWindowOptionsArgsDict'] off_peak_window_options: Off Peak update options
    :param Mapping[str, str] tags: Tags assigned to the domain.
    """
    __args__ = dict()
    __args__['domainName'] = domain_name
    __args__['offPeakWindowOptions'] = off_peak_window_options
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:opensearch/getDomain:getDomain', __args__, opts=opts, typ=GetDomainResult).value

    return AwaitableGetDomainResult(
        access_policies=pulumi.get(__ret__, 'access_policies'),
        advanced_options=pulumi.get(__ret__, 'advanced_options'),
        advanced_security_options=pulumi.get(__ret__, 'advanced_security_options'),
        arn=pulumi.get(__ret__, 'arn'),
        auto_tune_options=pulumi.get(__ret__, 'auto_tune_options'),
        cluster_configs=pulumi.get(__ret__, 'cluster_configs'),
        cognito_options=pulumi.get(__ret__, 'cognito_options'),
        created=pulumi.get(__ret__, 'created'),
        dashboard_endpoint=pulumi.get(__ret__, 'dashboard_endpoint'),
        dashboard_endpoint_v2=pulumi.get(__ret__, 'dashboard_endpoint_v2'),
        deleted=pulumi.get(__ret__, 'deleted'),
        domain_endpoint_v2_hosted_zone_id=pulumi.get(__ret__, 'domain_endpoint_v2_hosted_zone_id'),
        domain_id=pulumi.get(__ret__, 'domain_id'),
        domain_name=pulumi.get(__ret__, 'domain_name'),
        ebs_options=pulumi.get(__ret__, 'ebs_options'),
        encryption_at_rests=pulumi.get(__ret__, 'encryption_at_rests'),
        endpoint=pulumi.get(__ret__, 'endpoint'),
        endpoint_v2=pulumi.get(__ret__, 'endpoint_v2'),
        engine_version=pulumi.get(__ret__, 'engine_version'),
        id=pulumi.get(__ret__, 'id'),
        ip_address_type=pulumi.get(__ret__, 'ip_address_type'),
        kibana_endpoint=pulumi.get(__ret__, 'kibana_endpoint'),
        log_publishing_options=pulumi.get(__ret__, 'log_publishing_options'),
        node_to_node_encryptions=pulumi.get(__ret__, 'node_to_node_encryptions'),
        off_peak_window_options=pulumi.get(__ret__, 'off_peak_window_options'),
        processing=pulumi.get(__ret__, 'processing'),
        snapshot_options=pulumi.get(__ret__, 'snapshot_options'),
        software_update_options=pulumi.get(__ret__, 'software_update_options'),
        tags=pulumi.get(__ret__, 'tags'),
        vpc_options=pulumi.get(__ret__, 'vpc_options'))
def get_domain_output(domain_name: Optional[pulumi.Input[str]] = None,
                      off_peak_window_options: Optional[pulumi.Input[Optional[Union['GetDomainOffPeakWindowOptionsArgs', 'GetDomainOffPeakWindowOptionsArgsDict']]]] = None,
                      tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainResult]:
    """
    Use this data source to get information about an OpenSearch Domain

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    my_domain = aws.opensearch.get_domain(domain_name="my-domain-name")
    ```


    :param str domain_name: Name of the domain.
    :param Union['GetDomainOffPeakWindowOptionsArgs', 'GetDomainOffPeakWindowOptionsArgsDict'] off_peak_window_options: Off Peak update options
    :param Mapping[str, str] tags: Tags assigned to the domain.
    """
    __args__ = dict()
    __args__['domainName'] = domain_name
    __args__['offPeakWindowOptions'] = off_peak_window_options
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:opensearch/getDomain:getDomain', __args__, opts=opts, typ=GetDomainResult)
    return __ret__.apply(lambda __response__: GetDomainResult(
        access_policies=pulumi.get(__response__, 'access_policies'),
        advanced_options=pulumi.get(__response__, 'advanced_options'),
        advanced_security_options=pulumi.get(__response__, 'advanced_security_options'),
        arn=pulumi.get(__response__, 'arn'),
        auto_tune_options=pulumi.get(__response__, 'auto_tune_options'),
        cluster_configs=pulumi.get(__response__, 'cluster_configs'),
        cognito_options=pulumi.get(__response__, 'cognito_options'),
        created=pulumi.get(__response__, 'created'),
        dashboard_endpoint=pulumi.get(__response__, 'dashboard_endpoint'),
        dashboard_endpoint_v2=pulumi.get(__response__, 'dashboard_endpoint_v2'),
        deleted=pulumi.get(__response__, 'deleted'),
        domain_endpoint_v2_hosted_zone_id=pulumi.get(__response__, 'domain_endpoint_v2_hosted_zone_id'),
        domain_id=pulumi.get(__response__, 'domain_id'),
        domain_name=pulumi.get(__response__, 'domain_name'),
        ebs_options=pulumi.get(__response__, 'ebs_options'),
        encryption_at_rests=pulumi.get(__response__, 'encryption_at_rests'),
        endpoint=pulumi.get(__response__, 'endpoint'),
        endpoint_v2=pulumi.get(__response__, 'endpoint_v2'),
        engine_version=pulumi.get(__response__, 'engine_version'),
        id=pulumi.get(__response__, 'id'),
        ip_address_type=pulumi.get(__response__, 'ip_address_type'),
        kibana_endpoint=pulumi.get(__response__, 'kibana_endpoint'),
        log_publishing_options=pulumi.get(__response__, 'log_publishing_options'),
        node_to_node_encryptions=pulumi.get(__response__, 'node_to_node_encryptions'),
        off_peak_window_options=pulumi.get(__response__, 'off_peak_window_options'),
        processing=pulumi.get(__response__, 'processing'),
        snapshot_options=pulumi.get(__response__, 'snapshot_options'),
        software_update_options=pulumi.get(__response__, 'software_update_options'),
        tags=pulumi.get(__response__, 'tags'),
        vpc_options=pulumi.get(__response__, 'vpc_options')))
