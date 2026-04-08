from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from src.database.config import Base


class Post(Base):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True , null=False, autoincrement=True)
    content = Column(String(512), nullable = False , index = True)


    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User" , back_populates="posts" , cascade = "all, delete")
    likes = relationship("Like" , back_populates="posts" , cascade = "all, delete")
    comments = relationship("Comment" , back_populates="posts" , cascade = "all, delete")

    def to_json(self):

        return {
            "id" : self.id,
            "content" : self.content,
            "user_id" : self.user_id,
        }
