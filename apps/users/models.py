# from apps.common.models import Category
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.deconstruct import deconstructible

@deconstructible
class PhoneValidator(validators.RegexValidator):
    regex = r"^\+998\d{9}$"
    message = "To'g'ri keladigan telefon raqam kiriting"
    flags = 0

ADMIN, CLIENT, EXPERT = 'admin', 'client', 'expert'

class Category(models.Model):
     image = models.ImageField(upload_to='category_image/')
     name = models.CharField(max_length=255,
                             verbose_name='Name')
     
     def str(self):
         return f"{self.id}-{self.name}"

class User(AbstractUser):

    phone_validator = PhoneValidator()

    phone_number = models.CharField(
        max_length=13,
        verbose_name='Phone number',
        validators=[phone_validator],
        unique=True
    )

    TYPE = (
        (ADMIN, 'Admin'),
        (CLIENT, 'Client'),
        (EXPERT, 'Expert')
    )

    type = models.CharField(choices=TYPE, default=CLIENT, max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='img/', null=True, blank=True)
    degree = models.FileField(upload_to='file/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    free_time = models.CharField(max_length=255, null=True, blank=True)
    cost = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.username}"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
