from app.constants.constants import SYSTEM_PROMPT
from app.services.conversation_service import ConversationService
from app.services.llm_service import LLMService
from app.tools.create_ticket_tool import create_ticket_tool
from app.utils.json_parser import JsonParser
from app.utils.logger import logger


class ToolRouterService:

    @staticmethod
    def process_question(session_id: str, question: str):

        # -----------------------------------------
        # Get Conversation History
        # -----------------------------------------
        history = ConversationService.get_prompt_history(session_id)

        prompt = f"""
            {SYSTEM_PROMPT}

            Conversation History:
            {history}

            Current User Question:
            {question}
        """

        # -----------------------------------------
        # Call LLM
        # -----------------------------------------
        response = LLMService.generate(prompt)

        logger.info(response)

        data = JsonParser.parse_response(response)

        if data is None:

            assistant_message = "Unable to understand request."

            ConversationService.save_user_message(
                session_id=session_id,
                message=question
            )

            ConversationService.save_assistant_message(
                session_id=session_id,
                message=assistant_message
            )

            return {
                "status": False,
                "message": assistant_message,
                "data": None
            }

        intent = data.get("intent", "").lower().strip()

        assistant_message = ""
        response_data = None
        status = False

        # =========================================
        # CREATE TICKET
        # =========================================

        if intent == "create_ticket":

            issue = data.get("issue", "").strip()

            invalid_values = [
                "",
                "...",
                "none",
                "null",
                "unknown",
                "n/a"
            ]

            if issue.lower() in invalid_values:

                assistant_message = "Please provide valid issue details."

            else:

                ticket = create_ticket_tool(issue)

                status = ticket["status"]

                assistant_message = ticket["message"]

                response_data = ticket["data"]

        # =========================================
        # GENERAL QUERY
        # =========================================

        elif intent == "general_query":

            answer = data.get("answer", "").strip()

            if answer:

                assistant_message = answer
                status = True

            else:

                assistant_message = "Unable to generate response."

        # =========================================
        # UNKNOWN INTENT
        # =========================================

        else:

            assistant_message = "Unsupported intent."

        # -----------------------------------------
        # Save Conversation Memory
        # -----------------------------------------

        ConversationService.save_user_message(
            session_id=session_id,
            message=question
        )

        ConversationService.save_assistant_message(
            session_id=session_id,
            message=assistant_message
        )

        # -----------------------------------------
        # Return Response
        # -----------------------------------------

        return {
            "status": status,
            "message": assistant_message,
            "data": response_data
        }