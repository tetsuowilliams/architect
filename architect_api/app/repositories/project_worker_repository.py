from sqlalchemy import select, func, distinct
from sqlalchemy.orm import Session
from app.database import get_session
from fastapi import Depends
from app.models.project_worker import ProjectWorker


class ProjectWorkerRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_project_worker_with_id(self, id: str) -> ProjectWorker:
        query = (
            select(ProjectWorker)
            .where(ProjectWorker.id == id)
        )

        result = self.session.execute(query)
        return result.scalars().first()
    
    def add_project_worker(self, project_worker: ProjectWorker):
        self.session.add(project_worker)
        self.session.flush()
        return project_worker
    

def get_project_worker_repository(
    session: Session = Depends(get_session)
) -> ProjectWorkerRepository:
    return ProjectWorkerRepository(session)    