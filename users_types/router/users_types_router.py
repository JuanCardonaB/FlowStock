from fastapi import APIRouter
from models.response_model import APIResponse
from products.infrastructure.products_infrastructure import get_products
from users_types.infrastructure import users_types_infrastructure
from users_types.models import users_types_models
from db.models.FlowStockDB import users_types

# This is the router for the users types.
router = APIRouter()

# This route returns all users types.
@router.get("", response_model=APIResponse)
def all_users_types():
    return users_types_infrastructure.get_users_types()

# This route creates a user type.
@router.post("/create_user_type", response_model=APIResponse)
def create_user_type(request: users_types_models.UserTypeRequest):
    return users_types_infrastructure.create_user_type(request.name)

# This route deletes a user type.
@router.delete("/delete_user_type", response_model=APIResponse)
def delete_user_type(request: users_types_models.UserTypeDeleteRequest):
    return users_types_infrastructure.delete_user_type(request.id)

# This route return a user type by id.
@router.get("/get_user_type/{id}", response_model=APIResponse)
def get_user_type(id: int):
    return users_types_infrastructure.get_user_type_by_id(id)

# This route updates a user type.
@router.put("/update_user_type", response_model=APIResponse)
def edit_users_types(request: users_types_models.UpdateTypeRequest):
    return users_types_infrastructure.update_user_type(request)