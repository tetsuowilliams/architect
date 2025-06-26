from sqlalchemy import select, func, distinct
from sqlalchemy.orm import Session
from app.database import get_session
from fastapi import Depends
from app.models.blackboard import Blackboard

class BlackboardRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_blackboard_with_id(self, id: str) -> Blackboard:
        query = (
            select(Blackboard)
            .where(Blackboard.id == id)
        )

        result = self.session.execute(query)
        return result.scalars().first()
    
    def add_blackboard(self, blackboard: Blackboard):
        self.session.add(blackboard)
        self.session.commit()
        return blackboard
    

def get_blackboard_repository(
    session: Session = Depends(get_session)
) -> BlackboardRepository:
    return BlackboardRepository(session)    