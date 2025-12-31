from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.analytics import router as analytics_router
from app.routes.nlp import router as nlp_router
from app.routes import traffic
from app.routes import chatbot

app = FastAPI(title="UrbanPulse AI", version="1.0")

app.include_router(health_router, prefix="/health")
app.include_router(analytics_router, prefix="/analytics")
app.include_router(nlp_router, prefix="/nlp")
app.include_router(traffic.router)
app.include_router(chatbot.router)

@app.get("/")
def root():
    return {"message": "UrbanPulse AI Backend Running"}
