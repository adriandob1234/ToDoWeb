from sqlalchemy import sessionmaker
from app import engine


Session = sessionmaker(bind=engine)
