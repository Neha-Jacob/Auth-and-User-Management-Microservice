from fastapi import FastAPI
from app.api.v1.routes import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "This is the Auth and User Management Service"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
