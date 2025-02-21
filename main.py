from fastapi import FastAPI
from user import router as user_router
from book import router as book_router
from database import engine, Base  # Import engine and Base

app = FastAPI()

# Include routers
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(book_router, prefix="/books", tags=["books"])

# Create tables immediately
Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"message": "welcome to the project"}