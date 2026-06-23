def validate_question(question: str):

    if not question:
        return False, "Question cannot be empty"

    if not question.strip():
        return False, "Question cannot be empty"

    return True, ""