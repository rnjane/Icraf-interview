from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=30)

    def __str__(self):
        return self.student_name