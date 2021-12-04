from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Event(BaseModel):
    id: Optional[UUID] = uuid4()
    avenue: str
