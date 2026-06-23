from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import Transaction, PaymentEvent, FraudAlert
import json
import os
from datetime import datetime
from app.services.s3_service import upload_file_to_s3

router = APIRouter(prefix="/payments", tags=["Payments"])


class PaymentRequest(BaseModel):
    transaction_id: int
    amount: float

class WebhookEvent(BaseModel):
    transaction_id: int
    event_type: str
    amount: float
    provider: str = "SIMULATED_GATEWAY"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# PASTE STEP 3 HERE
def save_payment_event_report(event_data: dict):
    folder_path = "reports/payment_events"
    os.makedirs(folder_path, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f")

    file_name = f"payment_event_{timestamp}.json"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        json.dump(event_data, file, indent=4)

    return file_path

def get_latest_payment_status(transaction_id: int, db: Session):
    latest_event = (
        db.query(PaymentEvent)
        .filter(PaymentEvent.transaction_id == transaction_id)
        .order_by(PaymentEvent.created_at.desc())
        .first()
    )

    return latest_event.payment_status if latest_event else None

@router.post("/authorize")
def authorize_payment(payment: PaymentRequest, db: Session = Depends(get_db)):

    transaction = db.query(Transaction).filter(
        Transaction.transaction_id == payment.transaction_id
    ).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    event = PaymentEvent(
        transaction_id=payment.transaction_id,
        event_type="AUTHORIZATION",
        payment_status="AUTHORIZED",
        amount=payment.amount
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return {
        "payment_event_id": event.payment_event_id,
        "transaction_id": event.transaction_id,
        "event_type": event.event_type,
        "payment_status": event.payment_status,
        "amount": float(event.amount),
        "provider": event.provider
    }


@router.post("/capture")
def capture_payment(payment: PaymentRequest, db: Session = Depends(get_db)):

    transaction = db.query(Transaction).filter(
        Transaction.transaction_id == payment.transaction_id
    ).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    latest_status = get_latest_payment_status(payment.transaction_id, db)

    if latest_status != "AUTHORIZED":
        raise HTTPException(
            status_code=400,
            detail="Payment must be AUTHORIZED before CAPTURE"
        )

    
    event = PaymentEvent(
        transaction_id=payment.transaction_id,
        event_type="CAPTURE",
        payment_status="CAPTURED",
        amount=payment.amount
    )

    
    db.add(event)
    db.commit()
    db.refresh(event)

    return {
        "payment_event_id": event.payment_event_id,
        "transaction_id": event.transaction_id,
        "event_type": event.event_type,
        "payment_status": event.payment_status,
        "amount": float(event.amount),
        "provider": event.provider
    }


@router.post("/refund")
def refund_payment(payment: PaymentRequest, db: Session = Depends(get_db)):

    transaction = db.query(Transaction).filter(
        Transaction.transaction_id == payment.transaction_id
    ).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    event = PaymentEvent(
        transaction_id=payment.transaction_id,
        event_type="REFUND",
        payment_status="REFUNDED",
        amount=payment.amount
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return {
        "payment_event_id": event.payment_event_id,
        "transaction_id": event.transaction_id,
        "event_type": event.event_type,
        "payment_status": event.payment_status,
        "amount": float(event.amount),
        "provider": event.provider
    }


@router.post("/chargeback")
def chargeback_payment(payment: PaymentRequest, db: Session = Depends(get_db)):

    transaction = db.query(Transaction).filter(
        Transaction.transaction_id == payment.transaction_id
    ).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    latest_status = get_latest_payment_status(payment.transaction_id, db)

    if latest_status != "CAPTURED":
        raise HTTPException(
            status_code=400,
            detail="Payment must be CAPTURED before CHARGEBACK"
        )
    event = PaymentEvent(
        transaction_id=payment.transaction_id,
        event_type="CHARGEBACK",
        payment_status="CHARGEBACK",
        amount=payment.amount
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    fraud_alert = FraudAlert(
        transaction_id=payment.transaction_id,
        rule_name="CHARGEBACK_CREATED",
        severity="HIGH",
        alert_status="OPEN"
    )   

    db.add(fraud_alert)
    db.commit()
    db.refresh(fraud_alert)

    return {
        "payment_event_id": event.payment_event_id,
        "transaction_id": event.transaction_id,
        "event_type": event.event_type,
        "payment_status": event.payment_status,
        "amount": float(event.amount),
        "provider": event.provider,
        "fraud_alert_id": fraud_alert.alert_id,
        "fraud_rule": fraud_alert.rule_name
    }

@router.post("/webhook")
def process_payment_webhook(webhook: WebhookEvent, db: Session = Depends(get_db)):

    transaction = db.query(Transaction).filter(
        Transaction.transaction_id == webhook.transaction_id
    ).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    normalized_event_type = webhook.event_type.upper()

    event = PaymentEvent(
        transaction_id=webhook.transaction_id,
        event_type=normalized_event_type,
        payment_status=normalized_event_type,
        amount=webhook.amount,
        provider=webhook.provider
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    fraud_alert_id = None
    fraud_rule = None

    if normalized_event_type == "CHARGEBACK":
        fraud_alert = FraudAlert(
            transaction_id=webhook.transaction_id,
            rule_name="WEBHOOK_CHARGEBACK",
            severity="HIGH",
            alert_status="OPEN"
        )

        db.add(fraud_alert)
        db.commit()
        db.refresh(fraud_alert)

        fraud_alert_id = fraud_alert.alert_id
        fraud_rule = fraud_alert.rule_name

    report_data = {
        "message": "Webhook processed successfully",
        "payment_event_id": event.payment_event_id,
        "transaction_id": event.transaction_id,
        "event_type": event.event_type,
        "payment_status": event.payment_status,
        "amount": float(event.amount),
        "provider": event.provider,
        "fraud_alert_id": fraud_alert_id,
        "fraud_rule": fraud_rule,
        "created_at": str(event.created_at)
    }

    report_path = save_payment_event_report(report_data)
    s3_result = upload_file_to_s3(report_path)


    return {
        **report_data,
        "report_path": report_path,
        "s3_upload": s3_result
    }


@router.get("/")
def get_payment_events(db: Session = Depends(get_db)):

    events = db.query(PaymentEvent).all()

    return [
        {
            "payment_event_id": event.payment_event_id,
            "transaction_id": event.transaction_id,
            "event_type": event.event_type,
            "payment_status": event.payment_status,
            "amount": float(event.amount),
            "provider": event.provider,
            "created_at": str(event.created_at)
        }
        for event in events
    ]

