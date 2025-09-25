from config import *
from database import *
from models import *
from sqlalchemy import text
import asyncio

async def test():
    async with session_factory() as session:
        query = await session.execute(text("SELECT VERSION()"))
        res = query.all()
        print(res)

asyncio.run(test())