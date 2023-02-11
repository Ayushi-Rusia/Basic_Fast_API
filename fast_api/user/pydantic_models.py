from pydantic import BaseModel
import uuid


class createuser(BaseModel):
    name:str
    email:str
    password:str

