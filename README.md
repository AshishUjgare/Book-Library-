Book Library Project
A Django-based web application for book registration and management, using MySQL as the backend database.

Project Overview
This project allows users to add and manage books using a clean web interface. The backend is built with Django, and the frontend uses custom HTML/CSS stored in separate branches for better organization.

Branching Strategy
main: Default branch containing core settings and project-level files.

app: Contains Django app-level files (e.g., models.py, admin.py, views.py).

static: Contains static assets like CSS files.

templates: Contains HTML template files.

This separation helps in organizing work but keep branches synchronized by merging changes regularly.

File Structure
text
book-library/
├── manage.py
├── requirements.txt
├── booklibrary/                  # Project-level folder
│   ├── __init__.py
│   ├── settings.py              # Project configurations
│   ├── urls.py                  # Root URL configurations
│   ├── wsgi.py
│   └── asgi.py
├── app/                        # Django app folder (in 'app' branch)
│   ├── __init__.py
│   ├── admin.py                # Admin interface config
│   ├── apps.py
│   ├── models.py               # Database models for books
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── templates/              # (in 'templates' branch)
│   │   └── app/
│   │       └── book_form.html # HTML form template for book registration
│   └── static/                 # (in 'static' branch)
│       └── app/
│           └── style.css       # CSS file for styling forms
└── README.md
Setup Instructions
Clone the repository and checkout the required branches:

bash
git clone https://github.com/yourusername/Book-Library.git
cd Book-Library
git checkout main
git checkout app
git checkout static
git checkout templates
Create and activate a Python virtual environment and install dependencies:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Configure your MySQL database in booklibrary/settings.py.

Run migrations and start the development server:

bash
python manage.py migrate
python manage.py runserver
Access the app at http://127.0.0.1:8000.

Usage
Add new books via the web form.

Use the clear fields button to reset the form after submission.

Notes on Branching
Keep branches regularly merged to avoid conflicts.

Normally, static and template files reside in the app folder, but they are separated here for organizational clarity.

Merge static and templates branches into app or main before deployment.

