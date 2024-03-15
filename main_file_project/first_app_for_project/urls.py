from django import views
from django.urls import path,include
from first_app_for_project.views import index,getting_data
from django.conf import settings
from django.conf.urls.static import static
from .views import get_company_data, home, login

urlpatterns = [
    path('', index, name='about'),
    path('/home', home, name='home'),
    path('/search', get_company_data, name='getting_company_data'),
    path('meeting_request/', views.save_request_for_meeting, name='save_request_for_meeting'),
  
]
