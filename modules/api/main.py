from fastapi import FastAPI, Request

from config_handler import ConfigHandler


app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/confg")
async def get_config():
    return await ConfigHandler.get_config()


@app.post("/request")
async def send_request(body: dict, request: Request):
    return await request.app.state.comms_handler.add_request(input_request=body)
