from sqlalchemy import select, func, distinct
from sqlalchemy.orm import Session
from app.database import get_session
from fastapi import Depends
from app.models.artifact import Artifact


class ArtifactRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_artifact_with_id(self, id: str) -> Artifact:
        query = (
            select(Artifact)
            .where(Artifact.id == id)
        )

        result = self.session.execute(query)
        return result.scalars().first()
    
    def add_artifact(self, artifact: Artifact):
        self.session.add(artifact)
        self.session.flush()
        return artifact
    

def get_artifact_repository(
    session: Session = Depends(get_session)
) -> ArtifactRepository:
    return ArtifactRepository(session)    