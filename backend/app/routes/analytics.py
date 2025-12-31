from fastapi import APIRouter
from app.services.ml_service import predict_urban_score

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    score = predict_urban_score(data)
    return {"urban_score": score}
