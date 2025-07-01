from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from app.models.base import Base


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)

    root_blackboard_id: Mapped[int] = mapped_column(ForeignKey("blackboards.id"), nullable=True)

    root_blackboard = relationship("Blackboard", foreign_keys=[root_blackboard_id])
    blackboards = relationship("Blackboard", back_populates="project", foreign_keys="Blackboard.project_id")
    project_workers = relationship("ProjectWorker", back_populates="project")
    artifacts = relationship("Artifact", back_populates="project")