import strawberry
from src.models.user import User
from src.models.file import File

@strawberry.type
class Project():
    id: int
    name: str
    category: str
    userId: int
    fileId: int
    user: User
    file: File