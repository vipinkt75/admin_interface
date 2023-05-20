from django.db import models
from versatileimagefield.fields import VersatileImageField
# Create your models here.
class Filtter(models.Model):
    ClassName_CHOICES = (
        ('malayalam', 'malayalam'),
        ('english', 'english'),
        ('hindi', 'hindi'),
    )
    image = VersatileImageField(upload_to = "filtter")
    name = models.CharField(max_length=100,blank=True,null=True)
    tittle = models.CharField(max_length=100,blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    ClassName= models.CharField(max_length=50,choices=ClassName_CHOICES,verbose_name="category")