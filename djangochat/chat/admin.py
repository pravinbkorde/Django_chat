from django.contrib import admin
# import all the classes from models.py
#then create the super user using the command python manage.py createsuperuser
from .models import Room, Message
# username= admin,password  = pravin
# Register your models here.
admin.site.register(Room)
admin.site.register(Message)