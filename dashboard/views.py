from django.http import HttpResponseForbidden, JsonResponse
from rest_framework import generics, permissions, response

from . import models, serializers


class CreateStudent(generics.CreateAPIView):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()

    def create(self, serializer):
        if not self.request.user.has_perm('student.create_a_new_student'):
            return response.Response({"error": "you do not have permission to create a student."})
        else:
            serializer.save()
            return response.Response(serializer.data)


class ListStudents(generics.ListAPIView):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()

    def list(self, request):
        if not request.user.has_perm('student.view_all_students'):
            return response.Response({"error": "you do not have permission to view students."})
        else:
            queryset = self.get_queryset()
            serializer = serializers.StudentSerializer(queryset, many=True)
            return response.Response(serializer.data)
