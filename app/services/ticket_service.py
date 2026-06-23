from datetime import datetime
import random


class TicketService:

    @staticmethod
    def create_ticket(issue: str):

        ticket_id = f"TKT{random.randint(1000,9999)}"

        return {
            "ticket_id": ticket_id,
            "issue": issue,
            "status": "OPEN",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }