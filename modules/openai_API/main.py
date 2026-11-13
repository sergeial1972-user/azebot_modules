import asyncio
from typing import Any
from openai import AsyncOpenAI
from pathlib import Path
import json

CONFIG_FILE = Path("config.json")

def check_config() -> bool:
    """Проверяет, существует ли файл конфигурации."""
    return CONFIG_FILE.exists()

def load_config():
    check_config()
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    return config

    


#automaticly configure module
def autosetup():
    if not check_config():
        print("Welcome to Openai_API autosetup")
        base_url = input("Enter base url of your llm inference server (leave blank for Openai server)").strip() or None
        api_key = input("Enter your Openai API key (leave blank if using local instance)").strip() or "not-needed"
        model = input("model").strip() or "gpt-5.5"

    data = {
        "base_url": base_url,
        "api_key": api_key,
        "model": model
    }

    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)





async def main(


        
    prompt: str | None = None,
    model: str = "gpt-5.5",
    client_params: dict[str, Any] | None = None,
    response_params: dict[str, Any] | None = None,
) -> Any:
    
    config = load_config()

    client_kwargs = client_params.copy() if client_params else {}

    if "api_key" not in client_kwargs:
        client_kwargs["api_key"] = config.get("api_key") or "not_used"

    if config.get("base_url"):
        client_kwargs["base_url"] = config.get("base_url")
        



    response_kwargs = response_params.copy() if response_params else {}
    response_kwargs.setdefault("model", config.get("model") or model)

    if prompt is not None:
        response_kwargs.setdefault("input", prompt)


    async with AsyncOpenAI(**client_kwargs) as client:
        response = await client.responses.create(**response_kwargs)

    return response
