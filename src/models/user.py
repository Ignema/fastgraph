import strawberry

@strawberry.type
class User:
    id: int
    email: str
    password: str