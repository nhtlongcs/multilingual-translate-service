from typing import List, Optional
from pydantic import BaseModel

# Request and response models
class TranslationRequest(BaseModel):
    text: str
    lang: Optional[str] = "ru"
    method: Optional[str] = "offline"

class TranslationResponse(BaseModel):
    translated_text: str

class BulkTranslationRequest(BaseModel):
    texts: List[str]
    lang: Optional[str] = "ru"
    method: Optional[str] = "offline"

class BulkTranslationResponse(BaseModel):
    translated_texts: List[str]