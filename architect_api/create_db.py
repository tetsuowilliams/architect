from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app.config import settings


class DatabaseFacade:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = create_engine(connection_string)
        self.session = sessionmaker(bind=self.engine)

    def create_database(self, db_name, default_connection_str="postgresql://postgres:postgres@localhost:54320"):
        default_engine = create_engine(default_connection_str, isolation_level="AUTOCOMMIT")
        
        with default_engine.connect() as connection:
            result = connection.execute(
                text("SELECT 1 FROM pg_database WHERE datname = :db_name"),
                {"db_name": db_name}
            )
            if not result.scalar():
                connection.execute(text(f"CREATE DATABASE {db_name}"))
                print(f"Database '{db_name}' created successfully.")
            else:
                print(f"Database '{db_name}' already exists.")
    
    def drop_database(self, db_name, default_connection_str="postgresql://postgres:postgres@localhost:54320"):
        default_engine = create_engine(default_connection_str, isolation_level="AUTOCOMMIT")
        with default_engine.connect() as connection:
            result = connection.execute(
                text("SELECT 1 FROM pg_database WHERE datname = :db_name"),
                {"db_name": db_name}
            )
            if result.scalar():
                connection.execute(text(f"DROP DATABASE {db_name}"))
                print(f"Database '{db_name}' deleted successfully.")
            else:
                print(f"Database '{db_name}' already exists.")
    
    def add_vector_extension(self):
        default_engine = create_engine(self.connection_string, isolation_level="AUTOCOMMIT")
        with default_engine.connect() as connection:
            connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
            print(f"VECTOR extension added successfully.")
            
    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def drop_all_rows(self):
        session = self.session()
        try:
            session.execute(text("TRUNCATE TABLE blackboards RESTART IDENTITY CASCADE"))
            session.commit()
            print("All rows from all tables have been dropped.")
        finally:
            session.close()


if __name__ == "__main__":
    # Use connection string from config
    connection_str = settings.CONN_STRING

    db = DatabaseFacade(connection_str)
    
    rebuild = True
    if rebuild:
        db.drop_database(db_name=settings.DATABASE_NAME)    
        db.create_database(db_name=settings.DATABASE_NAME)
        db.add_vector_extension()
        db.create_tables()
        print("Success!")
    #db.drop_all_rows()