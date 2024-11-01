from functools import cached_property

import instructor
import openai as oa

from ..settings import settings
from ._base import BaseProvider

PROVIDER_NAME = "xai"
DEFAULT_MODEL = "grok-beta"
BASE_URL = "https://api.x.ai/v1"
DEFAULT_MAX_TOKENS = 1000


class XAI(BaseProvider):
    NAME = PROVIDER_NAME
    DEFAULT_MODEL = DEFAULT_MODEL

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or settings.get_api_key(PROVIDER_NAME)

    @cached_property
    def client(self):
        """The raw OpenAI client."""
        if not self.api_key:
            raise ValueError("XAI API key is required")
        return oa.OpenAI(
            api_key=self.api_key,
            base_url=BASE_URL,
        )

    @cached_property
    def structured_client(self):
        """A client patched with Instructor."""
        return instructor.from_openai(self.client)

    def send_conversation(self, conversation: "Conversation", **kwargs):
        """Send a conversation to the OpenAI API."""
        from ..models import Message

        messages = [
            {"role": msg.role, "content": msg.text} for msg in conversation.messages
        ]

        response = self.client.chat.completions.create(
            model=conversation.llm_model or self.DEFAULT_MODEL,
            messages=messages,
            **kwargs,
        )

        # Get the response content from the OpenAI response
        assistant_message = response.choices[0].message

        # Create and return a properly formatted Message instance
        return Message(
            role="assistant",
            text=assistant_message.content,
            raw=response,
            llm_model=conversation.llm_model or self.DEFAULT_MODEL,
            llm_provider=PROVIDER_NAME,
        )

    def structured_response(self, prompt: str, response_model, *, llm_model: str):
        raise NotImplementedError("XAI does not support structured responses")

    def generate_text(self, prompt: str, *, llm_model: str, **kwargs):
        messages = [
            {"role": "user", "content": prompt},
        ]

        response = self.client.chat.completions.create(
            messages=messages,
            model=llm_model or self.DEFAULT_MODEL,
            **kwargs,
        )

        return response.choices[0].message.content
