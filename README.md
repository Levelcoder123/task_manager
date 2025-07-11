# Django Task Management API

A robust RESTful API for managing user-specific tasks, built with Django and Django REST Framework. This project features JWT authentication and auto-generated API documentation with Swagger for easy interaction and testing.

<img width="2020" height="1304" alt="image" src="https://github.com/user-attachments/assets/72aa2e46-2abb-4705-ace9-f7fdfe2bbad6" />


---

## Features

-   **User Authentication:** Secure user registration and login using JSON Web Tokens (JWT).
-   **Task Management:** Full CRUD (Create, Read, Update, Delete) operations for tasks.
-   **User-Specific Data:** Ensures that users can only access and modify their own tasks.
-   **Live API Documentation:** Interactive API documentation available via Swagger UI (`drf-yasg`).
-   **Admin Ready:** Comes with the standard Django Admin interface for data management.

---

## Technologies Used

-   **Backend:** Python, Django
-   **API:** Django REST Framework
-   **Authentication:** Simple JWT
-   **API Docs:** drf-yasg (Swagger)
-   **Database:** SQLite 3 (Default)

---

## API Endpoints Summary

For full interactive details, run the project and visit `/swagger/`.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/register/` | Creates a new user. |
| `POST` | `/api/login/` | Logs in a user to get an access token. |
| `GET` | `/api/tasks/` | Lists all tasks for the authenticated user. |
| `POST` | `/api/tasks/` | Creates a new task for the authenticated user. |
| `GET`| `/api/tasks/{id}/` | Retrieves a specific task. |
| `PUT/PATCH` | `/api/tasks/{id}/`| Updates a specific task. |
| `DELETE` | `/api/tasks/{id}/` | Deletes a specific task. |

---

## Installation

1. **Clone this repository**
   ```bash
   git clone git@github.com:Levelcoder123/task_manager.git
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

## How to Use the API (Authentication)

1.  After running the server, go to the `/api/login/` endpoint, provide your username and password to get an access token.

2.  In the Swagger UI, click the "Authorize" button:

    <img width="316" height="112" alt="Authorize Button" src="https://github.com/user-attachments/assets/f65d9323-085f-4ec3-935f-64e51162c833" />

3.  Enter your token in the format `Bearer <your_token>`.

<img width="854" height="519" alt="Bearer Token Example" src="https://github.com/user-attachments/assets/2e52f309-de3c-4921-978e-96e41f1d8d9d" />

4.  You can now make authenticated requests to the protected endpoints.
