from fastapi import APIRouter
from models.response_model import APIResponse
from products.infrastructure  import products_infrastructure
from products.model import product_model
from db.models.FlowStockDB import products

# This is the router for the products.
router = APIRouter()

# This route returns all products.
@router.get("", response_model=APIResponse)
def all_products():
    return products_infrastructure.get_products()

# This route creates a product.
@router.post("/create_product", response_model=APIResponse)
def create_product(request: product_model.ProductRequest):
    return products_infrastructure.create_product(request)

# This route returns a product by id.
@router.get("/get_product/{id}", response_model=APIResponse)
def get_product(id: int):
    return products_infrastructure.get_product_by_id(id)

# This route updates a product.
@router.put("/update_product", response_model=APIResponse)
def edit_product(request: product_model.ProductUpdateRequest):
    return products_infrastructure.update_product(request)

# This route deletes a product.
@router.delete("/delete_product", response_model=APIResponse)
def delete_product(request: product_model.ProductDeleteRequest):
    return products_infrastructure.delete_product(request.id)