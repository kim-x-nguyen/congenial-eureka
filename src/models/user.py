from pydantic import BaseModel, Field
from typing import Optional

class UserModel(BaseModel):
    user_id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    age: int = Field(..., ge=18, description="Age must be greater than 18")