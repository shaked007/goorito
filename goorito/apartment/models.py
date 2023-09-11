from django.db import models
from gooritouser.models import GooritoUser
# Create your models here.

class Apartment(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)    
    price =  models.DecimalField(decimal_places=4,max_digits=10)
    user_id =  models.ForeignKey(GooritoUser,on_delete=models.CASCADE)

    class Meta:
        db_table  = 'apartment'
