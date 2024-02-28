from django.urls import path
from first_app_for_project.views import index

urlpatterns = [
    path('', index, name='index'),
]
