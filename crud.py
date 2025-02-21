from sqlalchemy.orm import Session
from model import Book
from schema import BookCreate, BookUpdate

def get_books(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Book).filter(Book.owner_id == user_id).offset(skip).limit(limit).all()

def get_book(db: Session, user_id: int, book_id: int):
    return db.query(Book).filter(Book.owner_id == user_id, Book.id == book_id).first()

def create_book(db: Session, book: BookCreate, user_id: int):
    db_book = Book(**book.model_dump(), owner_id=user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book: BookUpdate, user_id: int):
    db_book = db.query(Book).filter(Book.owner_id == user_id, Book.id == book_id).first()
    if db_book:
        for key, value in book.model_dump().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int, user_id: int):
    db_book = db.query(Book).filter(Book.owner_id == user_id, Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
    