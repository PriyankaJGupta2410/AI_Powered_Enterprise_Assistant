from pydantic import BaseModel


class AskResponse(BaseModel):
    status: bool
    message: str
    data: dict | None = None