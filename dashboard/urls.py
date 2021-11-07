from django.urls import path
from . import views

urlpatterns = [
    path('student-dashboard', views.student_dashboard, name='sudents-dashboard'),
    path('teacher-dashboard', views.teacher_dashboard, name='teacber-dashboard')
]