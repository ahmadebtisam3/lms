from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Book(models.Model):
    number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return "{} ({})".format(self.name, self.number)
