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
    'GetObjectsResult',
    'AwaitableGetObjectsResult',
    'get_objects',
    'get_objects_output',
]

@pulumi.output_type
class GetObjectsResult:
    """
    A collection of values returned by getObjects.
    """
    def __init__(__self__, bucket=None, common_prefixes=None, delimiter=None, encoding_type=None, fetch_owner=None, id=None, keys=None, max_keys=None, owners=None, prefix=None, request_charged=None, request_payer=None, start_after=None):
        if bucket and not isinstance(bucket, str):
            raise TypeError("Expected argument 'bucket' to be a str")
        pulumi.set(__self__, "bucket", bucket)
        if common_prefixes and not isinstance(common_prefixes, list):
            raise TypeError("Expected argument 'common_prefixes' to be a list")
        pulumi.set(__self__, "common_prefixes", common_prefixes)
        if delimiter and not isinstance(delimiter, str):
            raise TypeError("Expected argument 'delimiter' to be a str")
        pulumi.set(__self__, "delimiter", delimiter)
        if encoding_type and not isinstance(encoding_type, str):
            raise TypeError("Expected argument 'encoding_type' to be a str")
        pulumi.set(__self__, "encoding_type", encoding_type)
        if fetch_owner and not isinstance(fetch_owner, bool):
            raise TypeError("Expected argument 'fetch_owner' to be a bool")
        pulumi.set(__self__, "fetch_owner", fetch_owner)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if keys and not isinstance(keys, list):
            raise TypeError("Expected argument 'keys' to be a list")
        pulumi.set(__self__, "keys", keys)
        if max_keys and not isinstance(max_keys, int):
            raise TypeError("Expected argument 'max_keys' to be a int")
        pulumi.set(__self__, "max_keys", max_keys)
        if owners and not isinstance(owners, list):
            raise TypeError("Expected argument 'owners' to be a list")
        pulumi.set(__self__, "owners", owners)
        if prefix and not isinstance(prefix, str):
            raise TypeError("Expected argument 'prefix' to be a str")
        pulumi.set(__self__, "prefix", prefix)
        if request_charged and not isinstance(request_charged, str):
            raise TypeError("Expected argument 'request_charged' to be a str")
        pulumi.set(__self__, "request_charged", request_charged)
        if request_payer and not isinstance(request_payer, str):
            raise TypeError("Expected argument 'request_payer' to be a str")
        pulumi.set(__self__, "request_payer", request_payer)
        if start_after and not isinstance(start_after, str):
            raise TypeError("Expected argument 'start_after' to be a str")
        pulumi.set(__self__, "start_after", start_after)

    @property
    @pulumi.getter
    def bucket(self) -> str:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="commonPrefixes")
    def common_prefixes(self) -> Sequence[str]:
        """
        List of any keys between `prefix` and the next occurrence of `delimiter` (i.e., similar to subdirectories of the `prefix` "directory"); the list is only returned when you specify `delimiter`
        """
        return pulumi.get(self, "common_prefixes")

    @property
    @pulumi.getter
    def delimiter(self) -> Optional[str]:
        return pulumi.get(self, "delimiter")

    @property
    @pulumi.getter(name="encodingType")
    def encoding_type(self) -> Optional[str]:
        return pulumi.get(self, "encoding_type")

    @property
    @pulumi.getter(name="fetchOwner")
    def fetch_owner(self) -> Optional[bool]:
        return pulumi.get(self, "fetch_owner")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def keys(self) -> Sequence[str]:
        """
        List of strings representing object keys
        """
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter(name="maxKeys")
    def max_keys(self) -> Optional[int]:
        return pulumi.get(self, "max_keys")

    @property
    @pulumi.getter
    def owners(self) -> Sequence[str]:
        """
        List of strings representing object owner IDs (see `fetch_owner` above)
        """
        return pulumi.get(self, "owners")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="requestCharged")
    def request_charged(self) -> str:
        """
        If present, indicates that the requester was successfully charged for the request.
        """
        return pulumi.get(self, "request_charged")

    @property
    @pulumi.getter(name="requestPayer")
    def request_payer(self) -> Optional[str]:
        return pulumi.get(self, "request_payer")

    @property
    @pulumi.getter(name="startAfter")
    def start_after(self) -> Optional[str]:
        return pulumi.get(self, "start_after")


class AwaitableGetObjectsResult(GetObjectsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetObjectsResult(
            bucket=self.bucket,
            common_prefixes=self.common_prefixes,
            delimiter=self.delimiter,
            encoding_type=self.encoding_type,
            fetch_owner=self.fetch_owner,
            id=self.id,
            keys=self.keys,
            max_keys=self.max_keys,
            owners=self.owners,
            prefix=self.prefix,
            request_charged=self.request_charged,
            request_payer=self.request_payer,
            start_after=self.start_after)


def get_objects(bucket: Optional[str] = None,
                delimiter: Optional[str] = None,
                encoding_type: Optional[str] = None,
                fetch_owner: Optional[bool] = None,
                max_keys: Optional[int] = None,
                prefix: Optional[str] = None,
                request_payer: Optional[str] = None,
                start_after: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetObjectsResult:
    """
    > **NOTE on `max_keys`:** Retrieving very large numbers of keys can adversely affect the provider's performance.

    The objects data source returns keys (i.e., file names) and other metadata about objects in an S3 bucket.


    :param str bucket: Lists object keys in this S3 bucket. Alternatively, an [S3 access point](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-access-points.html) ARN can be specified
    :param str delimiter: Character used to group keys (Default: none)
    :param str encoding_type: Encodes keys using this method (Default: none; besides none, only "url" can be used)
    :param bool fetch_owner: Boolean specifying whether to populate the owner list (Default: false)
    :param int max_keys: Maximum object keys to return (Default: 1000)
    :param str prefix: Limits results to object keys with this prefix (Default: none)
    :param str request_payer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If included, the only valid value is `requester`.
    :param str start_after: Returns key names lexicographically after a specific object key in your bucket (Default: none; S3 lists object keys in UTF-8 character encoding in lexicographical order)
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    __args__['delimiter'] = delimiter
    __args__['encodingType'] = encoding_type
    __args__['fetchOwner'] = fetch_owner
    __args__['maxKeys'] = max_keys
    __args__['prefix'] = prefix
    __args__['requestPayer'] = request_payer
    __args__['startAfter'] = start_after
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:s3/getObjects:getObjects', __args__, opts=opts, typ=GetObjectsResult).value

    return AwaitableGetObjectsResult(
        bucket=pulumi.get(__ret__, 'bucket'),
        common_prefixes=pulumi.get(__ret__, 'common_prefixes'),
        delimiter=pulumi.get(__ret__, 'delimiter'),
        encoding_type=pulumi.get(__ret__, 'encoding_type'),
        fetch_owner=pulumi.get(__ret__, 'fetch_owner'),
        id=pulumi.get(__ret__, 'id'),
        keys=pulumi.get(__ret__, 'keys'),
        max_keys=pulumi.get(__ret__, 'max_keys'),
        owners=pulumi.get(__ret__, 'owners'),
        prefix=pulumi.get(__ret__, 'prefix'),
        request_charged=pulumi.get(__ret__, 'request_charged'),
        request_payer=pulumi.get(__ret__, 'request_payer'),
        start_after=pulumi.get(__ret__, 'start_after'))
def get_objects_output(bucket: Optional[pulumi.Input[str]] = None,
                       delimiter: Optional[pulumi.Input[Optional[str]]] = None,
                       encoding_type: Optional[pulumi.Input[Optional[str]]] = None,
                       fetch_owner: Optional[pulumi.Input[Optional[bool]]] = None,
                       max_keys: Optional[pulumi.Input[Optional[int]]] = None,
                       prefix: Optional[pulumi.Input[Optional[str]]] = None,
                       request_payer: Optional[pulumi.Input[Optional[str]]] = None,
                       start_after: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetObjectsResult]:
    """
    > **NOTE on `max_keys`:** Retrieving very large numbers of keys can adversely affect the provider's performance.

    The objects data source returns keys (i.e., file names) and other metadata about objects in an S3 bucket.


    :param str bucket: Lists object keys in this S3 bucket. Alternatively, an [S3 access point](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-access-points.html) ARN can be specified
    :param str delimiter: Character used to group keys (Default: none)
    :param str encoding_type: Encodes keys using this method (Default: none; besides none, only "url" can be used)
    :param bool fetch_owner: Boolean specifying whether to populate the owner list (Default: false)
    :param int max_keys: Maximum object keys to return (Default: 1000)
    :param str prefix: Limits results to object keys with this prefix (Default: none)
    :param str request_payer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If included, the only valid value is `requester`.
    :param str start_after: Returns key names lexicographically after a specific object key in your bucket (Default: none; S3 lists object keys in UTF-8 character encoding in lexicographical order)
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    __args__['delimiter'] = delimiter
    __args__['encodingType'] = encoding_type
    __args__['fetchOwner'] = fetch_owner
    __args__['maxKeys'] = max_keys
    __args__['prefix'] = prefix
    __args__['requestPayer'] = request_payer
    __args__['startAfter'] = start_after
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:s3/getObjects:getObjects', __args__, opts=opts, typ=GetObjectsResult)
    return __ret__.apply(lambda __response__: GetObjectsResult(
        bucket=pulumi.get(__response__, 'bucket'),
        common_prefixes=pulumi.get(__response__, 'common_prefixes'),
        delimiter=pulumi.get(__response__, 'delimiter'),
        encoding_type=pulumi.get(__response__, 'encoding_type'),
        fetch_owner=pulumi.get(__response__, 'fetch_owner'),
        id=pulumi.get(__response__, 'id'),
        keys=pulumi.get(__response__, 'keys'),
        max_keys=pulumi.get(__response__, 'max_keys'),
        owners=pulumi.get(__response__, 'owners'),
        prefix=pulumi.get(__response__, 'prefix'),
        request_charged=pulumi.get(__response__, 'request_charged'),
        request_payer=pulumi.get(__response__, 'request_payer'),
        start_after=pulumi.get(__response__, 'start_after')))
