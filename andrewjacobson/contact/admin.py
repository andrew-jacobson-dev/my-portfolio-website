from django.contrib import admin
from .models import ContactPoint, ContactMessage

# Register your models here.
admin.site.register(ContactPoint)
admin.site.register(ContactMessage)