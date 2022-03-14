import strawberry
from typing import Optional
from pydantic import BaseModel
from src.models.file import File

@strawberry.type
class Video(BaseModel):
    id: int
    height: Optional[int]
    width: Optional[int]
    length: Optional[int]
    genre: str
    season: str
    title: str
    type: str
    fileId: int
    file: File