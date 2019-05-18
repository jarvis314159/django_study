from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    bname = models.CharField(max_length=20)
    bprice = models.FloatField()
    class Meta:
        db_table = 'book_info'