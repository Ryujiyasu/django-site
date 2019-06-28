from django.db import models
from django.contrib.auth.models import User
from sale.models import Mt_Service

class User_request(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service_type = models.ForeignKey(Mt_Service,verbose_name="サービスタイプ", on_delete=models.CASCADE)
    request=models.TextField(verbose_name="要望")
    def __str__(self):
        return str(self.user)
