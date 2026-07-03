from fastapi import APIRouter

from app.models.request_model import AskRequest
from app.services.tool_router_service import ToolRouterService
from app.utils.error_handler import error_response
from app.utils.validators import validate_question

router = APIRouter()


@router.post("/ask")
def ask_question(request: AskRequest):

    is_valid, message = validate_question(request.question)

    if not is_valid:
        return error_response(message)

    response = ToolRouterService.process_question(
        request.question
    )

    return response