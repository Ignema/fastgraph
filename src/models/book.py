import strawberry

@strawberry.type
class Book:
    title: str
    author: str