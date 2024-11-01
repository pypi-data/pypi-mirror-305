from functools import cached_property
from typing import Type, TypeVar

import instructor
import ollama as ol
from openai import OpenAI
from pydantic import BaseModel

from ..settings import settings
from ._base import BaseProvider

T = TypeVar("T", bound=BaseModel)


PROVIDER_NAME = "ollama"
DEFAULT_MODEL = "llama3.2"
DEFAULT_TIMEOUT = 60


class Ollama(BaseProvider):
    NAME = PROVIDER_NAME
    DEFAULT_MODEL = DEFAULT_MODEL
    TIMEOUT = DEFAULT_TIMEOUT

    def __init__(self, host_url: str | None = None):
        self.host_url = host_url or settings.OLLAMA_HOST_URL

    @cached_property
    def client(self):
        """The raw Ollama client."""
        if not self.host_url:
            raise ValueError("No ollama host url provided")
        return ol.Client(timeout=self.TIMEOUT, host=self.host_url)

    @cached_property
    def structured_client(self) -> instructor.Instructor:
        """A client patched with Instructor."""
        return instructor.from_openai(
            OpenAI(
                base_url=f"{self.host_url}/v1",
                api_key="ollama",
            ),
            mode=instructor.Mode.JSON,
        )

    def send_conversation(self, conversation: "Conversation") -> "Message":
        """Send a conversation to the Ollama API."""
        from ..models import Message

        messages = [
            {"role": msg.role, "content": msg.text} for msg in conversation.messages
        ]
        response = self.client.chat(
            model=conversation.llm_model or DEFAULT_MODEL, messages=messages
        )
        assistant_message = response.get("message")

        # Create and return a properly formatted Message instance
        return Message(
            role="assistant",
            text=assistant_message.get("content"),
            raw=response,
            llm_model=conversation.llm_model or self.DEFAULT_MODEL,
            llm_provider=PROVIDER_NAME,
        )

    def structured_response(
        self,
        prompt: str,
        response_model: Type[T],
        *,
        llm_model: str | None = None,
        **kwargs,
    ) -> T:
        """Get a structured response from the Ollama API."""
        messages = [
            {"role": "user", "content": prompt},
        ]

        response = self.structured_client.chat.completions.create(
            messages=messages,
            model=llm_model or self.DEFAULT_MODEL,
            response_model=response_model,
            **kwargs,
        )
        return response

    def generate_text(self, prompt: str, *, llm_model: str | None = None) -> str:
        """Generate text using the Ollama API."""
        messages = [
            {"role": "user", "content": prompt},
        ]

        response = self.client.chat(
            messages=messages, model=llm_model or self.DEFAULT_MODEL
        )

        return response.get("message", {}).get("content", "")
