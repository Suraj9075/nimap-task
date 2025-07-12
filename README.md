

# Client and Project Management API

This Django REST Framework project allows you to:

- Register and manage Clients.
- Assign multiple Projects under a Client.
- Assign multiple existing Users to a Project.
- View all Projects assigned to a specific User.
- Automatically capture `created_by`, `created_at`, and `updated_at` fields.
- Works without authentication (assigns default user if none is provided).

## Features

- CRUD operations on Clients.
- Create Projects under a Client and assign registered Users.
- Filter Projects assigned to a specific (simulated) logged-in User.
- JSON-based APIs for easy frontend integration or testing via Postman.

## Tech Stack

- Django
- Django REST Framework
- SQLite (default, switchable to PostgreSQL/MySQL)
- Python 3.11+

## Endpoints Overview

- `GET http://127.0.0.1:8000/api/clients/` — List all clients.
- `POST http://127.0.0.1:8000/api/clients/` — Create a new client.
- `GET http://127.0.0.1:8000/api/clients/<id>/` — Retrieve client info with projects.
- `PUT/PATCH http://127.0.0.1:8000/api/clients/<id>/` — Update client info.
- `DELETE http://127.0.0.1:8000/api/clients/<id>/` — Delete a client.
- `POST http://127.0.0.1:8000/api/clients/<id>/projects/` — Create a project under a client with user assignment.
- `GET http://127.0.0.1:8000/api/projects/` — List all projects assigned to the (simulated) logged-in user.

## How to Run

```bash
git clone <your-repo-url>
cd project-folder
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
