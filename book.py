from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from model import Book
from schema import BookCreate, BookUpdate, Book as BookSchema
from auth import get_current_user
from model import User
from crud import get_book, get_books, create_book,  update_book, delete_book

router = APIRouter()

@router.post("/", response_model=BookSchema)
async def create_book_for_user(book: BookCreate,  db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_book(db=db, book=book, user_id=current_user.id)

@router.get("/", response_model=list[BookSchema])
async def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    books = get_books(db, user_id=current_user.id, skip=skip, limit=limit)
    return books

@router.get("/{book_id}", response_model=BookSchema)
async def read_book(book_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_book = get_book(db, user_id=current_user.id, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=BookSchema)
async def update_book_for_user(book_id: int, book: BookUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_book = update_book(db=db, book_id=book_id, book=book, user_id=current_user.id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.delete("/{book_id}", response_model=BookSchema)
async def delete_book_for_user(book_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_book = delete_book(db=db, book_id=book_id, user_id=current_user.id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
