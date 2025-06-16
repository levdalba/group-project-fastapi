# Group Project: FastAPI Setup

## Description

This project is a boilerplate setup for a FastAPI backend using modern Python tooling. It leverages FastAPI for API development, Pydantic for data validation, pytest for testing, and ruff and mypy for code quality and type checking.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/group-project-fastapi.git
    cd group-project-fastapi
    ```
2. **Set Up a Python Virtual Environment**
    ```bash
    uv venv
    source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
    ```
3. **Install Dependencies**
    ```bash
    uv sync --group dev
    ```

## Running the App

1. **Start the FastAPI Server**

    ```bash
    uvicorn app.main:app --reload
    ```

    The server will be available at `http://127.0.0.1:8000`. Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

2. **Run Tests**

    ```bash
    pytest
    ```

## Code Quality

-   **Linting with Ruff**
    ```bash
    ruff check .
    ```
-   **Type Checking with Mypy**
    ```bash
    mypy .
    ```
