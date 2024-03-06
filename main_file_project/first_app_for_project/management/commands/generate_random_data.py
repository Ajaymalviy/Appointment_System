from django.core.management.base import BaseCommand
from faker import Faker
from first_app_for_project.models import User, Employee, Company, Schedule, Appointment
import random



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

class Command(BaseCommand):
    help = 'Generate random data for MongoDB collections'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate Users
        for _ in range(10):
            user = User.objects.create(
                username=fake.user_name(),
                password=fake.password(),
                email=fake.email(),
                phone=fake.phone_number()
            )

        # Generate Employees
        for _ in range(10):
            employee = Employee.objects.create(
                employee_email=fake.email(),
                employee_role=fake.job(),
                employee_name=fake.name(),
                experience=random.randint(1, 10),
                skills=random.sample(skills, random.randint(1, len(skills)))
            )

        # Generate Companies
        for _ in range(5):
            company = Company.objects.create(
                company_name=random.choice(companies),
                employee_email=fake.email(),
                email=fake.email(),
                location=fake.city(),
                company_schedule=fake.sentence()
            )

        # Generate Schedules
        for _ in range(10):
            schedule = Schedule.objects.create(
                schedule_id=fake.uuid4(),
                date=fake.date(),
                number_of_slots=random.randint(1, 10),
                available=fake.boolean(),
                employee_email=fake.email()
            )

        # Generate Appointments
        for _ in range(10):
            appointment = Appointment.objects.create(
                appointment_id=fake.uuid4(),
                date=fake.date(),
                time=fake.time(),
                description=fake.sentence(),
                status=random.choice(['Confirmed', 'Pending', 'Cancelled']),
                employee_email=fake.email(),
                user_email=fake.email(),
                schedule_id=fake.uuid4()
            )

        self.stdout.write(self.style.SUCCESS('Data generated successfully'))
