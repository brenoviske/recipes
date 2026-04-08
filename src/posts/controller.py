from src.posts.model import Post
from src.posts.repo import  PostRepo
from sqlalchemy.orm import Session


class PostController:

    @staticmethod
    def add(new_post:Post , db:Session):

        return PostRepo.add(new_post, db)

    @staticmethod
    def remove(id:int , db:Session):

        return PostRepo.delete(id,db)

