from django.contrib import admin

# Register your models here.

from first_app_for_project.models import Employee, Schedule, User, Company, Appointment



class ScheduleData(admin.ModelAdmin) :

    list_display =['schedule_id','date','number_of_slots','available','employee_email']

class Userdata(admin.ModelAdmin):
    list_display = ['username','password','email']

class Companydata(admin.ModelAdmin):
    list_display = ['company_name','company_email','location','company_schedule']

class Appointmentdata(admin.ModelAdmin):
    list_display = ['appointment_id','date','time','description','status','employee_email','user_email','schedule_id',]

admin.site.register(Employee)
admin.site.register(Schedule,ScheduleData)
admin.site.register(User,Userdata)
admin.site.register(Company,Companydata)
admin.site.register(Appointment,Appointmentdata)

