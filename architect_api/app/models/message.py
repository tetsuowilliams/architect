from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from app.models.base import Base


class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(nullable=False)
    sender_id: Mapped[int] = mapped_column(ForeignKey("workers.id"), nullable=False)
    blackboard_id: Mapped[int] = mapped_column(ForeignKey("blackboards.id"), nullable=False)

    sender = relationship("Worker", back_populates="messages")
    blackboard = relationship("Blackboard", back_populates="messages")
    sender = relationship("Worker", back_populates="messages")
