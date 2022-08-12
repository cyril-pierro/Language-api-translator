from fastapi import APIRouter

from core.config import get_model
from schemas.translate import TranslateText

router = APIRouter()


@router.post("/translate")
async def translate_text(data: TranslateText):
    model = await get_model()
    translated_text = model.generate_text(
        f"translate {data.source_language} to \
            {data.destination_language}: {data.input_text}"
    )
    return {"translated_text": translated_text.text}
