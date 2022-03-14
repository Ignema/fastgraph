import strawberry
from src.models.video import Video
from src.models.image import Image

@strawberry.type
class Thumbnail():
    id: int
    videoId: int
    imageId: int
    video: Video
    image: Image