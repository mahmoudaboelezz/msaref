from django.db import models

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Paid(models.Model):
    related_to = models.CharField(max_length=100)
    