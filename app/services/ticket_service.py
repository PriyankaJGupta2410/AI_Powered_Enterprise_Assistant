from app.database.connection import DatabaseConnection
from app.database.queries import TicketQueries
from app.utils.logger import logger
from psycopg2.extras import RealDictCursor


class TicketService:

    @staticmethod
    def create_ticket(issue: str):

        connection = None
        cursor = None

        try:

            connection = DatabaseConnection.get_connection()

            cursor = connection.cursor(
                cursor_factory=RealDictCursor
            )

            cursor.execute(
                TicketQueries.INSERT_TICKET,
                (
                    issue,
                    "OPEN"
                )
            )

            ticket = cursor.fetchone()

            connection.commit()

            return {
                "status": True,
                "message": "Ticket created successfully.",
                "data": {
                    "ticket_id": str(ticket.get("ticket_id")),
                    "issue": ticket.get("issue"),
                    "status": ticket.get("status"),
                    "created_at": ticket.get("created_at").strftime("%Y-%m-%d %H:%M:%S")
                }
            }

        except Exception as e:

            if connection:
                connection.rollback()

            logger.error(f"Create Ticket Error : {e}")

            return {
                "status": False,
                "message": "Unable to create ticket.",
                "data": None
            }

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()