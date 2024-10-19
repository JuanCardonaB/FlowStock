from models.response_model import APIResponse
from db.models.FlowStockDB import users_types
from db.connection import Session

# This function returns all users types.
def get_users_types() -> APIResponse:
    try :
        session = Session()
        users_types_list = session.query(users_types).all()
        session.close()
        if not users_types_list:
            return APIResponse(
                message="No users types found",
                data=None,
                status="ok",
                status_code=200
            )
        return APIResponse(
            message="All users types",
            data=[users_types.to_dict() for users_types in users_types_list],
            status="ok",
            status_code=200
        )
    except Exception as e:
        return APIResponse(
            message="An error occurred while fetching users types",
            data=None,
            status="error",
            status_code=500
        )