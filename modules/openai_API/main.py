import asyncio
import json
from pathlib import Path
from typing import Any

from openai import AsyncOpenAI


CONFIG_FILE = Path("config.json")


def check_config() -> bool:
    return CONFIG_FILE.exists()


def load_config() -> dict[str, Any]:
    if not check_config():
        autosetup()

    with CONFIG_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def autosetup() -> None:
    if check_config():
        return

    print("Welcome to Openai_API autosetup")

    base_url = input(
        "Enter base url of your llm inference server "
        "(leave blank for OpenAI server): "
    ).strip() or None

    api_key = input(
        "Enter your OpenAI API key "
        "(leave blank if using local instance): "
    ).strip() or "not-needed"

    model = input("Model: ").strip() or "gpt-5.5"

    data = {
        "base_url": base_url,
        "api_key": api_key,
        "model": model,
    }

    with CONFIG_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


async def main(
    prompt: str | None = None,
    model: str | None = None,
    client_params: dict[str, Any] | None = None,
    response_params: dict[str, Any] | None = None,
) -> Any:
    config = load_config()

    client_kwargs = dict(client_params or {})

    client_kwargs.setdefault(
        "api_key",
        config.get("api_key") or "not-needed",
    )

    if config.get("base_url"):
        client_kwargs.setdefault("base_url", config["base_url"])

    response_kwargs = dict(response_params or {})

    response_kwargs.setdefault(
        "model",
        model or config.get("model") or "gpt-5.5",
    )

    if prompt is not None:
        response_kwargs.setdefault("input", prompt)

    async with AsyncOpenAI(**client_kwargs) as client:
        response = await client.responses.create(**response_kwargs)

    return response