from django.core.management.base import BaseCommand
import random
from faker import Faker
from datetime import datetime, timedelta

from first_app_for_project.models import Company, Employee, User

fake = Faker()


class Command(BaseCommand):
    help = 'Generate random data for models'

    def add_arguments(self, parser):
        parser.add_argument('num_data_sets', type=int, help='Number of data sets to generate')

    def handle(self, *args, **options):
        num_data_sets = options['num_data_sets']

        # Generate random data for User model
        for _ in range(num_data_sets):
            user = User(
                username=fake.user_name().replace(" ", ""),  # Generate a random username using Faker
                password=fake.password(),  # Generate a random password using Faker
                email=fake.email().split('@')[0] + '@gmail.com'  # Generate a random email address using Faker and ensure it ends with @gmail.com
            )
            user.save()

        # Generate random data for Company model
        companies = ["Apple Inc", "IBM", "Microsoft Corporation", "Amazon.com Inc", "Oracle Corporation", "Alphabet Inc. (Google)", "Techritzy pvt.Ltd", "cognem", "Atlesian", "fico"]
        for company_name in random.sample(companies, 10):
            # Calculate start and end date for this year
            start_date = datetime(datetime.now().year, 1, 1)
            end_date = start_date + timedelta(days=365)

            company_schedule = fake.date_time_between_dates(
                datetime_start=start_date,
                datetime_end=end_date
            )  # Generate a random date within the year 2024

            company = Company(
                company_name=company_name,
                company_email=fake.email().split('@')[0] + '@gmail.com',
                location=fake.address(),
                company_schedule=company_schedule
            )
            company.save()

        # Generate random data for Employee model
        employee_roles = [
            "Frontend Developer", "Backend Developer", "Full Stack Developer", "DevOps Engineer", "Systems Engineer",
            "Software Architect", "Software Engineer in Test", "Quality Assurance Engineer", "Security Engineer",
            "Data Engineer", "Machine Learning Engineer", "Embedded Software Engineer", "Game Developer",
            "Mobile Application Developer", "Cloud Engineer", "UI/UX Designer", "Site Reliability Engineer (SRE)",
            "Database Administrator (DBA)", "Automation Engineer", "Technical Support Engineer"
        ]
        companies = Company.objects.all()
        for _ in range(500):
            employee_name = fake.name().replace(" ", "")  # Generate employee name without spaces
            employee_role = random.choice(employee_roles)  # Choose a random employee role from the list
            company = random.choice(companies)  # Choose a random company
            employee = Employee(
                employee_email=fake.email().split('@')[0] + '@gmail.com',
                employee_role=employee_role,
                employee_name=employee_name,
                experience=random.randint(1, 20),
                company_name=company,
                password=fake.password()
            )
            employee.save()

    