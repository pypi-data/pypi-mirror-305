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
    'GetVoicesResult',
    'AwaitableGetVoicesResult',
    'get_voices',
    'get_voices_output',
]

@pulumi.output_type
class GetVoicesResult:
    """
    A collection of values returned by getVoices.
    """
    def __init__(__self__, engine=None, id=None, include_additional_language_codes=None, language_code=None, voices=None):
        if engine and not isinstance(engine, str):
            raise TypeError("Expected argument 'engine' to be a str")
        pulumi.set(__self__, "engine", engine)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_additional_language_codes and not isinstance(include_additional_language_codes, bool):
            raise TypeError("Expected argument 'include_additional_language_codes' to be a bool")
        pulumi.set(__self__, "include_additional_language_codes", include_additional_language_codes)
        if language_code and not isinstance(language_code, str):
            raise TypeError("Expected argument 'language_code' to be a str")
        pulumi.set(__self__, "language_code", language_code)
        if voices and not isinstance(voices, list):
            raise TypeError("Expected argument 'voices' to be a list")
        pulumi.set(__self__, "voices", voices)

    @property
    @pulumi.getter
    def engine(self) -> Optional[str]:
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Amazon Polly assigned voice ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includeAdditionalLanguageCodes")
    def include_additional_language_codes(self) -> Optional[bool]:
        return pulumi.get(self, "include_additional_language_codes")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[str]:
        """
        Language code of the voice.
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def voices(self) -> Optional[Sequence['outputs.GetVoicesVoiceResult']]:
        """
        List of voices with their properties. See `voices` Attribute Reference below.
        """
        return pulumi.get(self, "voices")


class AwaitableGetVoicesResult(GetVoicesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVoicesResult(
            engine=self.engine,
            id=self.id,
            include_additional_language_codes=self.include_additional_language_codes,
            language_code=self.language_code,
            voices=self.voices)


def get_voices(engine: Optional[str] = None,
               include_additional_language_codes: Optional[bool] = None,
               language_code: Optional[str] = None,
               voices: Optional[Sequence[Union['GetVoicesVoiceArgs', 'GetVoicesVoiceArgsDict']]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVoicesResult:
    """
    Data source for managing an AWS Polly Voices.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.polly.get_voices()
    ```

    ### With Language Code

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.polly.get_voices(language_code="en-GB")
    ```


    :param str engine: Engine used by Amazon Polly when processing input text for speech synthesis. Valid values are `standard`, `neural`, and `long-form`.
    :param bool include_additional_language_codes: Whether to return any bilingual voices that use the specified language as an additional language.
    :param str language_code: Language identification tag for filtering the list of voices returned. If not specified, all available voices are returned.
    :param Sequence[Union['GetVoicesVoiceArgs', 'GetVoicesVoiceArgsDict']] voices: List of voices with their properties. See `voices` Attribute Reference below.
    """
    __args__ = dict()
    __args__['engine'] = engine
    __args__['includeAdditionalLanguageCodes'] = include_additional_language_codes
    __args__['languageCode'] = language_code
    __args__['voices'] = voices
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:polly/getVoices:getVoices', __args__, opts=opts, typ=GetVoicesResult).value

    return AwaitableGetVoicesResult(
        engine=pulumi.get(__ret__, 'engine'),
        id=pulumi.get(__ret__, 'id'),
        include_additional_language_codes=pulumi.get(__ret__, 'include_additional_language_codes'),
        language_code=pulumi.get(__ret__, 'language_code'),
        voices=pulumi.get(__ret__, 'voices'))
def get_voices_output(engine: Optional[pulumi.Input[Optional[str]]] = None,
                      include_additional_language_codes: Optional[pulumi.Input[Optional[bool]]] = None,
                      language_code: Optional[pulumi.Input[Optional[str]]] = None,
                      voices: Optional[pulumi.Input[Optional[Sequence[Union['GetVoicesVoiceArgs', 'GetVoicesVoiceArgsDict']]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVoicesResult]:
    """
    Data source for managing an AWS Polly Voices.

    ## Example Usage

    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.polly.get_voices()
    ```

    ### With Language Code

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.polly.get_voices(language_code="en-GB")
    ```


    :param str engine: Engine used by Amazon Polly when processing input text for speech synthesis. Valid values are `standard`, `neural`, and `long-form`.
    :param bool include_additional_language_codes: Whether to return any bilingual voices that use the specified language as an additional language.
    :param str language_code: Language identification tag for filtering the list of voices returned. If not specified, all available voices are returned.
    :param Sequence[Union['GetVoicesVoiceArgs', 'GetVoicesVoiceArgsDict']] voices: List of voices with their properties. See `voices` Attribute Reference below.
    """
    __args__ = dict()
    __args__['engine'] = engine
    __args__['includeAdditionalLanguageCodes'] = include_additional_language_codes
    __args__['languageCode'] = language_code
    __args__['voices'] = voices
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:polly/getVoices:getVoices', __args__, opts=opts, typ=GetVoicesResult)
    return __ret__.apply(lambda __response__: GetVoicesResult(
        engine=pulumi.get(__response__, 'engine'),
        id=pulumi.get(__response__, 'id'),
        include_additional_language_codes=pulumi.get(__response__, 'include_additional_language_codes'),
        language_code=pulumi.get(__response__, 'language_code'),
        voices=pulumi.get(__response__, 'voices')))
