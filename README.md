# Appointment System
#project overview
The Appointment Management System is a web application designed to streamline the management or scheduling of interview metting b/w user and company employees. This system facilitates the efficient handling of appointment requests, schedules, and  information through a user-friendly interface. The project incorporates essential features such as CRUD operations, pagination, and robust authentication mechanisms to ensure secure access.


## Table of Contents

1. [Introduction](#introduction)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Database Initialization and Configuration](#database-initialization-and-configuration)
7. [Running the Application](#running-the-application)
8. [Functionalities](#functionalities)

## Introduction

The AMS Application simplifies employee data management by offering an intuitive web-based interface. Users can effortlessly perform CRUD operations on the following key components:

- User Profile
- User request
- Company Employees list
- Company Schedule 
- Employee Schedule


This application ensures that Appointment-related data can be easily viewed, added, edited, or deleted, with an added layer of security through user authentication.

## Technology Stack

### Frontend

- HTML
- CSS
- Bootstrap

### Backend

- Python
- Django (Web Framework)
- MongoDb (Database)
- Celery (Task scheduling)
- Apache celery (Task priotise)

## Project Structure

The project directory includes the following files and directories:

  ```text
  Appointment_System/
  │
  ├── appointment_core/               # Core project configuration
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  │   ├── wsgi.py
  │   └── generate.py                 # Script to generate random DB entries
  │
  ├── appointments/                  # Main Django app
  │   ├── models.py
  │   ├── views.py
  │   ├── urls.py
  │   ├── templates/
  │   ├── static/
  │   ├── migrations/
  │   └── management/
  │
  ├── vercel_entry.py
  ├── manage.py
  ├── requirements.txt
  ├── db.sqlite3
  └── README.md  
  ```

## Prerequisites

Before proceeding with the installation and execution of the application, ensure you have the following dependencies installed on your system:

- Python 3.x
- Git
- MySQL server installed and running.
- pip
- MongoDB server (running locally)
- virtualenv
- Git


## Installation

1. Clone the GitHub repository to your desired location:

   ```bash
   git clone git@github.com:Ajaymalviy/Appointment_System.git
   ```

2. Navigate to the "Appointment_System" directory:

   ```bash
   cd Appointment_System
   ```
3. Create a virtual environment
   
   ```bash
   python3 -m venv venv
   ```

4. Activate this 

    ```bash
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

5. Install the required packages and libraries by executing:

   ```bash
   pip install -r requirements.txt
   ```
  
## Database Initialization and Configuration
Before running the application, it's essential to initialize the database and configure the connection. Follow these steps:

  1. Start your MongoDB server.
  2. Open the MongoDB shell and create a new database:
     '''sql
     use meetme
     '''
  3. Update the DATABASES section in appointment_core/settings.py:
     ```yaml
       DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'meetme',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'mongodb://localhost:27017/',
            }
        }
      }
     ```
  4. Now, You have to make db connection with this two commands:
     ```bash
       python3 manage.py makemigrations appointments
       #for creating all collections in your db using ORM.
       python3 manage.py migrate
       #for migrating all the collection
     ```
  5. Populate the database with random data:
     ```bash
      python3 appointment_core/generate.py xx
      #change xx with random number
     ```
## Running the Application
   ```bash
    python3 manage.py runserver
    #now visit  http://127.0.0.0/8000
  ```


##Functionalities
1. User Management
  -Signup/Login using JWT
  -Secure user profile management

2. Appointment Handling
  -Create, update, delete appointments
  -Track and view upcoming meetings

3. Employee Features
  -Manage own schedule and availability
  -Respond to meeting requests

4. Admin Features
  -Manage companies and employees
  -View all appointment activity

5.Contact System
  -Contact form for user feedback
  -Admin access to contact details

   



