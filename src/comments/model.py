from src.database.config import Base
from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship

class Comment(Base):

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, nullable=False , autoincrement=True)
    content = Column(String(1024), nullable = False )

    user_id = Column(Integer, ForeignKey('users.id') , nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id') , nullable=False)

    # ----- Setting here the comment relationships ------- #
    user = relationship('User', back_populates='comments', cascade='all, delete-orphan')
    post = relationship('Post', back_populates='comments', cascade='all, delete-orphan')
    def to_json(self):

        return {
            'id':self.id,
            'user_id':self.user_id,
        }


