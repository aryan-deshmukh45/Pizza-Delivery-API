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

class Settings(BaseModel):
    authjwt_secret_key:str='f2b42e76033e7d876c49faa90eea330d6c8022e31b9916f67f630b907f53e6da'

class LoginModel(BaseModel):
    username:str
    password:str
    

