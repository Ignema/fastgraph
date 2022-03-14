from prisma import Prisma

async def connect(resolver):
    prisma = Prisma(
        datasource={
            "url": "file:prisma/dev.db"
        },
    )
    await prisma.connect()
    result = await resolver(prisma)
    await prisma.disconnect()
    return result