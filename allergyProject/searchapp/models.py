from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    prdlstReportNo = models.BigIntegerField(primary_key=True)
    prdlstNm = models.CharField(max_length=200)
    prdkind = models.CharField(max_length=200)
    rawmtrl = models.TextField()
    allergy = models.TextField()
    manufacture = models.CharField(max_length=200)
    nutrient = models.TextField(blank=True)
    seller = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.prdlstNm

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
