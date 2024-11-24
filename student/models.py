from django.db import models


# Create your models here.
class Student(models.Model):
    role_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.role_number)
