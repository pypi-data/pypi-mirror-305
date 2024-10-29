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
    'GroupExternalIdArgs',
    'GroupExternalIdArgsDict',
    'UserAddressesArgs',
    'UserAddressesArgsDict',
    'UserEmailsArgs',
    'UserEmailsArgsDict',
    'UserExternalIdArgs',
    'UserExternalIdArgsDict',
    'UserNameArgs',
    'UserNameArgsDict',
    'UserPhoneNumbersArgs',
    'UserPhoneNumbersArgsDict',
    'GetGroupAlternateIdentifierArgs',
    'GetGroupAlternateIdentifierArgsDict',
    'GetGroupAlternateIdentifierExternalIdArgs',
    'GetGroupAlternateIdentifierExternalIdArgsDict',
    'GetGroupAlternateIdentifierUniqueAttributeArgs',
    'GetGroupAlternateIdentifierUniqueAttributeArgsDict',
    'GetGroupFilterArgs',
    'GetGroupFilterArgsDict',
    'GetUserAlternateIdentifierArgs',
    'GetUserAlternateIdentifierArgsDict',
    'GetUserAlternateIdentifierExternalIdArgs',
    'GetUserAlternateIdentifierExternalIdArgsDict',
    'GetUserAlternateIdentifierUniqueAttributeArgs',
    'GetUserAlternateIdentifierUniqueAttributeArgsDict',
    'GetUserFilterArgs',
    'GetUserFilterArgsDict',
]

MYPY = False

if not MYPY:
    class GroupExternalIdArgsDict(TypedDict):
        id: NotRequired[pulumi.Input[str]]
        """
        The identifier issued to this resource by an external identity provider.
        """
        issuer: NotRequired[pulumi.Input[str]]
        """
        The issuer for an external identifier.
        """
elif False:
    GroupExternalIdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GroupExternalIdArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] id: The identifier issued to this resource by an external identity provider.
        :param pulumi.Input[str] issuer: The issuer for an external identifier.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if issuer is not None:
            pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier issued to this resource by an external identity provider.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[str]]:
        """
        The issuer for an external identifier.
        """
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issuer", value)


if not MYPY:
    class UserAddressesArgsDict(TypedDict):
        country: NotRequired[pulumi.Input[str]]
        """
        The country that this address is in.
        """
        formatted: NotRequired[pulumi.Input[str]]
        """
        The name that is typically displayed when the address is shown for display.
        """
        locality: NotRequired[pulumi.Input[str]]
        """
        The address locality.
        """
        postal_code: NotRequired[pulumi.Input[str]]
        """
        The postal code of the address.
        """
        primary: NotRequired[pulumi.Input[bool]]
        """
        When `true`, this is the primary address associated with the user.
        """
        region: NotRequired[pulumi.Input[str]]
        """
        The region of the address.
        """
        street_address: NotRequired[pulumi.Input[str]]
        """
        The street of the address.
        """
        type: NotRequired[pulumi.Input[str]]
        """
        The type of address.
        """
elif False:
    UserAddressesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class UserAddressesArgs:
    def __init__(__self__, *,
                 country: Optional[pulumi.Input[str]] = None,
                 formatted: Optional[pulumi.Input[str]] = None,
                 locality: Optional[pulumi.Input[str]] = None,
                 postal_code: Optional[pulumi.Input[str]] = None,
                 primary: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 street_address: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] country: The country that this address is in.
        :param pulumi.Input[str] formatted: The name that is typically displayed when the address is shown for display.
        :param pulumi.Input[str] locality: The address locality.
        :param pulumi.Input[str] postal_code: The postal code of the address.
        :param pulumi.Input[bool] primary: When `true`, this is the primary address associated with the user.
        :param pulumi.Input[str] region: The region of the address.
        :param pulumi.Input[str] street_address: The street of the address.
        :param pulumi.Input[str] type: The type of address.
        """
        if country is not None:
            pulumi.set(__self__, "country", country)
        if formatted is not None:
            pulumi.set(__self__, "formatted", formatted)
        if locality is not None:
            pulumi.set(__self__, "locality", locality)
        if postal_code is not None:
            pulumi.set(__self__, "postal_code", postal_code)
        if primary is not None:
            pulumi.set(__self__, "primary", primary)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if street_address is not None:
            pulumi.set(__self__, "street_address", street_address)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        """
        The country that this address is in.
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter
    def formatted(self) -> Optional[pulumi.Input[str]]:
        """
        The name that is typically displayed when the address is shown for display.
        """
        return pulumi.get(self, "formatted")

    @formatted.setter
    def formatted(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "formatted", value)

    @property
    @pulumi.getter
    def locality(self) -> Optional[pulumi.Input[str]]:
        """
        The address locality.
        """
        return pulumi.get(self, "locality")

    @locality.setter
    def locality(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "locality", value)

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[str]]:
        """
        The postal code of the address.
        """
        return pulumi.get(self, "postal_code")

    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "postal_code", value)

    @property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, this is the primary address associated with the user.
        """
        return pulumi.get(self, "primary")

    @primary.setter
    def primary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "primary", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the address.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[pulumi.Input[str]]:
        """
        The street of the address.
        """
        return pulumi.get(self, "street_address")

    @street_address.setter
    def street_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "street_address", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of address.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


if not MYPY:
    class UserEmailsArgsDict(TypedDict):
        primary: NotRequired[pulumi.Input[bool]]
        """
        When `true`, this is the primary email associated with the user.
        """
        type: NotRequired[pulumi.Input[str]]
        """
        The type of email.
        """
        value: NotRequired[pulumi.Input[str]]
        """
        The email address. This value must be unique across the identity store.
        """
elif False:
    UserEmailsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class UserEmailsArgs:
    def __init__(__self__, *,
                 primary: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] primary: When `true`, this is the primary email associated with the user.
        :param pulumi.Input[str] type: The type of email.
        :param pulumi.Input[str] value: The email address. This value must be unique across the identity store.
        """
        if primary is not None:
            pulumi.set(__self__, "primary", primary)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, this is the primary email associated with the user.
        """
        return pulumi.get(self, "primary")

    @primary.setter
    def primary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "primary", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of email.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The email address. This value must be unique across the identity store.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


if not MYPY:
    class UserExternalIdArgsDict(TypedDict):
        id: NotRequired[pulumi.Input[str]]
        """
        The identifier issued to this resource by an external identity provider.
        """
        issuer: NotRequired[pulumi.Input[str]]
        """
        The issuer for an external identifier.
        """
elif False:
    UserExternalIdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class UserExternalIdArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] id: The identifier issued to this resource by an external identity provider.
        :param pulumi.Input[str] issuer: The issuer for an external identifier.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if issuer is not None:
            pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier issued to this resource by an external identity provider.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[str]]:
        """
        The issuer for an external identifier.
        """
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issuer", value)


if not MYPY:
    class UserNameArgsDict(TypedDict):
        family_name: pulumi.Input[str]
        """
        The family name of the user.
        """
        given_name: pulumi.Input[str]
        """
        The given name of the user.

        The following arguments are optional:
        """
        formatted: NotRequired[pulumi.Input[str]]
        """
        The name that is typically displayed when the name is shown for display.
        """
        honorific_prefix: NotRequired[pulumi.Input[str]]
        """
        The honorific prefix of the user.
        """
        honorific_suffix: NotRequired[pulumi.Input[str]]
        """
        The honorific suffix of the user.
        """
        middle_name: NotRequired[pulumi.Input[str]]
        """
        The middle name of the user.
        """
elif False:
    UserNameArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class UserNameArgs:
    def __init__(__self__, *,
                 family_name: pulumi.Input[str],
                 given_name: pulumi.Input[str],
                 formatted: Optional[pulumi.Input[str]] = None,
                 honorific_prefix: Optional[pulumi.Input[str]] = None,
                 honorific_suffix: Optional[pulumi.Input[str]] = None,
                 middle_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] family_name: The family name of the user.
        :param pulumi.Input[str] given_name: The given name of the user.
               
               The following arguments are optional:
        :param pulumi.Input[str] formatted: The name that is typically displayed when the name is shown for display.
        :param pulumi.Input[str] honorific_prefix: The honorific prefix of the user.
        :param pulumi.Input[str] honorific_suffix: The honorific suffix of the user.
        :param pulumi.Input[str] middle_name: The middle name of the user.
        """
        pulumi.set(__self__, "family_name", family_name)
        pulumi.set(__self__, "given_name", given_name)
        if formatted is not None:
            pulumi.set(__self__, "formatted", formatted)
        if honorific_prefix is not None:
            pulumi.set(__self__, "honorific_prefix", honorific_prefix)
        if honorific_suffix is not None:
            pulumi.set(__self__, "honorific_suffix", honorific_suffix)
        if middle_name is not None:
            pulumi.set(__self__, "middle_name", middle_name)

    @property
    @pulumi.getter(name="familyName")
    def family_name(self) -> pulumi.Input[str]:
        """
        The family name of the user.
        """
        return pulumi.get(self, "family_name")

    @family_name.setter
    def family_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "family_name", value)

    @property
    @pulumi.getter(name="givenName")
    def given_name(self) -> pulumi.Input[str]:
        """
        The given name of the user.

        The following arguments are optional:
        """
        return pulumi.get(self, "given_name")

    @given_name.setter
    def given_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "given_name", value)

    @property
    @pulumi.getter
    def formatted(self) -> Optional[pulumi.Input[str]]:
        """
        The name that is typically displayed when the name is shown for display.
        """
        return pulumi.get(self, "formatted")

    @formatted.setter
    def formatted(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "formatted", value)

    @property
    @pulumi.getter(name="honorificPrefix")
    def honorific_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The honorific prefix of the user.
        """
        return pulumi.get(self, "honorific_prefix")

    @honorific_prefix.setter
    def honorific_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "honorific_prefix", value)

    @property
    @pulumi.getter(name="honorificSuffix")
    def honorific_suffix(self) -> Optional[pulumi.Input[str]]:
        """
        The honorific suffix of the user.
        """
        return pulumi.get(self, "honorific_suffix")

    @honorific_suffix.setter
    def honorific_suffix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "honorific_suffix", value)

    @property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[pulumi.Input[str]]:
        """
        The middle name of the user.
        """
        return pulumi.get(self, "middle_name")

    @middle_name.setter
    def middle_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "middle_name", value)


if not MYPY:
    class UserPhoneNumbersArgsDict(TypedDict):
        primary: NotRequired[pulumi.Input[bool]]
        """
        When `true`, this is the primary phone number associated with the user.
        """
        type: NotRequired[pulumi.Input[str]]
        """
        The type of phone number.
        """
        value: NotRequired[pulumi.Input[str]]
        """
        The user's phone number.
        """
elif False:
    UserPhoneNumbersArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class UserPhoneNumbersArgs:
    def __init__(__self__, *,
                 primary: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] primary: When `true`, this is the primary phone number associated with the user.
        :param pulumi.Input[str] type: The type of phone number.
        :param pulumi.Input[str] value: The user's phone number.
        """
        if primary is not None:
            pulumi.set(__self__, "primary", primary)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, this is the primary phone number associated with the user.
        """
        return pulumi.get(self, "primary")

    @primary.setter
    def primary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "primary", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of phone number.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The user's phone number.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


if not MYPY:
    class GetGroupAlternateIdentifierArgsDict(TypedDict):
        external_id: NotRequired['GetGroupAlternateIdentifierExternalIdArgsDict']
        """
        Configuration block for filtering by the identifier issued by an external identity provider. Detailed below.
        """
        unique_attribute: NotRequired['GetGroupAlternateIdentifierUniqueAttributeArgsDict']
        """
        An entity attribute that's unique to a specific entity. Detailed below.

        > Exactly one of the above arguments must be provided.
        """
elif False:
    GetGroupAlternateIdentifierArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetGroupAlternateIdentifierArgs:
    def __init__(__self__, *,
                 external_id: Optional['GetGroupAlternateIdentifierExternalIdArgs'] = None,
                 unique_attribute: Optional['GetGroupAlternateIdentifierUniqueAttributeArgs'] = None):
        """
        :param 'GetGroupAlternateIdentifierExternalIdArgs' external_id: Configuration block for filtering by the identifier issued by an external identity provider. Detailed below.
        :param 'GetGroupAlternateIdentifierUniqueAttributeArgs' unique_attribute: An entity attribute that's unique to a specific entity. Detailed below.
               
               > Exactly one of the above arguments must be provided.
        """
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if unique_attribute is not None:
            pulumi.set(__self__, "unique_attribute", unique_attribute)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional['GetGroupAlternateIdentifierExternalIdArgs']:
        """
        Configuration block for filtering by the identifier issued by an external identity provider. Detailed below.
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional['GetGroupAlternateIdentifierExternalIdArgs']):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="uniqueAttribute")
    def unique_attribute(self) -> Optional['GetGroupAlternateIdentifierUniqueAttributeArgs']:
        """
        An entity attribute that's unique to a specific entity. Detailed below.

        > Exactly one of the above arguments must be provided.
        """
        return pulumi.get(self, "unique_attribute")

    @unique_attribute.setter
    def unique_attribute(self, value: Optional['GetGroupAlternateIdentifierUniqueAttributeArgs']):
        pulumi.set(self, "unique_attribute", value)


if not MYPY:
    class GetGroupAlternateIdentifierExternalIdArgsDict(TypedDict):
        id: str
        """
        The identifier issued to this resource by an external identity provider.
        """
        issuer: str
        """
        The issuer for an external identifier.
        """
elif False:
    GetGroupAlternateIdentifierExternalIdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetGroupAlternateIdentifierExternalIdArgs:
    def __init__(__self__, *,
                 id: str,
                 issuer: str):
        """
        :param str id: The identifier issued to this resource by an external identity provider.
        :param str issuer: The issuer for an external identifier.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier issued to this resource by an external identity provider.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: str):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def issuer(self) -> str:
        """
        The issuer for an external identifier.
        """
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: str):
        pulumi.set(self, "issuer", value)


if not MYPY:
    class GetGroupAlternateIdentifierUniqueAttributeArgsDict(TypedDict):
        attribute_path: str
        """
        Attribute path that is used to specify which attribute name to search. For example: `DisplayName`. Refer to the [Group data type](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html).
        """
        attribute_value: str
        """
        Value for an attribute.
        """
elif False:
    GetGroupAlternateIdentifierUniqueAttributeArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetGroupAlternateIdentifierUniqueAttributeArgs:
    def __init__(__self__, *,
                 attribute_path: str,
                 attribute_value: str):
        """
        :param str attribute_path: Attribute path that is used to specify which attribute name to search. For example: `DisplayName`. Refer to the [Group data type](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html).
        :param str attribute_value: Value for an attribute.
        """
        pulumi.set(__self__, "attribute_path", attribute_path)
        pulumi.set(__self__, "attribute_value", attribute_value)

    @property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> str:
        """
        Attribute path that is used to specify which attribute name to search. For example: `DisplayName`. Refer to the [Group data type](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html).
        """
        return pulumi.get(self, "attribute_path")

    @attribute_path.setter
    def attribute_path(self, value: str):
        pulumi.set(self, "attribute_path", value)

    @property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> str:
        """
        Value for an attribute.
        """
        return pulumi.get(self, "attribute_value")

    @attribute_value.setter
    def attribute_value(self, value: str):
        pulumi.set(self, "attribute_value", value)


if not MYPY:
    class GetGroupFilterArgsDict(TypedDict):
        attribute_path: str
        """
        Attribute path that is used to specify which attribute name to search. Currently, `DisplayName` is the only valid attribute path.
        """
        attribute_value: str
        """
        Value for an attribute.
        """
elif False:
    GetGroupFilterArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetGroupFilterArgs:
    def __init__(__self__, *,
                 attribute_path: str,
                 attribute_value: str):
        """
        :param str attribute_path: Attribute path that is used to specify which attribute name to search. Currently, `DisplayName` is the only valid attribute path.
        :param str attribute_value: Value for an attribute.
        """
        pulumi.set(__self__, "attribute_path", attribute_path)
        pulumi.set(__self__, "attribute_value", attribute_value)

    @property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> str:
        """
        Attribute path that is used to specify which attribute name to search. Currently, `DisplayName` is the only valid attribute path.
        """
        return pulumi.get(self, "attribute_path")

    @attribute_path.setter
    def attribute_path(self, value: str):
        pulumi.set(self, "attribute_path", value)

    @property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> str:
        """
        Value for an attribute.
        """
        return pulumi.get(self, "attribute_value")

    @attribute_value.setter
    def attribute_value(self, value: str):
        pulumi.set(self, "attribute_value", value)


if not MYPY:
    class GetUserAlternateIdentifierArgsDict(TypedDict):
        external_id: NotRequired['GetUserAlternateIdentifierExternalIdArgsDict']
        """
        Configuration block for filtering by the identifier issued by an external identity provider. Detailed below.
        """
        unique_attribute: NotRequired['GetUserAlternateIdentifierUniqueAttributeArgsDict']
        """
        An entity attribute that's unique to a specific entity. Detailed below.

        > Exactly one of the above arguments must be provided.
        """
elif False:
    GetUserAlternateIdentifierArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetUserAlternateIdentifierArgs:
    def __init__(__self__, *,
                 external_id: Optional['GetUserAlternateIdentifierExternalIdArgs'] = None,
                 unique_attribute: Optional['GetUserAlternateIdentifierUniqueAttributeArgs'] = None):
        """
        :param 'GetUserAlternateIdentifierExternalIdArgs' external_id: Configuration block for filtering by the identifier issued by an external identity provider. Detailed below.
        :param 'GetUserAlternateIdentifierUniqueAttributeArgs' unique_attribute: An entity attribute that's unique to a specific entity. Detailed below.
               
               > Exactly one of the above arguments must be provided.
        """
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if unique_attribute is not None:
            pulumi.set(__self__, "unique_attribute", unique_attribute)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional['GetUserAlternateIdentifierExternalIdArgs']:
        """
        Configuration block for filtering by the identifier issued by an external identity provider. Detailed below.
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional['GetUserAlternateIdentifierExternalIdArgs']):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="uniqueAttribute")
    def unique_attribute(self) -> Optional['GetUserAlternateIdentifierUniqueAttributeArgs']:
        """
        An entity attribute that's unique to a specific entity. Detailed below.

        > Exactly one of the above arguments must be provided.
        """
        return pulumi.get(self, "unique_attribute")

    @unique_attribute.setter
    def unique_attribute(self, value: Optional['GetUserAlternateIdentifierUniqueAttributeArgs']):
        pulumi.set(self, "unique_attribute", value)


if not MYPY:
    class GetUserAlternateIdentifierExternalIdArgsDict(TypedDict):
        id: str
        """
        The identifier issued to this resource by an external identity provider.
        """
        issuer: str
        """
        The issuer for an external identifier.
        """
elif False:
    GetUserAlternateIdentifierExternalIdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetUserAlternateIdentifierExternalIdArgs:
    def __init__(__self__, *,
                 id: str,
                 issuer: str):
        """
        :param str id: The identifier issued to this resource by an external identity provider.
        :param str issuer: The issuer for an external identifier.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier issued to this resource by an external identity provider.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: str):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def issuer(self) -> str:
        """
        The issuer for an external identifier.
        """
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: str):
        pulumi.set(self, "issuer", value)


if not MYPY:
    class GetUserAlternateIdentifierUniqueAttributeArgsDict(TypedDict):
        attribute_path: str
        """
        Attribute path that is used to specify which attribute name to search. For example: `UserName`. Refer to the [User data type](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html).
        """
        attribute_value: str
        """
        Value for an attribute.
        """
elif False:
    GetUserAlternateIdentifierUniqueAttributeArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetUserAlternateIdentifierUniqueAttributeArgs:
    def __init__(__self__, *,
                 attribute_path: str,
                 attribute_value: str):
        """
        :param str attribute_path: Attribute path that is used to specify which attribute name to search. For example: `UserName`. Refer to the [User data type](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html).
        :param str attribute_value: Value for an attribute.
        """
        pulumi.set(__self__, "attribute_path", attribute_path)
        pulumi.set(__self__, "attribute_value", attribute_value)

    @property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> str:
        """
        Attribute path that is used to specify which attribute name to search. For example: `UserName`. Refer to the [User data type](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html).
        """
        return pulumi.get(self, "attribute_path")

    @attribute_path.setter
    def attribute_path(self, value: str):
        pulumi.set(self, "attribute_path", value)

    @property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> str:
        """
        Value for an attribute.
        """
        return pulumi.get(self, "attribute_value")

    @attribute_value.setter
    def attribute_value(self, value: str):
        pulumi.set(self, "attribute_value", value)


if not MYPY:
    class GetUserFilterArgsDict(TypedDict):
        attribute_path: str
        """
        Attribute path that is used to specify which attribute name to search. Currently, `UserName` is the only valid attribute path.
        """
        attribute_value: str
        """
        Value for an attribute.
        """
elif False:
    GetUserFilterArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetUserFilterArgs:
    def __init__(__self__, *,
                 attribute_path: str,
                 attribute_value: str):
        """
        :param str attribute_path: Attribute path that is used to specify which attribute name to search. Currently, `UserName` is the only valid attribute path.
        :param str attribute_value: Value for an attribute.
        """
        pulumi.set(__self__, "attribute_path", attribute_path)
        pulumi.set(__self__, "attribute_value", attribute_value)

    @property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> str:
        """
        Attribute path that is used to specify which attribute name to search. Currently, `UserName` is the only valid attribute path.
        """
        return pulumi.get(self, "attribute_path")

    @attribute_path.setter
    def attribute_path(self, value: str):
        pulumi.set(self, "attribute_path", value)

    @property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> str:
        """
        Value for an attribute.
        """
        return pulumi.get(self, "attribute_value")

    @attribute_value.setter
    def attribute_value(self, value: str):
        pulumi.set(self, "attribute_value", value)


