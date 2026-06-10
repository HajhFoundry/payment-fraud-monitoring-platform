from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import Customer

router = APIRouter(prefix="/customers", tags=["Customers"])


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    country: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    new_customer = Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        email=customer.email,
        country=customer.country,
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return {
        "customer_id": new_customer.customer_id,
        "first_name": new_customer.first_name,
        "last_name": new_customer.last_name,
        "email": new_customer.email,
        "country": new_customer.country,
        "created_at": str(new_customer.created_at)
    }

@router.get("/")
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(Customer).all()

    return [
        {
            "customer_id": customer.customer_id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "country": customer.country,
            "created_at": str(customer.created_at)
        }
        for customer in customers
    ]