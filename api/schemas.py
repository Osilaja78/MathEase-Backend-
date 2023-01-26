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

    class Config():
        orm_mode = True

class Login(BaseModel):
    email: EmailStr
    password: str

# FOR JWT AUTHENTICATION
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class ResetPasswordInit(BaseModel):
    email: EmailStr

class FinalizeResetPassword(BaseModel):
    new_password: str
    code: str

class QuestionHistory(BaseModel):
    question: str
    answer: str