from fastapi import FastAPI

app = FastAPI(
    title="Payment Fraud Detection Platform",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {
        "application": "Payment Fraud Detection Platform",
        "status": "running"
    }