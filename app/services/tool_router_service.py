from app.constants.constants import SYSTEM_PROMPT
from app.services.llm_service import LLMService
from app.tools.create_ticket_tool import create_ticket_tool
from app.utils.json_parser import JsonParser
from app.utils.logger import logger


class ToolRouterService:

    @staticmethod
    def process_question(question):

        prompt = f"""
            {SYSTEM_PROMPT}

            User Question:
            {question}
        """

        response = LLMService.generate(prompt)

        logger.info(response)

        data = JsonParser.parse_response(response)

        if data is None:
            return {
                "status": False,
                "message": "Unable to understand request.",
                "data": None
            }

        intent = data.get("intent", "").lower().strip()

        # -----------------------------
        # CREATE TICKET FLOW
        # -----------------------------
        if intent == "create_ticket":

            issue = data.get("issue", "")

            # ✅ FIX: strong validation (IMPORTANT)
            invalid_issues = ["", "...", "none", "null", "unknown", "n/a"]

            if issue is None or issue.strip().lower() in invalid_issues:
                return {
                    "status": False,
                    "message": "Please provide valid issue details.",
                    "data": None
                }

            ticket = create_ticket_tool(issue)

            return {
                "status": True,
                "message": "Ticket created successfully.",
                "data": ticket
            }

        # -----------------------------
        # GENERAL QUERY FLOW
        # -----------------------------
        elif intent == "general_query":

            answer = data.get("answer", "")

            if not answer:
                return {
                    "status": False,
                    "message": "Unable to generate response.",
                    "data": None
                }

            return {
                "status": True,
                "message": answer,
                "data": None
            }

        # -----------------------------
        # FALLBACK
        # -----------------------------
        return {
            "status": False,
            "message": "Unsupported intent.",
            "data": None
        }