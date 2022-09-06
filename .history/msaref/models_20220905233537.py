from turtle import update
from django.db import models

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Total(models.Model):
    Total = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.Total}'
    
class Paid(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    # add price to total price
    def add_price(self):
        # get first total and add price to it
        total = Total.objects.first()
        total.Total += self.price
        total.save()

    # run add_price when saving
    def save(self, *args, **kwargs):
        self.add_price()
        super().save(*args, **kwargs)