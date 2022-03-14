import strawberry
from typing import Optional
from src.models.file import File

@strawberry.type
class Audio():
    id: int
    length: Optional[int]
    fileId: int
    file: File