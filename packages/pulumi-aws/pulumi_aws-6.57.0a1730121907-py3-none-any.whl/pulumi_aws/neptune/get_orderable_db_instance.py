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
    'GetOrderableDbInstanceResult',
    'AwaitableGetOrderableDbInstanceResult',
    'get_orderable_db_instance',
    'get_orderable_db_instance_output',
]

@pulumi.output_type
class GetOrderableDbInstanceResult:
    """
    A collection of values returned by getOrderableDbInstance.
    """
    def __init__(__self__, availability_zones=None, engine=None, engine_version=None, id=None, instance_class=None, license_model=None, max_iops_per_db_instance=None, max_iops_per_gib=None, max_storage_size=None, min_iops_per_db_instance=None, min_iops_per_gib=None, min_storage_size=None, multi_az_capable=None, preferred_instance_classes=None, read_replica_capable=None, storage_type=None, supports_enhanced_monitoring=None, supports_iam_database_authentication=None, supports_iops=None, supports_performance_insights=None, supports_storage_encryption=None, vpc=None):
        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError("Expected argument 'availability_zones' to be a list")
        pulumi.set(__self__, "availability_zones", availability_zones)
        if engine and not isinstance(engine, str):
            raise TypeError("Expected argument 'engine' to be a str")
        pulumi.set(__self__, "engine", engine)
        if engine_version and not isinstance(engine_version, str):
            raise TypeError("Expected argument 'engine_version' to be a str")
        pulumi.set(__self__, "engine_version", engine_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_class and not isinstance(instance_class, str):
            raise TypeError("Expected argument 'instance_class' to be a str")
        pulumi.set(__self__, "instance_class", instance_class)
        if license_model and not isinstance(license_model, str):
            raise TypeError("Expected argument 'license_model' to be a str")
        pulumi.set(__self__, "license_model", license_model)
        if max_iops_per_db_instance and not isinstance(max_iops_per_db_instance, int):
            raise TypeError("Expected argument 'max_iops_per_db_instance' to be a int")
        pulumi.set(__self__, "max_iops_per_db_instance", max_iops_per_db_instance)
        if max_iops_per_gib and not isinstance(max_iops_per_gib, float):
            raise TypeError("Expected argument 'max_iops_per_gib' to be a float")
        pulumi.set(__self__, "max_iops_per_gib", max_iops_per_gib)
        if max_storage_size and not isinstance(max_storage_size, int):
            raise TypeError("Expected argument 'max_storage_size' to be a int")
        pulumi.set(__self__, "max_storage_size", max_storage_size)
        if min_iops_per_db_instance and not isinstance(min_iops_per_db_instance, int):
            raise TypeError("Expected argument 'min_iops_per_db_instance' to be a int")
        pulumi.set(__self__, "min_iops_per_db_instance", min_iops_per_db_instance)
        if min_iops_per_gib and not isinstance(min_iops_per_gib, float):
            raise TypeError("Expected argument 'min_iops_per_gib' to be a float")
        pulumi.set(__self__, "min_iops_per_gib", min_iops_per_gib)
        if min_storage_size and not isinstance(min_storage_size, int):
            raise TypeError("Expected argument 'min_storage_size' to be a int")
        pulumi.set(__self__, "min_storage_size", min_storage_size)
        if multi_az_capable and not isinstance(multi_az_capable, bool):
            raise TypeError("Expected argument 'multi_az_capable' to be a bool")
        pulumi.set(__self__, "multi_az_capable", multi_az_capable)
        if preferred_instance_classes and not isinstance(preferred_instance_classes, list):
            raise TypeError("Expected argument 'preferred_instance_classes' to be a list")
        pulumi.set(__self__, "preferred_instance_classes", preferred_instance_classes)
        if read_replica_capable and not isinstance(read_replica_capable, bool):
            raise TypeError("Expected argument 'read_replica_capable' to be a bool")
        pulumi.set(__self__, "read_replica_capable", read_replica_capable)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)
        if supports_enhanced_monitoring and not isinstance(supports_enhanced_monitoring, bool):
            raise TypeError("Expected argument 'supports_enhanced_monitoring' to be a bool")
        pulumi.set(__self__, "supports_enhanced_monitoring", supports_enhanced_monitoring)
        if supports_iam_database_authentication and not isinstance(supports_iam_database_authentication, bool):
            raise TypeError("Expected argument 'supports_iam_database_authentication' to be a bool")
        pulumi.set(__self__, "supports_iam_database_authentication", supports_iam_database_authentication)
        if supports_iops and not isinstance(supports_iops, bool):
            raise TypeError("Expected argument 'supports_iops' to be a bool")
        pulumi.set(__self__, "supports_iops", supports_iops)
        if supports_performance_insights and not isinstance(supports_performance_insights, bool):
            raise TypeError("Expected argument 'supports_performance_insights' to be a bool")
        pulumi.set(__self__, "supports_performance_insights", supports_performance_insights)
        if supports_storage_encryption and not isinstance(supports_storage_encryption, bool):
            raise TypeError("Expected argument 'supports_storage_encryption' to be a bool")
        pulumi.set(__self__, "supports_storage_encryption", supports_storage_encryption)
        if vpc and not isinstance(vpc, bool):
            raise TypeError("Expected argument 'vpc' to be a bool")
        pulumi.set(__self__, "vpc", vpc)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[str]:
        """
        Availability zones where the instance is available.
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter
    def engine(self) -> Optional[str]:
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> str:
        return pulumi.get(self, "instance_class")

    @property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[str]:
        return pulumi.get(self, "license_model")

    @property
    @pulumi.getter(name="maxIopsPerDbInstance")
    def max_iops_per_db_instance(self) -> int:
        """
        Maximum total provisioned IOPS for a DB instance.
        """
        return pulumi.get(self, "max_iops_per_db_instance")

    @property
    @pulumi.getter(name="maxIopsPerGib")
    def max_iops_per_gib(self) -> float:
        """
        Maximum provisioned IOPS per GiB for a DB instance.
        """
        return pulumi.get(self, "max_iops_per_gib")

    @property
    @pulumi.getter(name="maxStorageSize")
    def max_storage_size(self) -> int:
        """
        Maximum storage size for a DB instance.
        """
        return pulumi.get(self, "max_storage_size")

    @property
    @pulumi.getter(name="minIopsPerDbInstance")
    def min_iops_per_db_instance(self) -> int:
        """
        Minimum total provisioned IOPS for a DB instance.
        """
        return pulumi.get(self, "min_iops_per_db_instance")

    @property
    @pulumi.getter(name="minIopsPerGib")
    def min_iops_per_gib(self) -> float:
        """
        Minimum provisioned IOPS per GiB for a DB instance.
        """
        return pulumi.get(self, "min_iops_per_gib")

    @property
    @pulumi.getter(name="minStorageSize")
    def min_storage_size(self) -> int:
        """
        Minimum storage size for a DB instance.
        """
        return pulumi.get(self, "min_storage_size")

    @property
    @pulumi.getter(name="multiAzCapable")
    def multi_az_capable(self) -> bool:
        """
        Whether a DB instance is Multi-AZ capable.
        """
        return pulumi.get(self, "multi_az_capable")

    @property
    @pulumi.getter(name="preferredInstanceClasses")
    def preferred_instance_classes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "preferred_instance_classes")

    @property
    @pulumi.getter(name="readReplicaCapable")
    def read_replica_capable(self) -> bool:
        """
        Whether a DB instance can have a read replica.
        """
        return pulumi.get(self, "read_replica_capable")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> str:
        """
        Storage type for a DB instance.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter(name="supportsEnhancedMonitoring")
    def supports_enhanced_monitoring(self) -> bool:
        """
        Whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60 seconds.
        """
        return pulumi.get(self, "supports_enhanced_monitoring")

    @property
    @pulumi.getter(name="supportsIamDatabaseAuthentication")
    def supports_iam_database_authentication(self) -> bool:
        """
        Whether a DB instance supports IAM database authentication.
        """
        return pulumi.get(self, "supports_iam_database_authentication")

    @property
    @pulumi.getter(name="supportsIops")
    def supports_iops(self) -> bool:
        """
        Whether a DB instance supports provisioned IOPS.
        """
        return pulumi.get(self, "supports_iops")

    @property
    @pulumi.getter(name="supportsPerformanceInsights")
    def supports_performance_insights(self) -> bool:
        """
        Whether a DB instance supports Performance Insights.
        """
        return pulumi.get(self, "supports_performance_insights")

    @property
    @pulumi.getter(name="supportsStorageEncryption")
    def supports_storage_encryption(self) -> bool:
        """
        Whether a DB instance supports encrypted storage.
        """
        return pulumi.get(self, "supports_storage_encryption")

    @property
    @pulumi.getter
    def vpc(self) -> bool:
        return pulumi.get(self, "vpc")


class AwaitableGetOrderableDbInstanceResult(GetOrderableDbInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrderableDbInstanceResult(
            availability_zones=self.availability_zones,
            engine=self.engine,
            engine_version=self.engine_version,
            id=self.id,
            instance_class=self.instance_class,
            license_model=self.license_model,
            max_iops_per_db_instance=self.max_iops_per_db_instance,
            max_iops_per_gib=self.max_iops_per_gib,
            max_storage_size=self.max_storage_size,
            min_iops_per_db_instance=self.min_iops_per_db_instance,
            min_iops_per_gib=self.min_iops_per_gib,
            min_storage_size=self.min_storage_size,
            multi_az_capable=self.multi_az_capable,
            preferred_instance_classes=self.preferred_instance_classes,
            read_replica_capable=self.read_replica_capable,
            storage_type=self.storage_type,
            supports_enhanced_monitoring=self.supports_enhanced_monitoring,
            supports_iam_database_authentication=self.supports_iam_database_authentication,
            supports_iops=self.supports_iops,
            supports_performance_insights=self.supports_performance_insights,
            supports_storage_encryption=self.supports_storage_encryption,
            vpc=self.vpc)


def get_orderable_db_instance(engine: Optional[str] = None,
                              engine_version: Optional[str] = None,
                              instance_class: Optional[str] = None,
                              license_model: Optional[str] = None,
                              preferred_instance_classes: Optional[Sequence[str]] = None,
                              vpc: Optional[bool] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrderableDbInstanceResult:
    """
    Information about Neptune orderable DB instances.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.neptune.get_orderable_db_instance(engine_version="1.0.3.0",
        preferred_instance_classes=[
            "db.r5.large",
            "db.r4.large",
            "db.t3.medium",
        ])
    ```


    :param str engine: DB engine. (Default: `neptune`)
    :param str engine_version: Version of the DB engine. For example, `1.0.1.0`, `1.0.1.2`, `1.0.2.2`, and `1.0.3.0`.
    :param str instance_class: DB instance class. Examples of classes are `db.r5.large`, `db.r5.xlarge`, `db.r4.large`, `db.r5.4xlarge`, `db.r5.12xlarge`, `db.r4.xlarge`, and `db.t3.medium`.
    :param str license_model: License model. (Default: `amazon-license`)
    :param Sequence[str] preferred_instance_classes: Ordered list of preferred Neptune DB instance classes. The first match in this list will be returned. If no preferred matches are found and the original search returned more than one result, an error is returned.
    :param bool vpc: Enable to show only VPC offerings.
    """
    __args__ = dict()
    __args__['engine'] = engine
    __args__['engineVersion'] = engine_version
    __args__['instanceClass'] = instance_class
    __args__['licenseModel'] = license_model
    __args__['preferredInstanceClasses'] = preferred_instance_classes
    __args__['vpc'] = vpc
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:neptune/getOrderableDbInstance:getOrderableDbInstance', __args__, opts=opts, typ=GetOrderableDbInstanceResult).value

    return AwaitableGetOrderableDbInstanceResult(
        availability_zones=pulumi.get(__ret__, 'availability_zones'),
        engine=pulumi.get(__ret__, 'engine'),
        engine_version=pulumi.get(__ret__, 'engine_version'),
        id=pulumi.get(__ret__, 'id'),
        instance_class=pulumi.get(__ret__, 'instance_class'),
        license_model=pulumi.get(__ret__, 'license_model'),
        max_iops_per_db_instance=pulumi.get(__ret__, 'max_iops_per_db_instance'),
        max_iops_per_gib=pulumi.get(__ret__, 'max_iops_per_gib'),
        max_storage_size=pulumi.get(__ret__, 'max_storage_size'),
        min_iops_per_db_instance=pulumi.get(__ret__, 'min_iops_per_db_instance'),
        min_iops_per_gib=pulumi.get(__ret__, 'min_iops_per_gib'),
        min_storage_size=pulumi.get(__ret__, 'min_storage_size'),
        multi_az_capable=pulumi.get(__ret__, 'multi_az_capable'),
        preferred_instance_classes=pulumi.get(__ret__, 'preferred_instance_classes'),
        read_replica_capable=pulumi.get(__ret__, 'read_replica_capable'),
        storage_type=pulumi.get(__ret__, 'storage_type'),
        supports_enhanced_monitoring=pulumi.get(__ret__, 'supports_enhanced_monitoring'),
        supports_iam_database_authentication=pulumi.get(__ret__, 'supports_iam_database_authentication'),
        supports_iops=pulumi.get(__ret__, 'supports_iops'),
        supports_performance_insights=pulumi.get(__ret__, 'supports_performance_insights'),
        supports_storage_encryption=pulumi.get(__ret__, 'supports_storage_encryption'),
        vpc=pulumi.get(__ret__, 'vpc'))
def get_orderable_db_instance_output(engine: Optional[pulumi.Input[Optional[str]]] = None,
                                     engine_version: Optional[pulumi.Input[Optional[str]]] = None,
                                     instance_class: Optional[pulumi.Input[Optional[str]]] = None,
                                     license_model: Optional[pulumi.Input[Optional[str]]] = None,
                                     preferred_instance_classes: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                     vpc: Optional[pulumi.Input[Optional[bool]]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrderableDbInstanceResult]:
    """
    Information about Neptune orderable DB instances.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.neptune.get_orderable_db_instance(engine_version="1.0.3.0",
        preferred_instance_classes=[
            "db.r5.large",
            "db.r4.large",
            "db.t3.medium",
        ])
    ```


    :param str engine: DB engine. (Default: `neptune`)
    :param str engine_version: Version of the DB engine. For example, `1.0.1.0`, `1.0.1.2`, `1.0.2.2`, and `1.0.3.0`.
    :param str instance_class: DB instance class. Examples of classes are `db.r5.large`, `db.r5.xlarge`, `db.r4.large`, `db.r5.4xlarge`, `db.r5.12xlarge`, `db.r4.xlarge`, and `db.t3.medium`.
    :param str license_model: License model. (Default: `amazon-license`)
    :param Sequence[str] preferred_instance_classes: Ordered list of preferred Neptune DB instance classes. The first match in this list will be returned. If no preferred matches are found and the original search returned more than one result, an error is returned.
    :param bool vpc: Enable to show only VPC offerings.
    """
    __args__ = dict()
    __args__['engine'] = engine
    __args__['engineVersion'] = engine_version
    __args__['instanceClass'] = instance_class
    __args__['licenseModel'] = license_model
    __args__['preferredInstanceClasses'] = preferred_instance_classes
    __args__['vpc'] = vpc
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:neptune/getOrderableDbInstance:getOrderableDbInstance', __args__, opts=opts, typ=GetOrderableDbInstanceResult)
    return __ret__.apply(lambda __response__: GetOrderableDbInstanceResult(
        availability_zones=pulumi.get(__response__, 'availability_zones'),
        engine=pulumi.get(__response__, 'engine'),
        engine_version=pulumi.get(__response__, 'engine_version'),
        id=pulumi.get(__response__, 'id'),
        instance_class=pulumi.get(__response__, 'instance_class'),
        license_model=pulumi.get(__response__, 'license_model'),
        max_iops_per_db_instance=pulumi.get(__response__, 'max_iops_per_db_instance'),
        max_iops_per_gib=pulumi.get(__response__, 'max_iops_per_gib'),
        max_storage_size=pulumi.get(__response__, 'max_storage_size'),
        min_iops_per_db_instance=pulumi.get(__response__, 'min_iops_per_db_instance'),
        min_iops_per_gib=pulumi.get(__response__, 'min_iops_per_gib'),
        min_storage_size=pulumi.get(__response__, 'min_storage_size'),
        multi_az_capable=pulumi.get(__response__, 'multi_az_capable'),
        preferred_instance_classes=pulumi.get(__response__, 'preferred_instance_classes'),
        read_replica_capable=pulumi.get(__response__, 'read_replica_capable'),
        storage_type=pulumi.get(__response__, 'storage_type'),
        supports_enhanced_monitoring=pulumi.get(__response__, 'supports_enhanced_monitoring'),
        supports_iam_database_authentication=pulumi.get(__response__, 'supports_iam_database_authentication'),
        supports_iops=pulumi.get(__response__, 'supports_iops'),
        supports_performance_insights=pulumi.get(__response__, 'supports_performance_insights'),
        supports_storage_encryption=pulumi.get(__response__, 'supports_storage_encryption'),
        vpc=pulumi.get(__response__, 'vpc')))
