from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    #  we are overriding base user manager methods

    def create_user(self, email=None, phone=None, password=None, **extra_fields):
        if not email and not phone:
            raise ValueError(_('A user must provide either email or phone number'))
        
        # if email:
        #     email = self.normalize('email')
        #     # we add this normalize email to manager model
        #     extra_fields['email'] = email    or

        email = self.normalize_email('email') if email else None
        user = self.model(email=email, phone=phone, **extra_fields)

        # we can not store password directly  , it must be hashed 
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        
        user.save(using=self._db)
        return user


# if we want to create superuser user must be staff and is_superuser True 
# these are the extra fields we add it to above method


    def create_superuser(self,email=None, phone=None, password=None, **extra_fields):
        if not email and not phone:
            raise ValueError(_('A user must provide either email or phone'))
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        
        return self.create_user(email=email, phone=phone, password=password,**extra_fields)