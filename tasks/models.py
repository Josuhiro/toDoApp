from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

