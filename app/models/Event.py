from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    id: Optional[UUID] = uuid4()
    avenue: str
    datetime: datetime
