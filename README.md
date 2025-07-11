# Task Manager

A Django-based backend project for task management, featuring RESTful APIs, JWT authentication, and auto-generated API
documentation with Swagger.

## Features

- User registration and authentication (JWT)
- Task CRUD operations via REST API
- Django Admin ready
- API documentation with Swagger (drf_yasg)
- Uses SQLite by default for easy local development (Not implemented yet)

## Installation

1. **Clone this repository**
   ```bash
   git clone <your-repository-url>
   cd task_manager
   ```

2. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Documentation

Visit `http://127.0.0.1:8000/swagger/` after starting the server.

## Authentication

- Login with username and password to get a token.
- Use the token in the `Bearer` header for subsequent requests:
  Example:
  ```
  Bearer <your_token>
  ```