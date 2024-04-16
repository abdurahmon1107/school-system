from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from apps.common.models import *
from django.contrib.auth.hashers import make_password


PHONE_NUMBER_VALIDATOR = RegexValidator(regex=r"^\+998\d{9}$",message="Invalid phone number")



class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)




class User(AbstractUser):
    TURLAR = (
        ('Teacher', 'Teacher'),
        ('Director', 'Director'),
        ('Admin', 'Admin')
    )
    type = models.CharField(max_length=250,
                            choices=TURLAR,
                            default='Teacher',
                            verbose_name="Type")

    phone_number = models.CharField(max_length=13,
                                    validators=[PHONE_NUMBER_VALIDATOR],
                                    verbose_name='Phone number')
    experience = models.IntegerField(default=0,
                                      verbose_name='Experience')
    birthday = models.DateField(null=True)
    # objects = CustomUserManager()

    def __str__(self) -> str:
        return f" {self.type} - {self.username} - {self.id}"
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         # If the user is being created, hash the password
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)
    

 
