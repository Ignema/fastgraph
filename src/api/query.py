from datetime import datetime
import strawberry
import src.models as model
import src.data.services as services
from typing import List, Optional

@strawberry.type
class Query:
    # Audio find operation
    @strawberry.field
    async def audio(self, id: Optional[int], length: Optional[int], fileId: Optional[int]) -> List[model.Audio]:
        return await services.get_audios(id, length, fileId)

    # Document find operation
    @strawberry.field
    async def document(self, id: Optional[int], font: Optional[str], text_size: Optional[int], characters: Optional[int], fileId: Optional[int]) -> List[model.Document]:
        return await services.get_documents(id, font, text_size, characters, fileId)

    # File find operation
    @strawberry.field
    async def file(self, id: Optional[int], filename: Optional[str], extension: Optional[str], url: Optional[str], size: Optional[int], created_date: Optional[datetime], updated_date: Optional[datetime], private: Optional[bool], access_token: Optional[str], user_id: Optional[int]) -> List[model.File]:
        return await services.get_files(id, filename, extension, url, size, created_date, updated_date, private, access_token, user_id)

    # Image find operation
    @strawberry.field
    async def image(self, id: Optional[int], height: Optional[int], width: Optional[int], projectId: Optional[int], fileId: Optional[int]) -> List[model.Image]:
        return await services.get_images(id, height, width, projectId, fileId)

    # Music find operation
    @strawberry.field
    async def music(self, id: Optional[int], author: Optional[str], album: Optional[str], genre: Optional[str], audioId: Optional[int]) -> List[model.Music]:
        return await services.get_music(id, author, album, genre, audioId)

    # Presentation find operation
    @strawberry.field
    async def presentation(self, id: Optional[int], title: Optional[str], total_slides: Optional[int], fileId: Optional[int]) -> List[model.Presentation]:
        return await services.get_presentations(id, title, total_slides, fileId)

    # User find operation
    @strawberry.field
    async def user(self, id: Optional[int], email: Optional[str]) -> List[model.User]:
        return await services.get_users(id, email)
   
    # Video find operation
    @strawberry.field
    async def video(self, id: Optional[int], height: Optional[int], width: Optional[int], length: Optional[int], genre: Optional[str], season: Optional[str], title: Optional[str], type: Optional[str], fileId: Optional[int]) -> List[model.Video]:
        return await services.get_videos(id, height, width, length, genre, season, title, type, fileId)

    # Project find operation
    @strawberry.field
    async def projects(self, id: Optional[int], name: Optional[str], category: Optional[str], userId: Optional[int], fileId: Optional[int]) -> List[model.Project]:
        return await services.get_projects(id, name, category, userId, fileId)

    # Thumbnail find operation
    @strawberry.field
    async def thumbnail(self, id: Optional[int], videoId: Optional[int], imageId: Optional[int]) -> List[model.Thumbnail]:
        return await services.get_thumbnails(id, videoId, imageId)