from django.core.management.base import BaseCommand
import random
from faker import Faker
from first_app_for_project.models import Company, Employee, Schedule, Appointment, MeetingRequest,User

fake = Faker()


class Command(BaseCommand):
    help = 'Generate random data for models'

    def add_arguments(self, parser):
        parser.add_argument('num_data_sets', type=int, help='Number of data sets to generate')

    def handle(self, *args, **options):
        num_data_sets = options['num_data_sets']
        for _ in range(num_data_sets):
            # Your data generation logic here
            pass
# Generate random data for User model
for _ in range(100):
    user = User(
        username=fake.user_name(),  # Generate a random username using Faker
        password=fake.password(),  # Generate a random password using Faker
        email=fake.email()  # Generate a random email address using Faker
    )
    user.save()


# Generate random data for Company model
for company_name in random.sample(["Apple Inc", "IBM", "Microsoft Corporation", "Amazon.com Inc", "Oracle Corporation", "Alphabet Inc. (Google)", "Techritzy pvt.Ltd", "cognem", "Atlesian","fico"], 10):
    company = Company(
        company_name=company_name,
        company_email=fake.email(),
        location=fake.address(),
        company_schedule=fake.date()
    )
    company.save()

# Generate random data for Employee model
companies = Company.objects.all()
for _ in range(500):
    employee = Employee(
        employee_email=fake.email(),
        employee_role=fake.job(),
        employee_name=fake.name(),
        experience=random.randint(1, 20),
        skills=random.sample([
            "Python Programming", "Java Development", "JavaScript Development", "HTML/CSS",
            "Database Management (SQL)", "Web Development Frameworks (e.g., Django, Flask, Spring)",
            "Version Control (e.g., Git, SVN)", "Software Testing", "DevOps Tools (e.g., Docker, Kubernetes)",
            "Cloud Computing (e.g., AWS, Azure, Google Cloud)", "Mobile App Development (iOS/Android)",
            "Frontend Development (e.g., React, Angular, Vue.js)", "Backend Development", "RESTful APIs",
            "Cybersecurity", "Machine Learning/Artificial Intelligence", "Data Analysis/Visualization",
            "Agile Methodologies (e.g., Scrum, Kanban)", "Linux/Unix Administration", "Network Administration"
        ], random.randint(1, 10)),
        company_name=random.choice(companies),
        password=fake.password()
    )
    employee.save()

# Generate random data for Schedule model
employees = Employee.objects.all()
for _ in range(100):
    schedule = Schedule(
        schedule_id=fake.uuid4(),
        date=fake.date(),
        number_of_slots=random.randint(1, 5),
        available=fake.boolean(),
        employee_email=random.choice(employees)
    )
    schedule.save()

# Generate random data for Appointment model
users = User.objects.all()
for _ in range(100):
    appointment = Appointment(
        appointment_id=fake.uuid4(),
        date=fake.date(),
        time=fake.time(),
        description=fake.text(),
        status=random.choice(["Scheduled", "Cancelled", "Completed"]),
        employee_email=random.choice(employees),
        email=random.choice(users),
        schedule_id=random.choice(Schedule.objects.all())
    )
    appointment.save()

# Generate random data for MeetingRequest model

for _ in range(100):
    meeting_request = MeetingRequest(
        employee_email=random.choice(employees).employee_email,
        requester_email=fake.email(),
        description=fake.text(),
        date=fake.date()
    )
    meeting_request.save()

