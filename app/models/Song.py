from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Song(BaseModel):
    title: str
