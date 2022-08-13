import os

import happytransformer  # type: ignore
from pydantic import BaseSettings


class T5Model:
    def __init__(self):
        self._store_model: dict = {}

    def initialize_model(self):
        model_path = str(os.getenv("MODEL_PATH"))
        model = happytransformer.HappyTextToText(
            model_name="t5-base", load_path=os.path.expanduser(model_path)
        )
        self._store_model["model"] = model

    def get_model(self):
        return self._store_model.get("model")


class Settings(BaseSettings):
    endpoint_prefix: str = "/api/v1"
    app_version: str = "1.0"
    release_id: str = ".0"
    app_name: str = "Language Translator API"


setting = Settings()
t5_base = T5Model()
