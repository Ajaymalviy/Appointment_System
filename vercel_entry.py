# vercel_entry.py

import os
import sys

# Add the directory containing your Django project to the Python path
sys.path.append(os.path.join(os.getcwd(), 'appointments_core'))

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appointments_core.settings')

# Import and initialize the Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
