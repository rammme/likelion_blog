from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUser : User에서 동작은 그대로, 필드 추가 
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=50)

