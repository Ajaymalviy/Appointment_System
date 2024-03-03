from django.urls import path,include
from first_app_for_project.views import index
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='about'),
]
# +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)