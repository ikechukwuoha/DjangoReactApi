from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


# With this block of code, every User loging in to our site will be required to login using thier email address
class MyUserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError(_(f"Hello, Please Enter a Valid Email Address"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    
# With this block of code, every SuperUser loging in to our site will be required to login using thier email address    
    def create_superuser(self, email, username, password, **extra_fields):
        
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be assigned to is_superuser=True')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must be assigned to is_staff=True')
        
        if extra_fields.get('is_admin') is not True:
            raise ValueError('superuser must be assigned to is_admin=True')
        
        return self.create_user(email, username, password, **extra_fields)