# student_details/routes.py
#
# API endpoints (routes) for the student_details module with full CRUD functionality.

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.results import DeleteResult

from database import student_collection
from . import schemas
from authentication.utils import get_current_active_user
from authentication.schemas import User # Import User schema for dependency

router = APIRouter()

@router.post("/", response_model=schemas.Student, status_code=status.HTTP_201_CREATED)
async def create_student(
    student: schemas.StudentCreate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    Create a new student record in the database.
    - `enrollment_number` must be unique.
    """
    # Check if student with the same enrollment number already exists
    if student_collection.find_one({"enrollment_number": student.enrollment_number}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Student with enrollment number '{student.enrollment_number}' already exists."
        )
    
    student_doc = student.model_dump()
    student_collection.insert_one(student_doc)
    return student_doc


@router.get("/{enrollment_number}", response_model=schemas.Student)
async def get_student_by_id(
    enrollment_number: str,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    Fetches a single student's details by their enrollment number.
    """
    student = student_collection.find_one({"enrollment_number": enrollment_number})
    if student:
        return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")


@router.put("/{enrollment_number}", response_model=schemas.Student)
async def update_student(
    enrollment_number: str,
    student_update: schemas.StudentUpdate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    Update a student's record.
    - Only fields provided in the request body will be updated.
    """
    # Create a dictionary with only the fields that are set in the request
    update_data = {k: v for k, v in student_update.model_dump().items() if v is not None}

    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No update data provided."
        )

    result = student_collection.find_one_and_update(
        {"enrollment_number": enrollment_number},
        {"$set": update_data},
        return_document=True # Return the document after the update
    )

    if result:
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")


@router.delete("/{enrollment_number}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(
    enrollment_number: str,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    Delete a student record from the database.
    """
    result: DeleteResult = student_collection.delete_one({"enrollment_number": enrollment_number})

    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    # No content is returned on successful deletion
    return
