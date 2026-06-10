from fastapi import FastAPI
from app.api import customers
from app.api import accounts
from app.api import transactions
from app.api import fraud_alerts
from app.api import fraud_cases

app = FastAPI(
    title="Payment Fraud Detection Platform",
    version="1.0.0"
)

app.include_router(customers.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(fraud_alerts.router)
app.include_router(fraud_cases.router)

@app.get("/")
def health_check():
    return {
        "application": "Payment Fraud Detection Platform",
        "status": "running"
    }