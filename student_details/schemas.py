# student_details/schemas.py
#
# Pydantic models (schemas) for the student_details module, now with CRUD support.

from pydantic import BaseModel, Field
from typing import List, Optional

class SubjectMark(BaseModel):
    subject_name: str
    marks: int = Field(..., ge=0, le=100)

class StudentBase(BaseModel):
    """Base model with common student fields."""
    name: str
    enrollment_number: str
    branch: str
    year: int
    subjects: List[SubjectMark]

class StudentCreate(StudentBase):
    """Schema for creating a new student."""
    pass

class StudentUpdate(BaseModel):
    """Schema for updating a student. All fields are optional."""
    name: Optional[str] = None
    branch: Optional[str] = None
    year: Optional[int] = None
    subjects: Optional[List[SubjectMark]] = None

class Student(StudentBase):
    """Schema for returning a student from the API."""
    pass

class StudentInDB(StudentBase):
    """Schema to represent a student as stored in the database."""
    id: str = Field(alias="_id")
