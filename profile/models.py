from django.db import models

class Profile(models.Model):
    user_id = models.OneToOneField("authentication.CustomUser",  on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name