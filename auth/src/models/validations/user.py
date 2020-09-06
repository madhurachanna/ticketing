from pydantic import BaseModel, constr, validator
import re


class User(BaseModel):
    email: str
    password: constr(min_length=4, max_length=20)

    @validator("email")
    def email_validation(cls, v):
        regex = "^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$"
        if not re.search(regex, v):
            raise ValueError("must be valid email")
        return v

    class Config:
        extra = "forbid"