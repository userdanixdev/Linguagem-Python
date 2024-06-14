from pydantic import BaseModel, Field
from store.core.schemas.base import BaseSchemaMixin

class ProductIn(BaseSchemaMixin):
    name: str = Field(...,description="Product Name")
    quantity: int = Field(...,description="Product Quantity")
    price: float = Field(...,description="Product price")
    status: bool = Field(...,description="Product Status")