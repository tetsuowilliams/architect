from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config import settings 
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)


engine = create_engine(
    settings.CONN_STRING
)


SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Dependency that will be used by FastAPI
def get_session(): 
    with SessionLocal() as session:
        try:
            yield session
            session.commit()
        except Exception as e:
            logger.error(f"Error committing session: {e}")
            session.rollback()
            raise e
        finally:
             session.close() 

@contextmanager
def get_db_session():
    """Context manager for database sessions."""
    session = next(get_session())
    try:
        yield session
    finally:
        session.close()