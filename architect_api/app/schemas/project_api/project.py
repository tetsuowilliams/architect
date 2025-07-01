from pydantic import BaseModel, ConfigDict
from app.schemas.blackboard_api.blackboard import  BlackboardTree


class Project(BaseModel):
    id: int
    name: str
    description: str
    title: str

    model_config = ConfigDict(from_attributes=True)


class ProjectTree(BaseModel):
    id: int
    name: str
    description: str
    title: str
    root_blackboard: BlackboardTree
    
    model_config = ConfigDict(from_attributes=True)
    
    