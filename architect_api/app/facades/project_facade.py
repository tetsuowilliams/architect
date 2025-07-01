from app.repositories.project_repository import ProjectRepository, get_project_repository
from app.schemas.project_api.project import Project as ProjectSchema
from app.models.project import Project as ProjectModel
from app.database import get_session
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from app.schemas.project_api.project import ProjectTree

class ProjectFacade:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def get_project_tree_with_id(self, id: str) -> ProjectTree:
        project = self.project_repository.get_project_with_id(id)

        project_tree = ProjectTree(
            id=project.id,
            name=project.name,
            description=project.description,
            title=project.title,
            root_blackboard=project.root_blackboard
        )

        return project_tree
    
    def get_all_projects(self) -> List[ProjectSchema]:
        return self.project_repository.get_all_projects()
    
    def add_project(self, project_schema: ProjectSchema) -> ProjectSchema:
        project_model = ProjectModel(
            id=project_schema.id,
            name=project_schema.name,
            description=project_schema.description,
            title=project_schema.title
        )
        
        return self.project_repository.add_project(project_model)
        

def get_project_facade(session: Session = Depends(get_session)) -> ProjectFacade:
    return ProjectFacade(
        project_repository=get_project_repository(session), 
    )