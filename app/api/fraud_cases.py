from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime

from app.database.connection import SessionLocal
from app.database.models import FraudAlert, FraudCase
from app.services.audit_service import create_audit_log

router = APIRouter(prefix="/fraud-cases", tags=["Fraud Cases"])


class FraudCaseCreate(BaseModel):
    alert_id: int
    assigned_to: str
    notes: str | None = None


class FraudCaseUpdate(BaseModel):
    case_status: str
    notes: str | None = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_fraud_case(case: FraudCaseCreate, db: Session = Depends(get_db)):
    alert = db.query(FraudAlert).filter(
        FraudAlert.alert_id == case.alert_id
    ).first()

    if not alert:
        raise HTTPException(
            status_code=404,
            detail="Fraud alert not found"
        )

    new_case = FraudCase(
        alert_id=case.alert_id,
        assigned_to=case.assigned_to,
        notes=case.notes
    )

    db.add(new_case)
    db.commit()
    db.refresh(new_case)

    create_audit_log(
        db=db,
        event_type="CASE_CREATED",
        entity_name="FRAUD_CASE",
        entity_id=new_case.case_id,
        description=f"Case created for alert {new_case.alert_id}"
    )

    db.commit()
    return {
        "case_id": new_case.case_id,
        "alert_id": new_case.alert_id,
        "assigned_to": new_case.assigned_to,
        "case_status": new_case.case_status,
        "notes": new_case.notes,
        "created_at": str(new_case.created_at),
        "updated_at": str(new_case.updated_at)
    }


@router.get("/")
def get_fraud_cases(db: Session = Depends(get_db)):
    cases = db.query(FraudCase).all()

    return [
        {
            "case_id": case.case_id,
            "alert_id": case.alert_id,
            "assigned_to": case.assigned_to,
            "case_status": case.case_status,
            "notes": case.notes,
            "created_at": str(case.created_at),
            "updated_at": str(case.updated_at)
        }
        for case in cases
    ]


@router.patch("/{case_id}")
def update_fraud_case(case_id: int, update: FraudCaseUpdate, db: Session = Depends(get_db)):
    fraud_case = db.query(FraudCase).filter(
        FraudCase.case_id == case_id
    ).first()

    if not fraud_case:
        raise HTTPException(
            status_code=404,
            detail="Fraud case not found"
        )

    fraud_case.case_status = update.case_status
    fraud_case.notes = update.notes
    fraud_case.updated_at = datetime.utcnow()

    create_audit_log(
        db=db,
        event_type="CASE_UPDATED",
        entity_name="FRAUD_CASE",
        entity_id=fraud_case.case_id,
        description=f"Status changed to {update.case_status}"
    )
    db.commit()
    db.refresh(fraud_case)

    return {
        "case_id": fraud_case.case_id,
        "alert_id": fraud_case.alert_id,
        "assigned_to": fraud_case.assigned_to,
        "case_status": fraud_case.case_status,
        "notes": fraud_case.notes,
        "created_at": str(fraud_case.created_at),
        "updated_at": str(fraud_case.updated_at)
    }