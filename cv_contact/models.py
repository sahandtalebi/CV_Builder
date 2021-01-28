from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    massage = models.TextField()

    def __str__(self):
        return self.full_name


class Information(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map = models.URLField()

    def __str__(self):
        return self.phone
