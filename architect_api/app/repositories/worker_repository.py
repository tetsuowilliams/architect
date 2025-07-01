from sqlalchemy import select, func, distinct
from sqlalchemy.orm import Session
from app.database import get_session
from fastapi import Depends
from app.models.worker import Worker


class WorkerRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_worker_with_id(self, id: str) -> Worker:
        query = (
            select(Worker)
            .where(Worker.id == id)
        )

        result = self.session.execute(query)
        return result.scalars().first()

    def add_worker(self, worker: Worker):
        self.session.add(worker)
        self.session.flush()
        return worker
    

def get_worker_repository(
    session: Session = Depends(get_session)
) -> WorkerRepository:
    return WorkerRepository(session)    