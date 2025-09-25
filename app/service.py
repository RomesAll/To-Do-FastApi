from repository import TasksDAO
from schemas import TasksSchemas, TasksAddSchemas
from models import Tasks

class TasksService:

    def __init__(self):
        self.task_dao = TasksDAO()

    async def service_get_all_tasks(self):
        orm = await self.task_dao.dao_get_all_tasks()
        dto = [TasksSchemas.model_validate(row, from_attributes=True) for row in orm]
        return dto

    async def service_get_task_by_id(self, id: int):
        orm = await self.task_dao.dao_get_task_by_id(id)
        dto = TasksSchemas.model_validate(orm, from_attributes=True)
        return dto

    async def service_create_task(self, new_data: TasksAddSchemas):
        orm = Tasks(title=new_data.title, is_complete=new_data.is_complete)
        res = await self.task_dao.dao_create_task(orm)
        return res

    async def service_update_task(self, new_data: TasksSchemas):
        orm = Tasks(id=new_data.id, title=new_data.title, is_complete=new_data.is_complete)
        res = await self.task_dao.dao_update_task(orm)
        return res

    async def service_update_complete_task(self, id: int, flag: bool):
        res = await self.task_dao.dao_update_complete_task(id, flag)
        return res

    async def service_delete_task(self, id: int):
        res = await self.task_dao.dao_delete_task(id)
        return res