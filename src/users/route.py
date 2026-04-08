from fastapi import APIRouter , Form , Depends
from sqlalchemy.orm import Session


# ------- Imports related to the src.users folder entirely -----

from src.database.config import get_db
from src.users.model import User
from src.users.controller import UserController

router = APIRouter()

# ------- Security methods ------

def hash(password:str):

def check(plain:str,password_hashed:str):



@router.post('/add')
def add(
    email:str = Form(...),
    username:str = Form(...),
    password:str = Form(...),
    db:Session = Depends(get_db)
):

    new_user = User(
        email = email,
        username = username,
        password_hash = password
    )

    return UserController.add(new_user,db)

@router.post('/login')
def login(
        email:str = Form(...),
        password:str = Form(...),
        db:Session = Depends(get_db)
):

    existing_user = db.query(User).filter(User.email == email).first() # --- Checking here to see if the user lies within the current database

    if existing_user and check(password,existing_user.password_hash):
        return {'status':'success'}
    return {'status':'error','message':'Email or Password is incorrect'}



@router.delete('/delete')
def delete(
        id:int ,
        db:Session = Depends(get_db)
):
    return UserController.remove(id,db)

@router.put('/update')
def update(
        id:int ,
        email:str = Form(...),
        username:str = Form(...),
        db:Session = Depends(get_db)
):

    return UserController.update(id,email,username,db)
