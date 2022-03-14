import strawberry
from typing import Optional
from src.models.file import File

@strawberry.type
class Presentation():
    id: int
    title: str
    total_slides: Optional[int]
    fileId: int
    file: File