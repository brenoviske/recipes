from sqlalchemy.orm import Session
from src.users.model import User

class UserRepo:


    @staticmethod
    def add_user(user:User,db:Session):

        user_email = db.query(User).filter(User.email == user.email).first()
        user_username = db.query(User).filter(User.username == user.username).first()

        if user_email:

            return {'status':'error','message':'User already exists'}

        if user_username:

            return {'status':'error','message':'User already exists'}

        try:

            db.add(user)
            db.commit()
            db.refresh(user)

            return {'status':'success'}

        except Exception as e:

            return {'status':'error','message':str(e)}

    @staticmethod
    def remove_user(id:int,db:Session):

        existing_user = db.query(User).filter(User.id == id).first()

        if not existing_user:

            return {'status':'error','message':'User does not exist'}

        try:

            db.delete(existing_user)
            db.commit()
            db.refresh(existing_user)

            return {'status':'success'}

        except Exception as e:

            return {'status':'error','message':str(e)}


    @staticmethod
    def update_user(id:int , email:str , username:str, db:Session):

        existing_user = db.query(User).filter(User.id == id).first()

        if not existing_user:

            return {'status':'error','message':'User does not exist'}

        try:

            if email:
                existing_user.email = email
            if username:
                existing_user.username = username

            db.commit()

            return {'status':'success'}

        except Exception as e:

            return {'status':'error','message':str(e)}

