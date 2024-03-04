from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request, 'about.html')

#--------------------------------Login------------------------------------------------------------


from django.shortcuts import render
from django.http import HttpResponse
from .models import authenticate_user  # Assuming authenticate_user function is defined in models.py

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        authenticated, user = authenticate_user(username, password)
        if authenticated:
            return HttpResponse(f"Login successful! Welcome, {user['username']}")
        else:
            return HttpResponse("Invalid username or password")

    return render(request, 'login_page.html')  # Assuming you have a login.html template for the login page


#------------------------------------Registration--------------------------------------------
from django.shortcuts import render
from django.http import HttpResponse
from .models import User  # Assuming User model is defined in models.py

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Create a new User object
        user = User(username=username, password=password, email=email, phone=phone)
        
        # Save the user object to the MongoDB collection
        user.save()
        
        return HttpResponse("User registered successfully")

    return render(request, 'registration.html')  # Assuming you have a registration.html template for the registration page


#---------------------------------------------------------------------