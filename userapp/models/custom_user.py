from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    phone = models.CharField(_('phone number'), max_length=15, unique=True, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

     # Link to the custom manager
    objects = CustomUserManager()
    
    # which field is used to login
    USERNAME_FIELD = 'email'  # can be phone either
    REQUIRED_FIELDS = ['phone']  #fields required when creating user

    def __str__(self):
        return self.email if self.email else self.phone
    
