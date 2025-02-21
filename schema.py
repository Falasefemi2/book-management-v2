from pydantic import BaseModel
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Book Schemas
class BookBase(BaseModel):
    title: str
    author: str
    year: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None

class Book(BookBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
