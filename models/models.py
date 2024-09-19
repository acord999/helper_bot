from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import Session

def create_new_engine(db):
    # Подключение к существующей базе данных SQLite
    engine = create_engine(f"sqlite:///files/user_databases/{db}", echo=True)
    return engine

def create_new_session(engine):
    # Создание сессии
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


