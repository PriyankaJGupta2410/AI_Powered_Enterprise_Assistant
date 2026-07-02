from fastapi import APIRouter

from app.models.request_model import AskRequest
from app.services.tool_router_service import ToolRouterService

router = APIRouter()


@router.post("/ask")
def ask(request: AskRequest):

    return ToolRouterService.process_question(
        session_id=request.session_id ,
        question=request.question
    )