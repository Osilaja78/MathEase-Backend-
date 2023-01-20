from pydantic import BaseModel, EmailStr

class Question(BaseModel):
    question: str

    class Config():
        orm_mode = True

class Users(BaseModel):
    name: str
    email: EmailStr
    password: str
    confirm_password: str