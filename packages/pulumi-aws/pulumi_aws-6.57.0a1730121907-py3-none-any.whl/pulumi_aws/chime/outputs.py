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
    'SdkvoiceGlobalSettingsVoiceConnector',
    'SdkvoiceSipMediaApplicationEndpoints',
    'SdkvoiceSipRuleTargetApplication',
    'SdkvoiceVoiceProfileDomainServerSideEncryptionConfiguration',
    'VoiceConnectorGroupConnector',
    'VoiceConnectorOrganizationRoute',
    'VoiceConnectorStreamingMediaInsightsConfiguration',
    'VoiceConnectorTerminationCredentialsCredential',
]

@pulumi.output_type
class SdkvoiceGlobalSettingsVoiceConnector(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cdrBucket":
            suggest = "cdr_bucket"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SdkvoiceGlobalSettingsVoiceConnector. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SdkvoiceGlobalSettingsVoiceConnector.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SdkvoiceGlobalSettingsVoiceConnector.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cdr_bucket: Optional[str] = None):
        """
        :param str cdr_bucket: The S3 bucket that stores the Voice Connector's call detail records.
        """
        if cdr_bucket is not None:
            pulumi.set(__self__, "cdr_bucket", cdr_bucket)

    @property
    @pulumi.getter(name="cdrBucket")
    def cdr_bucket(self) -> Optional[str]:
        """
        The S3 bucket that stores the Voice Connector's call detail records.
        """
        return pulumi.get(self, "cdr_bucket")


@pulumi.output_type
class SdkvoiceSipMediaApplicationEndpoints(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lambdaArn":
            suggest = "lambda_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SdkvoiceSipMediaApplicationEndpoints. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SdkvoiceSipMediaApplicationEndpoints.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SdkvoiceSipMediaApplicationEndpoints.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 lambda_arn: str):
        """
        :param str lambda_arn: Valid Amazon Resource Name (ARN) of the Lambda function, version, or alias. The function must be created in the same AWS Region as the SIP media application.
        """
        pulumi.set(__self__, "lambda_arn", lambda_arn)

    @property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> str:
        """
        Valid Amazon Resource Name (ARN) of the Lambda function, version, or alias. The function must be created in the same AWS Region as the SIP media application.
        """
        return pulumi.get(self, "lambda_arn")


@pulumi.output_type
class SdkvoiceSipRuleTargetApplication(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "awsRegion":
            suggest = "aws_region"
        elif key == "sipMediaApplicationId":
            suggest = "sip_media_application_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SdkvoiceSipRuleTargetApplication. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SdkvoiceSipRuleTargetApplication.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SdkvoiceSipRuleTargetApplication.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 aws_region: str,
                 priority: int,
                 sip_media_application_id: str):
        """
        :param str aws_region: The AWS Region of the target application.
        :param int priority: Priority of the SIP media application in the target list.
        :param str sip_media_application_id: The SIP media application ID.
        """
        pulumi.set(__self__, "aws_region", aws_region)
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "sip_media_application_id", sip_media_application_id)

    @property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> str:
        """
        The AWS Region of the target application.
        """
        return pulumi.get(self, "aws_region")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        Priority of the SIP media application in the target list.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="sipMediaApplicationId")
    def sip_media_application_id(self) -> str:
        """
        The SIP media application ID.
        """
        return pulumi.get(self, "sip_media_application_id")


@pulumi.output_type
class SdkvoiceVoiceProfileDomainServerSideEncryptionConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsKeyArn":
            suggest = "kms_key_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SdkvoiceVoiceProfileDomainServerSideEncryptionConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SdkvoiceVoiceProfileDomainServerSideEncryptionConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SdkvoiceVoiceProfileDomainServerSideEncryptionConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_key_arn: str):
        """
        :param str kms_key_arn: ARN for KMS Key.
               
               The following arguments are optional:
        """
        pulumi.set(__self__, "kms_key_arn", kms_key_arn)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> str:
        """
        ARN for KMS Key.

        The following arguments are optional:
        """
        return pulumi.get(self, "kms_key_arn")


@pulumi.output_type
class VoiceConnectorGroupConnector(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "voiceConnectorId":
            suggest = "voice_connector_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VoiceConnectorGroupConnector. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VoiceConnectorGroupConnector.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VoiceConnectorGroupConnector.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 priority: int,
                 voice_connector_id: str):
        """
        :param int priority: The priority associated with the Amazon Chime Voice Connector, with 1 being the highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.
        :param str voice_connector_id: The Amazon Chime Voice Connector ID.
        """
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "voice_connector_id", voice_connector_id)

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        The priority associated with the Amazon Chime Voice Connector, with 1 being the highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> str:
        """
        The Amazon Chime Voice Connector ID.
        """
        return pulumi.get(self, "voice_connector_id")


@pulumi.output_type
class VoiceConnectorOrganizationRoute(dict):
    def __init__(__self__, *,
                 host: str,
                 priority: int,
                 protocol: str,
                 weight: int,
                 port: Optional[int] = None):
        """
        :param str host: The FQDN or IP address to contact for origination traffic.
        :param int priority: The priority associated with the host, with 1 being the highest priority. Higher priority hosts are attempted first.
        :param str protocol: The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice Connectors use TCP protocol by default.
        :param int weight: The weight associated with the host. If hosts are equal in priority, calls are redistributed among them based on their relative weight.
        :param int port: The designated origination route port. Defaults to `5060`.
        """
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "weight", weight)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        The FQDN or IP address to contact for origination traffic.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        The priority associated with the host, with 1 being the highest priority. Higher priority hosts are attempted first.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice Connectors use TCP protocol by default.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def weight(self) -> int:
        """
        The weight associated with the host. If hosts are equal in priority, calls are redistributed among them based on their relative weight.
        """
        return pulumi.get(self, "weight")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        The designated origination route port. Defaults to `5060`.
        """
        return pulumi.get(self, "port")


@pulumi.output_type
class VoiceConnectorStreamingMediaInsightsConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "configurationArn":
            suggest = "configuration_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VoiceConnectorStreamingMediaInsightsConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VoiceConnectorStreamingMediaInsightsConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VoiceConnectorStreamingMediaInsightsConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 configuration_arn: Optional[str] = None,
                 disabled: Optional[bool] = None):
        """
        :param str configuration_arn: The media insights configuration that will be invoked by the Voice Connector.
        :param bool disabled: When `true`, the media insights configuration is not enabled. Defaults to `false`.
        """
        if configuration_arn is not None:
            pulumi.set(__self__, "configuration_arn", configuration_arn)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)

    @property
    @pulumi.getter(name="configurationArn")
    def configuration_arn(self) -> Optional[str]:
        """
        The media insights configuration that will be invoked by the Voice Connector.
        """
        return pulumi.get(self, "configuration_arn")

    @property
    @pulumi.getter
    def disabled(self) -> Optional[bool]:
        """
        When `true`, the media insights configuration is not enabled. Defaults to `false`.
        """
        return pulumi.get(self, "disabled")


@pulumi.output_type
class VoiceConnectorTerminationCredentialsCredential(dict):
    def __init__(__self__, *,
                 password: str,
                 username: str):
        """
        :param str password: RFC2617 compliant password associated with the SIP credentials.
        :param str username: RFC2617 compliant username associated with the SIP credentials.
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        RFC2617 compliant password associated with the SIP credentials.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        RFC2617 compliant username associated with the SIP credentials.
        """
        return pulumi.get(self, "username")


