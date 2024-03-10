"""
URL configuration for main_file_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from first_app_for_project.views import get_company_data, index,home
from django.conf import settings
from django.conf.urls.static import static
from first_app_for_project import views
urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('', index, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register_user, name='register'),
    path('home/', home, name='home'),
    path('search/', get_company_data, name='getting_company_data'),
    # Other URL patterns...
]

