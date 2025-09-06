from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text: str):
    result = sentiment_pipeline(text)[0]
    return {
        "label": result['label'].lower(),
        "confidence": round(result['score'], 4)
    }
