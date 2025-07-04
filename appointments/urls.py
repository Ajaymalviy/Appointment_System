from django import views
from django.urls import path,include
from appointments.views import index,getting_data,servicepage,contactpage,aboutpage
from django.conf import settings
from django.conf.urls.static import static
from .views import get_company_data, home, login, sendmail
from django.contrib import admin

urlpatterns = [
    path('/admin', ),
    path('', index, name='index'),
    path('/home', home, name='home'),
    path('/search', get_company_data, name='getting_company_data'),
    path('meeting_request/', views.save_request_for_meeting, name='save_request_for_meeting'),
    path('about/', views.aboutpage, name='aboutpage'),
    path('service/', views.servicepage, name='servicepage'),
    path('contact/', views.contactpage, name='contactpage'),
    path('user_login/', views.user_login, name='user_login'),
    

]
