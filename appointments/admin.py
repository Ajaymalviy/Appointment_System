from django.contrib import admin

# Register your models here.

from appointments.models import Employee, Schedule, User, Company, Appointment,MeetingRequest



class Userdata(admin.ModelAdmin):
    list_display = ['username','password','email']

class Companydata(admin.ModelAdmin):
    list_display = ('company_name', 'company_email', 'location', 'company_schedule')

class Employeedata(admin.ModelAdmin):
    list_display = ('employee_email', 'employee_role', 'employee_name', 'experience', 'company_name')

class ScheduleData(admin.ModelAdmin) :
    list_display = ('schedule_id', 'date', 'number_of_slots', 'available', 'employee_email')

class Appointmentdata(admin.ModelAdmin):
    list_display = ('appointment_id', 'date', 'time', 'description', 'status', 'employee_email', 'email', 'schedule_id')

class MeetingRequestdata(admin.ModelAdmin):
    list_display = ('employee_email', 'requester_email', 'description', 'date')

admin.site.register(User,Userdata)
admin.site.register(Company,Companydata)
admin.site.register(Employee,Employeedata)
admin.site.register(Schedule,ScheduleData)
admin.site.register(Appointment,Appointmentdata)
admin.site.register(MeetingRequest,MeetingRequestdata)

