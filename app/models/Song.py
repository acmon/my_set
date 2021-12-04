from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Song(BaseModel):
    # SEE - Pydantic
    id: Optional[UUID] = uuid4()
    title: str
