from unittest.mock import patch

from app.services.tool_router_service import (
    ToolRouterService
)


@patch(
    "app.services.llm_service.LLMService.generate"
)
def test_process_question(
    mock_generate
):

    mock_generate.return_value = """
{
    "intent":"create_ticket",
    "issue":"printer issue"
}
"""

    response = ToolRouterService.process_question(
        "Create a ticket for printer issue"
    )

    assert response["status"] is True

    assert response["message"] == (
        "Ticket created successfully."
    )