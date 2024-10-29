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
    'GetUserPoolSigningCertificateResult',
    'AwaitableGetUserPoolSigningCertificateResult',
    'get_user_pool_signing_certificate',
    'get_user_pool_signing_certificate_output',
]

@pulumi.output_type
class GetUserPoolSigningCertificateResult:
    """
    A collection of values returned by getUserPoolSigningCertificate.
    """
    def __init__(__self__, certificate=None, id=None, user_pool_id=None):
        if certificate and not isinstance(certificate, str):
            raise TypeError("Expected argument 'certificate' to be a str")
        pulumi.set(__self__, "certificate", certificate)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if user_pool_id and not isinstance(user_pool_id, str):
            raise TypeError("Expected argument 'user_pool_id' to be a str")
        pulumi.set(__self__, "user_pool_id", user_pool_id)

    @property
    @pulumi.getter
    def certificate(self) -> str:
        """
        Certificate string
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> str:
        return pulumi.get(self, "user_pool_id")


class AwaitableGetUserPoolSigningCertificateResult(GetUserPoolSigningCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserPoolSigningCertificateResult(
            certificate=self.certificate,
            id=self.id,
            user_pool_id=self.user_pool_id)


def get_user_pool_signing_certificate(user_pool_id: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserPoolSigningCertificateResult:
    """
    Use this data source to get the signing certificate for a Cognito IdP user pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    sc = aws.cognito.get_user_pool_signing_certificate(user_pool_id=my_pool["id"])
    ```


    :param str user_pool_id: Cognito user pool ID.
    """
    __args__ = dict()
    __args__['userPoolId'] = user_pool_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:cognito/getUserPoolSigningCertificate:getUserPoolSigningCertificate', __args__, opts=opts, typ=GetUserPoolSigningCertificateResult).value

    return AwaitableGetUserPoolSigningCertificateResult(
        certificate=pulumi.get(__ret__, 'certificate'),
        id=pulumi.get(__ret__, 'id'),
        user_pool_id=pulumi.get(__ret__, 'user_pool_id'))
def get_user_pool_signing_certificate_output(user_pool_id: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserPoolSigningCertificateResult]:
    """
    Use this data source to get the signing certificate for a Cognito IdP user pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    sc = aws.cognito.get_user_pool_signing_certificate(user_pool_id=my_pool["id"])
    ```


    :param str user_pool_id: Cognito user pool ID.
    """
    __args__ = dict()
    __args__['userPoolId'] = user_pool_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:cognito/getUserPoolSigningCertificate:getUserPoolSigningCertificate', __args__, opts=opts, typ=GetUserPoolSigningCertificateResult)
    return __ret__.apply(lambda __response__: GetUserPoolSigningCertificateResult(
        certificate=pulumi.get(__response__, 'certificate'),
        id=pulumi.get(__response__, 'id'),
        user_pool_id=pulumi.get(__response__, 'user_pool_id')))
