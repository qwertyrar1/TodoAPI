from pydantic import BaseModel, Field
from typing import Optional


class TaskCreateSchema(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None


class TaskUpdateSchema(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
