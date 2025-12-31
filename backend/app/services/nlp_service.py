from textblob import TextBlob

def analyze_text(text: str):
    polarity = TextBlob(text).sentiment.polarity
    label = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return {"polarity": polarity, "sentiment": label}
