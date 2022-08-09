from django.db import models

# Create your models here.



class ElasticDemo(models.Model):
    # url=models.CharField(max_length=500)
    # date=models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.TextField()
    