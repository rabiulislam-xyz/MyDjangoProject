from django.db import models


# Create your models here.
from django.urls import reverse


class OrganizationInfo(models.Model):
    email = models.EmailField(unique=True, db_index=True, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('organization_detail', kwargs={"pk": self.email})

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    email = models.EmailField(unique=True, db_index=True, primary_key=True)
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(OrganizationInfo, related_name="contact_infos", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('contact_detail', kwargs={"pk": self.email})

    def __str__(self):
        return self.name
