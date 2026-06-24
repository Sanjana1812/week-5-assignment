from fastapi import FastAPI

from app.database.connection import engine
from app.models.student_model import Base
from app.routers.student_router import router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management System"
)

app.include_router(router)


@app.get("/")
async def home():
    return {
        "message": "Student Management System Running"
    }
from fastapi import FastAPI
from app.routers.student_router import router
from app.middleware.request_logger import request_logger
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

app.add_middleware(
    BaseHTTPMiddleware,
    dispatch=request_logger
)

app.include_router(router)