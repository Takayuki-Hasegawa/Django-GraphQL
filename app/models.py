from django.db import models


class UserTable (models.Model):
    name = models.CharField(max_length=50)
    displayName = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name
