from django.core.management.base import BaseCommand
import random
from faker import Faker
from datetime import datetime, timedelta
from pytz import timezone

from first_app_for_project.models import Company, Employee, User, Schedule, Appointment

fake = Faker()


class Command(BaseCommand):
    help = 'Generate random data for models'

    def add_arguments(self, parser):
        parser.add_argument('num_data_sets', type=int, help='Number of data sets to generate')

    def handle(self, *args, **options):
        num_data_sets = options['num_data_sets']

        # Generate random data for Schedule model (unchanged)
        # ... your existing code for User, Company, and Employee models ...

        # Generate random data for Schedule model
        employees = Employee.objects.all()
        for _ in range(200):  # You can adjust the number of schedules generated
            schedule_id = str(fake.uuid4())[:100]

            # Generate random date between 2023 and 2024
            date = generate_random_date_in_range(2023, 2024)

            number_of_slots = random.randint(1, 10)
            available = random.choice([True, False])
            employee = random.choice(employees)

            schedule = Schedule(
                schedule_id=schedule_id,
                date=date,
                number_of_slots=number_of_slots,
                available=available,
                employee_email=employee,
            )
            schedule.save()

        # Generate random data for Appointment model
        appointments_per_schedule = 2  # You can adjust appointments per schedule
        schedules = Schedule.objects.all()
        for schedule in schedules:
            for _ in range(appointments_per_schedule):
                appointment_id = str(fake.uuid4())[:100]  # Generate unique appointment ID

                # Generate time in iOS format (HH:MM)
                time = fake.time("%H:%M")

                description = fake.text()
                status = random.choice(["pending", "approved", "cancelled"])
                employee = schedule.employee_email
                user = random.choice(User.objects.all())

                # Set time zone to "America/Los_Angeles" (adjust for other iOS regions)
                ios_tz = timezone('America/Los_Angeles')  # Replace with desired iOS time zone
                time_obj = datetime.strptime(time, "%H:%M").time()
                ios_datetime = datetime.combine(schedule.date, time_obj)
                ios_datetime = ios_tz.localize(ios_datetime)  # Convert to iOS time zone

                appointment = Appointment(
                    appointment_id=appointment_id,
                    date=schedule.date,
                    time=ios_datetime.strftime("%H:%M"),  # Use strftime to format in iOS time zone
                    description=description,
                    status=status,
                    employee_email=employee,
                    email=user,
                    schedule_id=schedule,
                )
                appointment.save()


def generate_random_date_in_range(start_year, end_year):
    """Generates a random date object within a specified year range."""
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)  # Adjust for December 31st if needed
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates + 1)
    return start_date + timedelta(days=random_number_of_days)
