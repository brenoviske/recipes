# ------- FastApi imports ------

from fastapi import  FastAPI , Request
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# -------- Other imports ------

from sqlalchemy.orm import Session


# ------ Src modules imports ------
from src.users.model import User
from src.users.route import router as user_router
from src.users.route import get_current_user
from src.comments.route import router as comment_router
from src.posts.route import router as post_router
from src.database.config import get_db



# ------- Main route , addressing the FastAPI to the main file -----
app = FastAPI()
templates = Jinja2Templates(directory="./templates")

# -------- Including the folders routers on the main file --------
app.include_router(user_router,  prefix="/users", tags=["users"])
app.include_router(comment_router, prefix="/comments", tags=["comments"])
app.include_router(post_router, prefix="/posts", tags=["posts"])




# ------- Helper methods -------

def render(template:str,request:Request, content:dict = None):

    return templates.TemplateResponse(template, {"request": request, "content": content})



# --------- Public routes -------- #

def index(request:Request):

    return render('index.html', request)

def register(request:Request):

    return render('register.html', request)

def forget_password(request:Request):

    return render('forget_password.html', request)

def redefine_password(request:Request):

    return render('redefine_password.html', request)


# ---- Authenticated routes -------

def main(
        request:Request,
        current_user:User = Depends(get_current_user),
        db:Session = Depends(get_db)
):

    user = db.query(User).filter_by(
        id = current_user.id
    ).first()

    content = {'user': user}

    return render('main.html',request,content = content)


