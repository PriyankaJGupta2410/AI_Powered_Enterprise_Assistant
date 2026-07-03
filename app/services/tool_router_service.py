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

        # -----------------------------
        # 3. CALL LLM
        # -----------------------------
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

            assistant_msg = (
                f"Ticket created successfully. "
                f"Ticket ID: {ticket['ticket_id']}, Issue: {issue}"
            )

            # -----------------------------
            # SAVE ASSISTANT MESSAGE
            # -----------------------------
            MemoryService.save_message("assistant", assistant_msg)

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
            MemoryService.save_message("user", question)
            MemoryService.save_message("assistant", answer)

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