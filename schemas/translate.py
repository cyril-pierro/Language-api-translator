from enum import Enum

from pydantic import BaseModel


class UseLanguage(str, Enum):
    English = "English"
    French = "French"
    Romanian = "Romanian"
    German = "German"


class TranslateText(BaseModel):
    source_language: UseLanguage
    destination_language: UseLanguage
    input_text: str

    class Config:
        schema_extra = {
            "example": {
                "source_language": "English",
                "destination_language": "German",
                "input_text": "I love playing songs",
            }
        }
