from pydantic import BaseModel, Field

class TasksAddSchemas(BaseModel):
    title: str
    is_complete: bool = False

class TasksSchemas(TasksAddSchemas):
    id: int = Field(ge=1)