from django.db import models

# Create your models here.
class BOOK(models.Model) :
    bid = models.IntegerField()
    bname = models.CharField(max_length=50)
    bauthor = models.CharField(max_length=50)
    bprice = models.FloatField()
