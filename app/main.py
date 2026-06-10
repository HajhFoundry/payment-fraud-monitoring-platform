from fastapi import FastAPI
from app.api import customers

app = FastAPI(
    title="Payment Fraud Detection Platform",
    version="1.0.0"
)

app.include_router(customers.router)


@app.get("/")
def health_check():
    return {
        "application": "Payment Fraud Detection Platform",
        "status": "running"
    }