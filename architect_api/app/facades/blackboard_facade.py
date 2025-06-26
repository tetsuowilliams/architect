from app.repositories.blackboard_repository import BlackboardRepository, get_blackboard_repository
from app.schemas.blackboard_api.blackboard import Blackboard as BlackboardSchema
from app.models.blackboard import Blackboard as BlackboardModel
from app.database import get_session
from sqlalchemy.orm import Session
from fastapi import Depends


class BlackboardFacade:
    def __init__(self, blackboard_repository: BlackboardRepository):
        self.blackboard_repository = blackboard_repository

    def get_blackboard_with_id(self, id: str) -> BlackboardSchema:
        return  self.blackboard_repository.get_blackboard_with_id(id)
    
    def add_blackboard(self, blackboard_schema: BlackboardSchema) -> BlackboardSchema:
        blackboard_model = BlackboardModel(
            id=blackboard_schema.id,
            content=blackboard_schema.content
        )
        
        return self.blackboard_repository.add_blackboard(blackboard_model)
        

def get_blackboard_facade(session: Session = Depends(get_session)) -> BlackboardFacade:
    return BlackboardFacade(
        blackboard_repository=get_blackboard_repository(session), 
    )