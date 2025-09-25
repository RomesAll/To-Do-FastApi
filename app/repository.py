from config import settings
from database import session_factory, engine
from models import Tasks
from sqlalchemy import select

class TasksDAO:

    async def dao_get_all_tasks(self):
        async with session_factory() as session:
            query = select(Tasks)
            res = await session.execute(query)
            orm = res.scalars().all()
            return orm

    async def dao_get_task_by_id(self, id: int):
        async with session_factory() as session:
            orm = await session.get(Tasks, id)
            return orm

    async def dao_create_task(self, new_data: Tasks):
        async with session_factory() as session:
            session.add(new_data)
            await session.flush()
            await session.commit()

    async def dao_update_task(self, new_data: Tasks):
        async with session_factory() as session:
            old_data = await session.get(Tasks, new_data.id)
            if old_data:
                old_data.title = new_data.title
                old_data.is_complete = new_data.is_complete
            await session.commit()

    async def dao_update_complete_task(self, id: int, flag: bool):
        async with session_factory() as session:
            old_data = await session.get(Tasks, id)
            old_data.is_complete = flag
            await session.commit()

    async def dao_delete_task(self, id: int):
        async with session_factory() as session:
            old_data = await session.get(Tasks, id)
            if old_data:
                await session.delete(old_data)
            await session.commit()