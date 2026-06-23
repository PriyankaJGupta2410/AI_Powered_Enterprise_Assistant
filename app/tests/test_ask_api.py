from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


@patch(
    "app.services.tool_router_service.ToolRouterService.process_question"
)
def test_ask_endpoint(
    mock_process_question
):

    mock_process_question.return_value = {
        "status": True,
        "message": "Ticket created successfully.",
        "data": {
            "ticket_id": "TKT1234",
            "issue": "printer issue",
            "status": "OPEN"
        }
    }

    response = client.post(
        "/ask",
        json={
            "question":
            "Create a ticket for printer issue"
        }
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["status"] is True

    assert response_data["message"] == (
        "Ticket created successfully."
    )