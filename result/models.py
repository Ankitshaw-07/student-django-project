from django.db import models
from studentapp.models import Student
from subject.models import Subject

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=5, blank=True)

    def save(self, *args, **kwargs):
        # Simple grade calculation
        if self.marks >= 90:
            self.grade = 'A+'
        elif self.marks >= 80:
            self.grade = 'A'
        elif self.marks >= 70:
            self.grade = 'B+'
        elif self.marks >= 60:
            self.grade = 'B'
        elif self.marks >= 50:
            self.grade = 'C'
        else:
            self.grade = 'F'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} ({self.marks})"
