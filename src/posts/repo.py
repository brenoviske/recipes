from src.posts.model import Post
from sqlalchemy.orm import Session


class PostRepo:

    @staticmethod
    def add(post:Post, db:Session):

        try:

            db.add(post)
            db.commit()
            db.refresh(post)

            return {'status':'success'}

        except Exception as e:

            return {'status':'error','message':str(e)}

    @staticmethod
    def delete(id:int , db:Session):

        existing_post = db.query(Post).filter(Post.id == id).first()

        if not existing_post:

            return {'status':'error','message':'Post not found'}

        try:

            db.delete(existing_post)
            db.commit()

            return {'status':'success'}

        except Exception as e:

            return {'status':'error','message':str(e)}



