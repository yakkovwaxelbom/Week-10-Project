from pydantic import BaseModel, field_validator


class UserIn(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

    @field_validator('phone_number')
    @classmethod
    def validate_email_format(cls, v: str) -> str:
        return v
    
    def to_dict(self):
        return self.model_dump()
    

class UserOut(UserIn):
    id: int | str
