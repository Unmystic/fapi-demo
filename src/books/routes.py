from fastapi import APIRouter, status
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel

from fastapi.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

router = APIRouter()


@router.get("/", response_model=List[Book])
async def get_all_books():
    return books


@router.post("/", status_code=HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)

    return new_book


@router.get("/{book_id}")
async def get_a_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Book not found")


@router.patch("/{book_id}")
async def update_a_book(book_id: int, book_update: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["publisher"] = book_update.publisher
            book["page_count"] = book_update.page_count
            book["language"] = book_update.language

            return book
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Book not found")


@router.delete("/{book_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}

    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Book not found")
