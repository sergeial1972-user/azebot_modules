#imports
from config_handler import ConfigHandler
from fastapi import FastAPI
import json

app = FastAPI(root_path="/api")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/confg")
async def get_config():
    return ConfigHandler.get_config
