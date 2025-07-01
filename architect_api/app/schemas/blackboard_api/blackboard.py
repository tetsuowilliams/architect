from pydantic import BaseModel, ConfigDict
from typing import List
from app.schemas.messages_api.message import Message

class Blackboard(BaseModel):
    id: int
    title: str
    content: str | None = None
    parent_blackboard_id: int | None = None
    messages: List[Message] = []

    model_config = ConfigDict(from_attributes=True)

class BlackboardTree(BaseModel):
    id: int
    title: str
    content: str | None = None
    parent_blackboard_id: int | None = None
    child_blackboards: List["BlackboardTree"] = []

    model_config = ConfigDict(from_attributes=True)

    
    