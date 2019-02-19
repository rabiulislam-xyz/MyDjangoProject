from django.urls import path, include
from .views import OrganizationInfoListView, OrganizationInfoCreateView, OrganizationInfoDetailView, \
    ContactInfoListView, ContactInfoCreateView, ContactInfoDetailView, SearchView

urlpatterns = [
    path('', OrganizationInfoListView.as_view(), name='organization_list'),
    path('create/', OrganizationInfoCreateView.as_view(), name='organization_create'),
    path('detail/<pk>/', OrganizationInfoDetailView.as_view(), name='organization_detail'),

    path('contacts/', ContactInfoListView.as_view(), name='contact_list'),
    path('contacts/create/', ContactInfoCreateView.as_view(), name='contact_create'),
    path('contacts/detail/<pk>/', ContactInfoDetailView.as_view(), name='contact_detail'),

    path('search/', SearchView.as_view(), name='search'),
    path('api/', include("MyOrganizationApp.api.urls"))
]
