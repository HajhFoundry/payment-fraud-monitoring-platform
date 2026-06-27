import pandas as pd
from datetime import datetime

from app.database.connection import SessionLocal
from app.database.models import ImportJob, Customer, Account, Transaction, FraudAlert


CSV_PATH = "data/kaggle/PS_20174392719_1491204439457_log.csv"


def import_kaggle_transactions(limit: int = 1000):
    db = SessionLocal()

    job = ImportJob(
        file_name=CSV_PATH,
        source="KAGGLE_PAYSIM",
        status="STARTED",
        started_at=datetime.utcnow()
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    imported_rows = 0
    rejected_rows = 0
    fraud_rows = 0

    try:
        df = pd.read_csv(CSV_PATH, nrows=limit)

        job.total_rows = len(df)
        db.commit()

        customer = Customer(
            first_name="Kaggle",
            last_name="Importer",
            email=f"kaggle_import_{job.job_id}@test.com",
            country="Canada"
        )

        db.add(customer)
        db.commit()
        db.refresh(customer)

        account = Account(
            customer_id=customer.customer_id,
            account_type="CHECKING",
            balance=1000000,
            status="ACTIVE"
        )

        db.add(account)
        db.commit()
        db.refresh(account)

        for _, row in df.iterrows():
            try:
                amount = float(row["amount"])
                transaction_type = str(row["type"])
                country = "Canada"
                merchant_name = str(row["nameDest"])
                merchant_category = transaction_type

                transaction = Transaction(
                    account_id=account.account_id,
                    merchant_name=merchant_name,
                    merchant_category=merchant_category,
                    amount=amount,
                    currency="CAD",
                    country=country,
                    status="APPROVED"
                )

                db.add(transaction)
                db.commit()
                db.refresh(transaction)

                is_kaggle_fraud = int(row["isFraud"])

                if is_kaggle_fraud == 1 or amount >= 5000:
                    rule_name = "KAGGLE_LABEL_FRAUD" if is_kaggle_fraud == 1 else "HIGH_AMOUNT_TRANSACTION"

                    fraud_alert = FraudAlert(
                        transaction_id=transaction.transaction_id,
                        rule_name=rule_name,
                        severity="HIGH",
                        alert_status="OPEN"
                    )

                    db.add(fraud_alert)
                    fraud_rows += 1

                imported_rows += 1
                db.commit()

            except Exception:
                rejected_rows += 1
                db.rollback()

        job.imported_rows = imported_rows
        job.rejected_rows = rejected_rows
        job.fraud_rows = fraud_rows
        job.status = "COMPLETED"
        job.completed_at = datetime.utcnow()

        db.commit()

        print("Kaggle import completed")
        print(f"Job ID: {job.job_id}")
        print(f"Total Rows: {job.total_rows}")
        print(f"Imported Rows: {job.imported_rows}")
        print(f"Rejected Rows: {job.rejected_rows}")
        print(f"Fraud Rows: {job.fraud_rows}")

    except Exception as error:
        job.status = "FAILED"
        job.completed_at = datetime.utcnow()
        db.commit()
        print(f"Kaggle import failed: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    import_kaggle_transactions(limit=1000)