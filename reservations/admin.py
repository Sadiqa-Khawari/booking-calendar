from django.contrib import admin
from .models import Members 

# Register your models here.
admin.site.register(Members)
admin.site.site_header = "Booking Calendar Admin"
