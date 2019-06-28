from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mt_Service(models.Model):
    service_typoe=models.CharField(max_length=50)
    def __str__(self):
        return self.service_typoe

class Mt_aritstname(models.Model):
    artist_name = models.CharField(max_length=50,primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type=models.ForeignKey(Mt_Service,on_delete=models.CASCADE)
    def __str__(self):
        return self.artist_name


class Sale(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    artist_name=models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    count=models.IntegerField()
    price=models.FloatField()
    pricesum=models.FloatField()
    service_type=models.ForeignKey(Mt_Service,on_delete=models.CASCADE)
    date=models.DateField()
    importdate=models.DateField()
    def __str__(self):
        return self.item
