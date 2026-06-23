from app.services.ticket_service import (
    TicketService
)


def test_create_ticket():

    ticket = TicketService.create_ticket(
        "printer issue"
    )

    assert ticket["status"] == "OPEN"

    assert ticket["issue"] == "printer issue"

    assert "ticket_id" in ticket