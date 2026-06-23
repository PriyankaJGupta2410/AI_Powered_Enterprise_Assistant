def error_response(message: str):

    return {
        "status": False,
        "message": message,
        "data": None
    }