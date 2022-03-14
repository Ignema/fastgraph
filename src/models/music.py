import strawberry
from src.models.audio import Audio

@strawberry.type
class Music():
    id: int
    author: str
    album: str
    genre: str
    audioId: int
    audio: Audio