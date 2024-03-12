from django.http import HttpResponse

from django.shortcuts import render,redirect



# def index(request):
#     return render(request, 'index.html')


#--------------------------------Login------------------------------------------------------------
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import User


def index(request):
    return render(request, 'about.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            print(username)
        except User.DoesNotExist:
            # User does not exist, (e.g., show error message)
            print('errror')
            return render(request, 'login_page.html', {'error': 'Invalid username or password'})
            
        
        # Check if the password matches
        if check_password(password, user.password):
            print('success')
            # Password matches, login successful
            # You may set session variables or use Django's built-in authentication mechanisms here
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # Password does not match, handle appropriately (e.g., show error message)
            return render(request, 'login_page.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login_page.html')

#------------------------------------Registration--------------------------------------------
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.urls import reverse

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Hash the password
        hashed_password = make_password(password)
        
        # Create a new User object
        user = User(username=username, password=hashed_password, email=email, phone=phone)
        
        # Save the user object to the MongoDB collection, which is user
        user.save()
        
        # Redirect to the login page after register
        return redirect(reverse('login'))  

    return render(request, 'registration.html')

#-----------------------------------------------------home after login-----------

def home(request):
    return render(request, 'index.html')

#--------------------search-company------------------------
from django.http import JsonResponse
import pymongo
import json
from bson import ObjectId 
from django.shortcuts import render

def get_company_data(request):

    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method. Use POST to retrieve company data.'})

    company_name = request.POST.get('company_name')

    if not company_name:
        return JsonResponse({'error': 'Invalid company name'})

    try:
        # Establish a connection to the MongoDB database
        client = pymongo.MongoClient('mongodb://localhost:27017/')  
        db = client['meetme'] 
        # Query MongoDB collection for company details
        collection = db['Employee']  
        employees = collection.find({'company_name': company_name})

        data_list = []
        for employee in employees:
            data_list.append({
                'employee_name': employee['employee_name'],
                'skills': employee['skills'],
                'experience': str(employee['experience']) +'Yr'
            })

        if data_list:
            return render(request, 'services.html', {'company_name': company_name, 'employees': data_list})
        else:
            return JsonResponse({'error': 'No details found for the selected company'})

    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'})
    
#---------------------rating page call-----------------------------------
    
def rating(request):
    return render(request, 'rating.html')    

#------------------------logout---------------------------------------------

from django.contrib.auth import logout as auth_logout
def logout(request):
    auth_logout(request)  # Clear session and log out the user
    return redirect('index')  # Redirect to the login page

#__________takescheduleby___________user-------------------------

def takeschedule(request):
    return render(request, 'takeschedule.html')   


