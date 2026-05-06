from pydantic import BaseModel

class RequestCreate(BaseModel):
    name: str
    email: str
