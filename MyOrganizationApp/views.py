from itertools import chain

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import View

from MyOrganizationApp.forms import OrganizationInfoForm, ContactInfoForm
from MyOrganizationApp.models import OrganizationInfo, ContactInfo


class OrganizationInfoListView(View):
    def get(self, request):
        organizations = OrganizationInfo.objects.all().order_by("-created_at")
        context = {
            "organizations": organizations
        }
        return render(request, "MyOrganizationApp/organization_list.html", context)


class OrganizationInfoCreateView(View):
    def get(self, request):
        form = OrganizationInfoForm()
        context = {
            "form": form
        }
        return render(request, "MyOrganizationApp/organization_create.html", context)

    def post(self, request):
        form = OrganizationInfoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Organization Info Created Successfully!")
            return redirect("organization_list")

        context = {
            "form": form
        }
        return render(request, "MyOrganizationApp/organization_create.html", context)


class OrganizationInfoDetailView(View):
    def get(self, request, pk):
        organization = get_object_or_404(OrganizationInfo, pk=pk)

        context = {
            "organization": organization
        }
        return render(request, "MyOrganizationApp/organization_detail.html", context)


############################################## CONTACT INFO VIEWS AREA ################################################

class ContactInfoListView(View):
    def get(self, request):
        contacts = ContactInfo.objects.all().order_by("-created_at")
        context = {
            "contacts": contacts
        }
        return render(request, "MyOrganizationApp/contact_list.html", context)


class ContactInfoCreateView(View):
    def get(self, request):
        form = ContactInfoForm()
        context = {
            "form": form
        }
        return render(request, "MyOrganizationApp/contact_create.html", context)

    def post(self, request):
        form = ContactInfoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Contact Info Created Successfully!")
            return redirect("contact_list")

        context = {
            "form": form
        }
        return render(request, "MyOrganizationApp/contact_create.html", context)


class ContactInfoDetailView(View):
    def get(self, request, pk):
        contact = get_object_or_404(ContactInfo, pk=pk)

        context = {
            "contact": contact
        }
        return render(request, "MyOrganizationApp/contact_detail.html", context)


class SearchView(View):
    def get(self, request):
        q = request.GET.get('q')
        result_list = []

        if q:
            organizations = OrganizationInfo.objects.filter(Q(email=q) |
                                                            Q(name__icontains=q) |
                                                            Q(address__icontains=q)).distinct()

            contacts = ContactInfo.objects.filter(Q(email=q) |
                                                  Q(name__icontains=q) |
                                                  Q(organization__email=q) |
                                                  Q(organization__name__icontains=q) |
                                                  Q(organization__address__icontains=q)).distinct()

            result_list = list(chain(organizations, contacts))

        context = {
            "items": result_list
        }
        return render(request, "MyOrganizationApp/search.html", context)
