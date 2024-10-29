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
    'StreamKinesisConfiguration',
]

@pulumi.output_type
class StreamKinesisConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "streamArn":
            suggest = "stream_arn"
        elif key == "aggregationEnabled":
            suggest = "aggregation_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StreamKinesisConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StreamKinesisConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StreamKinesisConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 stream_arn: str,
                 aggregation_enabled: Optional[bool] = None):
        """
        :param str stream_arn: The Amazon Resource Name (ARN) of the Kinesis Data Streams resource.
        :param bool aggregation_enabled: Enables QLDB to publish multiple data records in a single Kinesis Data Streams record, increasing the number of records sent per API call. Default: `true`.
        """
        pulumi.set(__self__, "stream_arn", stream_arn)
        if aggregation_enabled is not None:
            pulumi.set(__self__, "aggregation_enabled", aggregation_enabled)

    @property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the Kinesis Data Streams resource.
        """
        return pulumi.get(self, "stream_arn")

    @property
    @pulumi.getter(name="aggregationEnabled")
    def aggregation_enabled(self) -> Optional[bool]:
        """
        Enables QLDB to publish multiple data records in a single Kinesis Data Streams record, increasing the number of records sent per API call. Default: `true`.
        """
        return pulumi.get(self, "aggregation_enabled")


