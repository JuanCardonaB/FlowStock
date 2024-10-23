from models.response_model import APIResponse
from db.models.FlowStockDB import users_types
from db.connection import Session
from datetime import datetime

# This function returns all users types.
def get_users_types() -> APIResponse:
    try :
        session = Session()
        # Fetch all users types
        users_types_list = session.query(users_types).all()
        session.close()

        # if there are no users types return an empty list
        if not users_types_list:
            return APIResponse(
                message="No users types found",
                data=None,
                status="ok",
                status_code=200
            )
        
        # return all users types
        return APIResponse(
            message="All users types",
            data=[users_types.to_dict() for users_types in users_types_list],
            status="ok",
            status_code=200
        )
    
    except Exception as e:
        return APIResponse(
            message=f"An error occurred while fetching users types {e}",
            data=None,
            status="error",
            status_code=500
        )

# This function creates a user type.
def create_user_type(name: users_types) -> APIResponse:
    try:
        session = Session()
        # Create a new user type
        new_user_type = users_types(
            name=name,
            created_at=datetime.now(),
        )

        # Add the new user type to the session
        session.add(new_user_type)
        # Commit the session
        session.commit()
        # Get the new user type data
        user_type_data = new_user_type.to_dict()
        # Close the session
        session.close()

        return APIResponse(
            message="User type created",
            data=user_type_data,
            status="ok",
            status_code=201
        )
    
    except Exception as e:
        return APIResponse(
            message=f"An error occurred while creating the user type {e}",
            data=None,
            status="error",
            status_code=500
        )

# This function deletes a user type.
def delete_user_type(id: users_types) -> APIResponse:
    try:
        session = Session()
        # Fetch the user type by id
        user_type = session.query(users_types).filter_by(id=id).first()
        # If the user type does not exist return an error
        if not user_type:
            return APIResponse(
                message="User type not found",
                data=None,
                status="error",
                status_code=404
            )
        
        # Delete the user type
        session.delete(user_type)
        # Commit the session
        session.commit()
        # Close the session
        session.close()

        return APIResponse(
            message="User type deleted",
            data=None,
            status="ok",
            status_code=200
        )
    
    except Exception as e:
        return APIResponse(
            message=f"An error occurred while deleting the user type {e}",
            data=None,
            status="error",
            status_code=500
        )

# This function returns a user type by id.
def get_user_type_by_id(id: users_types) -> APIResponse:
    try:
        session = Session()
        # Fetch the user type by id
        user_type = session.query(users_types).filter_by(id=id).first()
        # If the user type does not exist return an error
        if not user_type:
            return APIResponse(
                message="User type not found",
                data=None,
                status="error",
                status_code=404
            )
        
        # Get the user type data
        user_type_data = user_type.to_dict()
        # Close the session
        session.close()

        return APIResponse(
            message="User type found",
            data=user_type_data,
            status="ok",
            status_code=200
        )
    
    except Exception as e:
        return APIResponse(
            message=f"An error occurred while fetching the user type {e}",
            data=None,
            status="error",
            status_code=500
        )

# This function updates a user type.
def update_user_type(user_type_data: users_types) -> APIResponse:
    try:
        session = Session()
        # Fetch the user type by id
        user_type = session.query(users_types).filter_by(id=user_type_data.id).first()
        # If the user type does not exist return an error
        if not user_type:
            return APIResponse(
                message="User type not found",
                data=None,
                status="error",
                status_code=404
            )
        
        # Update the user type name
        user_type.name = user_type_data.name
        # Commit the session
        session.commit()
        # Get the user type data
        user_type_data = user_type.to_dict()
        # Close the session
        session.close()

        return APIResponse(
            message="User type updated",
            data=user_type_data,
            status="ok",
            status_code=200
        )
    except Exception as e:
        return APIResponse(
            message=f"An error occurred while updating the user type {e}",
            data=None,
            status="error",
            status_code=500
        )