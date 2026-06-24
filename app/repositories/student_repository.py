from sqlalchemy.orm import Session
from app.models.student_model import Student


def create_student(db: Session, student):

    new_student = Student(
        name=student.name,
        age=student.age,
        email=student.email,
        course=student.course
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return new_student
def get_students(db):
    return db.query(Student).all()
def get_student_by_id(db, student_id):
    return (
        db.query(Student)
        .filter(
            Student.id == student_id
        )
        .first()
    )
def update_student(
    db,
    student_id,
    data
):

    student = (
        db.query(Student)
        .filter(
            Student.id == student_id
        )
        .first()
    )

    if student:

        student.name = data.name
        student.age = data.age
        student.email = data.email
        student.course = data.course

        db.commit()
        db.refresh(student)

    return student
def delete_student(
    db,
    student_id
):

    student = (
        db.query(Student)
        .filter(
            Student.id == student_id
        )
        .first()
    )

    if student:

        db.delete(student)
        db.commit()

    return student
def search_students(
    db,
    search="",
    page=1,
    limit=5
):

    query = db.query(Student)

    if search:

        query = (
            query.filter(
                Student.name
                .ilike(
                    f"%{search}%"
                )
            )
        )

    start = (
        page - 1
    ) * limit

    return (
        query
        .offset(start)
        .limit(limit)
        .all()
    )