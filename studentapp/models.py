from django.db import models
from department.models import Department
from course.models import Course
from subject.models import Subject

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField()
    subjects = models.ManyToManyField(Subject, blank=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
