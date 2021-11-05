from rest_framework import serializers
from . import models

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permission
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContentType
        fields = '__all__'

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'