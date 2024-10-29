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
    'OrganizationConfigurationAutoEnable',
]

@pulumi.output_type
class OrganizationConfigurationAutoEnable(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lambda":
            suggest = "lambda_"
        elif key == "lambdaCode":
            suggest = "lambda_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OrganizationConfigurationAutoEnable. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OrganizationConfigurationAutoEnable.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OrganizationConfigurationAutoEnable.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ec2: bool,
                 ecr: bool,
                 lambda_: Optional[bool] = None,
                 lambda_code: Optional[bool] = None):
        """
        :param bool ec2: Whether Amazon EC2 scans are automatically enabled for new members of your Amazon Inspector organization.
        :param bool ecr: Whether Amazon ECR scans are automatically enabled for new members of your Amazon Inspector organization.
        :param bool lambda_: Whether Lambda Function scans are automatically enabled for new members of your Amazon Inspector organization.
        :param bool lambda_code: Whether AWS Lambda code scans are automatically enabled for new members of your Amazon Inspector organization. **Note:** Lambda code scanning requires Lambda standard scanning to be activated. Consequently, if you are setting this argument to `true`, you must also set the `lambda` argument to `true`. See [Scanning AWS Lambda functions with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html#lambda-code-scans) for more information.
        """
        pulumi.set(__self__, "ec2", ec2)
        pulumi.set(__self__, "ecr", ecr)
        if lambda_ is not None:
            pulumi.set(__self__, "lambda_", lambda_)
        if lambda_code is not None:
            pulumi.set(__self__, "lambda_code", lambda_code)

    @property
    @pulumi.getter
    def ec2(self) -> bool:
        """
        Whether Amazon EC2 scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        return pulumi.get(self, "ec2")

    @property
    @pulumi.getter
    def ecr(self) -> bool:
        """
        Whether Amazon ECR scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        return pulumi.get(self, "ecr")

    @property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[bool]:
        """
        Whether Lambda Function scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        return pulumi.get(self, "lambda_")

    @property
    @pulumi.getter(name="lambdaCode")
    def lambda_code(self) -> Optional[bool]:
        """
        Whether AWS Lambda code scans are automatically enabled for new members of your Amazon Inspector organization. **Note:** Lambda code scanning requires Lambda standard scanning to be activated. Consequently, if you are setting this argument to `true`, you must also set the `lambda` argument to `true`. See [Scanning AWS Lambda functions with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html#lambda-code-scans) for more information.
        """
        return pulumi.get(self, "lambda_code")


