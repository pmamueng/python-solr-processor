from pydantic import BaseModel


class MessageBase(BaseModel):
    id: int
    message: str
