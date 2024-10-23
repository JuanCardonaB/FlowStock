from pydantic import BaseModel

# This class is used to receive the information to create a product.
class ProductRequest(BaseModel):
    title: str
    description: str
    price: float
    stock: int

# This class is used to receive the information to update a product.
class ProductUpdateRequest(BaseModel):
    id: int
    title: str
    description: str
    price: float
    stock: int
    created_at: str

class ProductDeleteRequest(BaseModel):
    id: int