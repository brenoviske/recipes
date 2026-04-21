from sqlalchemy.orm import Session
from src.comments.model import Comment
from src.comments.repo import CommentRepo


class CommentController:

    @staticmethod
    def add(new_comment:str, db:Session):

        return CommentRepo.add(new_comment, db)

    @staticmethod
    def delete(id:int , db:Session):

        return CommentRepo.delete(id,db)

    @staticmethod
    def update(id:int , new_comment:str, db:Session):

        return CommentRepo.update(id, new_comment, db)


