from django.contrib import admin
from .models import OrganizationInfo, ContactInfo


# Register your models here.
admin.site.register(OrganizationInfo)
admin.site.register(ContactInfo)
