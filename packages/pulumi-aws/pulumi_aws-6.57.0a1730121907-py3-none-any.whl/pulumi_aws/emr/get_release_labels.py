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
    'GetReleaseLabelsResult',
    'AwaitableGetReleaseLabelsResult',
    'get_release_labels',
    'get_release_labels_output',
]

@pulumi.output_type
class GetReleaseLabelsResult:
    """
    A collection of values returned by getReleaseLabels.
    """
    def __init__(__self__, filters=None, id=None, release_labels=None):
        if filters and not isinstance(filters, dict):
            raise TypeError("Expected argument 'filters' to be a dict")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if release_labels and not isinstance(release_labels, list):
            raise TypeError("Expected argument 'release_labels' to be a list")
        pulumi.set(__self__, "release_labels", release_labels)

    @property
    @pulumi.getter
    def filters(self) -> Optional['outputs.GetReleaseLabelsFiltersResult']:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="releaseLabels")
    def release_labels(self) -> Sequence[str]:
        """
        Returned release labels.
        """
        return pulumi.get(self, "release_labels")


class AwaitableGetReleaseLabelsResult(GetReleaseLabelsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReleaseLabelsResult(
            filters=self.filters,
            id=self.id,
            release_labels=self.release_labels)


def get_release_labels(filters: Optional[Union['GetReleaseLabelsFiltersArgs', 'GetReleaseLabelsFiltersArgsDict']] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReleaseLabelsResult:
    """
    Retrieve information about EMR Release Labels.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.emr.get_release_labels(filters={
        "application": "spark@2.1.0",
        "prefix": "emr-5",
    })
    ```


    :param Union['GetReleaseLabelsFiltersArgs', 'GetReleaseLabelsFiltersArgsDict'] filters: Filters the results of the request. Prefix specifies the prefix of release labels to return. Application specifies the application (with/without version) of release labels to return. See Filters.
    """
    __args__ = dict()
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:emr/getReleaseLabels:getReleaseLabels', __args__, opts=opts, typ=GetReleaseLabelsResult).value

    return AwaitableGetReleaseLabelsResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        release_labels=pulumi.get(__ret__, 'release_labels'))
def get_release_labels_output(filters: Optional[pulumi.Input[Optional[Union['GetReleaseLabelsFiltersArgs', 'GetReleaseLabelsFiltersArgsDict']]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReleaseLabelsResult]:
    """
    Retrieve information about EMR Release Labels.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.emr.get_release_labels(filters={
        "application": "spark@2.1.0",
        "prefix": "emr-5",
    })
    ```


    :param Union['GetReleaseLabelsFiltersArgs', 'GetReleaseLabelsFiltersArgsDict'] filters: Filters the results of the request. Prefix specifies the prefix of release labels to return. Application specifies the application (with/without version) of release labels to return. See Filters.
    """
    __args__ = dict()
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:emr/getReleaseLabels:getReleaseLabels', __args__, opts=opts, typ=GetReleaseLabelsResult)
    return __ret__.apply(lambda __response__: GetReleaseLabelsResult(
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        release_labels=pulumi.get(__response__, 'release_labels')))
