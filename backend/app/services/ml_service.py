import numpy as np

def predict_urban_score(data: dict):
    values = list(data.values())

    if not values:
        return {"urban_score": 0.0, "category": "Poor"}

    score = float(np.mean(values))

    if score < 40:
        category = "Poor"
    elif score < 70:
        category = "Moderate"
    else:
        category = "Good"

    return {
        "urban_score": round(score, 2),
        "category": category
    }
