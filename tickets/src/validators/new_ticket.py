from pydantic import BaseModel, confloat


class NewTicketValidator(BaseModel):
    title: str
    price: confloat(gt=0)

    class Config:
        extra = "forbid"
