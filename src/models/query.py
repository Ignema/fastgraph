import typing
import strawberry
from src.models.book import Book
from src.data.books import get_books

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)