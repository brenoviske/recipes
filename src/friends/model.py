from sqlalchemy import Column, Integer, String
from src.database.config import Base
from sqlalchemy.orm import sessionmaker

class Friend(Base):

    __tablename__ = 'friends'

    id = Column(Integer, primary_key=True, autoincrement=True , nullable=False)
