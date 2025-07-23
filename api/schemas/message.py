from pydantic import BaseModel, Field


class MessageSend(BaseModel):
    message: str
    to: str
    from_: str = Field(..., alias="from")
    timeToLifeSec: int

    class ConfigDict:
        validate_by_name = True


class MessageResponse(BaseModel):
    message: str
