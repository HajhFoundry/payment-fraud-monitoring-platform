from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import ImportJob

router = APIRouter(prefix="/import-jobs", tags=["Import Jobs"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_import_jobs(db: Session = Depends(get_db)):
    jobs = db.query(ImportJob).order_by(ImportJob.job_id.desc()).all()

    return [
        {
            "job_id": job.job_id,
            "file_name": job.file_name,
            "source": job.source,
            "status": job.status,
            "total_rows": job.total_rows,
            "imported_rows": job.imported_rows,
            "rejected_rows": job.rejected_rows,
            "fraud_rows": job.fraud_rows,
            "started_at": str(job.started_at),
            "completed_at": str(job.completed_at) if job.completed_at else None
        }
        for job in jobs
    ]