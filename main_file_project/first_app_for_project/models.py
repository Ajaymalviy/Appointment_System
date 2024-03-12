from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)



class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    location = models.CharField(max_length=100)
    company_schedule = models.CharField(max_length=100)
    def __str__(self):
        return self.company_name
    

class Employee(models.Model):
    employee_email = models.EmailField()
    employee_role = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    experience = models.IntegerField()
    skills = models.JSONField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE) 


    
class Schedule(models.Model):
    schedule_id = models.CharField(max_length=100)
    date = models.DateField()
    number_of_slots = models.IntegerField()
    available = models.BooleanField()
    employee_email = models.EmailField()


class Appointment(models.Model):
    appointment_id = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100)
    employee_email = models.EmailField()
    user_email = models.CharField(max_length=100)
    schedule_id = models.CharField(max_length=100)




from django.db import connections
from passlib.hash import sha256_crypt

def authenticate_user(username, password):
    # Get the MongoDB connection from Django's ORM
    db_connection = connections['phone']

    # Access the MongoDB database and collection
    db = db_connection.get_database('phone')  # Specify the database name
    collection = db['user']  # Specify the collection name

    # Find user by username
    user = collection.find_one({'username': username})

    if user:
        # Check if password matches
        if sha256_crypt.verify(password, user['password']):
            return True, user
    return False, None

