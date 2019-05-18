from django.db import models



class Userinfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=20,default="")
    class Meta:
        db_table = 'user_info'


