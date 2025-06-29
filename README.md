# Collaborative Task Manager API (FastAPI)

## Objective
A RESTful backend API using FastAPI and MongoDB for a collaborative task manager. Supports user registration, login, and task CRUD operations with JWT authentication.

---

## Tech Stack
- **Framework:** FastAPI
- **Database:** MongoDB (motor)
- **Authentication:** JWT (python-jose)
- **Password Hashing:** passlib (bcrypt)
- **Input Validation:** Pydantic
- **Security:**
  - JWT-secured routes
  - Password hashing with bcrypt
  - Input validation with Pydantic
  - NoSQL injection protection (input sanitization)
- **Config:** Environment variables via `.env` file

---

## Features & Requirements Coverage
- [x] **User Registration** (`POST /api/auth/register`)
- [x] **User Login** (`POST /api/auth/login`)
- [x] **JWT Authentication** (all task routes are protected)
- [x] **Task CRUD**
  - [x] Create (`POST /api/tasks`)
  - [x] List (`GET /api/tasks`)
  - [x] Update (`PUT /api/tasks/{id}`)
  - [x] Delete (`DELETE /api/tasks/{id}`)
- [x] **Password Hashing** (bcrypt)
- [x] **Input Validation** (Pydantic)
- [x] **NoSQL Injection Protection** (input sanitization on all user input)
- [x] **Environment Variables** loaded from `.env` file

---

## Setup & Run
1. **Clone the repo**
   ```bash
   git clone https://github.com/anujdarji2001/MCS.git
   ```
3. **Create a virtual environment and activate it**
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Create a `.env` file** in the project root (see below for example)
6. **Start MongoDB server**
7. **Run the app:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## .env Example
```
MONGO_URI=mongodb://localhost:27017
DB_NAME=taskdb
JWT_SECRET=supersecret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## API Documentation
- Visit `/docs` for Swagger UI
- Visit `/redoc` for ReDoc

---

## Endpoints
### Auth
- `POST /api/auth/register` — Register user (email, password)
- `POST /api/auth/login` — Login, returns JWT (OAuth2 password flow, use email as username)

### Tasks (JWT required)
- `POST /api/tasks/` — Create task (title, description, status)
- `GET /api/tasks/` — List my tasks
- `PUT /api/tasks/{id}` — Update my task
- `DELETE /api/tasks/{id}` — Delete my task

---

## Security Notes
- All task routes are JWT-protected (must be authenticated)
- Passwords are hashed with bcrypt before storage
- All input is validated with Pydantic schemas
- All user input is sanitized to prevent NoSQL injection (rejects keys with `$` or `.`)
- Environment variables are loaded from `.env` for secrets/config
