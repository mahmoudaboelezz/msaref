from turtle import update
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    paid_elm = models.ForeignKey('Paid', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.name} - {self.section}'
    
class Paid(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    band_elm = models.ForeignKey(Band, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    residual = models.IntegerField(default=0, blank=True, null=True)
    paid_up = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    
    def save(self,request, *args, **kwargs):
        self.residual = self.price - self.paid_up
        if self.residual == 0:
            self.done = True
        if self.done == True:
            self.residual = 0
            self.paid_up = self.price
        
        # set user to current user
        if self.by is None:
            self.by = self.request.user
       
        
        
        
        super().save(request, *args, **kwargs)
    
    # add price to total price
class Total(models.Model):
    Total = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE,blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.ManyToManyField(Paid, blank=True)
    residual_total = models.IntegerField(default=0)
    overall_total = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.Total}'
    
    def get_total(self):
        total = 0
        for item in self.paid.all():
            total += item.paid_up
        return total
    
    def get_residual(self):
        residual = 0
        for item in self.paid.all():
            residual += item.residual
        return residual
    
    def get_overall_total(self):
        total = 0
        for item in self.paid.all():
            total += item.price
        return total
    
    
    
    def save(self, *args, **kwargs):
        self.Total = self.get_total()
        self.residual_total = self.get_residual()
        self.overall_total = self.get_overall_total()
        super().save(*args, **kwargs)