from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Preference(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
          db_table  = 'preference'






class GooritoUserProfile(models.Model):
    bio =  models.TextField(null=True)
    location  = models.CharField(max_length=250,null=True)
    budget = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    gender = models.CharField(max_length=1,choices=(('M','Male'),('F','Female'),('O','Other')),null=True,blank=True)
    lifestyle_preferences =  models.ManyToManyField(Preference)

    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    class Meta:
        db_table = 'user_profile'
# Create your models here.
class GooritoUser(AbstractUser):
    user = models.OneToOneField(GooritoUserProfile, on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'gooritouser'