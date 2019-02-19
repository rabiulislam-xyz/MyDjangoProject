from django.urls import path

from MyOrganizationApp.api.views import OrganizationInfoListCreateAPIView, ContactInfoListCreateAPIView

urlpatterns = [
    path('organizations/', OrganizationInfoListCreateAPIView.as_view(), name='organization_api_list'),
    path('contacts/', ContactInfoListCreateAPIView.as_view(), name='contact_api_list'),
]
