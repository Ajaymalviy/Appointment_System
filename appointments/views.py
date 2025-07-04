


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
# from bson import ObjectId 
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout as auth_logout, authenticate,login 
from first_app_for_project.models import User, Employee, Company,MeetingRequest
from django.urls import reverse
import pymongo
from pymongo import MongoClient
from datetime import datetime
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
# from allauth.socialaccount.models import SocialAccount
import pdb


def index(request):
    print(request)
    return render(request, 'home.html')

# def callback_view(request):
#     # Handle OAuth callback
#     return redirect('index')

# # views.py

# def profile_view(request):
#     # Get user's social account
#     social_account = SocialAccount.objects.get(user=request.user)
#     print(social_account)
#     # Access user data through the social account
#     pdb.set_trace()
#     print('error counter')
#     print(social_account.extra_data)

# def techritzy(request):
#     return render(request ,'techritzy.html')    

# def codemos(request):
#     return render(request, 'codemos.html') 

def aboutpage(request):
    return render(request, 'aboutus.html')

def servicepage(request):
    return render(request, 'service.html')

def contactpage(request):
    return render(request, 'con.html')

def back(request):
    return render(request, 'mainnew.html')


def choose(request): 
    return render(request, 'choose_login.html') 


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


def loginnew(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, 'You have been successfully logged in.')
            return redirect('meeting')
 # Redirect to the 'meeting' view
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'loginnew.html')



def registernew(request):
    print('goodydm')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        print(username,password,email)
        hashed_password = make_password(password)
        user = User(username=username, password=hashed_password, email=email )
        user.save()
        return redirect('loginnew') 
    return render(request, 'registernew.html')


# def employee_registration(request):
#     if request.method == 'POST':
#         # Retrieve data from the form
#         employee_email = request.POST.get('employee_email')
#         employee_role = request.POST.get('employee_role')
#         employee_name = request.POST.get('employee_name')
#         experience = request.POST.get('experience')
#         skills = request.POST.get('skills')
#         company_name = request.POST.get('company')
#         company, created = Company.objects.get_or_create(company_name=company_name)

#         # if created:
#         #     company.save()
        
#         password = request.POST.get('password')
        
#         # Save data to the Employee model
#         employee = Employee(
#             employee_email=employee_email,
#             employee_role=employee_role,
#             employee_name=employee_name,
#             experience=experience,
#             skills=skills,
#             company_name=company,
#             password=password
#         )
#         employee.save()
#         print('successful data entry')
        
#         # Optionally, you can redirect to a success page
#         return render(request, 'login.html')
    
#     return render(request, 'employee_register.html')
   

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
                            return render(request, 'employee_dashboard1.html', {'employee': employee_document, 
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

        return render(request, 'employee_login.html')
    return render(request, 'employee_login.html')

def dashboard(request):
    return render(request, 'employee_dashboard1.html')


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             user = User.objects.get(username=username)
#             print(username)
#         except User.DoesNotExist:
#             print('Error: User does not exist')
#             return render(request, 'loginnew.html', {'error': 'Invalid username or password'})

#         if check_password(password, user.password):
#             print('Success: Logged in as', username)
#             return redirect('meeting', user=user)  # Redirect with user parameter
#         else:
#             print('Error: Invalid password')
#             return render(request, 'loginnew.html', {'error': 'Invalid username or password'})

#     print('No user')  
#     return render(request, 'loginnew.html', {'user': None})
# from django.contrib.auth import authenticate, login

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)  # Log in the user
#             print(user)
#             return redirect('meeting')  # Redirect with user parameter
#         else:
#             print('Error: Invalid username or password')
#             return render(request, 'loginnew.html', {'error': 'Invalid username or password'})

#     return render(request, 'loginnew.html')



def home(request):
    return render(request, 'index.html')

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def search_company_view(request):
    if request.method != 'POST':
        print('not yours')
        return JsonResponse({'error': 'Invalid request method. Use POST to retrieve company data.'})
    
    company_name = request.POST.get('company_name')
    print(company_name)
    
    if not company_name:
        print('not company name')
        return JsonResponse({'error': 'Invalid company name'})
    
    try:
        print('gooooodydm')
        # Retrieve company object using the company name
        company = Company.objects.get(company_name=company_name)
        print(company)  
        
        # Retrieve all employees of the company and order them by primary key
        employees = Employee.objects.filter(company_name=company).order_by('pk')
        print(employees)

        # The warning you're seeing, UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list, 
        # is raised because the employees queryset passed to the paginator isn't ordered.
        #  Pagination works best when the queryset is ordered consistently, ensuring the same set of results is returned each time the queryset is paginated.
        
        # Pagination
        paginator = Paginator(employees, 15)  # Show 15 employees per page
        print('paginator', paginator)
        page_number = request.GET.get('page')
        print('page_number', page_number)
        try:
            employees = paginator.page(page_number)
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        
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
            print('chal gya re baaba')
            return render(request, 'company_Dev.html', {'company_name': company_name, 'employees': data_list, 'paginator': paginator, 'page_obj': employees})
        else:
            return JsonResponse({'error': 'No details found for the selected company'})
    
    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}) 

    
def meeting(request, user=None):
    if user is not None:
        # You can access user information here (e.g., user.username)
        print('User:', user.username)
    else:
        print('No user provided')
    
    return render(request, 'mainnew.html')


def logout(request):
    auth_logout(request)  
    return render(request, 'home.html') 

  

def save_request_for_meeting(request):
    if request.method == 'POST':
        employee_email = request.POST.get('employee_email')
        # requester_email = request.POST.get('requester_email')
        description = request.POST.get('description')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')

        # Retrieve the email of the logged-in user
        requester_email = request.user.email
        print("Employee Email:", employee_email)
        print("Requester Email:", requester_email)
        print("date is :" , date_str)
        print("time is :" , time_str)
        print("next from this data was not lodede")
        # Check if employee_email is available in POST data
        if employee_email:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            time_obj = datetime.strptime(time_str, '%H:%M').time()  # Assuming HH:MM format
            meeting_request = MeetingRequest.objects.create(
                employee_email=employee_email,
                requester_email=requester_email,
                description=description,
                date=date,
                time=time_obj
            )
            return render(request, 'company_Dev.html')
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


def sendmail(request):

    if 'email' in request.GET:
        requester_email = request.GET['email']

    # Your email-sending logic here
        send_mail(
            'THANKYOU BY MEETME',
             f'Hi there,\n\nYour meeting request has been accepted. You can expect the meeting to take place as scheduled.\n\nThank you for using our services.\n\nBest regards,\n[Ajay-Malviya]',
            'ajeymalviya143@gmail.com',
            [requester_email],
            fail_silently=False,
        )
        return render(request, 'emailsent.html')
        # return HttpResponse('Email sent successfully!') 
    #return render(request, 'employee_dashboard.html')
    else:
        return HttpResponse('Requester email not provided!')
    

def sendmailforcancel(request):
    if 'email' in request.GET:
        requester_email = request.GET['email']

    # Your email-sending logic here
        send_mail(
            'THANKYOU BY MEETME',
            f'Hi there,\n\nYour meeting request has been canced now. This is the busy schedule.\n\nThank you for using our services.\n\nBest regards,\n[Ajay-Malviya]',
            'ajeymalviya143@gmail.com',
            [requester_email],
            fail_silently=False,
        )
        return render(request, 'emailsent.html')
        # return HttpResponse('Email sent successfully!') 
    #return render(request, 'employee_dashboard.html')
    else:
        return HttpResponse('Requester email not provided!')

# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
# def codemos(request):
#     if request.user.username == 'ajay'  or request.user.username == 'it_2k21_04_ajaymalviya':
#         return render(request, 'codemos.html')
#     else:
#         return HttpResponse("You are not authorized to access this page.", status=403)
# @login_required
# def techritzy(request):
#     if request.user.username == 'ajayy' or request.user.username == 'it_2k21_04_ajaymalviya':
#         return render(request, 'techritzy.html')
#     else:
#         return HttpResponse("You are not authorized to access this page.", status=403)

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ContactDetail

def contactdetail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save the form data to the database
        contact = ContactDetail.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Add success message
        success_message = "Your message has been sent successfully!"
        messages.success(request, success_message)
        print(message)
        print('message')
        # Render the same page with the success message
        return render(request, 'conn.html')
    return render(request, 'conn.html')


#def include file for nginx setup :
