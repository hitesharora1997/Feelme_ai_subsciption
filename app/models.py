from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

subscription = {}


class Subscription(BaseModel):
    user_external_id: str
    user_email: EmailStr
    duration: int
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    def save(self) -> None:
        subscription[self.user_external_id] = self

    def to_dict(self):
        return self.dict
