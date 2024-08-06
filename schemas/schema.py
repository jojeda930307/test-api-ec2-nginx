from pydantic import BaseModel


# User Schema
class UserCreate(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


# Book Schema
class BookBase(BaseModel):
    title: str
    description: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


# Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
