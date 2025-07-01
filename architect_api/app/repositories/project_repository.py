from sqlalchemy import select, func, distinct
from sqlalchemy.orm import Session
from app.database import get_session
from fastapi import Depends
from app.models.project import Project
from typing import List

class ProjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_project_with_id(self, id: str) -> Project:
        query = (
            select(Project)
            .where(Project.id == id)
        )

        result = self.session.execute(query)
        return result.scalars().first()
    
    def add_project(self, project: Project):
        self.session.add(project)
        self.session.flush()
        return project
    
    def update_project(self, project: Project):
        self.session.add(project)
        self.session.flush()
        return project
    
    def get_all_projects(self) -> List[Project]:
        query = select(Project)
        result = self.session.execute(query)
        return result.scalars().all()
    

def get_project_repository(
    session: Session = Depends(get_session)
) -> ProjectRepository:
    return ProjectRepository(session)    