from django import forms

from MyOrganizationApp.models import OrganizationInfo, ContactInfo


class OrganizationInfoForm(forms.ModelForm):
    class Meta:
        model = OrganizationInfo
        fields = ("email", "name", "address")

        widgets = {
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'address': forms.Textarea(attrs={"class": "form-control"}),
        }


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ("email", "name", "organization")

        widgets = {
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'organization': forms.Select(attrs={"class": "form-control"}),
        }