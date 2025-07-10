# main.py
#
# Main application file. Initializes the FastAPI app and includes the routers
# from the authentication and student_details modules.

from fastapi import FastAPI
from database import populate_initial_student_data
from authentication.routes import router as auth_router
from student_details.routes import router as student_router

app = FastAPI(
    title="Student Information API",
    description="A modular API for managing users and student marks.",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    """Function to run on application startup."""
    print("🚀 Application starting up...")
    populate_initial_student_data()

# Include the routers from the modules
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(student_router, prefix="/students", tags=["Student Details"])


@app.get("/", tags=["Root"])
async def read_root():
    """A welcome message for the root endpoint."""
    return {"message": "Welcome to the Student Information API!"}

