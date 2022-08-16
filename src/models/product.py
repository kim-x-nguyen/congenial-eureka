from pydantic import BaseModel, Field
from typing import Optional

class ProductModel(BaseModel):
    item_id: Optional[int] = None
    name: str
    code: str
    description: Optional[str] = Field(None, description="Optional description", max_length=100)
    price: float = Field(..., gt=0, description="Price must be greater than 0")