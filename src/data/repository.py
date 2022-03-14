from .connector import connect


async def get_models(model):
    return await connect(lambda prisma: getattr(prisma, model).find_many())


async def get_model(model, id):
    return await connect(
        lambda prisma: getattr(prisma, model).find_first(where={"id": id})
    )

async def create_model(model, data):
    return await connect(lambda prisma: getattr(prisma, model).create(data))


async def update_model(model, id, data):
    return await connect(lambda prisma: getattr(prisma, model).update(id=id, data=data))


async def delete_model(model, id):
    return await connect(lambda prisma: getattr(prisma, model).delete(id=id))
