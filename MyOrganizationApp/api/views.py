from rest_framework.generics import ListCreateAPIView

from MyOrganizationApp.api.serializers import OrganizationInfoSerializer, ContactInfoSerializer
from MyOrganizationApp.models import OrganizationInfo, ContactInfo


class OrganizationInfoListCreateAPIView(ListCreateAPIView):
    serializer_class = OrganizationInfoSerializer
    queryset = OrganizationInfo.objects.all()


class ContactInfoListCreateAPIView(ListCreateAPIView):
    serializer_class = ContactInfoSerializer
    queryset = ContactInfo.objects.all()
