from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin 
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


from .managers import MyUserManager



class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Enter Your Email..."), unique=True)
    username = models.CharField(_("Your Username"), max_length=100, unique=True)
    date_registered = models.DateTimeField(_("Date Joined..."), default=timezone.now)
    is_staff = models.BooleanField(_("A Staff?"), default=False)
    is_admin = models.BooleanField(_("An Admin?"), default=False)
    is_active = models.BooleanField(_("Active User"), default=True)
   
    
    
    objects = MyUserManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    def __str__(self):
        return self.username
    
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    
    

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 100)
    other_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    bio = models.CharField(max_length= 650)
    location = models.CharField(max_length=700)
    image = models.ImageField(default='defaultpic.jpg', upload_to='profile_pic', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.user.username
    

    
    def get_full_name(self):
        """
            This Function returns the first name, midle name and last name with space in between
        """
        full_name = f"{self.first_name} {self.other_name} {self.last_name}"
        return full_name()
    
    
    def short_name(self):
        """This Function returns Just the first name..."""
        short_name = f"{self.first_name}"
        return short_name()
    
    
    
    
    
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_model(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()