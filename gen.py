from faker import Faker
from pymongo import MongoClient
import random
import uuid
for unique id

# List of companies and IT developer skills
companies = ["Apple Inc", "IBM", "Microsoft Corporation", "Amazon.com Inc", "Oracle Corporation", "Alphabet Inc. (Google)"]
skills = [
    "Python Programming",
    "Java Development",
    "JavaScript Development",
    "HTML/CSS",
    "Database Management (SQL)",
    "Web Development Frameworks (e.g., Django, Flask, Spring)",
    "Version Control (e.g., Git, SVN)",
    "Software Testing",
    "DevOps Tools (e.g., Docker, Kubernetes)",
    "Cloud Computing (e.g., AWS, Azure, Google Cloud)",
    "Mobile App Development (iOS/Android)",
    "Frontend Development (e.g., React, Angular, Vue.js)",
    "Backend Development",
    "RESTful APIs",
    "Cybersecurity",
    "Machine Learning/Artificial Intelligence",
    "Data Analysis/Visualization",
    "Agile Methodologies (e.g., Scrum, Kanban)",
    "Linux/Unix Administration",
    "Network Administration"
]

# Establish a connection to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')  # Replace with your connection string
db = client['meetme']  # Replace with your database name

# Generate fake data
fake = Faker()

# Generate Users
users_collection = db['first_app_for_project_user']  # Specify the collection for users
for _ in range(10):
    user_data = {
        # Generate a unique id
        'username': fake.user_name(),
        'password': fake.password(),
        'email': fake.email(),
        'phone': fake.phone_number()
    }
    users_collection.insert_one(user_data)
# Generate Companies
companies_collection = db['first_app_for_project_company']  # Specify the collection for companies
import uuid

for _ in range(10):
    user_data = {
       # Generate a unique id
        'username': fake.user_name(),
        'password': fake.password(),
        'email': fake.email(),
        'phone': fake.phone_number()
    }
    users_collection.insert_one(user_data)

# Generate Employees
employees_collection = db['first_app_for_project_employee']  # Specify the collection for employees
for _ in range(50):
    employee_data = {
        'employee_email': fake.email(),
        'employee_role': fake.job(),
        'employee_name': fake.name(),
        'experience': random.randint(1, 10),
        'skills': random.sample(skills, random.randint(1, len(skills))),
        'company_name': random.choice(companies)
    }
    employees_collection.insert_one(employee_data)

# Generate Schedules
schedules_collection = db['first_app_for_project_schedule']  # Specify the collection for schedules
for _ in range(20):
    schedule_data = {
        'schedule_id': fake.uuid4(),
        'date': fake.date(),
        'number_of_slots': random.randint(1, 10),
        'available': fake.boolean(),
        'employee_email': fake.email()
    }
    schedules_collection.insert_one(schedule_data)

# Generate Appointments
appointments_collection = db['first_app_for_project_appointment']  # Specify the collection for appointments
for _ in range(20):
    appointment_data = {
        'appointment_id': fake.uuid4(),
        'date': fake.date(),
        'time': fake.time(),
        'description': fake.sentence(),
        'status': random.choice(['Confirmed', 'Pending', 'Cancelled']),
        'employee_email': fake.email(),
        'user_email': fake.email(),
        'schedule_id': fake.uuid4()
    }
    appointments_collection.insert_one(appointment_data)

print('Data generated successfully')
