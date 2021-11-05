from authentication.models import User
from authentication.serializers import UserSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, views, permissions

from adminstration.models import Role

from . import models, serializers


class CreatePermission(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.PermissionsSerializer
    queryset = models.Permission.objects.all()


class CreateRole(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.RolesSerializer
    queryset = models.Role.objects.all()


class UserCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AssignUserToRole(views.APIView):
    permission_classes = (permissions.IsAdminUser,)
    def post(self, request, user_id):
        role_id = request.data.get("role_id")
        role = get_object_or_404(Role, pk=role_id)
        user = get_object_or_404(User, pk=user_id)
        role.user_set.add(user)
        serialized_user = UserSerializer(user)
        return JsonResponse(serialized_user.data)

class ListAllPermissions(generics.ListAPIView):
    serializer_class = serializers.PermissionsSerializer
    queryset = models.Permission.objects.all()


class ListAllContentTypes(generics.ListAPIView):
    serializer_class = serializers.ContentTypeSerializer
    queryset = models.ContentType.objects.all()