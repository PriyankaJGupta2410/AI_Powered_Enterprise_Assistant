from app.constants.constants import SYSTEM_PROMPT
from app.services.llm_service import LLMService
from app.services.memory_service import MemoryService
from app.tools.create_ticket_tool import create_ticket_tool
from app.utils.json_parser import JsonParser
from app.utils.logger import logger


class ToolRouterService:

    @staticmethod
    def process_question(question):

        # -----------------------------
        # 1. LOAD CONVERSATION MEMORY
        # -----------------------------
        conversation_context = MemoryService.build_context(question)

        logger.info("=" * 80)
        logger.info("CONVERSATION HISTORY")
        logger.info(conversation_context)
        logger.info("=" * 80)

        # -----------------------------
        # 2. BUILD PROMPT
        # -----------------------------
        prompt = f"""
            {SYSTEM_PROMPT}

            Conversation History
            --------------------
            {conversation_context}

            --------------------

            Current Question
            --------------------
            {question}

            IMPORTANT:
            - Use history only for context
            - Decide intent ONLY from current question
            - Do not repeat previous actions
            """
        
        logger.info("=" * 80)
        logger.info("PROMPT SENT TO LLM")
        logger.info(prompt)
        logger.info("=" * 80)

        # -----------------------------
        # 3. CALL LLM
        # -----------------------------
        response = LLMService.generate(prompt)

        logger.info("=" * 80)
        logger.info("RAW LLM RESPONSE")
        logger.info(response)
        logger.info("=" * 80)

        data = JsonParser.parse_response(response)
        logger.info("=" * 80)
        logger.info("PARSED JSON")
        logger.info(data)
        logger.info("=" * 80)

        if data is None:
            return {
                "status": False,
                "message": "Unable to understand request.",
                "data": None
            }

        intent = data.get("intent", "").lower().strip()

        # =====================================================
        # CREATE TICKET FLOW
        # =====================================================
        if intent == "create_ticket":

            issue = data.get("issue", "")

            invalid_issues = ["", "...", "none", "null", "unknown", "n/a"]

            if issue is None or issue.strip().lower() in invalid_issues:
                return {
                    "status": False,
                    "message": "Please provide valid issue details.",
                    "data": None
                }

            # -----------------------------
            # SAVE USER MESSAGE FIRST
            # -----------------------------
            MemoryService.save_message("user", question)

            # -----------------------------
            # CREATE TICKET
            # -----------------------------
            ticket = create_ticket_tool(issue)

            logger.info("=" * 80)
            logger.info("TICKET CREATED")
            logger.info(ticket)
            logger.info("=" * 80)

            assistant_message = f"""
                Ticket created successfully.

                Ticket Details:
                - Ticket ID: {ticket['ticket_id']}
                - Issue: {ticket['issue']}
                - Status: {ticket['status']}
                - Created At: {ticket['created_at']}
            """

            # -----------------------------
            # SAVE ASSISTANT MESSAGE
            # -----------------------------
            MemoryService.save_message("assistant", assistant_message.strip())

            return {
                "status": True,
                "message": "Ticket created successfully.",
                "data": ticket
            }

        # =====================================================
        # GENERAL QUERY FLOW
        # =====================================================
        elif intent == "general_query":

            answer = data.get("answer", "")

            if not answer:
                return {
                    "status": False,
                    "message": "Unable to generate response.",
                    "data": None
                }

            # -----------------------------
            # SAVE MEMORY
            # -----------------------------
            assistant_message = f"""
                Response:
                {answer}
            """
            MemoryService.save_message("user", question)
            MemoryService.save_message("assistant", assistant_message.strip())

            return {
                "status": True,
                "message": answer,
                "data": None
            }

        # =====================================================
        # FALLBACK
        # =====================================================
        return {
            "status": False,
            "message": "Unsupported intent.",
            "data": None
        }