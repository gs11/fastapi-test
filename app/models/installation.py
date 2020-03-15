from app.models.custom_types import StrictInt
from datetime import date
from pydantic import BaseModel

class Installation(BaseModel):
    id: StrictInt
    name: str
    creation_date: date
