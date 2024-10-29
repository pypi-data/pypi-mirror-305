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

__all__ = [
    'BrokerConfiguration',
    'BrokerEncryptionOptions',
    'BrokerInstance',
    'BrokerLdapServerMetadata',
    'BrokerLogs',
    'BrokerMaintenanceWindowStartTime',
    'BrokerUser',
    'GetBrokerConfigurationResult',
    'GetBrokerEncryptionOptionResult',
    'GetBrokerEngineTypesBrokerEngineTypeResult',
    'GetBrokerEngineTypesBrokerEngineTypeEngineVersionResult',
    'GetBrokerInstanceResult',
    'GetBrokerLdapServerMetadataResult',
    'GetBrokerLogsResult',
    'GetBrokerMaintenanceWindowStartTimeResult',
    'GetBrokerUserResult',
    'GetInstanceTypeOfferingsBrokerInstanceOptionResult',
    'GetInstanceTypeOfferingsBrokerInstanceOptionAvailabilityZoneResult',
]

@pulumi.output_type
class BrokerConfiguration(dict):
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 revision: Optional[int] = None):
        """
        :param str id: The Configuration ID.
        :param int revision: Revision of the Configuration.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if revision is not None:
            pulumi.set(__self__, "revision", revision)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The Configuration ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def revision(self) -> Optional[int]:
        """
        Revision of the Configuration.
        """
        return pulumi.get(self, "revision")


@pulumi.output_type
class BrokerEncryptionOptions(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsKeyId":
            suggest = "kms_key_id"
        elif key == "useAwsOwnedKey":
            suggest = "use_aws_owned_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BrokerEncryptionOptions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BrokerEncryptionOptions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BrokerEncryptionOptions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_key_id: Optional[str] = None,
                 use_aws_owned_key: Optional[bool] = None):
        """
        :param str kms_key_id: Amazon Resource Name (ARN) of Key Management Service (KMS) Customer Master Key (CMK) to use for encryption at rest. Requires setting `use_aws_owned_key` to `false`. To perform drift detection when AWS-managed CMKs or customer-managed CMKs are in use, this value must be configured.
        :param bool use_aws_owned_key: Whether to enable an AWS-owned KMS CMK that is not in your account. Defaults to `true`. Setting to `false` without configuring `kms_key_id` will create an AWS-managed CMK aliased to `aws/mq` in your account.
        """
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if use_aws_owned_key is not None:
            pulumi.set(__self__, "use_aws_owned_key", use_aws_owned_key)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of Key Management Service (KMS) Customer Master Key (CMK) to use for encryption at rest. Requires setting `use_aws_owned_key` to `false`. To perform drift detection when AWS-managed CMKs or customer-managed CMKs are in use, this value must be configured.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="useAwsOwnedKey")
    def use_aws_owned_key(self) -> Optional[bool]:
        """
        Whether to enable an AWS-owned KMS CMK that is not in your account. Defaults to `true`. Setting to `false` without configuring `kms_key_id` will create an AWS-managed CMK aliased to `aws/mq` in your account.
        """
        return pulumi.get(self, "use_aws_owned_key")


@pulumi.output_type
class BrokerInstance(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "consoleUrl":
            suggest = "console_url"
        elif key == "ipAddress":
            suggest = "ip_address"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BrokerInstance. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BrokerInstance.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BrokerInstance.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 console_url: Optional[str] = None,
                 endpoints: Optional[Sequence[str]] = None,
                 ip_address: Optional[str] = None):
        """
        :param str console_url: The URL of the [ActiveMQ Web Console](http://activemq.apache.org/web-console.html) or the [RabbitMQ Management UI](https://www.rabbitmq.com/management.html#external-monitoring) depending on `engine_type`.
        :param Sequence[str] endpoints: Broker's wire-level protocol endpoints in the following order & format referenceable e.g., as `instances.0.endpoints.0` (SSL):
               * For `ActiveMQ`:
               * `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
               * `amqp+ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
               * `stomp+ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
               * `mqtt+ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
               * `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
               * For `RabbitMQ`:
               * `amqps://broker-id.mq.us-west-2.amazonaws.com:5671`
        :param str ip_address: IP Address of the broker.
        """
        if console_url is not None:
            pulumi.set(__self__, "console_url", console_url)
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)

    @property
    @pulumi.getter(name="consoleUrl")
    def console_url(self) -> Optional[str]:
        """
        The URL of the [ActiveMQ Web Console](http://activemq.apache.org/web-console.html) or the [RabbitMQ Management UI](https://www.rabbitmq.com/management.html#external-monitoring) depending on `engine_type`.
        """
        return pulumi.get(self, "console_url")

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence[str]]:
        """
        Broker's wire-level protocol endpoints in the following order & format referenceable e.g., as `instances.0.endpoints.0` (SSL):
        * For `ActiveMQ`:
        * `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
        * `amqp+ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
        * `stomp+ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
        * `mqtt+ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
        * `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
        * For `RabbitMQ`:
        * `amqps://broker-id.mq.us-west-2.amazonaws.com:5671`
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[str]:
        """
        IP Address of the broker.
        """
        return pulumi.get(self, "ip_address")


@pulumi.output_type
class BrokerLdapServerMetadata(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "roleBase":
            suggest = "role_base"
        elif key == "roleName":
            suggest = "role_name"
        elif key == "roleSearchMatching":
            suggest = "role_search_matching"
        elif key == "roleSearchSubtree":
            suggest = "role_search_subtree"
        elif key == "serviceAccountPassword":
            suggest = "service_account_password"
        elif key == "serviceAccountUsername":
            suggest = "service_account_username"
        elif key == "userBase":
            suggest = "user_base"
        elif key == "userRoleName":
            suggest = "user_role_name"
        elif key == "userSearchMatching":
            suggest = "user_search_matching"
        elif key == "userSearchSubtree":
            suggest = "user_search_subtree"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BrokerLdapServerMetadata. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BrokerLdapServerMetadata.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BrokerLdapServerMetadata.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 hosts: Optional[Sequence[str]] = None,
                 role_base: Optional[str] = None,
                 role_name: Optional[str] = None,
                 role_search_matching: Optional[str] = None,
                 role_search_subtree: Optional[bool] = None,
                 service_account_password: Optional[str] = None,
                 service_account_username: Optional[str] = None,
                 user_base: Optional[str] = None,
                 user_role_name: Optional[str] = None,
                 user_search_matching: Optional[str] = None,
                 user_search_subtree: Optional[bool] = None):
        """
        :param Sequence[str] hosts: List of a fully qualified domain name of the LDAP server and an optional failover server.
        :param str role_base: Fully qualified name of the directory to search for a user’s groups.
        :param str role_name: Specifies the LDAP attribute that identifies the group name attribute in the object returned from the group membership query.
        :param str role_search_matching: Search criteria for groups.
        :param bool role_search_subtree: Whether the directory search scope is the entire sub-tree.
        :param str service_account_password: Service account password.
        :param str service_account_username: Service account username.
        :param str user_base: Fully qualified name of the directory where you want to search for users.
        :param str user_role_name: Specifies the name of the LDAP attribute for the user group membership.
        :param str user_search_matching: Search criteria for users.
        :param bool user_search_subtree: Whether the directory search scope is the entire sub-tree.
        """
        if hosts is not None:
            pulumi.set(__self__, "hosts", hosts)
        if role_base is not None:
            pulumi.set(__self__, "role_base", role_base)
        if role_name is not None:
            pulumi.set(__self__, "role_name", role_name)
        if role_search_matching is not None:
            pulumi.set(__self__, "role_search_matching", role_search_matching)
        if role_search_subtree is not None:
            pulumi.set(__self__, "role_search_subtree", role_search_subtree)
        if service_account_password is not None:
            pulumi.set(__self__, "service_account_password", service_account_password)
        if service_account_username is not None:
            pulumi.set(__self__, "service_account_username", service_account_username)
        if user_base is not None:
            pulumi.set(__self__, "user_base", user_base)
        if user_role_name is not None:
            pulumi.set(__self__, "user_role_name", user_role_name)
        if user_search_matching is not None:
            pulumi.set(__self__, "user_search_matching", user_search_matching)
        if user_search_subtree is not None:
            pulumi.set(__self__, "user_search_subtree", user_search_subtree)

    @property
    @pulumi.getter
    def hosts(self) -> Optional[Sequence[str]]:
        """
        List of a fully qualified domain name of the LDAP server and an optional failover server.
        """
        return pulumi.get(self, "hosts")

    @property
    @pulumi.getter(name="roleBase")
    def role_base(self) -> Optional[str]:
        """
        Fully qualified name of the directory to search for a user’s groups.
        """
        return pulumi.get(self, "role_base")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[str]:
        """
        Specifies the LDAP attribute that identifies the group name attribute in the object returned from the group membership query.
        """
        return pulumi.get(self, "role_name")

    @property
    @pulumi.getter(name="roleSearchMatching")
    def role_search_matching(self) -> Optional[str]:
        """
        Search criteria for groups.
        """
        return pulumi.get(self, "role_search_matching")

    @property
    @pulumi.getter(name="roleSearchSubtree")
    def role_search_subtree(self) -> Optional[bool]:
        """
        Whether the directory search scope is the entire sub-tree.
        """
        return pulumi.get(self, "role_search_subtree")

    @property
    @pulumi.getter(name="serviceAccountPassword")
    def service_account_password(self) -> Optional[str]:
        """
        Service account password.
        """
        return pulumi.get(self, "service_account_password")

    @property
    @pulumi.getter(name="serviceAccountUsername")
    def service_account_username(self) -> Optional[str]:
        """
        Service account username.
        """
        return pulumi.get(self, "service_account_username")

    @property
    @pulumi.getter(name="userBase")
    def user_base(self) -> Optional[str]:
        """
        Fully qualified name of the directory where you want to search for users.
        """
        return pulumi.get(self, "user_base")

    @property
    @pulumi.getter(name="userRoleName")
    def user_role_name(self) -> Optional[str]:
        """
        Specifies the name of the LDAP attribute for the user group membership.
        """
        return pulumi.get(self, "user_role_name")

    @property
    @pulumi.getter(name="userSearchMatching")
    def user_search_matching(self) -> Optional[str]:
        """
        Search criteria for users.
        """
        return pulumi.get(self, "user_search_matching")

    @property
    @pulumi.getter(name="userSearchSubtree")
    def user_search_subtree(self) -> Optional[bool]:
        """
        Whether the directory search scope is the entire sub-tree.
        """
        return pulumi.get(self, "user_search_subtree")


@pulumi.output_type
class BrokerLogs(dict):
    def __init__(__self__, *,
                 audit: Optional[bool] = None,
                 general: Optional[bool] = None):
        """
        :param bool audit: Enables audit logging. Auditing is only possible for `engine_type` of `ActiveMQ`. User management action made using JMX or the ActiveMQ Web Console is logged. Defaults to `false`.
        :param bool general: Enables general logging via CloudWatch. Defaults to `false`.
        """
        if audit is not None:
            pulumi.set(__self__, "audit", audit)
        if general is not None:
            pulumi.set(__self__, "general", general)

    @property
    @pulumi.getter
    def audit(self) -> Optional[bool]:
        """
        Enables audit logging. Auditing is only possible for `engine_type` of `ActiveMQ`. User management action made using JMX or the ActiveMQ Web Console is logged. Defaults to `false`.
        """
        return pulumi.get(self, "audit")

    @property
    @pulumi.getter
    def general(self) -> Optional[bool]:
        """
        Enables general logging via CloudWatch. Defaults to `false`.
        """
        return pulumi.get(self, "general")


@pulumi.output_type
class BrokerMaintenanceWindowStartTime(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dayOfWeek":
            suggest = "day_of_week"
        elif key == "timeOfDay":
            suggest = "time_of_day"
        elif key == "timeZone":
            suggest = "time_zone"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BrokerMaintenanceWindowStartTime. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BrokerMaintenanceWindowStartTime.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BrokerMaintenanceWindowStartTime.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 day_of_week: str,
                 time_of_day: str,
                 time_zone: str):
        """
        :param str day_of_week: Day of the week, e.g., `MONDAY`, `TUESDAY`, or `WEDNESDAY`.
        :param str time_of_day: Time, in 24-hour format, e.g., `02:00`.
        :param str time_zone: Time zone in either the Country/City format or the UTC offset format, e.g., `CET`.
        """
        pulumi.set(__self__, "day_of_week", day_of_week)
        pulumi.set(__self__, "time_of_day", time_of_day)
        pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> str:
        """
        Day of the week, e.g., `MONDAY`, `TUESDAY`, or `WEDNESDAY`.
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter(name="timeOfDay")
    def time_of_day(self) -> str:
        """
        Time, in 24-hour format, e.g., `02:00`.
        """
        return pulumi.get(self, "time_of_day")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        Time zone in either the Country/City format or the UTC offset format, e.g., `CET`.
        """
        return pulumi.get(self, "time_zone")


@pulumi.output_type
class BrokerUser(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "consoleAccess":
            suggest = "console_access"
        elif key == "replicationUser":
            suggest = "replication_user"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BrokerUser. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BrokerUser.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BrokerUser.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 password: str,
                 username: str,
                 console_access: Optional[bool] = None,
                 groups: Optional[Sequence[str]] = None,
                 replication_user: Optional[bool] = None):
        """
        :param str password: Password of the user. It must be 12 to 250 characters long, at least 4 unique characters, and must not contain commas.
        :param str username: Username of the user.
               
               > **NOTE:** AWS currently does not support updating RabbitMQ users. Updates to users can only be in the RabbitMQ UI.
        :param bool console_access: Whether to enable access to the [ActiveMQ Web Console](http://activemq.apache.org/web-console.html) for the user. Applies to `engine_type` of `ActiveMQ` only.
        :param Sequence[str] groups: List of groups (20 maximum) to which the ActiveMQ user belongs. Applies to `engine_type` of `ActiveMQ` only.
        :param bool replication_user: Whether to set set replication user. Defaults to `false`.
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)
        if console_access is not None:
            pulumi.set(__self__, "console_access", console_access)
        if groups is not None:
            pulumi.set(__self__, "groups", groups)
        if replication_user is not None:
            pulumi.set(__self__, "replication_user", replication_user)

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        Password of the user. It must be 12 to 250 characters long, at least 4 unique characters, and must not contain commas.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        Username of the user.

        > **NOTE:** AWS currently does not support updating RabbitMQ users. Updates to users can only be in the RabbitMQ UI.
        """
        return pulumi.get(self, "username")

    @property
    @pulumi.getter(name="consoleAccess")
    def console_access(self) -> Optional[bool]:
        """
        Whether to enable access to the [ActiveMQ Web Console](http://activemq.apache.org/web-console.html) for the user. Applies to `engine_type` of `ActiveMQ` only.
        """
        return pulumi.get(self, "console_access")

    @property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[str]]:
        """
        List of groups (20 maximum) to which the ActiveMQ user belongs. Applies to `engine_type` of `ActiveMQ` only.
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter(name="replicationUser")
    def replication_user(self) -> Optional[bool]:
        """
        Whether to set set replication user. Defaults to `false`.
        """
        return pulumi.get(self, "replication_user")


@pulumi.output_type
class GetBrokerConfigurationResult(dict):
    def __init__(__self__, *,
                 id: str,
                 revision: int):
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "revision", revision)

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def revision(self) -> int:
        return pulumi.get(self, "revision")


@pulumi.output_type
class GetBrokerEncryptionOptionResult(dict):
    def __init__(__self__, *,
                 kms_key_id: str,
                 use_aws_owned_key: bool):
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        pulumi.set(__self__, "use_aws_owned_key", use_aws_owned_key)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> str:
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="useAwsOwnedKey")
    def use_aws_owned_key(self) -> bool:
        return pulumi.get(self, "use_aws_owned_key")


@pulumi.output_type
class GetBrokerEngineTypesBrokerEngineTypeResult(dict):
    def __init__(__self__, *,
                 engine_type: str,
                 engine_versions: Sequence['outputs.GetBrokerEngineTypesBrokerEngineTypeEngineVersionResult']):
        """
        :param str engine_type: The MQ engine type to return version details for.
        :param Sequence['GetBrokerEngineTypesBrokerEngineTypeEngineVersionArgs'] engine_versions: The list of engine versions.
        """
        pulumi.set(__self__, "engine_type", engine_type)
        pulumi.set(__self__, "engine_versions", engine_versions)

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> str:
        """
        The MQ engine type to return version details for.
        """
        return pulumi.get(self, "engine_type")

    @property
    @pulumi.getter(name="engineVersions")
    def engine_versions(self) -> Sequence['outputs.GetBrokerEngineTypesBrokerEngineTypeEngineVersionResult']:
        """
        The list of engine versions.
        """
        return pulumi.get(self, "engine_versions")


@pulumi.output_type
class GetBrokerEngineTypesBrokerEngineTypeEngineVersionResult(dict):
    def __init__(__self__, *,
                 name: str):
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


@pulumi.output_type
class GetBrokerInstanceResult(dict):
    def __init__(__self__, *,
                 console_url: str,
                 endpoints: Sequence[str],
                 ip_address: str):
        pulumi.set(__self__, "console_url", console_url)
        pulumi.set(__self__, "endpoints", endpoints)
        pulumi.set(__self__, "ip_address", ip_address)

    @property
    @pulumi.getter(name="consoleUrl")
    def console_url(self) -> str:
        return pulumi.get(self, "console_url")

    @property
    @pulumi.getter
    def endpoints(self) -> Sequence[str]:
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        return pulumi.get(self, "ip_address")


@pulumi.output_type
class GetBrokerLdapServerMetadataResult(dict):
    def __init__(__self__, *,
                 hosts: Sequence[str],
                 role_base: str,
                 role_name: str,
                 role_search_matching: str,
                 role_search_subtree: bool,
                 service_account_password: str,
                 service_account_username: str,
                 user_base: str,
                 user_role_name: str,
                 user_search_matching: str,
                 user_search_subtree: bool):
        pulumi.set(__self__, "hosts", hosts)
        pulumi.set(__self__, "role_base", role_base)
        pulumi.set(__self__, "role_name", role_name)
        pulumi.set(__self__, "role_search_matching", role_search_matching)
        pulumi.set(__self__, "role_search_subtree", role_search_subtree)
        pulumi.set(__self__, "service_account_password", service_account_password)
        pulumi.set(__self__, "service_account_username", service_account_username)
        pulumi.set(__self__, "user_base", user_base)
        pulumi.set(__self__, "user_role_name", user_role_name)
        pulumi.set(__self__, "user_search_matching", user_search_matching)
        pulumi.set(__self__, "user_search_subtree", user_search_subtree)

    @property
    @pulumi.getter
    def hosts(self) -> Sequence[str]:
        return pulumi.get(self, "hosts")

    @property
    @pulumi.getter(name="roleBase")
    def role_base(self) -> str:
        return pulumi.get(self, "role_base")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> str:
        return pulumi.get(self, "role_name")

    @property
    @pulumi.getter(name="roleSearchMatching")
    def role_search_matching(self) -> str:
        return pulumi.get(self, "role_search_matching")

    @property
    @pulumi.getter(name="roleSearchSubtree")
    def role_search_subtree(self) -> bool:
        return pulumi.get(self, "role_search_subtree")

    @property
    @pulumi.getter(name="serviceAccountPassword")
    def service_account_password(self) -> str:
        return pulumi.get(self, "service_account_password")

    @property
    @pulumi.getter(name="serviceAccountUsername")
    def service_account_username(self) -> str:
        return pulumi.get(self, "service_account_username")

    @property
    @pulumi.getter(name="userBase")
    def user_base(self) -> str:
        return pulumi.get(self, "user_base")

    @property
    @pulumi.getter(name="userRoleName")
    def user_role_name(self) -> str:
        return pulumi.get(self, "user_role_name")

    @property
    @pulumi.getter(name="userSearchMatching")
    def user_search_matching(self) -> str:
        return pulumi.get(self, "user_search_matching")

    @property
    @pulumi.getter(name="userSearchSubtree")
    def user_search_subtree(self) -> bool:
        return pulumi.get(self, "user_search_subtree")


@pulumi.output_type
class GetBrokerLogsResult(dict):
    def __init__(__self__, *,
                 audit: bool,
                 general: bool):
        pulumi.set(__self__, "audit", audit)
        pulumi.set(__self__, "general", general)

    @property
    @pulumi.getter
    def audit(self) -> bool:
        return pulumi.get(self, "audit")

    @property
    @pulumi.getter
    def general(self) -> bool:
        return pulumi.get(self, "general")


@pulumi.output_type
class GetBrokerMaintenanceWindowStartTimeResult(dict):
    def __init__(__self__, *,
                 day_of_week: str,
                 time_of_day: str,
                 time_zone: str):
        pulumi.set(__self__, "day_of_week", day_of_week)
        pulumi.set(__self__, "time_of_day", time_of_day)
        pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> str:
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter(name="timeOfDay")
    def time_of_day(self) -> str:
        return pulumi.get(self, "time_of_day")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        return pulumi.get(self, "time_zone")


@pulumi.output_type
class GetBrokerUserResult(dict):
    def __init__(__self__, *,
                 console_access: bool,
                 groups: Sequence[str],
                 replication_user: bool,
                 username: str):
        pulumi.set(__self__, "console_access", console_access)
        pulumi.set(__self__, "groups", groups)
        pulumi.set(__self__, "replication_user", replication_user)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="consoleAccess")
    def console_access(self) -> bool:
        return pulumi.get(self, "console_access")

    @property
    @pulumi.getter
    def groups(self) -> Sequence[str]:
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter(name="replicationUser")
    def replication_user(self) -> bool:
        return pulumi.get(self, "replication_user")

    @property
    @pulumi.getter
    def username(self) -> str:
        return pulumi.get(self, "username")


@pulumi.output_type
class GetInstanceTypeOfferingsBrokerInstanceOptionResult(dict):
    def __init__(__self__, *,
                 availability_zones: Sequence['outputs.GetInstanceTypeOfferingsBrokerInstanceOptionAvailabilityZoneResult'],
                 engine_type: str,
                 host_instance_type: str,
                 storage_type: str,
                 supported_deployment_modes: Sequence[str],
                 supported_engine_versions: Sequence[str]):
        """
        :param Sequence['GetInstanceTypeOfferingsBrokerInstanceOptionAvailabilityZoneArgs'] availability_zones: List of available AZs. See Availability Zones. below
        :param str engine_type: Filter response by engine type.
        :param str host_instance_type: Filter response by host instance type.
        :param str storage_type: Filter response by storage type.
        :param Sequence[str] supported_deployment_modes: The list of supported deployment modes.
        :param Sequence[str] supported_engine_versions: The list of supported engine versions.
        """
        pulumi.set(__self__, "availability_zones", availability_zones)
        pulumi.set(__self__, "engine_type", engine_type)
        pulumi.set(__self__, "host_instance_type", host_instance_type)
        pulumi.set(__self__, "storage_type", storage_type)
        pulumi.set(__self__, "supported_deployment_modes", supported_deployment_modes)
        pulumi.set(__self__, "supported_engine_versions", supported_engine_versions)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence['outputs.GetInstanceTypeOfferingsBrokerInstanceOptionAvailabilityZoneResult']:
        """
        List of available AZs. See Availability Zones. below
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> str:
        """
        Filter response by engine type.
        """
        return pulumi.get(self, "engine_type")

    @property
    @pulumi.getter(name="hostInstanceType")
    def host_instance_type(self) -> str:
        """
        Filter response by host instance type.
        """
        return pulumi.get(self, "host_instance_type")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> str:
        """
        Filter response by storage type.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter(name="supportedDeploymentModes")
    def supported_deployment_modes(self) -> Sequence[str]:
        """
        The list of supported deployment modes.
        """
        return pulumi.get(self, "supported_deployment_modes")

    @property
    @pulumi.getter(name="supportedEngineVersions")
    def supported_engine_versions(self) -> Sequence[str]:
        """
        The list of supported engine versions.
        """
        return pulumi.get(self, "supported_engine_versions")


@pulumi.output_type
class GetInstanceTypeOfferingsBrokerInstanceOptionAvailabilityZoneResult(dict):
    def __init__(__self__, *,
                 name: str):
        """
        :param str name: Name of the Availability Zone.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the Availability Zone.
        """
        return pulumi.get(self, "name")


