from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Tasks(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    is_complete: Mapped[bool] = mapped_column(default=False)