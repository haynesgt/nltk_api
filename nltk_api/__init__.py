from fastapi import FastAPI
import nltk

from enum import Enum
import os
from pydantic import BaseModel
from typing import List

nltk.download("punkt")

app = FastAPI(root_path="/" if os.environ.get("ENV") != "prod" else "/nltk")


class Language(Enum):
    # These should match $HOME/nltk_data/tokenizers/punkt/*.pickle
    CZECH = "czech"
    DANISH = "danish"
    DUTCH = "dutch"
    ENGLISH = "english"
    ESTONIAN = "estonian"
    FINNISH = "finnish"
    FRENCH = "french"
    GERMAN = "german"
    GREEK = "greek"
    ITALIAN = "italian"
    NORWEGIAN = "norwegian"
    POLISH = "polish"
    PORTUGUESE = "portuguese"
    RUSSIAN = "russian"
    SLOVENE = "slovene"
    SPANISH = "spanish"
    SWEDISH = "swedish"
    TURKISH = "turkish"

    def _missing_(value):
        import pycountry
        try:
            lang = pycountry.languages.get(alpha_2=value)
            # this is no alpha_1
            if not lang:
                lang = pycountry.languages.get(alpha_3=value)
            if lang and not lang.name == value:
                return Language(lang.name.lower())
        except LookupError:
            return None


@app.get("/")
async def root():
        return {"message": "Ok. See docs at /docs"}

class SentTokenizeRequest(BaseModel):
    text: str
    language: Language = Language.ENGLISH

class SentTokenizeResponse(BaseModel):
    tokens: List[str]

@app.post("/sent_tokenize")
async def sent_tokenize(req: SentTokenizeRequest):
    tokens = nltk.sent_tokenize(req.text, language=req.language.value)
    response = SentTokenizeResponse(tokens=tokens)
    return response

class WordTokenizeRequest(BaseModel):
    text: str
    language: Language = Language.ENGLISH

class WordTokenizeResponse(BaseModel):
    tokens: List[str]
    preserve_line: bool = False

@app.post("/word_tokenize")
async def word_tokenize(req: WordTokenizeRequest):
    tokens = nltk.word_tokenize(req.text, language=req.language.value, preserve_line=req.preserve_line)
    response = WordTokenizeResponse(tokens=tokens)
    return response

