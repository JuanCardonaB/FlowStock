from pydantic import BaseModel

# This class is used to receive the information to create a user type.
class UserTypeRequest(BaseModel):
    name: str

class UserTypeDeleteRequest(BaseModel):
    id: int

class UpdateTypeRequest(BaseModel):
    id: int
    name: str