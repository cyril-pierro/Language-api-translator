import os

import torch
from pydantic import BaseSettings

store_model: dict = {}


async def get_model():
    model = store_model.get("model")
    if not model:
        model_path = str(os.getenv("MODEL_PATH"))
        model = torch.load(os.path.expanduser(model_path))
        store_model["model"] = model
    return model


class Settings(BaseSettings):
    endpoint_prefix: str = "/api/v1"
    app_version: str = "1.0"
    release_id: str = ".0"
    app_name: str = "Language Translator API"


setting = Settings()
