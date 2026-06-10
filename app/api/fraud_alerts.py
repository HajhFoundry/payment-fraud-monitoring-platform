from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import FraudAlert

router = APIRouter(prefix="/fraud-alerts", tags=["Fraud Alerts"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_fraud_alerts(db: Session = Depends(get_db)):
    alerts = db.query(FraudAlert).all()

    return [
        {
            "alert_id": alert.alert_id,
            "transaction_id": alert.transaction_id,
            "rule_name": alert.rule_name,
            "severity": alert.severity,
            "alert_status": alert.alert_status,
            "created_at": str(alert.created_at)
        }
        for alert in alerts
    ]