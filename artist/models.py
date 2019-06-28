from django.db import models
from django.contrib.auth.models import User


class Mt_group(models.Model):
    group_name=models.CharField(max_length=20)
    def __str__(self):
        return self.group_name

class Mt_role(models.Model):
    role_name=models.CharField(max_length=20)
    def __str__(self):
        return self.role_name


class Artist_group(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    artist_group=models.ForeignKey(Mt_group,on_delete=models.CASCADE)
    artist_roll=models.ForeignKey(Mt_role,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.artist_roll)






