


'''
Basically this is the file of python which contain many fucntion of python which redirect,renders on some other pages.

below are the listing of subfucntion.

index: Renders the "about.html" template
which is our first page.

register_user: Handles user registration. 
When a POST request is received, it takes username, password, email,
and phone number from the request, hashesing of password,
creates a new object of user, and saves it to the database. Then, redirects to the login page.

login: Handles user login.  
it extract the username and password from the request, 
and checks if the password matches correctly it renders the "index.html"
template; otherwise, it renders the "login_page.html" template with an error message.

home: Renders the "index.html" template, which i create for logo of my website.

get_company_data: taking company data from a database collection based on the provided company_name. 
and return the data as JSON response or may  renders the "services.html" template with the company_name and employee details.

rating: Renders the "rating.html" template, which i used for give the rating to by user

logout: this functin is used for just logout the basic session, "about.html" template.

takeschedule: Renders the "takeschedule.html" template, for taking the request for empty schedule by on the end of employee.

save_request_for_meeting: Saves meeting requests to a MongoDB collection. It extracts email, description, and date from the request, creates a document, inserts it into the collection, and renders the "success_page.html" template.

'''


import json
from bson import ObjectId 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout as auth_logout , authenticate,login as auth_login
from .models import User
from django.urls import reverse
import pymongo
from pymongo import MongoClient
from datetime import datetime
from django.contrib.auth.models import User


def index(request):
    return render(request, 'about.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        hashed_password = make_password(password)
        user = User(username=username, password=hashed_password, email=email )
        user.save()
        return render(request, 'login.html') 
    return render(request, 'registration.html')



def employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_employee:
                auth_login(request, user)
                return render(request, 'index1.html')   # Redirect to employee dashboard
            else:
                return render(request, 'login.html', {'error': 'You are not an employee'})
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not user.is_employee:
                auth_login(request, user)
                return render(request, 'index.html')  # Redirect to user dashboard
            else:
                return render(request, 'login.html', {'error': 'You are not a user'})
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             user = User.objects.get(username=username)
#             print(username)
#         except User.DoesNotExist:
#             print('errror')
#             return render(request, 'login_page.html', {'error': 'Invalid username or password'})
  
#         if check_password(password, user.password):
#             print('success')
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login_page.html', 
#                         {'error':'Invalid username or password' })  
#     return render(request, 'login_page.html')


def home(request):
    return render(request, 'index.html')

def get_company_data(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method. Use POST to retrieve company data.'
        })
    company_name = request.POST.get('company_name')
    if not company_name:
        return JsonResponse({'error': 'Invalid company name'})
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')  
        db = client['meetme'] 
        collection = db['Employee']  
        employees = collection.find({'company_name': company_name})
        data_list = []
        for employee in employees:
            data_list.append({
                'employee_email': employee['employee_email'],
                'employee_role': employee['employee_role'],
                'employee_name': employee['employee_name'],
                'skills': employee['skills'],
                'experience': str(employee['experience']) +'-Yr'
            })
        if data_list:
            return render(request, 'services.html', {
                'company_name': company_name, 'employees': data_list
            })
        else:
            return JsonResponse({'error':'No details found for the selected company'
            })
    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'})
    
def rating(request):
    return render(request, 'rating.html')    

def logout(request):
    auth_logout(request)  
    return render(request, 'about.html') 

def takeschedule(request):
    return render(request, 'takeschedule.html')   

def save_request_for_meeting(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        description = request.POST.get('description')
        date_str = request.POST.get('birthday')
        date = datetime.strptime(date_str, '%Y-%m-%d')

        client = MongoClient('mongodb://localhost:27017/')
        db = client['meetme']  
        collection = db['Request_for_meeting']
        request_document = {
            'email': email,
            'description': description,
            'date': date
        }

        collection.insert_one(request_document)
        client.close()
        return render(request, 'success_page.html')
    return render(request, 'takeshcedule.html')


