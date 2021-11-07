from django.http import HttpResponseForbidden, JsonResponse
from rest_framework import generics, permissions, response
from rest_framework.decorators import api_view

from . import models, serializers

@api_view(('GET',))
def student_dashboard(request):
    if request.user.has_perm('student.view_student_dashboard'):
        return response.Respons({"message": "Success!"})
    else:
        return response.Response({"message": "you do not have permissionn to access this page"})

@api_view(('GET',))
def teacher_dashboard(request):
    if request.user.has_perm('teacher.view_teacher_dashboard'):
        return response.Respons({"message": "Success!"})
    else:
        return response.Response({"message": "you do not have permissionn to access this page"})
