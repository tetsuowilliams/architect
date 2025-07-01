from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from app.models.base import Base


class Blackboard(Base):
    __tablename__ = 'blackboards'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    parent_blackboard_id: Mapped[int] = mapped_column(ForeignKey("blackboards.id"), nullable=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), nullable=False)

    project = relationship("Project", back_populates="blackboards", foreign_keys=[project_id])
    parent_blackboard = relationship("Blackboard", back_populates="child_blackboards", remote_side=[id])
    child_blackboards = relationship("Blackboard", back_populates="parent_blackboard")
    messages = relationship("Message", back_populates="blackboard")
