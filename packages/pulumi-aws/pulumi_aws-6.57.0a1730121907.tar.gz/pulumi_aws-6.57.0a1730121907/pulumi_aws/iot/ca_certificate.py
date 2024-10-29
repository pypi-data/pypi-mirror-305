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

__all__ = ['CaCertificateArgs', 'CaCertificate']

@pulumi.input_type
class CaCertificateArgs:
    def __init__(__self__, *,
                 active: pulumi.Input[bool],
                 allow_auto_registration: pulumi.Input[bool],
                 ca_certificate_pem: pulumi.Input[str],
                 certificate_mode: Optional[pulumi.Input[str]] = None,
                 registration_config: Optional[pulumi.Input['CaCertificateRegistrationConfigArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 verification_certificate_pem: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CaCertificate resource.
        :param pulumi.Input[bool] active: Boolean flag to indicate if the certificate should be active for device authentication.
        :param pulumi.Input[bool] allow_auto_registration: Boolean flag to indicate if the certificate should be active for device regisration.
        :param pulumi.Input[str] ca_certificate_pem: PEM encoded CA certificate.
        :param pulumi.Input[str] certificate_mode: The certificate mode in which the CA will be registered. Valida values: `DEFAULT` and `SNI_ONLY`. Default: `DEFAULT`.
        :param pulumi.Input['CaCertificateRegistrationConfigArgs'] registration_config: Information about the registration configuration. See below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] verification_certificate_pem: PEM encoded verification certificate containing the common name of a registration code. Review
               [CreateVerificationCSR](https://docs.aws.amazon.com/iot/latest/developerguide/register-CA-cert.html). Reuired if `certificate_mode` is `DEFAULT`.
        """
        pulumi.set(__self__, "active", active)
        pulumi.set(__self__, "allow_auto_registration", allow_auto_registration)
        pulumi.set(__self__, "ca_certificate_pem", ca_certificate_pem)
        if certificate_mode is not None:
            pulumi.set(__self__, "certificate_mode", certificate_mode)
        if registration_config is not None:
            pulumi.set(__self__, "registration_config", registration_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if verification_certificate_pem is not None:
            pulumi.set(__self__, "verification_certificate_pem", verification_certificate_pem)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Input[bool]:
        """
        Boolean flag to indicate if the certificate should be active for device authentication.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: pulumi.Input[bool]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter(name="allowAutoRegistration")
    def allow_auto_registration(self) -> pulumi.Input[bool]:
        """
        Boolean flag to indicate if the certificate should be active for device regisration.
        """
        return pulumi.get(self, "allow_auto_registration")

    @allow_auto_registration.setter
    def allow_auto_registration(self, value: pulumi.Input[bool]):
        pulumi.set(self, "allow_auto_registration", value)

    @property
    @pulumi.getter(name="caCertificatePem")
    def ca_certificate_pem(self) -> pulumi.Input[str]:
        """
        PEM encoded CA certificate.
        """
        return pulumi.get(self, "ca_certificate_pem")

    @ca_certificate_pem.setter
    def ca_certificate_pem(self, value: pulumi.Input[str]):
        pulumi.set(self, "ca_certificate_pem", value)

    @property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The certificate mode in which the CA will be registered. Valida values: `DEFAULT` and `SNI_ONLY`. Default: `DEFAULT`.
        """
        return pulumi.get(self, "certificate_mode")

    @certificate_mode.setter
    def certificate_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_mode", value)

    @property
    @pulumi.getter(name="registrationConfig")
    def registration_config(self) -> Optional[pulumi.Input['CaCertificateRegistrationConfigArgs']]:
        """
        Information about the registration configuration. See below.
        """
        return pulumi.get(self, "registration_config")

    @registration_config.setter
    def registration_config(self, value: Optional[pulumi.Input['CaCertificateRegistrationConfigArgs']]):
        pulumi.set(self, "registration_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="verificationCertificatePem")
    def verification_certificate_pem(self) -> Optional[pulumi.Input[str]]:
        """
        PEM encoded verification certificate containing the common name of a registration code. Review
        [CreateVerificationCSR](https://docs.aws.amazon.com/iot/latest/developerguide/register-CA-cert.html). Reuired if `certificate_mode` is `DEFAULT`.
        """
        return pulumi.get(self, "verification_certificate_pem")

    @verification_certificate_pem.setter
    def verification_certificate_pem(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "verification_certificate_pem", value)


@pulumi.input_type
class _CaCertificateState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 allow_auto_registration: Optional[pulumi.Input[bool]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 ca_certificate_pem: Optional[pulumi.Input[str]] = None,
                 certificate_mode: Optional[pulumi.Input[str]] = None,
                 customer_version: Optional[pulumi.Input[int]] = None,
                 generation_id: Optional[pulumi.Input[str]] = None,
                 registration_config: Optional[pulumi.Input['CaCertificateRegistrationConfigArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validities: Optional[pulumi.Input[Sequence[pulumi.Input['CaCertificateValidityArgs']]]] = None,
                 verification_certificate_pem: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CaCertificate resources.
        :param pulumi.Input[bool] active: Boolean flag to indicate if the certificate should be active for device authentication.
        :param pulumi.Input[bool] allow_auto_registration: Boolean flag to indicate if the certificate should be active for device regisration.
        :param pulumi.Input[str] arn: The ARN of the created CA certificate.
        :param pulumi.Input[str] ca_certificate_pem: PEM encoded CA certificate.
        :param pulumi.Input[str] certificate_mode: The certificate mode in which the CA will be registered. Valida values: `DEFAULT` and `SNI_ONLY`. Default: `DEFAULT`.
        :param pulumi.Input[int] customer_version: The customer version of the CA certificate.
        :param pulumi.Input[str] generation_id: The generation ID of the CA certificate.
        :param pulumi.Input['CaCertificateRegistrationConfigArgs'] registration_config: Information about the registration configuration. See below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[Sequence[pulumi.Input['CaCertificateValidityArgs']]] validities: When the CA certificate is valid.
        :param pulumi.Input[str] verification_certificate_pem: PEM encoded verification certificate containing the common name of a registration code. Review
               [CreateVerificationCSR](https://docs.aws.amazon.com/iot/latest/developerguide/register-CA-cert.html). Reuired if `certificate_mode` is `DEFAULT`.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if allow_auto_registration is not None:
            pulumi.set(__self__, "allow_auto_registration", allow_auto_registration)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if ca_certificate_pem is not None:
            pulumi.set(__self__, "ca_certificate_pem", ca_certificate_pem)
        if certificate_mode is not None:
            pulumi.set(__self__, "certificate_mode", certificate_mode)
        if customer_version is not None:
            pulumi.set(__self__, "customer_version", customer_version)
        if generation_id is not None:
            pulumi.set(__self__, "generation_id", generation_id)
        if registration_config is not None:
            pulumi.set(__self__, "registration_config", registration_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if validities is not None:
            pulumi.set(__self__, "validities", validities)
        if verification_certificate_pem is not None:
            pulumi.set(__self__, "verification_certificate_pem", verification_certificate_pem)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean flag to indicate if the certificate should be active for device authentication.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter(name="allowAutoRegistration")
    def allow_auto_registration(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean flag to indicate if the certificate should be active for device regisration.
        """
        return pulumi.get(self, "allow_auto_registration")

    @allow_auto_registration.setter
    def allow_auto_registration(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_auto_registration", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the created CA certificate.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="caCertificatePem")
    def ca_certificate_pem(self) -> Optional[pulumi.Input[str]]:
        """
        PEM encoded CA certificate.
        """
        return pulumi.get(self, "ca_certificate_pem")

    @ca_certificate_pem.setter
    def ca_certificate_pem(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_certificate_pem", value)

    @property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The certificate mode in which the CA will be registered. Valida values: `DEFAULT` and `SNI_ONLY`. Default: `DEFAULT`.
        """
        return pulumi.get(self, "certificate_mode")

    @certificate_mode.setter
    def certificate_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_mode", value)

    @property
    @pulumi.getter(name="customerVersion")
    def customer_version(self) -> Optional[pulumi.Input[int]]:
        """
        The customer version of the CA certificate.
        """
        return pulumi.get(self, "customer_version")

    @customer_version.setter
    def customer_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "customer_version", value)

    @property
    @pulumi.getter(name="generationId")
    def generation_id(self) -> Optional[pulumi.Input[str]]:
        """
        The generation ID of the CA certificate.
        """
        return pulumi.get(self, "generation_id")

    @generation_id.setter
    def generation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "generation_id", value)

    @property
    @pulumi.getter(name="registrationConfig")
    def registration_config(self) -> Optional[pulumi.Input['CaCertificateRegistrationConfigArgs']]:
        """
        Information about the registration configuration. See below.
        """
        return pulumi.get(self, "registration_config")

    @registration_config.setter
    def registration_config(self, value: Optional[pulumi.Input['CaCertificateRegistrationConfigArgs']]):
        pulumi.set(self, "registration_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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

    @property
    @pulumi.getter
    def validities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CaCertificateValidityArgs']]]]:
        """
        When the CA certificate is valid.
        """
        return pulumi.get(self, "validities")

    @validities.setter
    def validities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CaCertificateValidityArgs']]]]):
        pulumi.set(self, "validities", value)

    @property
    @pulumi.getter(name="verificationCertificatePem")
    def verification_certificate_pem(self) -> Optional[pulumi.Input[str]]:
        """
        PEM encoded verification certificate containing the common name of a registration code. Review
        [CreateVerificationCSR](https://docs.aws.amazon.com/iot/latest/developerguide/register-CA-cert.html). Reuired if `certificate_mode` is `DEFAULT`.
        """
        return pulumi.get(self, "verification_certificate_pem")

    @verification_certificate_pem.setter
    def verification_certificate_pem(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "verification_certificate_pem", value)


class CaCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 allow_auto_registration: Optional[pulumi.Input[bool]] = None,
                 ca_certificate_pem: Optional[pulumi.Input[str]] = None,
                 certificate_mode: Optional[pulumi.Input[str]] = None,
                 registration_config: Optional[pulumi.Input[Union['CaCertificateRegistrationConfigArgs', 'CaCertificateRegistrationConfigArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 verification_certificate_pem: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates and manages an AWS IoT CA Certificate.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_tls as tls

        ca_private_key = tls.PrivateKey("ca", algorithm="RSA")
        ca = tls.SelfSignedCert("ca",
            private_key_pem=ca_private_key.private_key_pem,
            subject={
                "common_name": "example.com",
                "organization": "ACME Examples, Inc",
            },
            validity_period_hours=12,
            allowed_uses=[
                "key_encipherment",
                "digital_signature",
                "server_auth",
            ],
            is_ca_certificate=True)
        verification_private_key = tls.PrivateKey("verification", algorithm="RSA")
        example = aws.iot.get_registration_code()
        verification = tls.CertRequest("verification",
            private_key_pem=verification_private_key.private_key_pem,
            subject={
                "common_name": example.registration_code,
            })
        verification_locally_signed_cert = tls.LocallySignedCert("verification",
            cert_request_pem=verification.cert_request_pem,
            ca_private_key_pem=ca_private_key.private_key_pem,
            ca_cert_pem=ca.cert_pem,
            validity_period_hours=12,
            allowed_uses=[
                "key_encipherment",
                "digital_signature",
                "server_auth",
            ])
        example_ca_certificate = aws.iot.CaCertificate("example",
            active=True,
            ca_certificate_pem=ca.cert_pem,
            verification_certificate_pem=verification_locally_signed_cert.cert_pem,
            allow_auto_registration=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Boolean flag to indicate if the certificate should be active for device authentication.
        :param pulumi.Input[bool] allow_auto_registration: Boolean flag to indicate if the certificate should be active for device regisration.
        :param pulumi.Input[str] ca_certificate_pem: PEM encoded CA certificate.
        :param pulumi.Input[str] certificate_mode: The certificate mode in which the CA will be registered. Valida values: `DEFAULT` and `SNI_ONLY`. Default: `DEFAULT`.
        :param pulumi.Input[Union['CaCertificateRegistrationConfigArgs', 'CaCertificateRegistrationConfigArgsDict']] registration_config: Information about the registration configuration. See below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] verification_certificate_pem: PEM encoded verification certificate containing the common name of a registration code. Review
               [CreateVerificationCSR](https://docs.aws.amazon.com/iot/latest/developerguide/register-CA-cert.html). Reuired if `certificate_mode` is `DEFAULT`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CaCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates and manages an AWS IoT CA Certificate.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_tls as tls

        ca_private_key = tls.PrivateKey("ca", algorithm="RSA")
        ca = tls.SelfSignedCert("ca",
            private_key_pem=ca_private_key.private_key_pem,
            subject={
                "common_name": "example.com",
                "organization": "ACME Examples, Inc",
            },
            validity_period_hours=12,
            allowed_uses=[
                "key_encipherment",
                "digital_signature",
                "server_auth",
            ],
            is_ca_certificate=True)
        verification_private_key = tls.PrivateKey("verification", algorithm="RSA")
        example = aws.iot.get_registration_code()
        verification = tls.CertRequest("verification",
            private_key_pem=verification_private_key.private_key_pem,
            subject={
                "common_name": example.registration_code,
            })
        verification_locally_signed_cert = tls.LocallySignedCert("verification",
            cert_request_pem=verification.cert_request_pem,
            ca_private_key_pem=ca_private_key.private_key_pem,
            ca_cert_pem=ca.cert_pem,
            validity_period_hours=12,
            allowed_uses=[
                "key_encipherment",
                "digital_signature",
                "server_auth",
            ])
        example_ca_certificate = aws.iot.CaCertificate("example",
            active=True,
            ca_certificate_pem=ca.cert_pem,
            verification_certificate_pem=verification_locally_signed_cert.cert_pem,
            allow_auto_registration=True)
        ```

        :param str resource_name: The name of the resource.
        :param CaCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CaCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 allow_auto_registration: Optional[pulumi.Input[bool]] = None,
                 ca_certificate_pem: Optional[pulumi.Input[str]] = None,
                 certificate_mode: Optional[pulumi.Input[str]] = None,
                 registration_config: Optional[pulumi.Input[Union['CaCertificateRegistrationConfigArgs', 'CaCertificateRegistrationConfigArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 verification_certificate_pem: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CaCertificateArgs.__new__(CaCertificateArgs)

            if active is None and not opts.urn:
                raise TypeError("Missing required property 'active'")
            __props__.__dict__["active"] = active
            if allow_auto_registration is None and not opts.urn:
                raise TypeError("Missing required property 'allow_auto_registration'")
            __props__.__dict__["allow_auto_registration"] = allow_auto_registration
            if ca_certificate_pem is None and not opts.urn:
                raise TypeError("Missing required property 'ca_certificate_pem'")
            __props__.__dict__["ca_certificate_pem"] = None if ca_certificate_pem is None else pulumi.Output.secret(ca_certificate_pem)
            __props__.__dict__["certificate_mode"] = certificate_mode
            __props__.__dict__["registration_config"] = registration_config
            __props__.__dict__["tags"] = tags
            __props__.__dict__["verification_certificate_pem"] = None if verification_certificate_pem is None else pulumi.Output.secret(verification_certificate_pem)
            __props__.__dict__["arn"] = None
            __props__.__dict__["customer_version"] = None
            __props__.__dict__["generation_id"] = None
            __props__.__dict__["tags_all"] = None
            __props__.__dict__["validities"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["caCertificatePem", "verificationCertificatePem"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(CaCertificate, __self__).__init__(
            'aws:iot/caCertificate:CaCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            allow_auto_registration: Optional[pulumi.Input[bool]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            ca_certificate_pem: Optional[pulumi.Input[str]] = None,
            certificate_mode: Optional[pulumi.Input[str]] = None,
            customer_version: Optional[pulumi.Input[int]] = None,
            generation_id: Optional[pulumi.Input[str]] = None,
            registration_config: Optional[pulumi.Input[Union['CaCertificateRegistrationConfigArgs', 'CaCertificateRegistrationConfigArgsDict']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            validities: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CaCertificateValidityArgs', 'CaCertificateValidityArgsDict']]]]] = None,
            verification_certificate_pem: Optional[pulumi.Input[str]] = None) -> 'CaCertificate':
        """
        Get an existing CaCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Boolean flag to indicate if the certificate should be active for device authentication.
        :param pulumi.Input[bool] allow_auto_registration: Boolean flag to indicate if the certificate should be active for device regisration.
        :param pulumi.Input[str] arn: The ARN of the created CA certificate.
        :param pulumi.Input[str] ca_certificate_pem: PEM encoded CA certificate.
        :param pulumi.Input[str] certificate_mode: The certificate mode in which the CA will be registered. Valida values: `DEFAULT` and `SNI_ONLY`. Default: `DEFAULT`.
        :param pulumi.Input[int] customer_version: The customer version of the CA certificate.
        :param pulumi.Input[str] generation_id: The generation ID of the CA certificate.
        :param pulumi.Input[Union['CaCertificateRegistrationConfigArgs', 'CaCertificateRegistrationConfigArgsDict']] registration_config: Information about the registration configuration. See below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CaCertificateValidityArgs', 'CaCertificateValidityArgsDict']]]] validities: When the CA certificate is valid.
        :param pulumi.Input[str] verification_certificate_pem: PEM encoded verification certificate containing the common name of a registration code. Review
               [CreateVerificationCSR](https://docs.aws.amazon.com/iot/latest/developerguide/register-CA-cert.html). Reuired if `certificate_mode` is `DEFAULT`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CaCertificateState.__new__(_CaCertificateState)

        __props__.__dict__["active"] = active
        __props__.__dict__["allow_auto_registration"] = allow_auto_registration
        __props__.__dict__["arn"] = arn
        __props__.__dict__["ca_certificate_pem"] = ca_certificate_pem
        __props__.__dict__["certificate_mode"] = certificate_mode
        __props__.__dict__["customer_version"] = customer_version
        __props__.__dict__["generation_id"] = generation_id
        __props__.__dict__["registration_config"] = registration_config
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["validities"] = validities
        __props__.__dict__["verification_certificate_pem"] = verification_certificate_pem
        return CaCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[bool]:
        """
        Boolean flag to indicate if the certificate should be active for device authentication.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="allowAutoRegistration")
    def allow_auto_registration(self) -> pulumi.Output[bool]:
        """
        Boolean flag to indicate if the certificate should be active for device regisration.
        """
        return pulumi.get(self, "allow_auto_registration")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the created CA certificate.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="caCertificatePem")
    def ca_certificate_pem(self) -> pulumi.Output[str]:
        """
        PEM encoded CA certificate.
        """
        return pulumi.get(self, "ca_certificate_pem")

    @property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The certificate mode in which the CA will be registered. Valida values: `DEFAULT` and `SNI_ONLY`. Default: `DEFAULT`.
        """
        return pulumi.get(self, "certificate_mode")

    @property
    @pulumi.getter(name="customerVersion")
    def customer_version(self) -> pulumi.Output[int]:
        """
        The customer version of the CA certificate.
        """
        return pulumi.get(self, "customer_version")

    @property
    @pulumi.getter(name="generationId")
    def generation_id(self) -> pulumi.Output[str]:
        """
        The generation ID of the CA certificate.
        """
        return pulumi.get(self, "generation_id")

    @property
    @pulumi.getter(name="registrationConfig")
    def registration_config(self) -> pulumi.Output[Optional['outputs.CaCertificateRegistrationConfig']]:
        """
        Information about the registration configuration. See below.
        """
        return pulumi.get(self, "registration_config")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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

    @property
    @pulumi.getter
    def validities(self) -> pulumi.Output[Sequence['outputs.CaCertificateValidity']]:
        """
        When the CA certificate is valid.
        """
        return pulumi.get(self, "validities")

    @property
    @pulumi.getter(name="verificationCertificatePem")
    def verification_certificate_pem(self) -> pulumi.Output[Optional[str]]:
        """
        PEM encoded verification certificate containing the common name of a registration code. Review
        [CreateVerificationCSR](https://docs.aws.amazon.com/iot/latest/developerguide/register-CA-cert.html). Reuired if `certificate_mode` is `DEFAULT`.
        """
        return pulumi.get(self, "verification_certificate_pem")

