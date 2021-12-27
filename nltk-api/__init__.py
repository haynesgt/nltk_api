from fastapi import FastAPI
import nltk

from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
async def root():
        return {"message": "Ok. See docs at /docs"}

class SentTokenizeRequest(BaseModel):
    text: str

class SentTokenizeResponse(BaseModel):
    tokens: List[str]

@app.post("/sent_tokenize")
async def sent_tokenize(req: SentTokenizeRequest):
    tokens = nltk.sent_tokenize(req.text)
    response = SentTokenizeResponse(tokens=tokens)
    return response

class WordTokenizeRequest(BaseModel):
    text: str

class WordTokenizeResponse(BaseModel):
    tokens: List[str]

@app.post("/word_tokenize")
async def word_tokenize(req: WordTokenizeRequest):
    tokens = nltk.word_tokenize(req.text)
    response = WordTokenizeResponse(tokens=tokens)
    return response

