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
    'GetDatabaseResult',
    'AwaitableGetDatabaseResult',
    'get_database',
    'get_database_output',
]

@pulumi.output_type
class GetDatabaseResult:
    """
    A collection of values returned by getDatabase.
    """
    def __init__(__self__, arn=None, created_time=None, id=None, kms_key_id=None, last_updated_time=None, name=None, table_count=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if table_count and not isinstance(table_count, int):
            raise TypeError("Expected argument 'table_count' to be a int")
        pulumi.set(__self__, "table_count", table_count)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The ARN that uniquely identifies this database.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        """
        Creation time of database.
        """
        return pulumi.get(self, "created_time")

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
        The ARN of the KMS key used to encrypt the data stored in the database.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> str:
        """
        Last time database was updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="tableCount")
    def table_count(self) -> int:
        """
        Total number of tables in the Timestream database.
        """
        return pulumi.get(self, "table_count")


class AwaitableGetDatabaseResult(GetDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseResult(
            arn=self.arn,
            created_time=self.created_time,
            id=self.id,
            kms_key_id=self.kms_key_id,
            last_updated_time=self.last_updated_time,
            name=self.name,
            table_count=self.table_count)


def get_database(name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseResult:
    """
    Data source for managing an AWS Timestream Write Database.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.timestreamwrite.get_database(name="database-example")
    ```
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:timestreamwrite/getDatabase:getDatabase', __args__, opts=opts, typ=GetDatabaseResult).value

    return AwaitableGetDatabaseResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_time=pulumi.get(__ret__, 'created_time'),
        id=pulumi.get(__ret__, 'id'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        name=pulumi.get(__ret__, 'name'),
        table_count=pulumi.get(__ret__, 'table_count'))
def get_database_output(name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseResult]:
    """
    Data source for managing an AWS Timestream Write Database.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.timestreamwrite.get_database(name="database-example")
    ```
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:timestreamwrite/getDatabase:getDatabase', __args__, opts=opts, typ=GetDatabaseResult)
    return __ret__.apply(lambda __response__: GetDatabaseResult(
        arn=pulumi.get(__response__, 'arn'),
        created_time=pulumi.get(__response__, 'created_time'),
        id=pulumi.get(__response__, 'id'),
        kms_key_id=pulumi.get(__response__, 'kms_key_id'),
        last_updated_time=pulumi.get(__response__, 'last_updated_time'),
        name=pulumi.get(__response__, 'name'),
        table_count=pulumi.get(__response__, 'table_count')))
