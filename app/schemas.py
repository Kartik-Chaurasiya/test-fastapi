from datetime import datetime
from secrets import token_bytes
from typing import Optional, Literal
from pydantic import BaseModel, EmailStr
# from pydantic.types import conint

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True
    # rating : Optional[int] = None

# class CreatePost(BaseModel):
#     title : str
#     content : str
#     published : bool = True

# class UpdatePost(BaseModel):
#     title : str
#     content : str
#     published : bool 

class CreatePost(PostBase):
    pass

class UserResponse(BaseModel):
    user_id : int
    username : str
    email : EmailStr
    created_at = datetime

    class Config:
        orm_mode = True
        
class PostResponse(PostBase):
    post_id : int
    user_id : int
    created_at = datetime
    user: UserResponse

    class Config:
        orm_mode = True
    
class Postvoteresponse(BaseModel):
    Post: PostResponse
    votes: int

# user
class UserBase(BaseModel):
    username : str
    email : EmailStr
    password : str

class CreateUser(UserBase):
    pass

class UserLogin(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    user_id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: Literal[0, 1]