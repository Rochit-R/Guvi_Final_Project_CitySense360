import requests

BASE_URL = "http://127.0.0.1:8000"


def analyze_sentiment(text):
    return requests.post(
        f"{BASE_URL}/nlp/sentiment",
        json={"text": text}
    ).json()


def predict_urban_score(payload):
    return requests.post(
        f"{BASE_URL}/analytics/predict",
        json=payload
    ).json()


def predict_traffic(levels):
    return requests.post(
        f"{BASE_URL}/traffic/predict",
        json={"recent_levels": levels}
    ).json()


def ask_city_bot(question):
    return requests.post(
        f"{BASE_URL}/chatbot/ask",
        json={"question": question}
    ).json()
