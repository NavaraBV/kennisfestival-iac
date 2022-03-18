from enum import Enum
from typing import Optional

from pydantic import BaseModel


class StatusEnum(str, Enum):
    new = 'new'
    completed = 'completed'


class Task(BaseModel):
    _id: Optional[str]
    task: str
    assignee: str
    status: StatusEnum
