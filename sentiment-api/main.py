from fastapi import FastAPI
from pydantic import BaseModel
from model import analyze_sentiment

app = FastAPI(title="Sentiment Analysis API")

class SentimentRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running!"}

@app.post("/analyze")
def analyze(request: SentimentRequest):
    result = analyze_sentiment(request.text)
    return {
        "input_text": request.text,
        "sentiment": result
    }
