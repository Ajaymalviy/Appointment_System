from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
  

class Company(models.Model):
    company_name = models.CharField(max_length=100, primary_key=True)
    company_email = models.EmailField(default='xyz@gmail.com')
    location = models.CharField(max_length=100)
    company_schedule = models.CharField(max_length=100)
    def __str__(self):
        return self.company_name
    

class Employee(models.Model):    
    employee_email = models.EmailField( primary_key=True)
    employee_role = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    experience = models.IntegerField()
    skills = models.JSONField()
    company_name = models.ForeignKey('Company', on_delete=models.CASCADE) 
    password = models.CharField(max_length=50 , default='ajay')
    def __str__(self):
        return self.employee_email
    
    
class Schedule(models.Model):
    schedule_id = models.CharField(primary_key=True,max_length=100)
    date = models.DateField()
    number_of_slots = models.IntegerField()
    available = models.BooleanField()
    employee_email = models.ForeignKey('Employee', on_delete=models.CASCADE) 
    def __str__(self):
        return self.schedule_id
    
class Appointment(models.Model):
    appointment_id = models.CharField(primary_key=True, max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100)
    employee_email = models.ForeignKey(Employee, on_delete=models.CASCADE)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.appointment_id

class MeetingRequest(models.Model):
    employee_email = models.EmailField()
    requester_email = models.EmailField()
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Meeting Request for {self.employee_email} on {self.date}"
    



