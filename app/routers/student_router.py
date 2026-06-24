from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.connection import get_db
from fastapi import BackgroundTasks


from app.schemas.student_schema import (
    StudentCreate,
    StudentResponse
)

from app.services.student_service import add_student


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "/",
    response_model=StudentResponse
)
async def create_student_api(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    return add_student(db, student)
from typing import List
from app.services.student_service import fetch_students

def send_notification(name):
    print(f"Notification sent to {name}")
@router.post("/notify")
async def notify_student(
    name: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        send_notification,
        name
    )

    return {
        "message": "Notification queued"
    }

@router.get(
    "/",
    response_model=List[StudentResponse]
)
async def get_students_api(
    db: Session = Depends(get_db)
):

    return fetch_students(db)
from fastapi import HTTPException
from app.services.student_service import (
    fetch_student
)
@router.get("/db-check")
async def db_check(db=Depends(get_db)):
    return {
        "message": db
    }
@router.get(
    "/{student_id}",
    response_model=StudentResponse
)
async def get_student_api(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = fetch_student(
        db,
        student_id
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student
from app.services.student_service import (
    edit_student
)
@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
async def update_student_api(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    updated = edit_student(
        db,
        student_id,
        student
    )

    if not updated:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated
from app.services.student_service import (
    remove_student
)
@router.delete(
    "/{student_id}"
)
async def delete_student_api(
    student_id: int,
    db: Session = Depends(get_db)
):

    deleted = remove_student(
        db,
        student_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message":
        "Student deleted successfully"
    }
from app.services.student_service import (
    search_student_service
)
@router.get(
    "/search/",
    response_model=list[StudentResponse]
)
async def search_students_api(

    search: str = "",

    page: int = 1,

    limit: int = 5,

    db: Session = Depends(
        get_db
    )

):

    return (
        search_student_service(
            db,
            search,
            page,
            limit
        )
    )
