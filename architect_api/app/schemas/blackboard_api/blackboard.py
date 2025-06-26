from pydantic import BaseModel

class Blackboard(BaseModel):
    id: int
    content: str
