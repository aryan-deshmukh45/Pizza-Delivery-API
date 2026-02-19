from pydantic import BaseModel, EmailStr
from typing import Optional

class SignUpModel(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = True

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "aryan",
                "email": "aryan@gmail.com",
                "password": "password123",
                "is_staff": False,
                "is_active": True
            }
        }
    }


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_staff: bool
    is_active: bool

    model_config = {
        "from_attributes": True
    }
