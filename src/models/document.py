import strawberry
from typing import Optional
from src.models.file import File

@strawberry.type
class Document():
    id: int
    font: str
    text_size: int
    characters: Optional[int]
    fileId: int
    file: File