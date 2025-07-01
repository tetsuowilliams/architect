from app.repositories.message_repository import MessageRepository, get_message_repository
from app.schemas.messages_api.message import Message as MessageSchema
from app.models.message import Message as MessageModel
from app.database import get_session
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

class MessageFacade:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    def get_messages_for_blackboard(self, blackboard_id: int) -> List[MessageSchema]:
        return self.message_repository.get_messages_for_blackboard(blackboard_id)
    
    def add_message(self, message_schema: MessageSchema) -> MessageSchema:
        message_model = MessageModel(
            id=message_schema.id,
            content=message_schema.content,
            blackboard_id=message_schema.blackboard_id,
            sender_id=message_schema.sender_id
        )
        
        return self.message_repository.add_message(message_model)

    def get_message_with_id(self, id: str) -> MessageSchema:
        return  self.message_repository.get_message_with_id(id)
    
    def get_messages_from_blackboard_for_worker(self, blackboard_id: int, worker_id: int) -> List[MessageSchema]:
        return self.message_repository.get_messages_from_blackboard_for_worker(blackboard_id, worker_id)

def get_message_facade(session: Session = Depends(get_session)) -> MessageFacade:
    return MessageFacade(
        message_repository=get_message_repository(session), 
    )