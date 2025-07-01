from sqlalchemy import select, func, distinct
from sqlalchemy.orm import Session
from typing import List
from app.database import get_session
from fastapi import Depends
from app.models.message import Message


class MessageRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_message_with_id(self, id: str) -> Message:
        query = (
            select(Message)
            .where(Message.id == id)
        )

        result = self.session.execute(query)
        return result.scalars().first()
    
    def get_messages_for_blackboard(self, blackboard_id: int) -> List[Message]:
        query = (
            select(Message)
            .where(Message.blackboard_id == blackboard_id)
        )

        result = self.session.execute(query)
        return result.scalars().all()
    
    def get_messages_from_blackboard_for_worker(self, blackboard_id: str, worker_id: str) -> List[Message]:
        query = (
            select(Message)
            .where(Message.blackboard_id == blackboard_id)
            .where(Message.worker_id == worker_id)
        )

        result = self.session.execute(query)
        return result.scalars().all()
    
    def add_message(self, message: Message):
        self.session.add(message)
        self.session.flush()
        return message
    

def get_message_repository(
    session: Session = Depends(get_session)
) -> MessageRepository:
    return MessageRepository(session)    