from django.db import models
from department.models import Department

# Create your models here.
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in years")

    def __str__(self):
        return self.name