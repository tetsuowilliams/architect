from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.facades.blackboard_facade import BlackboardFacade
from app.schemas.blackboard_api.blackboard import Blackboard
from app.repositories.blackboard_repository import BlackboardRepository

class DatabaseFacade:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = create_engine(connection_string)
        self.session = sessionmaker(bind=self.engine)

    def create_data(self):
        repository = BlackboardRepository(self.session())
        facade = BlackboardFacade(repository)
        facade.add_blackboard(Blackboard(id=1, content="Hello, world! The first blackboard"))


if __name__ == "__main__":
    # Use connection string from config
    connection_str = settings.CONN_STRING

    db = DatabaseFacade(connection_str)
    
    db.create_data()
    print("Success!")