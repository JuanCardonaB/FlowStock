from pydantic import BaseModel
from typing import List

# This class is used to receive the information to create a product.
class ProductRequest(BaseModel):
    title: str
    description: str
    price: float
    stock: int
    images: List[str]

# This class is used to receive the information to update a product.
class ProductUpdateRequest(BaseModel):
    id: int
    title: str
    description: str
    price: float
    stock: int
    created_at: str
    old_images: List[str]
    new_images: List[str]

class ProductResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    stock: int
    images: List[str] | str
    created_at: str

class ProductDeleteRequest(BaseModel):
    id: int