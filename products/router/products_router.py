from fastapi import APIRouter
from models.response_model import APIResponse
from products.infrastructure.get_products import get_products

router = APIRouter()

@router.get("", response_model=APIResponse)
def all_products():
    return get_products()