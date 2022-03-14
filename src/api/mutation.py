import typing
import strawberry

import src.models as model
import src.data.services as services

@strawberry.type
class Mutation:
    @strawberry.field
    def create_user(self, id: int) -> model.User:
        return services.create_model("user", {"id": id})
    # # User mutation operations (create, update, delete)
    # @strawberry.field
    # def create_user(self, user: model.User) -> model.User:
    #     return data.create_user(user)  
    # @strawberry.field
    # def update_user(self, id: int, user: model.User) -> model.User:
    #     return data.update_user(id, user)
    # @strawberry.field
    # def delete_user(self, id: int) -> model.User:
    #     return data.delete_user(id)

    # # Document mutation operations (create, update, delete)
    # @strawberry.field
    # def create_document(self, document: model.Document) -> model.Document:
    #     return data.create_document(document)
    # @strawberry.field
    # def update_document(self, id: int, document: model.Document) -> model.Document:
    #     return data.update_document(id, document)
    # @strawberry.field
    # def delete_document(self, id: int) -> model.Document:
    #     return data.delete_document(id)

    # # Audio mutation operations (create, update, delete)
    # @strawberry.field
    # def create_audio(self, audio: model.Audio) -> model.Audio:
    #     return data.create_audio(audio)
    # @strawberry.field
    # def update_audio(self, id: int, audio: model.Audio) -> model.Audio:
    #     return data.update_audio(id, audio)
    # @strawberry.field
    # def delete_audio(self, id: int) -> model.Audio:
    #     return data.delete_audio(id)

    # # Music mutation operations (create, update, delete)  
    # @strawberry.field
    # def create_music(self, music: model.Music) -> model.Music:
    #     return data.create_music(music)
    # @strawberry.field
    # def update_music(self, id: int, music: model.Music) -> model.Music:
    #     return data.update_music(id, music)
    # @strawberry.field
    # def delete_music(self, id: int) -> model.Music:
    #     return data.delete_music(id)

    # # Video mutation operations (create, update, delete)   
    # @strawberry.field
    # def create_video(self, video: model.Video) -> model.Video:
    #     return data.create_video(video)
    # @strawberry.field
    # def update_video(self, id: int, video: model.Video) -> model.Video:
    #     return data.update_video(id, video)
    # @strawberry.field
    # def delete_video(self, id: int) -> model.Video:
    #     return data.delete_video(id)

    # # File mutation operations (create, update, delete)
    # @strawberry.field
    # def create_file(self, file: model.File) -> model.File:
    #     return data.create_file(file)
    # @strawberry.field
    # def update_file(self, id: int, file: model.File) -> model.File:
    #     return data.update_file(id, file)
    # @strawberry.field
    # def delete_file(self, id: int) -> model.File:
    #     return data.delete_file(id)

    # # Image mutation operations (create, update, delete)
    # @strawberry.field
    # def create_image(self, image: model.Image) -> model.Image:
    #     return data.create_image(image)
    # @strawberry.field
    # def update_image(self, id: int, image: model.Image) -> model.Image:
    #     return data.update_image(id, image)
    # @strawberry.field
    # def delete_image(self, id: int) -> model.Image:
    #     return data.delete_image(id)

    # # Project mutation operations (create, update, delete)
    # @strawberry.field
    # def create_project(self, project: model.Project) -> model.Project:
    #     return data.create_project(project)
    # @strawberry.field
    # def update_project(self, id: int, project: model.Project) -> model.Project:
    #     return data.update_project(id, project)
    # @strawberry.field
    # def delete_project(self, id: int) -> model.Project:
    #     return data.delete_project(id)

    # # Presentation mutation operations (create, update, delete)
    # @strawberry.field
    # def create_presentation(self, presentation: model.Presentation) -> model.Presentation:
    #     return data.create_presentation(presentation)
    # @strawberry.field
    # def update_presentation(self, id: int, presentation: model.Presentation) -> model.Presentation:
    #     return data.update_presentation(id, presentation)
    # @strawberry.field
    # def delete_presentation(self, id: int) -> model.Presentation:
    #     return data.delete_presentation(id)

    # # Thumbnail mutation operations (create, update, delete)
    # @strawberry.field
    # def create_thumbnail(self, thumbnail: model.Thumbnail) -> model.Thumbnail:
    #     return data.create_thumbnail(thumbnail)
    # @strawberry.field
    # def update_thumbnail(self, id: int, thumbnail: model.Thumbnail) -> model.Thumbnail:
    #     return data.update_thumbnail(id, thumbnail)
    # @strawberry.field
    # def delete_thumbnail(self, id: int) -> model.Thumbnail:
    #     return data.delete_thumbnail(id)