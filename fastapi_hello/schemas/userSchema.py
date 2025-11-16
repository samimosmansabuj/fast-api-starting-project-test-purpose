from pydantic import BaseModel
from utils import Role

class UserSchema(BaseModel):
    name: str | None = "Default Name"
    email: str
    password: str
    role: Role = Role.USER


