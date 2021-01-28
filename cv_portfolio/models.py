from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField()
