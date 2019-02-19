from rest_framework import serializers

from MyOrganizationApp.models import OrganizationInfo, ContactInfo


class OrganizationInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrganizationInfo
            fields = ('email', 'name', 'address')


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ('email', 'name', 'organization')
