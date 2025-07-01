from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.facades.blackboard_facade import BlackboardFacade
from app.schemas.blackboard_api.blackboard import Blackboard
from app.repositories.blackboard_repository import BlackboardRepository
from app.repositories.project_repository import ProjectRepository
from app.repositories.worker_repository import WorkerRepository
from app.repositories.artifact_repository import ArtifactRepository
from app.repositories.message_repository import MessageRepository
from app.models.project import Project
from app.models.artifact import Artifact
from app.models.message import Message
from app.models.worker import Worker
from app.models.blackboard import Blackboard
from app.models.project_worker import ProjectWorker
from app.repositories.project_worker_repository import ProjectWorkerRepository


class DatabaseFacade:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = create_engine(connection_string)
        self.session = sessionmaker(bind=self.engine)

    def create_data(self):
        session = self.session()
        blackboard_repository = BlackboardRepository(session)
        project_repository = ProjectRepository(session)
        worker_repository = WorkerRepository(session)
        message_repository = MessageRepository(session)
        artifact_repository = ArtifactRepository(session)
        project_worker_repository = ProjectWorkerRepository(session)

        worker1 = worker_repository.add_worker(Worker(id=1, name="Worker 1", role="admin"))
        worker2 = worker_repository.add_worker(Worker(id=2, name="Worker 2", role="agent"))

        project = project_repository.add_project(Project(id=1, name="Project 1", description="Project 1 description", title="Project 1 title"))

        project_worker_repository.add_project_worker(ProjectWorker(id=1, project_id=project.id, worker_id=worker1.id))
        project_worker_repository.add_project_worker(ProjectWorker(id=2, project_id=project.id, worker_id=worker2.id))

        root_blackboard = blackboard_repository.add_blackboard(Blackboard(id=1, title="Root Blackboard", content="Hello, world! The first blackboard", project_id=project.id))
        project.root_blackboard_id = root_blackboard.id
        project_repository.update_project(project)

        child_blackboard = blackboard_repository.add_blackboard(Blackboard(id=2, title="Child Blackboard", content="Hello, world! The second blackboard hanging off the first blackboard", project_id=project.id, parent_blackboard_id=root_blackboard.id))

        child_child_blackboard1 = blackboard_repository.add_blackboard(Blackboard(id=3, title="Child Child Blackboard 1", content="Hello, world! The third blackboard hanging off the second blackboard", project_id=project.id, parent_blackboard_id=child_blackboard.id))
        child_child_blackboard2 = blackboard_repository.add_blackboard(Blackboard(id=4, title="Child Child Blackboard 2",   content="Hello, world! The fourth blackboard hanging off the second blackboard", project_id=project.id, parent_blackboard_id=child_blackboard.id))
        
        for i in range(10):
            message1 = Message(content=f"Hello, world! The {i}th message", blackboard_id=root_blackboard.id, sender_id=worker1.id)
            message_repository.add_message(message1)

            message2 = Message(content=f"Hello, world! The {i}th message", blackboard_id=child_blackboard.id, sender_id=worker2.id)
            message_repository.add_message(message2)

            message3 = Message(content=f"Hello, world! The {i}th message", blackboard_id=child_child_blackboard1.id, sender_id=worker1.id)
            message_repository.add_message(message3)

            message4 = Message(content=f"Hello, world! The {i}th message", blackboard_id=child_child_blackboard2.id, sender_id=worker1.id)
            message_repository.add_message(message4)

        for i in range(10):
            artifact = Artifact(id=i, name=f"Artifact {i}", content=f"Hello, world! The {i}th artifact", project_id=project.id)
            artifact_repository.add_artifact(artifact)

        session.commit()


if __name__ == "__main__":
    # Use connection string from config
    connection_str = settings.CONN_STRING

    db = DatabaseFacade(connection_str)
    
    db.create_data()
    print("Success!")