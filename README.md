Online Resume Builder

A web application that allows users to create, edit, preview, and download resumes using multiple templates. Users can register, log in, and manage their resumes, with an admin panel for management.

Features

User Authentication: Secure JWT-based authentication (Register, Login, Logout).

Resume Templates: Multiple professionally designed resume templates.

Real-time Preview: Users can see changes in real-time.

Download & Share: Generate resumes as PDFs and share links.

Database Integration: PostgreSQL/MySQL for storing user data.

Admin Panel: Manage users and resumes efficiently.


Tech Stack

Backend: Django (or Flask) + Django Rest Framework (DRF)

Frontend: HTML, CSS, JavaScript, Bootstrap (or React)

Database: PostgreSQL/MySQL

Authentication: JWT-based authentication (using djangorestframework-simplejwt or Flask-JWT-Extended)

PDF Generation: WeasyPrint / xhtml2pdf

Deployment: Docker, Gunicorn, Nginx
