from fastapi import APIRouter
from pydantic import BaseModel
from app.services.traffic_lstm import predict_traffic

router = APIRouter(prefix="/traffic", tags=["Traffic Prediction"])

class TrafficInput(BaseModel):
    recent_levels: list[float]

@router.post("/predict")
def traffic_prediction(data: TrafficInput):
    prediction = predict_traffic(data.recent_levels)
    return {
        "predicted_congestion_level": round(prediction, 2),
        "unit": "Traffic Index"
    }
