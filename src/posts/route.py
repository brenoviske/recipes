from fastapi import APIRouter , Form


router = APIRouter()

@router.post('/add')
def add(
        content:str = Form(...)
)