from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi_login import LoginManager
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from .pydantic_models import createuser
from fastapi import FastAPI
from fastapi import APIRouter
from . models import *
from passlib.context import CryptContext

router=APIRouter()

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
SECRET='your-secret-key'
manager=LoginManager(SECRET,token_url='/auth/token')

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

@router.post('/registration/')
async def create_user(data:createuser):
    if await User.exists(email=data.email):
        return {"message":"email already exist"}
    else:
        add_user=await User.create(email=data.email,name=data.name,password=get_password_hash(data.password))
        return add_user


@router.get("/data/")
async def all_data():
    user= await User.all()
    return user
