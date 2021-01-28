from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return self.title
