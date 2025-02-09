# LLM Class definition

import time

from openai import OpenAI
from openai.types.chat import ChatCompletion
from pydantic import BaseModel, field_validator

DEEPINFRA_API_KEY = None


class BaseLLMConfig(BaseModel):
    provider: str
    llm_model_name: str
    api_key: str
    base_url: str | None = None
    system_prompt: str | None = None


class BaseLLM:
    """Base class for LLM Models"""

    def __init__(self, config: BaseLLMConfig):
        self.config = config
        self.client = OpenAI(api_key=config.api_key, base_url=config.base_url)

    def prepare_msg(self, prompt: str, history: list[dict], system_prompt: str | None):

        system_msg = (
            [{"role": "system", "content": system_prompt}] if system_prompt else []
        )

        user_msg = {"role": "user", "content": prompt}

        return system_msg + history + [user_msg]

    def chat_completion(
        self,
        prompt: str,
        history: list[dict] | None = None,
        system_prompt: str | None = None,
        temperature=0,
        **kwargs,
    ):

        if history is None:
            history = []

        system_prompt = system_prompt if system_prompt else self.config.system_prompt
        message = self.prepare_msg(prompt, history, system_prompt)

        response: ChatCompletion = self.client.chat.completions.create(
            model=self.config.llm_model_name,
            messages=message,
            temperature=temperature,
            **kwargs,
        )

        return response

    def predict(
        self,
        prompt: str,
        history: list[dict] | None = None,
        system_prompt: str | None = None,
        stream=False,
        temperature=0,
        **kwargs,
    ):
        if stream:
            raise NotImplementedError("Stream is not implemented for this model")

        response = self.chat_completion(
            prompt, history, system_prompt, temperature=temperature, **kwargs
        )

        content = response.choices[0].message.content
        if content is None:
            print(f"!!!Error: {response}")
            content = "Error: No response from the model."

        meta = {}
        if response.usage:
            meta["prompt_tokens"] = response.usage.prompt_tokens
            meta["completion_tokens"] = response.usage.completion_tokens

        return content, meta


def get_llm(llm_name: str, system_prompt: str | None = None) -> BaseLLM:
    provider, model_name = llm_name.split("_")

    if provider == "deepinfra":
        api_key = DEEPINFRA_API_KEY
        if api_key is None:
            raise ValueError("DEEPINFRA_API_KEY is not set")
        base_url = "https://api.deepinfra.com/v1/openai"
    else:
        raise ValueError(f"Unknown provider: {provider}")

    config = BaseLLMConfig(
        provider=provider,
        llm_model_name=model_name,
        api_key=api_key,
        base_url=base_url,
        system_prompt=system_prompt,
    )
    return BaseLLM(config)
