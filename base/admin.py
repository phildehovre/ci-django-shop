from django.contrib import admin
from .models import Profile 
from .models import Address
from .models import Feature

# Register your models here.

admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Feature)