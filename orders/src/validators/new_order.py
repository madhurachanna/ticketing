from pydantic import BaseModel


class NewOrderValidatior(BaseModel):
    ticket_id: str

    class Config:
        extra = "forbid"
