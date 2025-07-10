# Student Information API

A modular and secure FastAPI application for managing student information and marks, complete with user authentication.

## 🌟 Features

* **FastAPI Backend**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
* **MongoDB Integration**: Uses MongoDB as the database to store user and student data, connected via `pymongo`.
* **Modular Design**: The project is organized into distinct modules for `authentication` and `student_details`, making it easy to maintain and scale.
* **User Authentication**: Secure user registration and login using JWT (JSON Web Tokens). Passwords are hashed for security.
* **CRUD Operations**: Full Create, Read, Update, and Delete functionality for student records.
* **Data Validation**: Pydantic models are used for robust data validation and serialization, ensuring data integrity.
* **Configuration Management**: Centralized configuration management using a `.env` file to handle sensitive keys and settings.
* **Automatic Documentation**: FastAPI provides automatic interactive API documentation (via Swagger UI and ReDoc).

---

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.7+
* MongoDB instance (local or cloud-based)
* `pip` for installing packages

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd student-information-api
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    *(Note: You'll need to create a `requirements.txt` file)*
    ```
    pip install fastapi "uvicorn[standard]" pymongo pydantic pydantic-settings python-jose "passlib[bcrypt]"
    ```
    Create a `requirements.txt` file and add the dependencies above, then run:
    ```sh
    pip install -r requirements.txt
    ```

---

## ⚙️ Configuration

1.  Create a `.env` file in the root directory of the project.
2.  Add the following configuration variables to your `.env` file:

    ```env
    # JWT Settings
    SECRET_KEY=your_very_secret_key
    ALGORITHM=HS256
    ACCESS_TOKENS_EXPIRE_MINUTES=30

    # Database Settings
    MONGO_URI=mongodb://localhost:27017/
    ```

---

## ▶️ Running the Application

1.  **Start the FastAPI server:**
    ```sh
    uvicorn main:app --reload
    ```
    The `--reload` flag makes the server restart after code changes.

2.  **Access the API:**
    The application will be running at `http://127.0.0.1:8000`.

3.  **Automatic API Documentation:**
    You can access the interactive API documentation at:
    * **Swagger UI**: `http://127.0.0.1:8000/docs`
    * **ReDoc**: `http://127.0.0.1:8000/redoc`

---

## Endpoints API

### Authentication (`/auth`)

* **`POST /auth/register`**: Register a new user.
* **`POST /auth/token`**: Authenticate a user and receive a JWT access token.
* **`GET /auth/me`**: Get the details of the currently authenticated user.

### Student Details (`/students`)

*(These endpoints require authentication)*

* **`POST /students/`**: Create a new student record.
* **`GET /students/{enrollment_number}`**: Retrieve a student's details by their enrollment number.
* **`PUT /students/{enrollment_number}`**: Update an existing student's record.
* **`DELETE /students/{enrollment_number}`**: Delete a student's record.

---

## 🛠️ Technologies Used

* **FastAPI**: Web framework
* **Pydantic**: Data validation
* **MongoDB**: NoSQL Database
* **PyMongo**: Python driver for MongoDB
* **JWT (JSON Web Tokens)**: For authentication
* **Passlib & Bcrypt**: For password hashing
* **Uvicorn**: ASGI server
