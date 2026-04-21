from fastapi import APIRouter , Form , Depends
from sqlalchemy.orm import Session

# ------ Src modules imports ------- #

from src.users.model import User
from src.posts.model import Post
from src.comments.model import Comment
from src.comments.controller import CommentController
from src.database.config import get_db


router = APIRouter()

@router.post('/add')
def add(
    content:str = Form(...),
    current_user:User = Depends(get_current_user),
    current_post:Post = Depends(get_current_post),
):

    new_comment = Comment(
        content = content,
        user_id = current_user.id,
        post_id = current_post.id
    )

    return CommentController.add(new_comment, current_user)


@router.delete('/delete')
def delete(
        id:int ,
        current_user:User= Depends(get_current_user),
        current_post:Post = Depends(get_current_post),
        db:Session = Depends(get_db)
):

    return CommentController.delete(id,current_user.id , current_post.id, db)

@router.put('/update')
def update(
        id:int ,
        current_user:User = Depends(get_db),
        current_post:Post = Depends(get_current_post),
        db:Session = Depends(get_db)
):

    return CommentController.update(id,current_user.id,current_post.id,db)



