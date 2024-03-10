from django.urls import path,include
from first_app_for_project.views import index,getting_data
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='about'),
]
# +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
from django.urls import path
from .views import get_company_data, home, login

urlpatterns = [
    path('/home', home, name='home'),
    path('/search', get_company_data, name='getting_company_data'),
    # Other URL patterns for your application
]
