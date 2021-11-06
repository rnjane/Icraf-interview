from django.urls import path
from . import views

urlpatterns = [
    path('create-permission', views.CreatePermission.as_view(), name='create_permission'),
    path('create-role', views.CreateRole.as_view(), name='create_role'),
    path('assign-role-to-user/<int:user_id>', views.AssignUserToRole.as_view(), name='assign_role_to_user'),
    path('add-user/', views.UserCreate.as_view(), name='register'),
    path('list-all-permissions/', views.ListAllPermissions.as_view(), name='list_all_permissions'),
    path('list-content-types/', views.ListAllContentTypes.as_view(), name='list_all_content-types'),
    path('list-roles/', views.ListAllRoles.as_view(), name='list_all_roles'),
]