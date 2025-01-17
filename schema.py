from typing import List
from pydantic import BaseModel

# Request and response models
class TranslationRequest(BaseModel):
    text: str
    lang: str = None
    method: str = "offline"

class TranslationResponse(BaseModel):
    translated_text: str

class BulkTranslationRequest(BaseModel):
    texts: List[str]
    lang: str = None
    method: str = "offline"

class BulkTranslationResponse(BaseModel):
    translated_texts: List[str]