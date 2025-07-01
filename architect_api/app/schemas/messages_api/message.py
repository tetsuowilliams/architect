from pydantic import BaseModel, ConfigDict
from app.schemas.worker_api.worker import Worker

class Message(BaseModel):
    id: int
    content: str
    blackboard_id: int
    sender: Worker

    model_config = ConfigDict(from_attributes=True)