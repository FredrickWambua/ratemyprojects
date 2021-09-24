from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models
from cloudinary.models import CloudinaryField








# Create your models here.

class CustomUserManager(BaseUserManager):
    '''
    Custom user manager where email is the unique identifiers
    for authentication instead of username
    '''
    def create_user(self, email, password, **kwargs):
        '''
        Create and save a User with the given email and password.
        '''
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password =(password)
        user.save()
        return user
    def create_superuser(self, email, password, **kwargs):
        '''
        Create and save a superuser with the given email and password.
        '''
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        return self.create_user(email, password, **kwargs)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email

class Profile(models.Model):
    name = models.CharField(max_length=70, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=255)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

class Project(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=255)
    image = CloudinaryField('image')
    link = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self) -> str:
        return f'{self.user.username} {self.title} Project '




class Rates(models.Model):
    content = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    design = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    usability = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    project = models.ForeignKey(Project, on_delete=CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'


    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()


    def __str__(self) -> str:
        return f' {self.user.username} {self.project.title} Rating ' 