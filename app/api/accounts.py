from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import Account, Customer


router = APIRouter(prefix="/accounts", tags=["Accounts"])


class AccountCreate(BaseModel):
    customer_id: int
    account_type: str
    balance: float


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_account(account: AccountCreate, db: Session = Depends(get_db)):

    customer = db.query(Customer).filter(
        Customer.customer_id == account.customer_id
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    new_account = Account(
        customer_id=account.customer_id,
        account_type=account.account_type,
        balance=account.balance
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

   

    db.commit()

    return {
        "account_id": new_account.account_id,
        "customer_id": new_account.customer_id,
        "account_type": new_account.account_type,
        "balance": float(new_account.balance),
        "status": new_account.status
    }

@router.get("/")
def get_accounts(db: Session = Depends(get_db)):

    accounts = db.query(Account).all()

    return [
        {
            "account_id": account.account_id,
            "customer_id": account.customer_id,
            "account_type": account.account_type,
            "balance": float(account.balance),
            "status": account.status
        }
        for account in accounts
    ]