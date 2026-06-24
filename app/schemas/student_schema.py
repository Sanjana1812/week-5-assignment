from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)

    age: int = Field(..., gt=0)

    email: EmailStr

    course: Optional[str] = None


class StudentUpdate(BaseModel):
    name: Optional[str] = None

    age: Optional[int] = None

    email: Optional[EmailStr] = None

    course: Optional[str] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str
    course: Optional[str]

    class Config:
        from_attributes = True