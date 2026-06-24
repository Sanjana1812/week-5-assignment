from sqlalchemy.orm import Session
from app.repositories.student_repository import create_student


def add_student(db: Session, student):
    return create_student(db, student)
from app.repositories.student_repository import get_students


def fetch_students(db):
    return get_students(db)
from app.repositories.student_repository import (
    get_student_by_id
)


def fetch_student(db, student_id):

    return get_student_by_id(
        db,
        student_id
    )
from app.repositories.student_repository import (
    update_student
)


def edit_student(
    db,
    student_id,
    data
):

    return update_student(
        db,
        student_id,
        data
    )
from app.repositories.student_repository import (
    delete_student
)


def remove_student(
    db,
    student_id
):

    return delete_student(
        db,
        student_id
    )