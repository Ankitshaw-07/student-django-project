from django.db import models
from course.models import Course

class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Sem {self.semester})"
