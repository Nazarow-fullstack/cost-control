from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    CHOISES = (
        ('user', 'User'),
        ('admin', 'Admin')
    )
    role = models.CharField(max_length=10, choices=CHOISES, default='user')