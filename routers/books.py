
from fastapi import APIRouter, HTTPException

router = APIRouter()

# Sample database (replace with actual data source)
books_db = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

@router.get("/api/v1/books/{book_id}")
async def get_book(book_id: int):
    book = next((b for b in books_db if b["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
