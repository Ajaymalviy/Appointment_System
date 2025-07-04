import random
from faker import Faker
from datetime import datetime
from first_app_for_project.models import Company, Employee, Schedule, Appointment, MeetingRequest

fake = Faker()

# Generate random data for Company model
for company_name in random.sample(["Apple Inc", "IBM", "Microsoft Corporation", "Amazon.com Inc", "Oracle Corporation", "Alphabet Inc. (Google)", "Techritzy pvt.Ltd", "cognem", "Atlesian"], 10):
    company = Company(
        company_name=company_name,
        company_email=fake.email(),
        location=fake.address(),
        company_schedule=fake.date_time_between_dates(datetime(2024, 1, 1), datetime(2024, 12, 31))  # Generating dates only from 2024
    )
    company.save()

# Generate random data for Employee model
companies = Company.objects.all()
for _ in range(300):
    employee = Employee(
        employee_email=fake.email().split('@')[0] + '@gmail.com',
        employee_role=random.choice([
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "DevOps Engineer",
            "Systems Engineer",
            "Software Architect",
            "Software Engineer in Test",
            "Quality Assurance Engineer",
            "Security Engineer",
            "Data Engineer",
            "Machine Learning Engineer",
            "Embedded Software Engineer",
            "Game Developer",
            "Mobile Application Developer",
            "Cloud Engineer",
            "UI/UX Designer",
            "Site Reliability Engineer (SRE)",
            "Database Administrator (DBA)",
            "Automation Engineer",
            "Technical Support Engineer"
        ]),
        employee_name = fake.name().replace(" ", ""), 
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
        date=fake.date_time_between_dates(datetime(2024, 1, 1), datetime(2024, 12, 31)),  # Generating dates only from 2024
        number_of_slots=random.randint(1, 5),
        available=fake.boolean(),
        employee_email=random.choice(employees)
    )
    schedule.save()

# Generate random data for Appointment model
for _ in range(100):
    appointment = Appointment(
        appointment_id=fake.uuid4(),
        date=fake.date_time_between_dates(datetime(2024, 1, 1), datetime(2024, 12, 31)),  # Generating dates only from 2024
        time=fake.time(),
        description=fake.text(max_nb_chars=random.randint(50, 70)),
        status=random.choice(["Scheduled", "Cancelled", "Completed"]),
        employee_email=random.choice(employees),
        user_email=fake.email().split('@')[0] + '@gmail.com',
        schedule_id=random.choice(Schedule.objects.all())
    )
    appointment.save()

# Generate random data for MeetingRequest model
for _ in range(100):
    meeting_request = MeetingRequest(
        employee_email=random.choice(employees).employee_email,
        requester_email=fake.email().split('@')[0] + '@gmail.com',
        description=fake.text(max_nb_chars=random.randint(50, 70)),
        date=fake.date_time_between_dates(datetime(2024, 1, 1), datetime(2024, 12, 31))  # Generating dates only from 2024
    )
    meeting_request.save()
