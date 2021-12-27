from fastapi import FastAPI

import nltk

app = FastAPI()

@app.get("/")
async def root():
        return {"message": "Ok"}

