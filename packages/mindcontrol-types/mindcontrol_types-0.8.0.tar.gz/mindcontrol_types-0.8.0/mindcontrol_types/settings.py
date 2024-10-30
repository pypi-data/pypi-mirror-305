from .anthropic import AnthropicSettingsV1
from .openai import OpenAISettingsV1
from typing import Union, TypeAlias


SettingsV1 : TypeAlias = Union[AnthropicSettingsV1, OpenAISettingsV1]
