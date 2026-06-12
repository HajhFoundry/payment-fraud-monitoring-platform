from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    country = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    account_type = Column(String(50), nullable=False)
    balance = Column(Numeric(12, 2), nullable=False)
    status = Column(String(30), default="ACTIVE")
    created_at = Column(DateTime, default=datetime.utcnow)


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.account_id"), nullable=False)
    merchant_name = Column(String(150), nullable=False)
    merchant_category = Column(String(100), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    currency = Column(String(10), default="CAD")
    country = Column(String(50), nullable=False)
    status = Column(String(30), default="APPROVED")
    transaction_time = Column(DateTime, default=datetime.utcnow)


class FraudAlert(Base):
    __tablename__ = "fraud_alerts"

    alert_id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, ForeignKey("transactions.transaction_id"), nullable=False)
    rule_name = Column(String(100), nullable=False)
    severity = Column(String(30), nullable=False)
    alert_status = Column(String(30), default="OPEN")
    created_at = Column(DateTime, default=datetime.utcnow)

class FraudCase(Base):
    __tablename__ = "fraud_cases"

    case_id = Column(Integer, primary_key=True, index=True)
    alert_id = Column(Integer, ForeignKey("fraud_alerts.alert_id"), nullable=False)
    assigned_to = Column(String(100), nullable=False)
    case_status = Column(String(30), default="OPEN")
    notes = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"

    audit_id = Column(Integer, primary_key=True, index=True)

    event_type = Column(String(100), nullable=False)

    entity_name = Column(String(100), nullable=False)

    entity_id = Column(Integer, nullable=False)

    description = Column(String(500))

    created_at = Column(DateTime, default=datetime.utcnow)

class LoginEvent(Base):
    __tablename__ = "login_events"

    login_id = Column(Integer, primary_key=True, index=True)
    otp_status = Column(String, nullable=False)
    customer_id = Column(
        Integer,
        ForeignKey("customers.customer_id"),
        nullable=False
    )

    device_type = Column(String(50))
    browser = Column(String(50))
    ip_address = Column(String(100))
    country = Column(String(100))

    login_status = Column(String(20))
    otp_status = Column(String)
    login_time = Column(
        DateTime,
        default=datetime.utcnow
    )