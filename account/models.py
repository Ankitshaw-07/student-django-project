from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    role = models.CharField(
        max_length=20,
        choices=(('admin', 'Admin'), ('student', 'Student')),
        default='student'
    )

    def __str__(self):
        return self.username