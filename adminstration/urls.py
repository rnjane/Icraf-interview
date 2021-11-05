from django.urls import path
from . import views

urlpatterns = [
    path('create-permission', views.CreatePermission.as_view(), name='create_permission'),
    path('create-role', views.CreateRole.as_view(), name='create_role'),
    path('assign-role-to-user/<int:user_id>', views.AssignUserToRole.as_view(), name='assign_role_to_user'),
    path('add-user/', views.UserCreate.as_view(), name='register'),
]