


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
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout as auth_logout , authenticate,login as auth_login
from first_app_for_project.models import User, Employee, Company,MeetingRequest
from django.urls import reverse
import pymongo
from pymongo import MongoClient
from datetime import datetime
from django.contrib.auth.models import User


def index(request):
    return render(request, 'about.html')

def register_user(request):
    print('goodydm')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        print(username,password,email)
        hashed_password = make_password(password)
        user = User(username=username, password=hashed_password, email=email )
        user.save()
        return redirect('user_login') 
    return render(request, 'registration.html')




def employee_registration(request):
    if request.method == 'POST':
        # Retrieve data from the form
        employee_email = request.POST.get('employee_email')
        employee_role = request.POST.get('employee_role')
        employee_name = request.POST.get('employee_name')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        company_name = request.POST.get('company')
        company, created = Company.objects.get_or_create(company_name=company_name)

        # if created:
        #     company.save()
        
        password = request.POST.get('password')
        
        # Save data to the Employee model
        employee = Employee(
            employee_email=employee_email,
            employee_role=employee_role,
            employee_name=employee_name,
            experience=experience,
            skills=skills,
            company_name=company,
            password=password
        )
        employee.save()
        print('successful data entry')
        
        # Optionally, you can redirect to a success page
        return render(request, 'login.html')
    
    return render(request, 'employee_register.html')

   

def employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print("username is type of", type(username))
        password = request.POST.get('password')
        print(username,password)
        if username and password:
            try:
                # list = [username]
                employee_document =  Employee.objects.get(employee_name=username)
                print("think is that it is a ", employee_document)
                if employee_document:
                    employee_username = employee_document.employee_name
                    print(employee_username)
                    username_list = [employee_username]
                    if employee_document.password == password:
                        print("Authentication successful")
                        meeting_requests = MeetingRequest.objects.filter(employee_email=employee_document)
                        print(type(meeting_requests))
                        # Redirect to employee dashboard
                        if meeting_requests:
                            print("yes metting req")
                            return render(request, 'employee_dashboard  .html', {'employee': employee_document, 
                                                                'meeting_requests':meeting_requests}) 
                        else:
                            print("No meeting requests found for the specified email.")
                            return render(request, 'employee_dashboard.html',{'employee': employee_document, 'error': 'No meeting requests found.'})
                    else:
                        error_message = 'Invalid email or password.'
                else:
                    error_message = 'Invalid email or password.'
            except Exception as e:
                print("Exception occurred:", e)
                error_message = 'An error occurred during login.'
        else:
            error_message = 'Email and password are required.'

        return render(request, 'login.html')
    return render(request, 'login.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            print(username)
        except User.DoesNotExist:
            print('errror')
  
        if check_password(password, user.password):
            print('success')
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', 
                        {'error':'Invalid username or password' })  
    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')

def get_company_data(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method. Use POST to retrieve company data.'})
    
    company_name = request.POST.get('company_name')
    
    if not company_name:
        return JsonResponse({'error': 'Invalid company name'})
    
    try:
        # Retrieve company object using the company name
        company = Company.objects.get(company_name=company_name)
        
        # Retrieve all employees of the company
        employees = Employee.objects.filter(company_name=company)
        
        data_list = []
        for employee in employees:
            data_list.append({
                'employee_email': employee.employee_email,
                'employee_role': employee.employee_role,
                'employee_name': employee.employee_name,
                'skills': employee.skills,
                'experience': f"{employee.experience}-Yr"
            })
        
        if data_list:
            return render(request, 'services.html', {'company_name': company_name, 'employees': data_list})
        else:
            return JsonResponse({'error': 'No details found for the selected company'})
    
    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'})    
    
    
def rating(request):
    return render(request, 'rating.html')    

def logout(request):
    auth_logout(request)  
    return render(request, 'about.html') 

  

def save_request_for_meeting(request):
    if request.method == 'POST':
        employee_email = request.POST.get('employee_email')
        requester_email = request.POST.get('requester_email')
        description = request.POST.get('description')
        date_str = request.POST.get('date')
        print("Employee Email:", employee_email)
        print("Requester Email:", requester_email)
        print("date is :" , date_str)
        print("next from this data was not lodede")
        # Check if employee_email is available in POST data
        if employee_email:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            meeting_request = MeetingRequest.objects.create(
                employee_email=employee_email,
                requester_email=requester_email,
                description=description,
                date=date
            )
            return render(request, 'services.html')
        else:
            # Handle the case where employee_email is missing (e.g., display an error message)
            print("Employee email is missing in the form submission.")
            return render(request, 'takeschedulee.html')  # Or redirect to an error page

    # If the request is not POST, redirect to the form page with the employee's email in the URL
    employee_email = request.GET.get('employee_email')
    if employee_email:
        print(employee_email)
        return HttpResponseRedirect(reverse('meeting_request') + f'?employee_email={employee_email}')
        
    else:
        return render(request, 'takeschedulee.html')




