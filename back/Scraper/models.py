from django.db import models
from django.contrib.postgres.fields import ArrayField

class Category(models.Model):
    name = models.CharField(max_length=100)

    
class JobListings(models.Model):
    title = models.CharField(max_length=500, default='')
    company = models.CharField(max_length=500, default='')
    company_link =  models.URLField(default='', blank=True, null=True)
    location = models.CharField(max_length=10000, default='')
    apply_link = models.URLField(max_length=500, default='',blank=True, null=True)
    sponsorship=models.BooleanField(default=False)
    closed=models.BooleanField(default=False)
    categories = ArrayField(models.CharField(max_length=100), blank=True, default=list)

    def __str__(self):
        return self.title