from adminstration.models import Role
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    role = models.ForeignKey(Role, related_name='user_role', on_delete=models.CASCADE, blank=True, null=True)
