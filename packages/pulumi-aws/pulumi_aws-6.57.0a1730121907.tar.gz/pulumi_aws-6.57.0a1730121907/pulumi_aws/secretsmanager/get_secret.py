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
    'GetSecretResult',
    'AwaitableGetSecretResult',
    'get_secret',
    'get_secret_output',
]

@pulumi.output_type
class GetSecretResult:
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, arn=None, created_date=None, description=None, id=None, kms_key_id=None, last_changed_date=None, name=None, policy=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if last_changed_date and not isinstance(last_changed_date, str):
            raise TypeError("Expected argument 'last_changed_date' to be a str")
        pulumi.set(__self__, "last_changed_date", last_changed_date)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if policy and not isinstance(policy, str):
            raise TypeError("Expected argument 'policy' to be a str")
        pulumi.set(__self__, "policy", policy)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the secret.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        """
        Created date of the secret in UTC.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the secret.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> str:
        """
        Key Management Service (KMS) Customer Master Key (CMK) associated with the secret.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="lastChangedDate")
    def last_changed_date(self) -> str:
        """
        Last updated date of the secret in UTC.
        """
        return pulumi.get(self, "last_changed_date")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def policy(self) -> str:
        """
        Resource-based policy document that's attached to the secret.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Tags of the secret.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            arn=self.arn,
            created_date=self.created_date,
            description=self.description,
            id=self.id,
            kms_key_id=self.kms_key_id,
            last_changed_date=self.last_changed_date,
            name=self.name,
            policy=self.policy,
            tags=self.tags)


def get_secret(arn: Optional[str] = None,
               name: Optional[str] = None,
               tags: Optional[Mapping[str, str]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretResult:
    """
    Retrieve metadata information about a Secrets Manager secret. To retrieve a secret value, see the `secretsmanager.SecretVersion` data source.

    ## Example Usage

    ### ARN

    ```python
    import pulumi
    import pulumi_aws as aws

    by_arn = aws.secretsmanager.get_secret(arn="arn:aws:secretsmanager:us-east-1:123456789012:secret:example-123456")
    ```

    ### Name

    ```python
    import pulumi
    import pulumi_aws as aws

    by_name = aws.secretsmanager.get_secret(name="example")
    ```


    :param str arn: ARN of the secret to retrieve.
    :param str name: Name of the secret to retrieve.
    :param Mapping[str, str] tags: Tags of the secret.
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['name'] = name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:secretsmanager/getSecret:getSecret', __args__, opts=opts, typ=GetSecretResult).value

    return AwaitableGetSecretResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_date=pulumi.get(__ret__, 'created_date'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        last_changed_date=pulumi.get(__ret__, 'last_changed_date'),
        name=pulumi.get(__ret__, 'name'),
        policy=pulumi.get(__ret__, 'policy'),
        tags=pulumi.get(__ret__, 'tags'))
def get_secret_output(arn: Optional[pulumi.Input[Optional[str]]] = None,
                      name: Optional[pulumi.Input[Optional[str]]] = None,
                      tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecretResult]:
    """
    Retrieve metadata information about a Secrets Manager secret. To retrieve a secret value, see the `secretsmanager.SecretVersion` data source.

    ## Example Usage

    ### ARN

    ```python
    import pulumi
    import pulumi_aws as aws

    by_arn = aws.secretsmanager.get_secret(arn="arn:aws:secretsmanager:us-east-1:123456789012:secret:example-123456")
    ```

    ### Name

    ```python
    import pulumi
    import pulumi_aws as aws

    by_name = aws.secretsmanager.get_secret(name="example")
    ```


    :param str arn: ARN of the secret to retrieve.
    :param str name: Name of the secret to retrieve.
    :param Mapping[str, str] tags: Tags of the secret.
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['name'] = name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:secretsmanager/getSecret:getSecret', __args__, opts=opts, typ=GetSecretResult)
    return __ret__.apply(lambda __response__: GetSecretResult(
        arn=pulumi.get(__response__, 'arn'),
        created_date=pulumi.get(__response__, 'created_date'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        kms_key_id=pulumi.get(__response__, 'kms_key_id'),
        last_changed_date=pulumi.get(__response__, 'last_changed_date'),
        name=pulumi.get(__response__, 'name'),
        policy=pulumi.get(__response__, 'policy'),
        tags=pulumi.get(__response__, 'tags')))
