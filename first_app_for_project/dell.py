from .models import User, Company, Employee, Schedule, Appointment, MeetingRequest

# Delete all existing data from each model
User.objects.all().delete()
Company.objects.all().delete()
Employee.objects.all().delete()
Schedule.objects.all().delete()
Appointment.objects.all().delete()
MeetingRequest.objects.all().delete()