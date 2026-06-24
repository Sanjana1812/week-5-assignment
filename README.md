# Student Management System

## Week 5 – Backend Engineering Assignment

A backend application developed using **FastAPI** and **PostgreSQL** to manage student records through REST APIs.

This project demonstrates backend engineering concepts including layered architecture, CRUD operations, validation, middleware, dependency injection, search, pagination, background tasks, and logging.

---

# Project Objective

Build a scalable Student Management System while applying modern backend engineering principles and API development practices.

---

# Features

✅ Create Student
✅ Get All Students
✅ Get Student By ID
✅ Update Student
✅ Delete Student
✅ Search Students
✅ Pagination
✅ Pydantic Validation
✅ Middleware Logging
✅ Dependency Injection
✅ Background Tasks
✅ Database Connection Check
✅ Swagger Documentation

---

# Project Structure

```plaintext
SMS/
│
├── app
│   ├── database
│   ├── middleware
│   ├── models
│   ├── repositories
│   ├── routers
│   ├── schemas
│   ├── services
│   └── utils
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Technology Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn
* Swagger UI
* GitHub

---

# API Endpoints

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| POST   | /students          | Create Student    |
| GET    | /students          | Get All Students  |
| GET    | /students/{id}     | Get Student       |
| PUT    | /students/{id}     | Update Student    |
| DELETE | /students/{id}     | Delete Student    |
| GET    | /students/search   | Search Students   |
| GET    | /students/db-check | Database Check    |
| POST   | /students/notify   | Send Notification |

---

# Installation

Clone repository

```bash
git clone https://github.com/Sanjana1812/week-5-assignment.git
```

Move into project

```bash
cd week-5-assignment
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

Swagger UI:

```plaintext
http://127.0.0.1:8000/docs
```

---

# Architecture

Frontend
↓
FastAPI
↓
Service Layer
↓
Repository Layer
↓
PostgreSQL

---

# Testing

Verified:

* CRUD Operations
* Validation
* Middleware
* Search
* Pagination
* Logging

---

# Author

Padma Sanjana

Week 5 Assignment Submission
