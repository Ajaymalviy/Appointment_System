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
from django.urls import path, include
from first_app_for_project.views import index,choose, aboutpage,servicepage, contactpage,loginnew,registernew, employee_login,back,  meeting,dashboard
# from first_app_for_project.views import index,callback_view, profile_view,codemos,techritzy
from django.conf import settings
from django.conf.urls.static import static
from first_app_for_project import views
from django.views.generic import TemplateView #useful in displaying oauth.html template
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path('/', views.index, name='index'),
    path('about/', views.aboutpage, name='aboutpage'),
    path('service/', views.servicepage, name='servicepage'),
    path('contact/', views.contactpage, name='contactpage'),
    path('loginnew/', views.loginnew, name='loginnew'),
    path('registernew/', views.registernew, name='registernew'),
    # path('user_login/', views.user_login, name='user_login'),
    # path('employee_registration/', views.employee_registration, name='employee_registration'),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('logout/', views.logout, name='logout'),
    path("meeting_home/", views.meeting,  name="meeting"),
    path('search/', views.search_company_view, name='search_company'),
    path('meeting_request/', views.save_request_for_meeting, name='meeting_request'),
    path('sendmail/', views.sendmail, name='sendmail'),
    path('home/', views.back, name="back"),
    path('choose/', views.choose, name='choose'),
    path("dashboard/",views.dashboard, name="dashboard"),



    # path('app/',include('first_app_for_project.urls')), #app urls
    # path('', TemplateView.as_view(template_name='oauth.html')),
    # path('accounts/', include('allauth.urls')), # all OAuth operations will be performed under this route 
    # path('logout/', LogoutView.as_view(), name='account_logout'),
    # path('oauth/callback/', callback_view, name='oauth_callback'),
    # path('profile/', profile_view, name='profile'),
    # path('techritzy/', techritzy, name='tech'),
    # path('codemos/', codemos, name='code'),
]

