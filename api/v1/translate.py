from fastapi import APIRouter

from core.config import t5_base
from schemas.translate import TranslateText

router = APIRouter()


@router.post("/translate")
async def translate_text(data: TranslateText):
    model = t5_base.get_model()
    translated_text = model.generate_text(
        f"translate {data.source_language} to \
            {data.destination_language}: {data.input_text}"
    )
    return {"translated_text": translated_text.text.split(".")[0]}
