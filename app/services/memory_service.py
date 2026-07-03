from app.database.db import Database
from app.utils.logger import logger


class MemoryService:

    @staticmethod
    def save_message(role, message):

        try:

            connection = Database.get_connection()

            cursor = connection.cursor()

            query = """
                INSERT INTO conversation_memory
                (
                    role,
                    message
                )
                VALUES
                (
                    %s,
                    %s
                )
            """

            cursor.execute(
                query,
                (
                    role,
                    message
                )
            )

            connection.commit()

            cursor.close()

        except Exception as ex:

            logger.exception(ex)
            raise ex

    @staticmethod
    def get_conversation_history(limit=10):

        try:

            connection = Database.get_connection()

            cursor = connection.cursor()

            query = """
                SELECT
                    role,
                    message
                FROM conversation_memory
                ORDER BY created_at DESC
                LIMIT %s
            """

            cursor.execute(
                query,
                (
                    limit,
                )
            )

            rows = cursor.fetchall()

            cursor.close()

            # Reverse so oldest message comes first
            rows.reverse()

            return rows

        except Exception as ex:

            logger.exception(ex)
            return []

    @staticmethod
    def build_context(question):

        history = MemoryService.get_conversation_history()

        prompt = ""

        for role, message in history:

            if role == "user":

                prompt += f"User: {message}\n"

            else:

                prompt += f"Assistant: {message}\n"

        prompt += f"\nCurrent Question:\n{question}"

        return prompt