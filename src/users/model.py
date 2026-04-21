from src.database.config import Base
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    email = Column(String(200) , nullable=False, index = True)
    username = Column(String(200), nullable=False , index=True)
    password_hash = Column(String(512) , nullable=False , index=True )
    created_at = Column(DateTime , nullable=False, default=datetime.utcnow())

    friends = relationship('Friend', back_populates="user", cascade="all, delete-orphan")
    likes = relationship('Reaction', back_populates="user", cascade="all, delete-orphan")
    comments = relationship('Comment', back_populates="user", cascade="all, delete-orphan")

    def to_json(self):

        return {

            'id' : self.id,
            'email' : self.email,
            'username' : self.username,
            'created_at' : self.created_at,

        }

