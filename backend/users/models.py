from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password= None, **extra_fields):
        if not email:
            raise ValueError("email required") #throws an error if the email isn't provided
        
        user= self.model(
            email = self.normalize_email(email), #makes sure the email is following the correct format
            password = password
        )

        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self, email, password = None, **extra_fields):
        user = self.create_user(
            email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique= True,
        max_length= 255,

    )

    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=150
    )
    is_active = models.BooleanField(
        default= True  
    )
    is_staff = models.BooleanField(
        default= False
    )
    date_joined = models.DateField(
        auto_now_add= True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']