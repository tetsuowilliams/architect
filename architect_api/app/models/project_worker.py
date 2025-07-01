from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from app.models.base import Base


class ProjectWorker(Base):
    __tablename__ = 'project_workers'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), nullable=False)
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id"), nullable=False)

    project = relationship("Project", back_populates="project_workers")
    worker = relationship("Worker", back_populates="project_workers")