from pydantic import BaseModel, ConfigDict

class Worker(BaseModel):
    id: int
    name: str
    role: str

    model_config = ConfigDict(from_attributes=True)
