Book Library Registration Web App
A web-based application for managing book registrations and records, built with Django, MySQL, and custom front-end components.

Features
Add, view, and manage book details securely via an intuitive web interface.

Responsive front-end styled with HTML5, CSS3, and gradient backgrounds.

Form validation, CSRF protection, and a user-friendly reset/clear fields option.

Data stored and managed efficiently using MySQL and Django ORM.



Clone the repository:

bash
git clone https://github.com/yourusername/book-library-app.git
cd book-library-app
Install dependencies:

bash
pip install -r requirements.txt
Configure MySQL database:
Edit settings.py to update your database configuration:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your-db-name>',
        'USER': '<your-db-user>',
        'PASSWORD': '<your-db-password>',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Run migrations:

bash
python manage.py makemigrations
python manage.py migrate
Start the development server:

bash
python manage.py runserver
Access the app:
Open http://127.0.0.1:8000 in your browser.

Usage
Visit the main page to register a new book.

Submit the form to add a book to the database.


Tech Stack
Backend: Django

Frontend: HTML5, CSS3, JavaScript

Database: MySQL

Project Structure
templates/: HTML template files (using Django templating)

static/css/: Custom stylesheet(s) for styling the forms and layout

app/models.py: Django models for book records

app/views.py: Page logic for displaying and processing the registration form

Contributing
Open to suggestions and improvements via pull requests.

License
MIT

