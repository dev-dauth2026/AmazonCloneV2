from django.contrib import admin
from .models import Customer,Admin

# Register your models here.
admin.site.register(Admin)
admin.site.register(Customer)