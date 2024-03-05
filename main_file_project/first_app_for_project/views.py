from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request, 'about.html')


# def index(request):
#     return render(request, 'index.html')


#--------------------------------Login------------------------------------------------------------
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import User


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            print(username)
        except User.DoesNotExist:
            # User does not exist, handle appropriately (e.g., show error message)
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
        
        # Save the user object to the MongoDB collection
        user.save()
        
        # Redirect to the login page
        return redirect(reverse('login'))  # Assuming 'login' is the name of your login URL pattern

    return render(request, 'registration.html')

#-----------------------------------------------------home after login-----------

def home(request):
    return render(request, 'index.html')