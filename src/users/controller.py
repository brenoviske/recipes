from src.users.model import User
from src.users.repo import UserRepo
from sqlalchemy.orm import Session

class UserController:

    @staticmethod
    def add(user:User,db:Session):

        return UserRepo.add_user(user,db)

    @staticmethod
    def remove(id:int, db:Session):

        return UserRepo.remove_user(id,db)

    @staticmethod
    def update(id:int , email:str , username:str, db:Session):

        return UserRepo.update_user(id,email,username,db)

