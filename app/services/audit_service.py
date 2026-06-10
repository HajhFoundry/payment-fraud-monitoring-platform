from app.database.models import AuditLog


def create_audit_log(
    db,
    event_type,
    entity_name,
    entity_id,
    description
):
    log = AuditLog(
        event_type=event_type,
        entity_name=entity_name,
        entity_id=entity_id,
        description=description
    )

    db.add(log)