from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    qq = models.CharField('QQ账号',max_length=16)
    weChat = models.CharField('微信',max_length=111)
    mobile = models.CharField('手机',max_length=11)
    address = models.CharField('地址',max_length=255)

    def __str__(self):
        return self.username