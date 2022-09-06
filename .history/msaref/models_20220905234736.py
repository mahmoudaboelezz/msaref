from turtle import update
from django.db import models

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



    
class Paid(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    price = models.IntegerField()
    residual = models.IntegerField(default=0, blank=True, null=True)
    paid_up = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.residual = self.price - self.paid_up
        if self.residual == 0:
            self.done = True
        if self.done == True:
            self.residual = 0
            self.paid_up = self.price
        
        super().save(*args, **kwargs)
    
    # add price to total price
class Total(models.Model):
    Total = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE,blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.ManyToManyField(Paid, blank=True)
    
    
    def __str__(self):
        return f'{self.Total}'
    
    def get_total(self):
        total = 0
        for item in self.paid.all():
            total += item.paid_up
        return total
    
    def save(self, *args, **kwargs):
        self.Total = self.get_total()
        super().save(*args, **kwargs)