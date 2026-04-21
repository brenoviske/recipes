from urllib.parse import uses_relative

from sqlalchemy.orm import Session
from src.comments.model import Comment

class CommentRepo:

    @staticmethod
    def add(new_comment:Comment, db:Session):

        try:

            db.add(new_comment)
            db.commit()
            db.refresh(new_comment)

            return {'status':'success'}

        except Exception as e:

            return {'status':'error','message':str(e)}

    @staticmethod
    def delete(id:int , user_id:int , post_id:int,db:Session):

        existingComment = db.query(Comment).filter_by(
            id = id ,
            user_id = user_id,
            post_id = post_id
        ).first()

        if not existingComment:

            return {'status':'error','message':'Comment not found'}

        try:

            db.delete(existingComment)
            db.commit()

            return {'status':'success'}

        except Exception as e:

            return {'status':'error','message':str(e)}

    @staticmethod
    def update(id:int ,user_id:int , post_id:int, new_content:str, db:Session):

        existingComment = db.query(Comment).filter_by(
            id = id ,
            user_id = user_id ,
            post_id = post_id
        ).first()

        if not existingComment:

            return {'status':'error','message':'Comment not found'}

        try:

            if new_content:
                existingComment.content = new_content

            db.commit()

            return {'status':'success'}


        except Exception as e:

            return {'status':'error','message':str(e)}

