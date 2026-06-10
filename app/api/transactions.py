from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import Account, Transaction, FraudAlert

router = APIRouter(prefix="/transactions", tags=["Transactions"])


class TransactionCreate(BaseModel):
    account_id: int
    merchant_name: str
    merchant_category: str
    amount: float
    currency: str = "CAD"
    country: str
    status: str = "APPROVED"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    account = db.query(Account).filter(
        Account.account_id == transaction.account_id
    ).first()

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    new_transaction = Transaction(
        account_id=transaction.account_id,
        merchant_name=transaction.merchant_name,
        merchant_category=transaction.merchant_category,
        amount=transaction.amount,
        currency=transaction.currency,
        country=transaction.country,
        status=transaction.status
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    fraud_alert = None

    if transaction.amount > 5000:
        fraud_alert = FraudAlert(
            transaction_id=new_transaction.transaction_id,
            rule_name="HIGH_AMOUNT_TRANSACTION",
            severity="HIGH",
            alert_status="OPEN"
        )

        db.add(fraud_alert)
        db.commit()
        db.refresh(fraud_alert)

    return {
        "transaction_id": new_transaction.transaction_id,
        "account_id": new_transaction.account_id,
        "merchant_name": new_transaction.merchant_name,
        "merchant_category": new_transaction.merchant_category,
        "amount": float(new_transaction.amount),
        "currency": new_transaction.currency,
        "country": new_transaction.country,
        "status": new_transaction.status,
        "fraud_alert_created": fraud_alert is not None
    }


@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()

    return [
        {
            "transaction_id": txn.transaction_id,
            "account_id": txn.account_id,
            "merchant_name": txn.merchant_name,
            "merchant_category": txn.merchant_category,
            "amount": float(txn.amount),
            "currency": txn.currency,
            "country": txn.country,
            "status": txn.status,
            "transaction_time": str(txn.transaction_time)
        }
        for txn in transactions
    ]