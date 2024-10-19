from fastapi import APIRouter
from models.response_model import APIResponse
from products.infrastructure.products_infrastructure import get_products

# This is the router for the products.
router = APIRouter()

# This route returns all products.
@router.get("", response_model=APIResponse)
def all_products():
    return get_products()

# This route creates a product.
@router.post("/create_product", response_model=APIResponse)
def create_product():
    return APIResponse(
        message="Product created",
        data={"name": "apple", "price": 1.0},
        status="ok",
        status_code=201
    )