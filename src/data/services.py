from datetime import datetime
from typing import List, Optional
from src.data.connector import connect
from src.models import *


async def get_audios(
    id: Optional[int], 
    length: Optional[int], 
    fileId: Optional[int],
) -> List[Audio]:
    return await connect(
        lambda prisma: prisma.audio.find_many(
            where={
                "id": id, 
                "length": length, 
                "fileId": fileId,
            }
        )
    )


async def get_documents(
    id: Optional[int], 
    font: Optional[str], 
    text_size: Optional[int], 
    characters: Optional[int], 
    fileId: Optional[int],
) -> List[Document]:
    return await connect(
        lambda prisma: prisma.document.find_many(
            where={
                "id": id,
                "font": font,
                "text_size": text_size,
                "characters": characters,
                "fileId": fileId,
            }
        )
    )


async def get_files(
    id: Optional[int],
    filename: Optional[str],
    extension: Optional[str],
    url: Optional[str],
    size: Optional[int],
    created_date: Optional[datetime],
    updated_date: Optional[datetime],
    private: Optional[bool],
    access_token: Optional[str],
    user_id: Optional[int],
) -> List[File]:
    return await connect(
        lambda prisma: prisma.file.find_many(
            where={
                "id": id,
                "filename": filename,
                "extension": extension,
                "url": url,
                "size": size,
                "created_date": created_date,
                "updated_date": updated_date,
                "private": private,
                "access_token": access_token,
                "user_id": user_id,
            }
        )
    )

async def get_images(
    id: Optional[int],
    height: Optional[int],
    width: Optional[int],
    projectId: Optional[int],
    fileId: Optional[int],
) -> List[Image]:
    return await connect(
        lambda prisma: prisma.image.find_many(
            where={
                "id": id,
                "height": height,
                "width": width,
                "projectId": projectId,
                "fileId": fileId,
            }
        )
    )

async def get_music(
    id: Optional[int],
    author: Optional[str],
    album: Optional[str],
    genre: Optional[str],
    audioId: Optional[int],
) -> List[Music]:
    return await connect(
        lambda prisma: prisma.music.find_many(
            where={
                "id": id,
                "author": author,
                "album": album,
                "genre": genre,
                "audioId": audioId,
            }
        )
    )

async def get_presentations(
    id: Optional[int],
    title: Optional[str],
    total_slides: Optional[int],
    fileId: Optional[int],
) -> List[Presentation]:
    return await connect(
        lambda prisma: prisma.presentation.find_many(
            where={
                "id": id,
                "title": title,
                "total_slides": total_slides,
                "fileId": fileId,
            }
        )
    )

async def get_projects(
    id: Optional[int],
    name: Optional[str],
    category: Optional[str],
    userId: Optional[int],
    fileId: Optional[int],
) -> List[Project]:
    return await connect(
        lambda prisma: prisma.project.find_many(
            where={
                "id": id,
                "name": name,
                "category": category,
                "userId": userId,
                "fileId": fileId,
            }
        )
    )

async def get_thumbnails(
    id: Optional[int],
    videoId: Optional[int],
    imageId: Optional[int],
) -> List[Thumbnail]:
    return await connect(
        lambda prisma: prisma.thumbnail.find_many(
            where={
                "id": id,
                "videoId": videoId,
                "imageId": imageId,
            }
        )
    )

async def get_users(
    id: Optional[int],
    email: Optional[str],
) -> List[User]:
    return await connect(
        lambda prisma: prisma.user.find_many(
            where={
                "id": id,
                "email": email,
            }
        )
    )

async def get_videos(
    id: Optional[int],
    height: Optional[int],
    width: Optional[int],
    length: Optional[int],
    genre: Optional[str],
    season: Optional[str],
    title: Optional[str],
    type: Optional[str],
    fileId: Optional[int],
) -> List[Video]:
    return await connect(
        lambda prisma: prisma.video.find_many(
            where={
                "id": id,
                "height": height,
                "width": width,
                "length": length,
                "genre": genre,
                "season": season,
                "title": title,
                "type": type,
                "fileId": fileId,
            }
        )
    )