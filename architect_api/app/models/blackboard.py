from sqlalchemy.orm import mapped_column, Mapped
from app.models.base import Base


class Blackboard(Base):
    __tablename__ = 'blackboards'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(nullable=False)
