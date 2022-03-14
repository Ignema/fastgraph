import strawberry
from datetime import datetime
from typing import Optional
from src.models.user import User

@strawberry.type
class File():
    id: int
    filename: str
    extension: str
    url: str
    size: Optional[int]
    created_date: datetime
    updated_date: datetime
    private: bool
    access_token: Optional[str]
    user_id: int
    user: User
