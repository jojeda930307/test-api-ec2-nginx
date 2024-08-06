from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud.crud import get_books, create_book
from database.db import get_db
from models.model import User
from schemas.schema import BookCreate, Book
from security.get_current_user import get_current_user

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    books = get_books(db, skip=skip, limit=limit)
    return books


@router.post("/", response_model=Book)
def create_new_book(book: BookCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_book(db=db, book=book, user_id=current_user.id)


