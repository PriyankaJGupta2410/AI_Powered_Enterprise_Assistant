from app.services.ticket_service import TicketService


def create_ticket_tool(issue: str):

    return TicketService.create_ticket(issue)