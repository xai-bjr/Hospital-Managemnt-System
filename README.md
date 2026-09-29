Hospital Information Management System (HIMS)

A web-based Hospital Information Management System built with Python and Django for managing patients, doctors, appointments, hospital beds, departments, wards, invoices, and hospital operations through a centralized dashboard.

Features

Patient registration and management

Patient directory

Add, edit, and delete patient records

Doctor management

Appointment management

Hospital bed management

Ward and department management

Bed occupancy monitoring

Available bed tracking

Invoice and revenue tracking

Hospital administration dashboard

Recent patient admissions

Resource allocation visualization

Django Admin interface

Responsive web interface

Technologies Used

Python

Django

Daphne / ASGI

HTML5

CSS3

Bootstrap

JavaScript

Chart.js

Font Awesome

SQLite for local development

Installation

Follow the steps below to install and run the project on your computer.

1. Requirements

Before installing the project, make sure you have:

Python 3.12+ recommended

Git

pip

A modern web browser

Check your Python installation:

python --version


Check Git:

git --version


Windows users: If python does not work, try py --version.

2. Clone the Repository

Open a terminal or PowerShell and run:

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git


Then enter the project directory:

cd YOUR-REPOSITORY


Replace YOUR-USERNAME/YOUR-REPOSITORY with the actual GitHub repository address.

3. Create a Virtual Environment

Creating a virtual environment keeps the project's Python packages separate from the rest of your computer.

Windows
python -m venv venv


Activate it:

.\venv\Scripts\Activate.ps1


If PowerShell blocks the activation script, you can use:

.\venv\Scripts\activate

Linux / macOS
python3 -m venv venv


Activate it:

source venv/bin/activate


After activation, you should see something similar to:

(venv)


at the beginning of your terminal prompt.

4. Install Dependencies

Make sure your virtual environment is activated, then run:

pip install -r requirements.txt


This installs the Python packages required by the project.

5. Configure Environment Variables

If the project contains an .env.example file, create your local .env file from it.

Windows PowerShell
Copy-Item .env.example .env

Linux / macOS
cp .env.example .env


Open .env and configure the required settings.

Example:

DEBUG=True
SECRET_KEY=your-development-secret-key


Never upload your real .env file or production secrets to GitHub.

6. Create the Database

Run Django's database migrations:

python manage.py migrate


This creates the required database tables.

7. Create an Administrator Account

Create a Django administrator account:

python manage.py createsuperuser


Django will ask you for:

Username:
Email address:
Password:
Password (again):


Choose your own username and password.

This account will allow you to access the Django administration panel.

8. Start the Development Server

Run:

python manage.py runserver


You should see something similar to:

Starting development server at http://127.0.0.1:8000/


Open your browser and visit:

Application:

http://127.0.0.1:8000/


Django Admin:

http://127.0.0.1:8000/admin/


Log in to /admin/ using the superuser account you created earlier.

9. Add Hospital Data

After logging into the Django Admin panel, you can add and manage data such as:

Patients

Doctors

Departments

Wards

Beds

Appointments

Invoices

Once data has been added, the dashboard can display the corresponding hospital statistics.

Running the Project Again

After closing your terminal or restarting your computer, you do not need to reinstall everything.

Navigate to the project:

cd YOUR-REPOSITORY


Activate the virtual environment.

Windows
.\venv\Scripts\Activate.ps1

Linux / macOS
source venv/bin/activate


Then start Django:

python manage.py runserver

Useful Django Commands
Check the project
python manage.py check

Create database migrations
python manage.py makemigrations

Apply migrations
python manage.py migrate

Create an administrator
python manage.py createsuperuser

Run tests
python manage.py test

Start the development server
python manage.py runserver

Project Structure
him-lan/
│
├── hims_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── patients/
│   ├── migrations/
│   ├── templates/
│   │   └── patients/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── base.html
│
├── static/
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

Troubleshooting
python is not recognized

On Windows, try:

py --version


If that works, use:

py -m venv venv
py manage.py migrate
py manage.py runserver


You may also need to install Python and enable Add Python to PATH during installation.

pip is not recognized

Try:

python -m pip --version


Then install packages using:

python -m pip install -r requirements.txt

No module named django

Make sure the virtual environment is activated:

.\venv\Scripts\Activate.ps1


Then:

pip install -r requirements.txt

Database errors

Run:

python manage.py makemigrations
python manage.py migrate


Then start the server again:

python manage.py runserver

Security Notice

This project is intended for development and educational purposes unless it has been properly secured and validated for production healthcare use.

Do not use real patient medical information in a public development environment.

For production deployment, additional security measures are required, including:

HTTPS

Secure authentication

Role-based access control

Secure environment variables

Database security

Backup and recovery procedures

Audit logging

Access controls

Privacy and regulatory compliance

Production server configuration

Project Status

Development / Educational Project

The system is actively designed for expansion. Additional healthcare management functionality can be added in future versions.

Future Improvements

Patient search and filtering

Advanced appointment scheduling

Doctor scheduling

Patient discharge workflow

PDF reports

Medical records

Pharmacy management

Laboratory management

Billing improvements

Role-based permissions

REST API

Automated testing

Production deployment configuration

Contributing

Contributions are welcome.

Fork the repository.

Create a new branch:

git checkout -b feature/your-feature


Make your changes.

Test your changes.

Commit your changes:

git commit -m "Add your feature"


Push your branch:

git push origin feature/your-feature


Open a Pull Request.

License

This project is currently intended for educational and development purposes.

A formal open-source license can be added to the repository according to the project's licensing requirements.

Disclaimer

This software is a development project and is not a substitute for professional healthcare information systems, medical advice, or clinical decision-making.

Any deployment in a real healthcare environment should undergo appropriate security, privacy, compliance, clinical, and technical review.
