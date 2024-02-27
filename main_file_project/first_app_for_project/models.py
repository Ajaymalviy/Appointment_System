from django.db import models
# from mongoengine import Document, fields

# class phone(Document):
#   name = fields.StringField()
#   topic = fields.StringField()
#   date = fields.DateTimeField()
#   addition_info = fields.DictField()


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    employee_email = models.EmailField()
    email = models.EmailField()
    location = models.CharField(max_length=100)
    company_schedule = models.CharField(max_length=100)

class Appointment(models.Model):
    appointment_id = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100)
    employee_email = models.EmailField()
    user_email = models.CharField(max_length=100)
    schedule_id = models.CharField(max_length=100)

class Employee(models.Model):
    employee_email = models.EmailField()
    employee_role = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    experience = models.IntegerField()
    skills = models.JSONField()

class Schedule(models.Model):
    schedule_id = models.CharField(max_length=100)
    date = models.DateField()
    number_of_slots = models.IntegerField()
    available = models.BooleanField()
    employee_email = models.EmailField()

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()


