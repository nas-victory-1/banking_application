from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password= None, **extra_fields):


    def create_superuser