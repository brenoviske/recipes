from sqlalchemy import Column, Integer, String , ForeignKey
from src.database.config import Base
from sqlalchemy.orm import relationship

class Friend(Base):

    __tablename__ = 'friends'

    id = Column(Integer, primary_key=True, autoincrement=True , nullable=False)
    user_id = Column(Integer, ForeignKey('users.id') ,nullable=False)

    user = relationship('User', back_populates='friends')

    def to_json(self):

        return {
            'id' : self.id,
            'user_id' : self.user_id,
        }
