import strawberry
from typing import Optional
from src.models.project import Project
from src.models.file import File

@strawberry.type
class Image():
    id: int
    height: Optional[int]
    width: Optional[int]
    projectId: int
    fileId: int
    project: Project
    file: File