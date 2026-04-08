from src.database.config import Base
from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship

class Like(Base):

    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True , nullable=False, autoincrement=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer,ForeignKey('posts.id'))
    comment_id = Column(Integer,ForeignKey('comments.id'))

    user = relationship("User" , back_populates="likes", cascade="all, delete-orphan")
    post = relationship("Post", back_populates="likes", cascade="all, delete-orphan")
    comment = relationship("Comment", back_populates="likes", cascade="all, delete-orphan")

    def to_json(self):

        return {

            'id':self.id,
            'user_id':self.user_id,
            'post_id':self.post_id,
            'comment_id':self.comment_id,

        }




