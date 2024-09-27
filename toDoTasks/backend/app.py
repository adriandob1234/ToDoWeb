from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.orm import DeclarativeBase

db_url = "sqlite:///database.db"
engine = create_engine(db_url)

class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True) 
    task = Column(String, unique=True)
    due = Column(String)

Base.metadata.create_all(engine)
