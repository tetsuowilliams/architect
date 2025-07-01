from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.models.base import Base
from enum import Enum


class WorkerRole(Enum):
    ADMIN = "admin"
    AGENT = "agent"


class Worker(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    messages = relationship("Message", back_populates="sender")
    project_workers = relationship("ProjectWorker", back_populates="worker")