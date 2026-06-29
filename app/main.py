from fastapi import FastAPI
from app.api import customers
from app.api import accounts
from app.api import transactions
from app.api import fraud_alerts
from app.api import fraud_cases
from app.api import login_events
from app.api import payments
from app.database.models import Base
from app.database.connection import engine
from app.api import import_jobs

app = FastAPI(
    title="Payment Fraud Detection Platform",
    version="1.0.0"
)

app.include_router(customers.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(fraud_alerts.router)
app.include_router(fraud_cases.router)
app.include_router(login_events.router)
app.include_router(payments.router)
app.include_router(import_jobs.router)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {
        "application": "Payment Fraud Detection Platform",
        "status": "running"
    }