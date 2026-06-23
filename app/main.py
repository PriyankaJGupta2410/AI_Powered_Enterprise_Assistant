from fastapi import FastAPI
from app.routes.ask_route import router
from app.exceptions.global_exception_handler import (
    global_exception_handler
)

app = FastAPI(
    title="AI Enterprise Assistant",
    version="1.0.0"
)

app.include_router(router)

app.add_exception_handler(
    Exception,
    global_exception_handler
)