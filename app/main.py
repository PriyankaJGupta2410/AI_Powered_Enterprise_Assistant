from fastapi import FastAPI
from app.routes.ask_route import router

app = FastAPI(
    title="AI Enterprise Assistant",
    version="1.0.0"
)

app.include_router(router)