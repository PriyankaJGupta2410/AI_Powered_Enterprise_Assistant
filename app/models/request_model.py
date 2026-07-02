from pydantic import BaseModel, Field


class AskRequest(BaseModel):

    session_id: str = Field(
        ...,
        description="Unique session identifier"
    )

    question: str = Field(
        ...,
        min_length=1
    )