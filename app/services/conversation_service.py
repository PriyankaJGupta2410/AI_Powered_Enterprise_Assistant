from app.memory.conversation_memory import ConversationMemory


class ConversationService:

    @staticmethod
    def save_user_message(session_id, message):

        ConversationMemory.add_message(
            session_id=session_id,
            role="user",
            content=message
        )

    @staticmethod
    def save_assistant_message(session_id, message):

        ConversationMemory.add_message(
            session_id=session_id,
            role="assistant",
            content=message
        )

    @staticmethod
    def get_history(session_id):

        return ConversationMemory.get_history(session_id)

    @staticmethod
    def clear_history(session_id):

        ConversationMemory.clear_history(session_id)

    @staticmethod
    def get_prompt_history(session_id, limit=6):

        history = ConversationMemory.get_history(session_id)

        history = history[-limit:]

        prompt = ""

        for item in history:

            prompt += f"{item['role']}: {item['content']}\n"

        return prompt