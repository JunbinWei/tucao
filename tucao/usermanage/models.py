from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=10)
    password=models.CharField(max_length=16)
    born_date=models.DateTimeField(null=True)
    gender=models.BooleanField()
    description=models.TextField(blank=True,null=True)
    head_img=models.TextField(null=True)
    exp=models.IntegerField()
    rank=models.IntegerField()
    telnumber=models.CharField(max_length=11,null=True)

    def __str__(self):
    	return self.name

