from django.db import models
from course.models import Course
from subject.models import Subject

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.subject.name})"
