from fastapi import FastAPI

from api.v1 import translate
from core.config import setting

app = FastAPI(
    docs_url="/",
    version=setting.app_version + setting.release_id,
    title=setting.app_name,
)

app.include_router(translate.router, prefix=setting.endpoint_prefix)
