from pydantic import BaseModel, field_validator

class UserIn(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

    @field_validator('phone_number')
    @classmethod
    def validate_phone_length(cls, v: str) -> str:
        if len(v) > 50:
            raise ValueError("phone_number too long, max 50 characters")
        return v
    

    @field_validator('last_name')
    @classmethod
    def validate_last_name(cls, v: str) -> str:
        if len(v) > 20:
            raise ValueError("last_name too long, max 20 characters")
        return v
    
    @field_validator('first_name')
    @classmethod
    def validate_first_name(cls, v: str) -> str:
        if len(v) > 20:
            raise ValueError("first_name too long, max 20 characters")
        return v


class UserOut(UserIn):
    id: int | str
