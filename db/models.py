import uuid
from datetime import datetime
from sqlalchemy import Column, String,  DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    title = Column(String(80), nullable=False)
    description = Column(String(350))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)




