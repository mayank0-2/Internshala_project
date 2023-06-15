from django.db import models

# Create your models here.
class apiModel(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    
    