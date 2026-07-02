from collections import defaultdict


class ConversationMemory:
    """
    In-memory conversation store.

    Structure:

    {
        "session1": [
            {
                "role": "user",
                "content": "Create ticket"
            },
            {
                "role": "assistant",
                "content": "Ticket created"
            }
        ]
    }
    """

    _memory = defaultdict(list)

    @classmethod
    def add_message(cls, session_id, role, content):

        cls._memory[session_id].append(
            {
                "role": role,
                "content": content
            }
        )

    @classmethod
    def get_history(cls, session_id):

        return cls._memory.get(session_id, [])

    @classmethod
    def clear_history(cls, session_id):

        cls._memory.pop(session_id, None)

    @classmethod
    def get_all_memory(cls):

        return cls._memory