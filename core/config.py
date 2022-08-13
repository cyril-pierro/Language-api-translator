import os

import happytransformer  # type: ignore
from pydantic import BaseSettings

store_model: dict = {}


def initialize_model():
    model = store_model.get("model")
    if model:
        return model

    model_path = str(os.getenv("MODEL_PATH"))
    model = happytransformer.HappyTextToText(
        model_name="t5-base", load_path=os.path.expanduser(model_path)
    )
    store_model["model"] = model


class Settings(BaseSettings):
    endpoint_prefix: str = "/api/v1"
    app_version: str = "1.0"
    release_id: str = ".0"
    app_name: str = "Language Translator API"


setting = Settings()
