from typing import Optional 
from sqlalchemy import select 
from sqlalchemy.orm import Session 
from app.models.alert import Alert 


class AlertRepository: 
    def __init__(self,db: Session):
        self.db = db 

    def create(self,alert:Alert) -> Alert: 
        self.db.add(alert)
        self.db.commit()
        self.db.refresh(alert)
        return alert 

    def get_all(self, status: Optional[str] = None) -> list[Alert]:
        stmt = select(Alert)
        if status is not None: 
            stmt = stmt.where(Alert.status == status)

        stmt = stmt.order_by(Alert.created_at.desc())
        return list(self.db.scalars(stmt))

    def get_by_id(self, alert_id:int)->Optional[Alert]:
        return self.db.get(Alert, alert_id)

    def update_status(self,alert_id:int,new_status:str)->Optional[Alert]:
        alert = self.get_by_id(alert_id)
        if alert is None: 
            return None
        alert.status = new_status
        self.db.commit()
        self.db.refresh(alert)
        return alert 
    