from django.contrib import admin

#import the models you created in models.py
from app.models import *


#To create admin, super user run command:
#python manage.py createsuperuser
#username
#email (can leave this field blank as well)
#password


#To access the models and data in models 
#Cant import more then one model in same request
admin.site.register(person)
admin.site.register(Empl)
admin.site.register(car)
