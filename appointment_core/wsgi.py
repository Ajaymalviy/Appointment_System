"""
WSGI config for main_file_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appointment_core.settings')
# print('goodydm')


application = get_wsgi_application()
# print(application)
app = application

# from first_app_for_project import app

# if __name__ == "__main__":
#     app.run()

