from django.urls import path
from . import views

urlpatterns = [
    path('create-student', views.CreateStudent.as_view(), name='create_student'),
    path('list-students', views.ListStudents.as_view(), name='list_students'),
]