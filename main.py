import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from translate import TranslatorWrapper
from schema import TranslationRequest, TranslationResponse, BulkTranslationRequest, BulkTranslationResponse

app = FastAPI()

# cache 
from functools import lru_cache

@lru_cache(maxsize=128)
def split_translate_merge(sentence, lang, verbose=False):
    mt = TranslatorWrapper()
    if lang == "en" or lang is None:
        return sentence
    try:
        chunk_size = 5000
        chunks = [
            sentence[i : i + chunk_size]
            for i in range(0, len(sentence), chunk_size)
        ]
        translated_chunks = [
            mt.translate(chunk, lang, method="offline")
            for chunk in chunks
        ]
        merged_sentence = "".join(translated_chunks)
        if verbose:
            print(merged_sentence)
        return merged_sentence
    except Exception as e:
        if verbose:
            print(f"Translation error: {e}")
        return ""

@app.on_event("startup")
async def on_startup():
    split_translate_merge("", lang='ru')# Warm-up call
    logging.info("Translator API is ready.")

@app.get("/")
def read_root() -> dict:
    return {"API Name": "Translation API", "Status": "Running"}

@app.post("/api/translate/", response_model=TranslationResponse)
def translate_text(request: TranslationRequest):
    try:
        logging.info(f"Translating text: {request.text}")
        translated_text = split_translate_merge(request.text, request.lang, verbose=True)
        return TranslationResponse(translated_text=translated_text)
    except ValueError as e:
        logging.error(f"Translation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# @app.get("/api/translate/bulk/", response_model=BulkTranslationResponse)
# def translate_texts(texts: List[str], lang: str = 'ru', method: str = "offline"):
#     try:
#         logging.info(f"Translating bulk texts: {len(texts)} items")
#         translated_texts = [
#             split_translate_merge(text, lang, verbose=True)
#             for text in texts
#         ]
#         return BulkTranslationResponse(translated_texts=translated_texts)
#     except ValueError as e:
#         logging.error(f"Bulk translation error: {e}")
#         raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)