from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import Customer, LoginEvent, FraudAlert
from datetime import timedelta

router = APIRouter(
    prefix="/login-events",
    tags=["Login Events"]
)


class LoginEventCreate(BaseModel):
    customer_id: int
    device_type: str
    browser: str
    ip_address: str
    country: str
    login_status: str
    otp_status: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_login_event(
    login_event: LoginEventCreate,
    db: Session = Depends(get_db)
):

    customer = db.query(Customer).filter(
        Customer.customer_id == login_event.customer_id
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    new_login = LoginEvent(
        customer_id=login_event.customer_id,
        device_type=login_event.device_type,
        browser=login_event.browser,
        ip_address=login_event.ip_address,
        country=login_event.country,
        login_status=login_event.login_status,
        otp_status=login_event.otp_status
    )

    db.add(new_login)
    db.commit()
    db.refresh(new_login)

    from datetime import timedelta

    window_start = new_login.login_time - timedelta(minutes=5)

    otp_failures = db.query(LoginEvent).filter(
        LoginEvent.customer_id == new_login.customer_id,
        LoginEvent.otp_status == "FAILED",
        LoginEvent.login_time >= window_start
    ).count()

    

    if otp_failures >= 3:
        existing_alert = db.query(FraudAlert).filter(
            FraudAlert.rule_name == "MULTIPLE_OTP_FAILURES",
            FraudAlert.alert_status == "OPEN"
        ).first()

        if not existing_alert:
            fraud_alert = FraudAlert(
                transaction_id=None,
                rule_name="MULTIPLE_OTP_FAILURES",
                severity="HIGH",
                alert_status="OPEN"
            )

            db.add(fraud_alert)
            db.commit()

    previous_login = db.query(LoginEvent).filter(
        LoginEvent.customer_id == new_login.customer_id,
        LoginEvent.login_id != new_login.login_id
    ).order_by(LoginEvent.login_time.desc()).first()

    if previous_login:
        time_difference = new_login.login_time - previous_login.login_time

        if (
            previous_login.country != new_login.country
            and time_difference <= timedelta(minutes=10)
        ):
            existing_travel_alert = db.query(FraudAlert).filter(
                FraudAlert.rule_name == "IMPOSSIBLE_TRAVEL_LOGIN",
                FraudAlert.alert_status == "OPEN"
            ).first()

            if not existing_travel_alert:
                travel_alert = FraudAlert(
                    transaction_id=None,
                    rule_name="IMPOSSIBLE_TRAVEL_LOGIN",
                    severity="HIGH",
                    alert_status="OPEN"
                )

                db.add(travel_alert)
                db.commit()

    if previous_login:
        risky_location = previous_login.country != new_login.country
        new_device = previous_login.device_type != new_login.device_type
        new_browser = previous_login.browser != new_login.browser

        if (
            new_login.otp_status == "SUCCESS"
            and (risky_location or new_device or new_browser)
        ):
            existing_otp_success_alert = db.query(FraudAlert).filter(
                FraudAlert.rule_name == "OTP_SUCCESS_ON_RISKY_LOGIN",
                FraudAlert.alert_status == "OPEN"
            ).first()

            if not existing_otp_success_alert:
                otp_success_alert = FraudAlert(
                    transaction_id=None,
                    rule_name="OTP_SUCCESS_ON_RISKY_LOGIN",
                    severity="HIGH",
                    alert_status="OPEN"
                )

                db.add(otp_success_alert)
                db.commit()

    failed_logins = db.query(LoginEvent).filter(
        LoginEvent.customer_id == new_login.customer_id,
        LoginEvent.login_status == "FAILED",
        LoginEvent.login_time >= window_start
    ).count()

    if failed_logins >= 5:

        existing_failed_login_alert = db.query(FraudAlert).filter(
            FraudAlert.rule_name == "MULTIPLE_FAILED_LOGINS",
            FraudAlert.alert_status == "OPEN"
        ).first()

        if not existing_failed_login_alert:

            failed_login_alert = FraudAlert(
                transaction_id=None,
                rule_name="MULTIPLE_FAILED_LOGINS",
                severity="HIGH",
                alert_status="OPEN"
            )

            db.add(failed_login_alert)
            db.commit()

    return {
        "login_id": new_login.login_id,
        "customer_id": new_login.customer_id,
        "device_type": new_login.device_type,
        "browser": new_login.browser,
        "ip_address": new_login.ip_address,
        "country": new_login.country,
        "login_status": new_login.login_status,
        "otp_status": new_login.otp_status
    }


@router.get("/")
def get_login_events(db: Session = Depends(get_db)):

    events = db.query(LoginEvent).all()

    return [
        {
            "login_id": event.login_id,
            "customer_id": event.customer_id,
            "device_type": event.device_type,
            "browser": event.browser,
            "ip_address": event.ip_address,
            "country": event.country,
            "login_status": event.login_status,
            "login_time": str(event.login_time)
        }
        for event in events
    ]